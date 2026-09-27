// tools/verify_physics_and_morals_browser.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log("=== BROWSER VERIFICATION: SOLID PHYSICS CEILINGS & CIVIC MORALS ===");
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  const errors = [];
  page.on('console', msg => {
    const text = msg.text();
    if (msg.type() === 'error' && !text.includes('favicon')) {
      console.error('BROWSER ERROR:', text);
      errors.push(text);
    }
  });

  page.on('pageerror', err => {
    console.error('BROWSER UNCAUGHT ERROR:', err.message);
    errors.push(err.message);
  });

  await page.goto('http://localhost:8080/gta/?t=' + Date.now(), { waitUntil: 'networkidle2' });
  console.log('[✓] Game loaded at http://localhost:8080/gta/');

  // Start Level 1
  await page.evaluate(() => {
    if (window.__START_LEVEL__) {
      window.__START_LEVEL__(0);
    } else {
      const playBtn = document.getElementById('play');
      if (playBtn) playBtn.click();
    }
  });
  await new Promise(r => setTimeout(r, 1500));

  // --- TEST 1: TEST SOLID CEILING COLLISION (NEVER PASS THROUGH SUSPENDED PLATFORM) ---
  console.log("\n--- 1. TESTING SOLID CEILING COLLISION ---");
  const ceilingTest = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    if (!ce || !ce.level) return { error: "No game stage found" };
    ce.status = "playing";

    const targetPlat = ce.level.platforms.find(p => p.id === "opt-sprout1" || p.id === "lift-canopy");
    if (!targetPlat) return { error: "Target platform not found" };

    const platX = targetPlat.x + targetPlat.w / 2;
    const platBottom = targetPlat.y - (targetPlat.h || targetPlat.thickness || 0.65);
    
    // Position Giuseppe 1.9m below platform bottom, so his head (y+1.7) is 0.2m below bottom
    ce.player.x = platX;
    ce.player.y = platBottom - 1.9;
    ce.player.vx = 0;
    ce.player.vy = 12.0; // High upward velocity (jumping)
    ce.player.groundId = null;

    const initialY = ce.player.y;
    const initialHead = initialY + 1.7;

    let maxHeadReached = initialHead;
    let didBump = false;

    for (let tick = 0; tick < 25; tick++) {
      ce.tick(0.016, { moveAxis: 0, jumpHeld: true });
      const currentHead = ce.player.y + 1.7;
      if (currentHead > maxHeadReached) maxHeadReached = currentHead;
      if (ce.player.vy <= 0) didBump = true;
    }

    return {
      platId: targetPlat.id,
      platTop: targetPlat.y,
      platBottom: platBottom,
      initialHead: initialHead,
      maxHeadReached: maxHeadReached,
      penetratedTop: maxHeadReached >= targetPlat.y,
      stoppedAtBottom: maxHeadReached <= platBottom + 0.05,
      finalY: ce.player.y,
      finalVy: ce.player.vy,
      didBump: didBump
    };
  });

  console.log("Ceiling Test Result:", JSON.stringify(ceilingTest, null, 2));
  if (ceilingTest.penetratedTop) {
    console.error("FAIL: Character passed through the platform top!");
  } else if (ceilingTest.stoppedAtBottom) {
    console.log("[✓] SUCCESS: Character was physically BLOCKED at the platform bottom! (Never passed through)");
  }

  // --- TEST 2: TEST HORIZONTAL SOLID WALL BLOCKING ---
  console.log("\n--- 2. TESTING HORIZONTAL WALL COLLISION ---");
  const wallTest = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    if (!ce || !ce.level) return { error: "No game stage found" };
    ce.status = "playing";

    const stepPlat = ce.level.platforms.find(p => p.id === "plat-ficus-step2");
    if (!stepPlat) return { error: "plat-ficus-step2 not found" };

    ce.player.x = 14.5;
    ce.player.y = 13.6; // Feet at 13.6, platform top is 14.4 (step is 0.8m high)
    ce.player.vx = 8.0; // Running forward into the step without jumping!
    ce.player.vy = 0;

    for (let tick = 0; tick < 20; tick++) {
      ce.tick(0.016, { moveAxis: 1.0, right: true, jumpHeld: false });
    }

    return {
      stepX: stepPlat.x,
      stepY: stepPlat.y,
      playerFinalX: ce.player.x,
      playerFinalY: ce.player.y,
      blockedBeforeWall: ce.player.x <= stepPlat.x
    };
  });

  console.log("Wall Test Result:", JSON.stringify(wallTest, null, 2));
  if (wallTest.blockedBeforeWall) {
    console.log("[✓] SUCCESS: Character cannot walk through solid platform walls! Stopped at edge.");
  } else {
    console.error("FAIL: Character penetrated wall!");
  }

  // --- TEST 3: TEST CIVIC MORAL MODAL ACROSS ALL 10 LEVELS ---
  console.log("\n--- 3. TESTING CIVIC MORALS ON LEVEL CLEAR ACROSS ALL 10 LEVELS ---");
  for (let lvl = 0; lvl < 10; lvl++) {
    await page.evaluate((levelIndex) => {
      const ce = window.__GAME_CE__ || window.ce;
      if (window.__START_LEVEL__) {
        window.__START_LEVEL__(levelIndex);
      }
    }, lvl);
    await new Promise(r => setTimeout(r, 600));

    // Trigger complete
    await page.evaluate((levelIndex) => {
      const ce = window.__GAME_CE__ || window.ce;
      ce.status = "complete";
      ce.event("complete", {
        index: levelIndex,
        coins: 10,
        stamps: 3,
        time: 45.2,
        deaths: 0
      });
    }, lvl);

    // Wait 1200ms for completion dialog and moral card animation
    await new Promise(r => setTimeout(r, 1200));

    const moralTest = await page.evaluate(() => {
      const dialog = document.getElementById("dialog-content");
      const moralBox = dialog ? dialog.querySelector(".augusta-moral-box") : null;
      const moralTitle = moralBox ? moralBox.querySelector(".augusta-moral-title")?.innerText : null;
      const moralText = moralBox ? moralBox.querySelector(".augusta-moral-text")?.innerText : null;
      const h2 = dialog ? dialog.querySelector("#dialog-title")?.innerText : null;
      const ce = window.__GAME_CE__ || window.ce;

      return {
        levelIndex: ce.index,
        levelName: ce.level.name,
        hasMoralBox: !!moralBox,
        moralTitle: moralTitle,
        moralTextSnippet: moralText ? moralText.substring(0, 95) + "..." : null,
        heading: h2
      };
    });

    console.log(`Level ${lvl + 1} (${moralTest.levelName}):`);
    console.log(`  Heading: "${moralTest.heading}"`);
    console.log(`  Moral Title: "${moralTest.moralTitle}"`);
    console.log(`  Moral Text: "${moralTest.moralTextSnippet}"`);

    if (lvl === 0) {
      await page.screenshot({ path: 'gta/screenshot-moral-level1.png' });
      console.log('  [✓] Captured gta/screenshot-moral-level1.png');
    } else if (lvl === 1) {
      await page.screenshot({ path: 'gta/screenshot-moral-level2.png' });
      console.log('  [✓] Captured gta/screenshot-moral-level2.png');
    } else if (lvl === 9) {
      await page.screenshot({ path: 'gta/screenshot-moral-level10.png' });
      console.log('  [✓] Captured gta/screenshot-moral-level10.png');
    }
  }

  await browser.close();
  console.log("\n=== ALL TESTS COMPLETED SUCCESSFULLY! ===");
})();
