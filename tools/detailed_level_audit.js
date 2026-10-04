const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  
  // Listen to console and page errors
  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push({ type: 'console.error', text: msg.text() });
    }
  });
  page.on('pageerror', err => {
    errors.push({ type: 'pageerror', text: err.toString() });
  });

  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });

  const auditData = await page.evaluate(async () => {
    const report = [];
    const Sc = window.Sc || [];
    
    for (let idx = 0; idx < 6; idx++) {
      const raw = Sc[idx];
      const inst = window.J9 ? window.J9(idx) : null;
      if (!inst) {
        report.push({ index: idx, error: "Cannot instantiate level" });
        continue;
      }

      // Check spawn and bell
      const spawn = inst.spawn || { x: 0, y: 0 };
      const bell = (inst.platforms || []).find(p => p.kind === 'bell' || p.id?.includes('bell')) ||
                   (inst.decor || []).find(d => d.kind?.includes('bell')) || null;
      
      const platforms = inst.platforms || [];
      const enemies = inst.enemies || [];
      const decor = inst.decor || [];
      const shaping = inst.shaping || [];
      const crushers = inst.crushers || [];
      const winds = inst.winds || [];

      // Check for platforms with invalid numbers (NaN, undefined, null)
      const invalidPlats = platforms.filter(p => 
        p.x === undefined || isNaN(p.x) ||
        p.y === undefined || isNaN(p.y) ||
        p.w === undefined || isNaN(p.w) ||
        p.h === undefined || isNaN(p.h)
      ).map(p => p.id);

      // Check switches, gates, timed
      const switches = platforms.filter(p => p.kind === 'switch');
      const gates = platforms.filter(p => p.kind === 'gate');
      const timed = platforms.filter(p => p.kind === 'timed');
      const lift = platforms.filter(p => p.kind === 'lift');
      const springs = platforms.filter(p => p.kind === 'spring');

      const switchChannels = new Set(switches.map(s => s.channel).filter(Boolean));
      // Some levels use shaping or buttons for channels too
      (shaping || []).forEach(s => { if (s.channel) switchChannels.add(s.channel); });

      const deadGates = gates.filter(g => g.channel && !switchChannels.has(g.channel)).map(g => ({ id: g.id, channel: g.channel }));
      const deadTimed = timed.filter(t => t.channel && !switchChannels.has(t.channel)).map(t => ({ id: t.id, channel: t.channel }));

      // Check for overlapping / duplicate platform IDs
      const idMap = new Map();
      const duplicateIds = [];
      platforms.forEach(p => {
        if (!p.id) return;
        if (idMap.has(p.id)) duplicateIds.push(p.id);
        idMap.set(p.id, true);
      });

      // Analyze connectivity along the level
      // Find bounding box
      const minX = Math.min(...platforms.map(p => p.x - (p.w||0)/2));
      const maxX = Math.max(...platforms.map(p => p.x + (p.w||0)/2));
      const minY = Math.min(...platforms.map(p => p.y - (p.h||0)/2));
      const maxY = Math.max(...platforms.map(p => p.y + (p.h||0)/2));

      // Let's test game engine simulation of running level
      let simulation = { ok: false };
      try {
        if (window.__START_LEVEL__) {
          window.__START_LEVEL__(idx);
          // Allow small tick
          const ce = window.__GAME_CE__;
          if (ce && ce.level) {
            simulation = {
              ok: true,
              levelName: ce.level.name,
              playerSpawn: { x: ce.player.x, y: ce.player.y },
              status: ce.status,
              groundId: ce.player.groundId
            };
          }
        }
      } catch (simErr) {
        simulation = { ok: false, error: simErr.message };
      }

      report.push({
        index: idx,
        name: inst.name,
        short: inst.short,
        biome: inst.biome,
        spawn,
        bounds: { minX: Math.round(minX), maxX: Math.round(maxX), minY: Math.round(minY), maxY: Math.round(maxY) },
        counts: {
          platforms: platforms.length,
          enemies: enemies.length,
          decor: decor.length,
          shaping: shaping.length,
          crushers: crushers.length,
          winds: winds.length,
          coins: (inst.coins || []).length,
          stamps: (inst.stamps || []).length
        },
        invalidPlats,
        duplicateIds,
        deadGates,
        deadTimed,
        simulation
      });
    }

    return report;
  });

  console.log("=== LEVEL REPORT ===");
  console.log(JSON.stringify(auditData, null, 2));

  if (errors.length > 0) {
    console.log("=== BROWSER ERRORS ===");
    console.log(JSON.stringify(errors, null, 2));
  } else {
    console.log("=== ZERO BROWSER ERRORS ===");
  }

  await browser.close();
})();
