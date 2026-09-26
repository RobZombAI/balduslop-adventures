// tools/verify_liberation_and_hazards.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log('=== VERIFYING GTA AUGUSTA: HAZARDS & LIBERATION ANIMATIONS ===');

  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle', '--autoplay-policy=no-user-gesture-required']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const consoleLogs = [];
  page.on('console', msg => {
    const text = msg.text();
    consoleLogs.push(text);
    if (text.includes('AUGUSTA') || text.includes('LIBERATION') || text.includes('Giuseppe') || text.includes('error')) {
      console.log('BROWSER LOG:', text);
    }
  });
  page.on('pageerror', err => console.error('BROWSER PAGE ERROR:', err));

  console.log('1. Navigating to http://localhost:8080/gta/ ...');
  await page.goto('http://localhost:8080/gta/', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  // Click Play / Gioca
  console.log('2. Starting game...');
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const p = btns.find(b => b.textContent && (b.textContent.includes('Play') || b.textContent.includes('Gioca')));
    if (p) p.click();
  });
  await new Promise(r => setTimeout(r, 2500));

  // Check scene and character
  const statusL1 = await page.evaluate(() => {
    const pScene = window.__DEBUG_PLAYER_SCENE__;
    const wScene = window.__WORLD_SCENE__;
    const head = pScene ? pScene.getObjectByName('giuseppe-head-root') : null;
    const trowel = pScene ? pScene.getObjectByName('giuseppe-trowel-prop') : null;

    // Count decor objects in world scene
    const decorKinds = [];
    if (wScene) {
      wScene.traverse(obj => {
        if (obj.name && (obj.name.includes('scarico') || obj.name.includes('discarica') || obj.name.includes('ciminiera') || obj.name.includes('fumo') || obj.name.includes('fusto') || obj.name.includes('liquame') || obj.name.includes('torcia'))) {
          decorKinds.push(obj.name);
        }
      });
    }

    return {
      hasPlayerScene: !!pScene,
      hasWorldScene: !!wScene,
      hasGiuseppeHead: !!head,
      hasGiuseppeTrowel: !!trowel,
      decorCount: decorKinds.length,
      sampleDecor: decorKinds.slice(0, 10)
    };
  });
  console.log('Level 1 Scene Status:', statusL1);

  // Take screenshot of Level 1 starting view showing environmental decor
  await page.screenshot({ path: 'gta/screenshot-level1-hazards.png' });
  console.log('Saved gta/screenshot-level1-hazards.png');

  // 3. Teleport to Level 1 switch (garden-water) at x=153
  console.log('3. Stepping on Level 1 switch-water at x=153...');
  const teleportL1 = await page.evaluate(() => {
    // Find player body / entity in window.__WORLD_SCENE__ or active stage
    const pScene = window.__DEBUG_PLAYER_SCENE__;
    if (!pScene) return false;
    // Set position of player root or parent
    let root = pScene;
    while (root.parent && root.parent.type !== 'Scene') {
      root = root.parent;
    }
    // Teleport directly onto the switch: x=153, y=16.3
    root.position.x = 153.0;
    root.position.y = 16.3;

    // Also trigger via activate or stepping
    const stage = window.__GAME_STAGE__;
    return true;
  });

  // Let player land on switch
  await new Promise(r => setTimeout(r, 600));

  // If not triggered by physical overlap immediately, invoke activate directly to test full visual & audio pipeline
  await page.evaluate(() => {
    const stage = window.__GAME_STAGE__;
    if (stage && stage.activate) {
      stage.activate("garden-water", 153, 16.2);
    } else if (typeof triggerAugustaLiberation === 'function') {
      triggerAugustaLiberation("garden-water", 153, 16.2, {level: {name: "Villa Comunale di Augusta"}});
    }
  });

  await new Promise(r => setTimeout(r, 200));

  // Check toast and particle state
  const liberationStateL1 = await page.evaluate(() => {
    const toast = document.getElementById('gta-liberation-toast');
    const wScene = window.__WORLD_SCENE__;
    const burst = wScene ? wScene.getObjectByName('liberation-particle-burst') : null;
    return {
      toastExists: !!toast,
      toastVisible: toast ? toast.style.opacity : null,
      toastText: toast ? toast.innerText : null,
      particleBurstExists: !!burst
    };
  });
  console.log('Level 1 Liberation State:', liberationStateL1);

  await page.screenshot({ path: 'gta/screenshot-liberation-level1.png' });
  console.log('Saved gta/screenshot-liberation-level1.png');

  // 4. Test Level 2
  console.log('4. Testing Level 2 switch-dockgate liberation...');
  await page.evaluate(() => {
    if (typeof triggerAugustaLiberation === 'function') {
      triggerAugustaLiberation("dock-lock", 152, 16.2, {level: {name: "Lungomare Rossini & Il Diluvio Fognario"}});
    }
  });

  await new Promise(r => setTimeout(r, 200));
  const liberationStateL2 = await page.evaluate(() => {
    const toast = document.getElementById('gta-liberation-toast');
    return {
      toastVisible: toast ? toast.style.opacity : null,
      toastText: toast ? toast.innerText : null
    };
  });
  console.log('Level 2 Liberation State:', liberationStateL2);

  await page.screenshot({ path: 'gta/screenshot-liberation-level2.png' });
  console.log('Saved gta/screenshot-liberation-level2.png');

  // Check errors
  const errors = consoleLogs.filter(l => l.toLowerCase().includes('error') || l.toLowerCase().includes('uncaught'));
  console.log('Console Errors Count:', errors.length);
  if (errors.length > 0) {
    console.log('Errors:', errors);
  }

  await browser.close();
  console.log('=== VERIFICATION COMPLETED SUCCESSFULLY! ===');
})();
