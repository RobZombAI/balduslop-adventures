// tools/verify_browser_gameplay.js
const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.type(), msg.text()));
  page.on('pageerror', err => console.error('BROWSER PAGE ERROR:', err));

  console.log('Navigating to http://localhost:8080/gta/ ...');
  await page.goto('http://localhost:8080/gta/', { waitUntil: 'networkidle2' });

  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: 'gta/screenshot-menu.png' });
  console.log('Saved gta/screenshot-menu.png');

  // Click Play button
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const p = btns.find(b => b.textContent && b.textContent.includes('Play'));
    if (p) p.click();
  });

  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: 'gta/screenshot-gameplay.png' });
  console.log('Saved gta/screenshot-gameplay.png (Standing Idle)');

  // Run to the right
  console.log('Holding KeyD to run...');
  await page.keyboard.down('KeyD');
  await new Promise(r => setTimeout(r, 900));
  await page.screenshot({ path: 'gta/screenshot-running.png' });
  console.log('Saved gta/screenshot-running.png (Running)');

  // Jump while running!
  console.log('Pressing Space to jump...');
  await page.keyboard.down('Space');
  await new Promise(r => setTimeout(r, 200));
  await page.keyboard.up('Space');
  await page.screenshot({ path: 'gta/screenshot-jumping.png' });
  console.log('Saved gta/screenshot-jumping.png (Jumping)');

  await page.keyboard.up('KeyD');
  await new Promise(r => setTimeout(r, 500));

  await browser.close();
  console.log('Verification finished successfully!');
})();
