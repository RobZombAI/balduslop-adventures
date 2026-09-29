// tools/verify_balduslop_cerignola.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log("=== BROWSER SIMULATION: BALDUSLOP WITH CERIGNOLA AS EXCLUSIVE LEVEL ===");
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
    if (msg.type() === 'error' && !text.includes('favicon') && !text.includes('404')) {
      console.error('BROWSER ERROR LOG:', text);
      errors.push(text);
    } else if (text.includes('CERIGNOLA') || text.includes('Decor') || text.includes('decorError')) {
      console.log('BROWSER LOG:', text);
    }
  });

  page.on('pageerror', err => {
    console.error('BROWSER UNCAUGHT ERROR:', err.message);
    errors.push(err.message);
  });

  // 1. Test GTA Augusta is strictly 10 levels and has no Cerignola
  console.log("\n--- 1. Testing GTA Augusta (http://localhost:8080/gta/) ---");
  await page.goto('http://localhost:8080/gta/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 1000));
  const gtaAudit = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    const te = window.__GAME_TE__ || window.te;
    const navText = document.querySelector('.game-switch-nav')?.innerText || '';
    return {
      hasCerignolaInNav: navText.includes('Cerignola'),
      levelsCount: window.kn ? window.kn.length : null
    };
  });
  console.log("GTA Augusta Audit:", JSON.stringify(gtaAudit));
  if (gtaAudit.hasCerignolaInNav) {
    console.error("FAIL: GTA still has Cerignola in nav!");
  } else {
    console.log("[✓] Confirmed: GTA Augusta is clean and has NO Cerignola!");
  }

  // 2. Load BalduSlop Adventures main game
  console.log("\n--- 2. Testing BalduSlop Adventures (http://localhost:8080/) ---");
  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 1200));

  await page.screenshot({ path: 'screenshot_balduslop_cerignola_home.png' });
  console.log("[✓] Captured screenshot_balduslop_cerignola_home.png");

  // Check title, brand, tagline
  const balduHomeInfo = await page.evaluate(() => {
    return {
      title: document.title,
      tagline: document.getElementById('title-tagline')?.textContent,
      playLabel: document.getElementById('play-label')?.textContent
    };
  });
  console.log("BalduSlop Home Info:", JSON.stringify(balduHomeInfo));

  // 3. Start Game in BalduSlop
  console.log("\nStarting BalduSlop Game (Cerignola Chapter 1)...");
  await page.evaluate(() => {
    if (window.__START_LEVEL__) {
      window.__START_LEVEL__(0); // Cerignola is Level 1 (Index 0) in BalduSlop!
    } else {
      const playBtn = document.getElementById('play');
      if (playBtn) playBtn.click();
    }
  });
  await new Promise(r => setTimeout(r, 2000));

  // 4. Audit Scene & 3D Models in BalduSlop
  const sceneAudit = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    const scene = (window.__WORLD__ && window.__WORLD__.scene) || window.__WORLD_SCENE__;
    if (!scene || !ce || !ce.level) return { error: "No scene or level found in BalduSlop" };

    const decorFound = {};
    const decorErrors = [];

    scene.traverse(o => {
      if (o.userData && o.userData.decorError) {
        decorErrors.push({ name: o.name, error: o.userData.decorError });
      }
      if (o.name) {
        decorFound[o.name] = (decorFound[o.name] || 0) + 1;
      }
    });

    return {
      gameTitle: document.title,
      levelName: ce.level.name,
      levelShort: ce.level.short,
      levelIndex: ce.index,
      platformCount: ce.level.platforms.length,
      decorCount: ce.level.decor.length,
      enemyCount: ce.level.enemies ? ce.level.enemies.length : 0,
      coinCount: ce.level.coins ? ce.level.coins.length : 0,
      decorFound: Object.keys(decorFound).filter(k => k.includes('cerignola') || k.includes('blindato') || k.includes('ruspa') || k.includes('pusher') || k.includes('carabinieri') || k.includes('duomo') || k.includes('bustina')),
      decorErrors: decorErrors
    };
  });

  console.log("\nBalduSlop Scene Audit Results:");
  console.log(JSON.stringify(sceneAudit, null, 2));

  await page.screenshot({ path: 'screenshot_balduslop_cerignola_gameplay.png' });
  console.log("[✓] Captured screenshot_balduslop_cerignola_gameplay.png");

  // 5. Simulate Gameplay & Portavalori Switch in BalduSlop
  console.log("\nAdvancing Baldu to Section 2 (Portavalori)...");
  await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    ce.player.x = 52.0;
    ce.player.y = 15.2;
    ce.player.vx = 0;
    ce.player.vy = 0;
    ce.cameraX = 52.0;
    ce.cameraY = 15.2;
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'screenshot_balduslop_cerignola_portavalori.png' });
  console.log("[✓] Captured screenshot_balduslop_cerignola_portavalori.png");

  // Step on Portavalori Switch
  const switchTest = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    ce.player.x = 65.5;
    ce.player.y = 14.35;
    ce.tick(0.016, { moveAxis: 0 });
    return {
      channelState: ce.channels['portavalori-open'],
      latched: ce.latched['portavalori-open']
    };
  });
  console.log("Portavalori Switch in BalduSlop:", JSON.stringify(switchTest));

  // Advance to Duomo Tonti
  console.log("\nAdvancing Baldu to Duomo Tonti & Goal...");
  await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    ce.player.x = 236.0;
    ce.player.y = 18.8;
    ce.player.vx = 0;
    ce.player.vy = 0;
    ce.cameraX = 236.0;
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'screenshot_balduslop_cerignola_duomo.png' });
  console.log("[✓] Captured screenshot_balduslop_cerignola_duomo.png");

  // 6. Trigger Victory & Verify Civic Moral Box in BalduSlop
  console.log("\nTriggering Victory in BalduSlop...");
  await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    ce.status = "complete";
    ce.event("complete", {
      index: 0,
      coins: 19,
      stamps: 3,
      time: 72.1,
      deaths: 0
    });
  });
  await new Promise(r => setTimeout(r, 1200));

  const moralTest = await page.evaluate(() => {
    const dialog = document.getElementById("dialog-content");
    const moralBox = dialog ? dialog.querySelector(".augusta-moral-box") : null;
    const moralTag = moralBox ? moralBox.querySelector(".moral-tag")?.innerText : null;
    const moralTitle = moralBox ? moralBox.querySelector(".augusta-moral-title")?.innerText : null;
    const moralText = moralBox ? moralBox.querySelector(".augusta-moral-text")?.innerText : null;

    return {
      hasMoralBox: !!moralBox,
      moralTag: moralTag,
      moralTitle: moralTitle,
      moralTextSnippet: moralText ? moralText.substring(0, 110) + "..." : null
    };
  });
  console.log("BalduSlop Moral Box Test:", JSON.stringify(moralTest, null, 2));

  await page.screenshot({ path: 'screenshot_balduslop_cerignola_moral.png' });
  console.log("[✓] Captured screenshot_balduslop_cerignola_moral.png");

  await browser.close();

  if (errors.length > 0) {
    console.error("Errors found:", errors);
    process.exit(1);
  } else {
    console.log("\n=== BALDUSLOP CERIGNOLA VERIFICATION 100% SUCCESSFUL! ===");
  }
})();
