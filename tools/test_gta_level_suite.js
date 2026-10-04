// tools/test_gta_level_suite.js
const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

async function runLevelTest(levelIndex, options = {}) {
  console.log(`\n======================================================`);
  console.log(`>>> TESTING GTA LEVEL ${levelIndex + 1} (index ${levelIndex}) <<<`);
  console.log(`======================================================`);

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--enable-webgl", "--use-gl=angle"]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto("http://localhost:8080/gta/?nocache=" + Date.now(), { waitUntil: "networkidle2" });

  const result = await page.evaluate(async (idx) => {
    try {
      await window.__START_LEVEL__(idx);
      await new Promise(r => setTimeout(r, 400));
      const ce = window.__GAME_CE__;
      if (!ce || !ce.level) {
        return { success: false, error: "Game engine or level not loaded" };
      }

      const lvl = ce.level;
      const initial = {
        name: lvl.name,
        short: lvl.short,
        label: lvl.label,
        biome: lvl.biome,
        sky: lvl.sky,
        fog: lvl.fog,
        spawn: lvl.spawn,
        end: lvl.end,
        platformCount: lvl.platforms.length,
        decorCount: lvl.decor?.length || 0,
        enemyCount: lvl.enemies?.length || 0,
        stampCount: lvl.stamps?.length || 0,
        coinCount: lvl.coins?.length || 0,
        sectionsCount: lvl.sections?.length || 0,
        moralTitle: lvl.moralTitle,
        moralStory: lvl.moralStory
      };

      // --- PHASE 1: JUMP AUDIT & PHYSICAL MEASUREMENTS ---
      const jumpAudits = [];
      const nonWalls = lvl.platforms
        .filter(p => p.kind !== "wall" && p.kind !== "hazard" && !p.spiked)
        .sort((a, b) => a.x - b.x);

      let maxJumpGap = 0;
      for (let i = 0; i < nonWalls.length - 1; i++) {
        const cur = nonWalls[i];
        const next = nonWalls[i + 1];
        const gapX = next.x - (cur.x + cur.w);
        const dy = next.y - cur.y;
        if (gapX > maxJumpGap) maxJumpGap = gapX;
        if (gapX > 5.2 && next.kind !== "timed") {
          jumpAudits.push({ from: cur.id, to: next.id, gapX: Math.round(gapX * 100) / 100, dy, warning: "Gap exceeds standard run jump (5.2)" });
        }
      }

      // --- PHASE 2: SPAWN & NATURAL PLAYTRAVERSAL (first 80 ticks) ---
      let startX = ce.player.x;
      let startY = ce.player.y;
      for (let f = 0; f < 80; f++) {
        ce.tick(1 / 60, {
          right: true,
          moveAxis: 1.0,
          jumpPressed: f % 25 === 0
        });
      }
      const earlyMotion = {
        movedX: Math.round((ce.player.x - startX) * 10) / 10,
        currentX: Math.round(ce.player.x * 10) / 10,
        currentY: Math.round(ce.player.y * 10) / 10,
        groundId: ce.player.groundId,
        hp: ce.player.hp
      };

      // --- PHASE 3: ENVIRONMENTAL MECHANISMS & FLUID SWITCH AUDIT ---
      const switches = lvl.platforms.filter(p => p.kind === "switch");
      const switchResults = [];
      for (const sw of switches) {
        // Teleport to switch and step on it
        ce.player.x = sw.x + sw.w / 2;
        ce.player.y = sw.y + 0.1;
        ce.player.vx = 0;
        ce.player.vy = -1;
        ce.player.groundId = sw.id;
        for (let i = 0; i < 20; i++) ce.tick(1 / 60, { right: false });

        const channel = sw.channel;
        const activated = (ce.channels[channel] > 0) || !!ce.latched?.[channel];
        switchResults.push({ id: sw.id, channel, activated });
      }

      // --- PHASE 4: GOAL APPROACH & VICTORY VERIFICATION ---
      const goalPlat = lvl.platforms.find(p => p.goal);
      if (!goalPlat) {
        return { success: false, initial, error: "No goal platform found" };
      }

      ce.player.x = goalPlat.x + 1.0;
      ce.player.y = goalPlat.y + 0.2;
      ce.player.vx = 0;
      ce.player.vy = 0;
      ce.player.groundId = goalPlat.id;
      if (ce.level.boss) ce.level.boss.state = "defeated";
      if (ce.finale) ce.finale.state = "awake";

      let completed = false;
      let victoryDetails = null;

      for (let i = 0; i < 180; i++) {
        ce.tick(1 / 60, { right: true, moveAxis: 1.0 });
        if (ce.status === "complete") {
          completed = true;
          victoryDetails = {
            step: i,
            x: Math.round(ce.player.x * 10) / 10,
            y: Math.round(ce.player.y * 10) / 10,
            status: ce.status
          };
          break;
        }
      }

      // --- PHASE 5: TEST COVERAGE SCORING ---
      let coverageScore = 100;
      if (jumpAudits.length > 0) coverageScore -= jumpAudits.length * 2;
      if (switchResults.some(s => !s.activated)) coverageScore -= 10;
      if (!completed) coverageScore -= 30;
      if (!lvl.moralTitle || !lvl.moralStory) coverageScore -= 10;
      if ((lvl.decor?.length || 0) < 15) coverageScore -= 5;
      if ((lvl.enemies?.length || 0) === 0) coverageScore -= 2;

      return {
        success: completed && switchResults.every(s => s.activated),
        initial,
        earlyMotion,
        maxJumpGap: Math.round(maxJumpGap * 100) / 100,
        jumpAudits,
        switchResults,
        completed,
        victoryDetails,
        coverageScore: Math.max(0, coverageScore)
      };
    } catch(err) {
      return { success: false, error: err.message, stack: err.stack };
    }
  }, levelIndex);

  const shotPath = `gta/screenshot-level${levelIndex + 1}-verified.png`;
  await page.screenshot({ path: shotPath });
  result.screenshotPath = shotPath;
  console.log(`[📸] Verified screenshot saved to: ${shotPath}`);

  await browser.close();
  console.log("TEST RESULT:\n", JSON.stringify(result, null, 2));
  return result;
}

// Command-line execution
if (require.main === module) {
  const arg = process.argv[2] || "3";
  (async () => {
    if (arg === "all") {
      const allResults = [];
      for (let i = 0; i < 10; i++) {
        const res = await runLevelTest(i);
        allResults.push(res);
      }
      console.log("\n================ FULL 10-LEVEL AUDIT REPORT ================");
      console.log(JSON.stringify(allResults.map(r => ({
        level: r.initial?.name,
        completed: r.completed,
        coverageScore: r.coverageScore,
        switches: r.switchResults
      })), null, 2));
    } else {
      const idx = parseInt(arg, 10) - 1;
      await runLevelTest(idx);
    }
  })();
}

module.exports = { runLevelTest };
