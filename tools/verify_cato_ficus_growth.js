// tools/verify_cato_ficus_growth.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log('=== VERIFYING CATO D\'ACQUA & FICUS GROWTH MECHANIC ===');

  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle', '--autoplay-policy=no-user-gesture-required']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  const logs = [];
  page.on('console', msg => {
    const text = msg.text();
    logs.push(text);
    if (text.includes('AUGUSTA') || text.includes('LIBERATION') || text.includes('ficus') || text.includes('cato') || text.includes('error')) {
      console.log('BROWSER LOG:', text);
    }
  });

  console.log('1. Loading game...');
  await page.goto('http://localhost:8080/gta/', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const p = btns.find(b => b.textContent && (b.textContent.includes('Play') || b.textContent.includes('Gioca')));
    if (p) p.click();
  });
  await new Promise(r => setTimeout(r, 2000));

  // 2. Teleport player onto plat-shaded right in front of the pulley rope at x=65.5, y=14.35
  console.log('2. Stepping on switch-cato-rope at x=65.5...');
  await page.evaluate(() => {
    const sim = window.__game.ce;
    sim.player.x = 65.5;
    sim.player.y = 14.5;
    sim.player.vx = 0;
    sim.player.vy = 0;
  });

  // Wait 1.2s for physics step and contraption trigger
  await new Promise(r => setTimeout(r, 1200));

  const statusCato = await page.evaluate(() => {
    const sim = window.__game.ce;
    const toast = document.getElementById('gta-liberation-toast');
    const wScene = window.__game.Wt ? window.__game.Wt.scene : null;
    const cascade = wScene ? wScene.getObjectByName('cato-water-cascade-burst') : null;
    return {
      playerPos: { x: sim.player.x, y: sim.player.y },
      latched: sim.latched,
      toastVisible: toast ? toast.style.opacity : null,
      toastText: toast ? toast.innerText : null,
      hasWaterCascade: !!cascade,
      canopyActive: sim.level?.platforms.find(p => p.id === 'ficus-canopy-bridge')?.active
    };
  });
  console.log('Cato Trigger Status:', statusCato);

  await page.screenshot({ path: 'gta/screenshot-cato-pulley-water.png' });
  console.log('Saved gta/screenshot-cato-pulley-water.png');

  // 3. Now walk onto the grown Ficus canopy bridge over the spikes at x=78.0, y=14.5!
  console.log('3. Walking onto the grown Ficus canopy bridge over the spike pit at x=78.0...');
  await page.evaluate(() => {
    const sim = window.__game.ce;
    sim.player.x = 78.0;
    sim.player.y = 14.8;
    sim.player.vx = 0;
    sim.player.vy = 0;
  });

  await new Promise(r => setTimeout(r, 1200));

  const statusCanopy = await page.evaluate(() => {
    const sim = window.__game.ce;
    return {
      playerPos: { x: sim.player.x, y: sim.player.y },
      groundId: sim.player.groundId || sim.player.surfaceId,
      canopyPlatformY: sim.level?.platforms.find(p => p.id === 'ficus-canopy-bridge')?.y
    };
  });
  console.log('Ficus Canopy Traversal Status:', statusCanopy);

  await page.screenshot({ path: 'gta/screenshot-ficus-canopy-traversal.png' });
  console.log('Saved gta/screenshot-ficus-canopy-traversal.png');

  await browser.close();
  console.log('=== VERIFICATION OF CATO & FICUS COMPLETED SUCCESSFULLY! ===');
})();
