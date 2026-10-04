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

  const consoleLogs = [];
  page.on('console', msg => {
    consoleLogs.push({ type: msg.type(), text: msg.text() });
  });
  page.on('pageerror', err => {
    consoleLogs.push({ type: 'pageerror', text: err.toString() });
  });

  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });

  // Wait 1.5s for engine init
  await new Promise(r => setTimeout(r, 1500));

  const results = [];

  for (let idx = 0; idx < 6; idx++) {
    console.log(`Testing Level ${idx}...`);
    const res = await page.evaluate(async (chapterIdx) => {
      if (!window.__START_LEVEL__) return { error: 'No __START_LEVEL__' };
      
      window.__START_LEVEL__(chapterIdx);
      
      // Let it load
      await new Promise(r => setTimeout(r, 500));
      
      const ce = window.__GAME_CE__;
      if (!ce || !ce.level) return { error: 'ce or ce.level missing' };

      const initial = {
        name: ce.level.name,
        short: ce.level.short,
        status: ce.status,
        startX: ce.player.x,
        startY: ce.player.y,
        groundId: ce.player.groundId,
        hp: ce.player.hp
      };

      // Now let's simulate 300 game ticks (about 5-10 seconds of gameplay)
      // Moving right, jumping when near edges or falling
      const trajectory = [];
      let fellOut = false;
      let deaths = ce.deaths || 0;

      for (let step = 0; step < 200; step++) {
        // Simple input: walk right, jump if falling or on ground
        const input = {
          right: true,
          left: false,
          moveAxis: 1.0,
          jumpPressed: (step % 25 === 0) || (ce.player.vy < -2),
          jumpHeld: true,
          stompPressed: false
        };

        try {
          ce.tick(1 / 60, input);
        } catch (e) {
          return { initial, tickError: e.message, step };
        }

        if (step % 20 === 0) {
          trajectory.push({
            step,
            x: Math.round(ce.player.x * 10) / 10,
            y: Math.round(ce.player.y * 10) / 10,
            groundId: ce.player.groundId,
            status: ce.status
          });
        }

        if (ce.player.y < -15) {
          fellOut = true;
        }
      }

      return {
        initial,
        final: {
          x: Math.round(ce.player.x * 10) / 10,
          y: Math.round(ce.player.y * 10) / 10,
          groundId: ce.player.groundId,
          status: ce.status,
          hp: ce.player.hp,
          deaths: ce.deaths || 0
        },
        fellOut,
        trajectorySample: trajectory
      };
    }, idx);

    // Wait a brief moment and take screenshot
    await new Promise(r => setTimeout(r, 300));
    const ssPath = `/Users/robzomb/Documents/antigravity/beautiful-pythagoras/screenshot_level_test_${idx}.png`;
    await page.screenshot({ path: ssPath });
    res.screenshot = ssPath;
    results.push(res);
  }

  console.log("=== PLAYTEST RESULTS ===");
  console.log(JSON.stringify(results, null, 2));

  console.log("=== LOGS / ERRORS ===");
  const errs = consoleLogs.filter(l => l.type === 'error' || l.type === 'pageerror');
  console.log(JSON.stringify(errs, null, 2));

  await browser.close();
})();
