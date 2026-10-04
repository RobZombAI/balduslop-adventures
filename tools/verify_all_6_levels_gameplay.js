const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push({ type: 'console.error', text: msg.text() });
  });
  page.on('pageerror', err => {
    errors.push({ type: 'pageerror', text: err.toString() });
  });

  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 1000));

  const simulationResults = [];

  for (let idx = 0; idx < 6; idx++) {
    console.log(`\n=== VERIFYING CHAPTER ${idx + 1} (Sc[${idx}]) ===`);
    
    // Start level
    const sim = await page.evaluate(async (chapterIdx) => {
      await window.__START_LEVEL__(chapterIdx);
      await new Promise(r => setTimeout(r, 400));
      const ce = window.__GAME_CE__;
      if (!ce || !ce.level) return { error: "Failed to load level" };

      const name = ce.level.name;
      const short = ce.level.short;
      const initial = {
        name,
        short,
        x: ce.player.x,
        y: ce.player.y,
        hp: ce.player.hp,
        groundId: ce.player.groundId
      };

      // 1. Simulate initial spawn & 60 ticks of natural player control
      for (let i = 0; i < 60; i++) {
        ce.tick(1/60, { right: true, moveAxis: 1.0, jumpPressed: i % 20 === 0 });
      }

      const earlyMovement = {
        x: Math.round(ce.player.x * 10) / 10,
        y: Math.round(ce.player.y * 10) / 10,
        groundId: ce.player.groundId,
        hp: ce.player.hp,
        status: ce.status
      };

      // 2. Teleport to near the goal platform and verify victory bell trigger
      const goalPlat = ce.level.platforms.find(p => p.goal);
      if (!goalPlat) return { initial, earlyMovement, error: "No goal platform found" };

      // Set player on the approach to the bell
      ce.player.x = goalPlat.x;
      ce.player.y = goalPlat.y;
      ce.player.vx = 0;
      ce.player.vy = 0;
      ce.player.groundId = goalPlat.id;
      if (ce.level.boss) ce.level.boss.state = "defeated";
      if (ce.finale) ce.finale.state = "awake";

      let completed = false;
      let victoryDetails = null;

      for (let i = 0; i < 150; i++) {
        ce.tick(1/60, { right: true, moveAxis: 1.0 });
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

      return {
        initial,
        earlyMovement,
        goalPlat: { id: goalPlat.id, x: goalPlat.x, w: goalPlat.w, y: goalPlat.y },
        completed,
        victoryDetails
      };
    }, idx);

    // Take screenshot during gameplay
    await new Promise(r => setTimeout(r, 200));
    const ssPath = `/Users/robzomb/Documents/antigravity/beautiful-pythagoras/screenshot_chapter_${idx + 1}_gameplay.png`;
    await page.screenshot({ path: ssPath });
    sim.screenshot = ssPath;

    console.log(`Chapter ${idx + 1}: ${sim.initial?.short || sim.error}`);
    console.log(`  Completed: ${sim.completed}`);
    if (sim.victoryDetails) {
      console.log(`  Victory at step ${sim.victoryDetails.step}, x=${sim.victoryDetails.x}, status=${sim.victoryDetails.status}`);
    }

    simulationResults.push(sim);
  }

  console.log("\n=======================================================");
  console.log(">>> FINAL ALL 6 LEVELS GAMEPLAY AUDIT REPORT <<<");
  console.log("=======================================================");
  console.log(JSON.stringify(simulationResults, null, 2));

  console.log("\nErrors:", errors);

  await browser.close();
})();
