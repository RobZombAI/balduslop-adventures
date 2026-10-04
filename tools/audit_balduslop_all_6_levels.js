const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--enable-webgl', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8080/?nocache=' + Date.now(), { waitUntil: 'networkidle2' });

  const audit = await page.evaluate(() => {
    const VX = 6.7;
    const VY0 = 11.8;
    const GRAV = 27.0;
    const MAX_JUMP_H = (VY0 * VY0) / (2 * GRAV); // ~2.578

    function maxJumpDistance(dy) {
      const disc = VY0 * VY0 - 2 * GRAV * dy;
      if (disc < 0) return 0;
      const t = (VY0 + Math.sqrt(disc)) / GRAV;
      return VX * t;
    }

    const report = [];

    for (let idx = 0; idx < 6; idx++) {
      const lvl = window.J9(idx);
      if (!lvl) {
        report.push({ index: idx, error: "Missing level" });
        continue;
      }

      const platforms = lvl.platforms || [];
      const enemies = lvl.enemies || [];
      const crushers = lvl.crushers || [];
      const shaping = lvl.shaping || [];
      const winds = lvl.winds || [];

      // Find all channels triggered by switches, timers, etc.
      const activeChannels = new Set();
      platforms.forEach(p => {
        if (p.kind === 'switch' && p.channel) activeChannels.add(p.channel);
        if (p.channel && (p.kind === 'balance' || p.kind === 'timed')) activeChannels.add(p.channel);
      });
      shaping.forEach(s => {
        if (s.channel) activeChannels.add(s.channel);
      });

      // Check dead gates or lifts waiting on nonexistent channels
      const deadGates = platforms.filter(p => p.kind === 'gate' && p.channel && !activeChannels.has(p.channel))
        .map(p => ({ id: p.id, channel: p.channel, x: p.x, y: p.y }));

      const deadLifts = platforms.filter(p => p.kind === 'lift' && p.channel && !activeChannels.has(p.channel))
        .map(p => ({ id: p.id, channel: p.channel, x: p.x, y: p.y }));

      // Check crushers without valid bounds
      const badCrushers = crushers.filter(c => isNaN(c.x) || isNaN(c.y) || isNaN(c.w) || isNaN(c.h));

      // Separate solid walkable platforms from hazards/spikes
      // In claybound/balduslop:
      // platforms have kind: 'stone', 'ledge', 'wood', 'lift', 'spring', 'ferry', 'timed', 'gate', 'crumble', 'balance', 'hazard'
      // spiked is boolean flag
      const walkable = platforms.filter(p => {
        if (p.spiked) return false;
        if (p.kind === 'hazard') return false;
        if (p.optional) return false; // secret paths
        if (p.kind === 'gate') return false; // vertical barrier
        if (p.kind === 'wall' && (p.h > 3 && p.w <= 2)) return false; // vertical walls
        return true;
      });

      // Sort by x
      walkable.sort((a, b) => (a.x - (a.w||0)/2) - (b.x - (b.w||0)/2));

      // Check sequential jumps along the main progression
      const jumpIssues = [];
      for (let i = 0; i < walkable.length - 1; i++) {
        const p1 = walkable[i];
        const p2 = walkable[i+1];

        const p1Right = p1.x + (p1.w || 0) / 2;
        const p2Left = p2.x - (p2.w || 0) / 2;
        const gap = p2Left - p1Right;
        const dy = p2.y - p1.y;

        const p1HasLiftOrSpring = ['lift', 'spring', 'ferry'].includes(p1.kind) || !!p1.shapeLift;
        const p2HasLiftOrSpring = ['lift', 'spring', 'ferry'].includes(p2.kind) || !!p2.shapeLift;

        // If there's an actual horizontal gap
        if (gap > 0 && !p1HasLiftOrSpring && !p2HasLiftOrSpring) {
          const maxD = maxJumpDistance(dy);
          // If dy > MAX_JUMP_H and gap > 0, player cannot jump up
          if (dy > MAX_JUMP_H) {
            jumpIssues.push({
              type: 'TOO_HIGH',
              from: { id: p1.id, kind: p1.kind, x: p1.x, y: p1.y, right: p1Right },
              to: { id: p2.id, kind: p2.kind, x: p2.x, y: p2.y, left: p2Left },
              dy: dy.toFixed(2),
              gap: gap.toFixed(2),
              maxAllowedH: MAX_JUMP_H.toFixed(2)
            });
          } else if (gap > maxD) {
            jumpIssues.push({
              type: 'TOO_FAR',
              from: { id: p1.id, kind: p1.kind, x: p1.x, y: p1.y, right: p1Right },
              to: { id: p2.id, kind: p2.kind, x: p2.x, y: p2.y, left: p2Left },
              dy: dy.toFixed(2),
              gap: gap.toFixed(2),
              maxAllowedD: maxD.toFixed(2)
            });
          } else if (gap > maxD * 0.85) {
            jumpIssues.push({
              type: 'VERY_TIGHT',
              from: { id: p1.id, kind: p1.kind, x: p1.x, y: p1.y, right: p1Right },
              to: { id: p2.id, kind: p2.kind, x: p2.x, y: p2.y, left: p2Left },
              dy: dy.toFixed(2),
              gap: gap.toFixed(2),
              maxAllowedD: maxD.toFixed(2)
            });
          }
        }
      }

      // Check enemy spawns (any falling into void or with NaN)
      const badEnemies = enemies.filter(e => isNaN(e.x) || isNaN(e.y) || e.y < -10);

      // Check goal bell
      const bell = platforms.find(p => p.kind === 'bell' || p.id?.includes('bell'));

      report.push({
        index: idx,
        name: lvl.name,
        short: lvl.short,
        biome: lvl.biome,
        spawn: lvl.spawn,
        bell: bell ? { id: bell.id, x: bell.x, y: bell.y } : 'NO_BELL_PLATFORM',
        platformCount: platforms.length,
        walkableCount: walkable.length,
        deadGates,
        deadLifts,
        badCrushers,
        badEnemies,
        jumpIssuesCount: jumpIssues.length,
        jumpIssues
      });
    }

    return report;
  });

  console.log(JSON.stringify(audit, null, 2));
  fs.writeFileSync('tools/audit_results.json', JSON.stringify(audit, null, 2));

  await browser.close();
})();
