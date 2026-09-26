// tools/capture_action_screenshot.js
const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto('http://localhost:8080/gta/', { waitUntil: 'networkidle2' });
  
  // Click Play
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const p = btns.find(b => b.textContent && b.textContent.includes('Play'));
    if (p) p.click();
  });

  await new Promise(r => setTimeout(r, 1500));
  
  // Move right for 800ms
  await page.keyboard.down('KeyD');
  await new Promise(r => setTimeout(r, 700));
  await page.keyboard.up('KeyD');
  
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'gta/screenshot-running.png' });
  await browser.close();
  console.log('Saved gta/screenshot-running.png');
})();
