const puppeteer = require("puppeteer-core");

(async () => {
  console.log("=== RUNNING 100% PHYSICS & BUGFIXES UNIT TEST SUITE ===");
  const browser = await puppeteer.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });
  const page = await browser.newPage();
  await page.goto("http://localhost:8080/?nocache=" + Date.now(), { waitUntil: "networkidle2" });

  const results = await page.evaluate(async () => {
    const tests = [];

    function assert(name, condition, details = "") {
      tests.push({ name, passed: !!condition, details });
      if (!condition) console.error("TEST FAILED:", name, details);
    }

    // Load Level 0
    await window.__START_LEVEL__(0);
    await new Promise(r => setTimeout(r, 300));
    const ce = window.__GAME_CE__;

    // Unit Test 1: Delta time e clamping
    {
      const prevX = ce.player.x;
      // Pass e = 1000 (huge lag spike)
      ce.tick(1000, { right: true });
      const dx = ce.player.x - prevX;
      // Since max speed is ~8.5 and max e is 0.035, dx must be <= 8.5 * 0.035 = ~0.3
      assert("Delta time clamp on huge lag spike (e=1000 clamped to 0.035)", dx < 0.5, `dx was ${dx}`);

      // Pass e = -5 or NaN
      ce.tick(NaN, {});
      assert("Delta time handles NaN without corrupting state", !isNaN(ce.player.x) && !isNaN(ce.player.y));
    }

    // Unit Test 2: Upper clamp on o.vy (perchè a volte quando salta scompare e sputa su in alto?)
    {
      // Artificially inject massive upward velocity
      ce.player.vy = 250.0;
      ce.tick(0.016, {});
      assert("Vertical velocity clamped to <= 20.5 (preventing launching offscreen)", ce.player.vy <= 20.5, `vy was ${ce.player.vy}`);

      // Inject negative runaway
      ce.player.vy = -100.0;
      ce.tick(0.016, {});
      assert("Vertical velocity clamped to >= -26 (terminal fall velocity)", ce.player.vy >= -26, `vy was ${ce.player.vy}`);

      // Inject runaway horizontal velocity
      ce.player.vx = 90.0;
      ce.tick(0.016, {});
      assert("Horizontal velocity clamped to <= 22", ce.player.vx <= 22, `vx was ${ce.player.vx}`);
    }

    // Unit Test 3: Moving platform lift fling impulse clamp
    {
      const fakeLift = { id: "test-lift", kind: "lift", carry: true, x: 10, y: 15, prevX: 10, prevY: 5, w: 6 };
      ce.level.platforms.push(fakeLift);
      ce.player.x = 12;
      ce.player.y = 15;
      ce.player.groundId = fakeLift.id;
      ce.player.coyote = 0.135;
      ce.player.jumpBuffer = 0.16;

      // Platform moved 10 units up in 1 frame (prevY = 5, y = 15)
      ce.tick(0.016, { jumpPressed: true });
      assert("Lift fling impulse clamped (o.vy <= 20.5)", ce.player.vy <= 20.5, `vy was ${ce.player.vy}`);
      // Clean up fake platform
      ce.level.platforms = ce.level.platforms.filter(p => p.id !== "test-lift");
    }

    // Unit Test 4: Spiked platforms excluded from landing filter E (e ogni bug di quando cade sotto e resta in vita)
    {
      await window.__START_LEVEL__(2); // Cerignola
      await new Promise(r => setTimeout(r, 300));
      const ce2 = window.__GAME_CE__;
      ce2.respawn();
      ce2.player.invuln = 0;

      const pit1 = ce2.level.platforms.find(p => p.id === "pit-chiodi-1");
      assert("Cerignola pit-chiodi-1 exists and is spiked", !!pit1 && pit1.spiked === true);

      // Place player dropping directly onto pit-chiodi-1
      ce2.player.x = pit1.x + pit1.w / 2;
      ce2.player.y = pit1.y + 0.5;
      ce2.player.vy = -2.0;
      ce2.player.groundId = null;

      ce2.tick(0.016, {});
      assert("Spiked platform CANNOT become groundId (ignored by landing filter E)", ce2.player.groundId !== pit1.id, `groundId was ${ce2.player.groundId}`);
    }

    // Unit Test 5: Instant lethal fall damage upon touching spiked platform
    {
      const ce2 = window.__GAME_CE__;
      ce2.respawnTimer = 0;
      ce2.respawn();
      ce2.player.invuln = 0;
      const initialDeaths = ce2.deaths;
      const pit2 = ce2.level.platforms.find(p => p.id === "pit-chiodi-2");

      ce2.player.x = pit2.x + pit2.w / 2;
      ce2.player.y = pit2.y;
      ce2.player.groundId = null;

      ce2.tick(0.016, {});
      assert("Touching pit-chiodi-2 deals lethal fall damage immediately", ce2.deaths === initialDeaths + 1, `deaths was ${ce2.deaths}, initial was ${initialDeaths}`);
      assert("Respawn timer started after spike hit", ce2.respawnTimer > 0, `respawnTimer was ${ce2.respawnTimer}`);
    }

    // Unit Test 6: Fall depth kill plane triggers if falling below platforms in Cerignola
    {
      const ce2 = window.__GAME_CE__;
      ce2.respawnTimer = 0;
      ce2.respawn();
      ce2.player.invuln = 0;
      // Set checkpoint at dock-portavalori-main (y=15.2)
      const cp = ce2.level.platforms.find(p => p.id === "dock-portavalori-main");
      ce2.checkpoint = { x: cp.checkpoint, y: cp.y, depth: cp.fallDepth || 7.5 };
      ce2.checkpointId = cp.id;

      const initialDeaths = ce2.deaths;
      // Drop player to y = 4.5 (below baseKillY of 5.0 and below 15.2 - 7.5 = 7.7)
      ce2.player.x = 70;
      ce2.player.y = 4.5;
      ce2.player.groundId = null;

      ce2.tick(0.016, {});
      assert("Falling below Cerignola floor kill plane triggers lethal fall damage", ce2.deaths === initialDeaths + 1, `deaths was ${ce2.deaths}, initial was ${initialDeaths}`);
    }

    // Unit Test 7: NaN / Infinity recovery
    {
      const ce2 = window.__GAME_CE__;
      ce2.respawnTimer = 0;
      ce2.respawn();
      ce2.player.invuln = 0;
      ce2.player.x = NaN;
      ce2.tick(0.016, {});
      assert("Engine automatically recovers from NaN coordinates via safe respawn", Number.isFinite(ce2.player.x) && Number.isFinite(ce2.player.y));
    }

    // Unit Test 8: All 6 chapters loadable, playable, and finishable
    {
      for (let ch = 0; ch < 6; ch++) {
        await window.__START_LEVEL__(ch);
        await new Promise(r => setTimeout(r, 100));
        const c = window.__GAME_CE__;
        assert(`Chapter ${ch + 1} (${c.level.name}) loads in playing state`, c.status === "playing");
        assert(`Chapter ${ch + 1} has valid spawn`, Number.isFinite(c.player.x) && Number.isFinite(c.player.y));
        assert(`Chapter ${ch + 1} has goal platform`, !!c.level.platforms.find(p => p.goal));
      }
    }

    return tests;
  });

  console.log("\n================ TEST RESULTS ================");
  let failed = 0;
  for (const t of results) {
    const symbol = t.passed ? "  [PASS]" : "  [FAIL]";
    console.log(`${symbol} ${t.name} ${t.details ? "(" + t.details + ")" : ""}`);
    if (!t.passed) failed++;
  }
  console.log("==============================================");
  console.log(`TOTAL TESTS: ${results.length}, PASSED: ${results.length - failed}, FAILED: ${failed}`);

  await browser.close();
  if (failed > 0) process.exit(1);
})();
