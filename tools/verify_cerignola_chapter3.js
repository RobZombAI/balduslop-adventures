// tools/verify_cerignola_chapter3.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log("=== VERIFYING CERIGNOLA AS CHAPTER 3 OF BALDUSLOP ===");
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

  // 1. Load BalduSlop
  console.log("Loading http://localhost:8080/ ...");
  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 1200));

  // 2. Open Chapters Modal
  console.log("Opening Chapters menu...");
  await page.evaluate(() => {
    const chBtn = document.getElementById('chapters');
    if (chBtn) chBtn.click();
  });
  await new Promise(r => setTimeout(r, 800));

  // Inspect Chapters
  const chaptersList = await page.evaluate(() => {
    const choices = Array.from(document.querySelectorAll('.chapter-choice'));
    return choices.map(c => {
      const num = c.querySelector('span')?.textContent?.trim();
      const title = c.querySelector('strong')?.textContent?.trim();
      const levelIdx = c.getAttribute('data-level');
      return { num, title, levelIdx };
    });
  });
  console.log("Chapters Found in BalduSlop Menu:\n", JSON.stringify(chaptersList, null, 2));

  await page.screenshot({ path: 'screenshot_chapters_menu_cerignola.png' });
  console.log("[✓] Captured screenshot_chapters_menu_cerignola.png");

  // 3. Start Chapter 3 (Cerignola, index 2)
  console.log("\nStarting Chapter 3 (Cerignola, index 2)...");
  await page.evaluate(() => {
    if (window.__START_LEVEL__) {
      window.__START_LEVEL__(2);
    } else {
      const cerBtn = Array.from(document.querySelectorAll('.chapter-choice')).find(b => b.textContent.includes('Cerignola'));
      if (cerBtn) cerBtn.click();
    }
  });
  await new Promise(r => setTimeout(r, 2000));

  // Verify Scene
  const activeLevel = await page.evaluate(() => {
    const ce = window.__GAME_CE__ || window.ce;
    if (!ce || !ce.level) return null;
    return {
      name: ce.level.name,
      short: ce.level.short,
      index: ce.index,
      biome: ce.level.biome,
      platformCount: ce.level.platforms.length,
      decorCount: ce.level.decor.length
    };
  });
  console.log("Active Level in Game:", JSON.stringify(activeLevel, null, 2));

  await page.screenshot({ path: 'screenshot_chapter3_cerignola_playing.png' });
  console.log("[✓] Captured screenshot_chapter3_cerignola_playing.png");

  await browser.close();

  if (activeLevel && activeLevel.index === 2 && activeLevel.short === "Cerignola") {
    console.log("\n=== SUCCESS: CERIGNOLA IS OFFICIALLY CHAPTER 3 OF BALDUSLOP! ===");
  } else {
    console.error("FAIL: Active level is not Cerignola at index 2!");
    process.exit(1);
  }
})();
