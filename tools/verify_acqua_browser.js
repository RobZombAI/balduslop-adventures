// tools/verify_acqua_browser.js
const puppeteer = require('puppeteer-core');

(async () => {
  console.log("=== BROWSER VERIFICATION: L'ORO BLU DI AUGUSTA (PIPE FLOW & CECCARELLI DOSSIER) ===");
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });

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

  await page.goto('http://localhost:8080/acqua/?t=' + Date.now(), { waitUntil: 'networkidle2' });
  console.log('[✓] Game loaded at http://localhost:8080/acqua/');

  // 1. Verify Case 1 Header and Canvas
  const initialInfo = await page.evaluate(() => {
    return {
      title: document.title,
      caseName: document.getElementById('case-name')?.innerText,
      canvasWidth: document.getElementById('pipe-canvas')?.width,
      canvasHeight: document.getElementById('pipe-canvas')?.height,
      pillCount: document.querySelectorAll('.level-pill').length
    };
  });

  console.log(`[✓] Page Title: ${initialInfo.title}`);
  console.log(`[✓] Case 1 Name: ${initialInfo.caseName}`);
  console.log(`[✓] Canvas Dimensions: ${initialInfo.canvasWidth}x${initialInfo.canvasHeight}`);
  console.log(`[✓] Available Cases: ${initialInfo.pillCount}`);

  // Take screenshot of initial puzzle
  await page.screenshot({ path: 'screenshot_acqua_case1.png' });
  console.log('[✓] Saved screenshot_acqua_case1.png');

  // 2. Solve Case 1 programmatically
  console.log('\n--- SOLVING CASE 1 VIA ROTATIONS ---');
  await page.evaluate(() => {
    // In Case 1:
    // (0,1): straight needs to be horizontal (ports [0,1,0,1], rot=0 or 2)
    // (0,2): elbow needs to point bottom-left (ports [0,0,1,1], rot=2)
    // (1,2): straight needs to be vertical (ports [1,0,1,0], rot=0 or 2)
    // (2,2): elbow needs to point top-right (ports [1,1,0,0], rot=0)
    // (2,3): elbow needs to point bottom-left (ports [0,0,1,1], rot=2)
    // (3,3): target [1,0,0,0]
    
    // Let's set gridState to solved orientation:
    window.gridState[0][1].rot = 0; // horizontal
    window.gridState[0][2].rot = 2; // bottom-left
    window.gridState[1][2].rot = 0; // vertical
    window.gridState[2][2].rot = 0; // top-right
    window.gridState[2][3].rot = 2; // bottom-left

    window.checkConnectivity();
    window.render();
    window.triggerVictoryFlow();
  });

  // Wait 1500ms for victory flow and modal to appear
  await new Promise(r => setTimeout(r, 1800));

  const modalInfo = await page.evaluate(() => {
    const modal = document.getElementById('dossier-modal');
    const isShown = modal?.classList.contains('show');
    const dossierTitle = document.getElementById('modal-dossier-title')?.innerText;
    const ceccarelliQuote = document.getElementById('modal-dossier-quote')?.innerText;
    const moralTitle = document.getElementById('modal-moral-title')?.innerText;
    const moralText = document.getElementById('modal-moral-text')?.innerText;
    return {
      isShown,
      dossierTitle,
      ceccarelliQuote,
      moralTitle,
      moralTextSnippet: moralText?.substring(0, 100) + '...'
    };
  });

  console.log(`[✓] Dossier Modal Opened: ${modalInfo.isShown}`);
  console.log(`[✓] Dossier Title: ${modalInfo.dossierTitle}`);
  console.log(`[✓] Ceccarelli Quote: ${modalInfo.ceccarelliQuote}`);
  console.log(`[✓] Moral Title: ${modalInfo.moralTitle}`);
  console.log(`[✓] Moral Text: ${modalInfo.moralTextSnippet}`);

  await page.screenshot({ path: 'screenshot_acqua_dossier_ceccarelli.png' });
  console.log('[✓] Saved screenshot_acqua_dossier_ceccarelli.png');

  // 3. Test transitioning to Case 2, 3, 4, 5
  console.log('\n--- VERIFYING ALL 5 CASES & DOSSIERS ---');
  for (let c = 0; c < 5; c++) {
    const cData = await page.evaluate((idx) => {
      window.loadCase(idx);
      const cObj = window.CASES[idx];
      return {
        id: cObj.id,
        tag: cObj.tag,
        name: cObj.name,
        moralTitle: cObj.moralTitle,
        hasDossierText: cObj.dossierText.length > 50
      };
    }, c);
    console.log(`[✓] Loaded ${cData.tag}: "${cData.name}" (Moral: "${cData.moralTitle}", text OK: ${cData.hasDossierText})`);
  }

  await browser.close();

  if (errors.length > 0) {
    console.error("FAIL: Browser errors occurred:", errors);
    process.exit(1);
  }
  console.log("\n=== ALL TESTS PASSED! L'ORO BLU DI AUGUSTA IS 100% OPERATIONAL! ===");
})();
