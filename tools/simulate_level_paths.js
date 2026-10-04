const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8080/');

  const analysis = await page.evaluate(() => {
    const VX = 6.7;
    const VY0 = 11.8;
    const GRAV = 27.0;
    const MAX_JUMP_H = (VY0 * VY0) / (2 * GRAV); // ~2.578

    function canJump(from, to) {
      // Platform left = p.x, right = p.x + p.w
      const fromLeft = from.x;
      const fromRight = from.x + from.w;
      const toLeft = to.x;
      const toRight = to.x + to.w;

      // Horizontal gap
      let gap = 0;
      if (toLeft > fromRight) {
        gap = toLeft - fromRight;
      } else if (fromLeft > toRight) {
        gap = fromLeft - toRight;
      }

      const dy = to.y - from.y;

      // Mechanics
      if (from.kind === 'spring' || to.kind === 'spring') {
        if (gap <= 8 && dy <= 9) return { ok: true, reason: 'spring' };
      }
      if (from.kind === 'lift' || to.kind === 'lift') {
        if (gap <= 4) return { ok: true, reason: 'lift' };
      }
      if (from.kind === 'ferry' || to.kind === 'ferry') {
        const tr = (from.travel || to.travel || 26);
        if (gap <= tr + 4) return { ok: true, reason: 'ferry' };
      }
      if (from.kind === 'zip' || to.kind === 'zip') {
        const tr = (from.travel || to.travel || 60);
        if (gap <= tr + 6) return { ok: true, reason: 'zip' };
      }

      // Normal jump upward
      if (dy > 0) {
        if (dy > MAX_JUMP_H) return { ok: false, reason: `dy ${dy.toFixed(2)} > maxH ${MAX_JUMP_H.toFixed(2)}` };
        const disc = VY0 * VY0 - 2 * GRAV * dy;
        const t = (VY0 + Math.sqrt(disc)) / GRAV;
        const maxD = VX * t;
        if (gap > maxD) return { ok: false, reason: `gap ${gap.toFixed(2)} > maxD ${maxD.toFixed(2)}` };
        return { ok: true, reason: 'jump_up' };
      }

      // Drop / jump downward
      if (dy < -16) return { ok: false, reason: `fall ${dy.toFixed(2)} too deep` };
      const disc = VY0 * VY0 - 2 * GRAV * dy;
      const t = (VY0 + Math.sqrt(disc)) / GRAV;
      const maxD = VX * t;
      if (gap > maxD) return { ok: false, reason: `gap ${gap.toFixed(2)} > fallD ${maxD.toFixed(2)}` };
      return { ok: true, reason: 'jump_down' };
    }

    const results = [];

    for (let idx = 0; idx < 6; idx++) {
      const lvl = window.J9(idx);
      const plats = lvl.platforms.filter(p => !p.spiked && p.kind !== 'hazard' && p.kind !== 'gate');
      const startPlat = plats.find(p => lvl.spawn.x >= p.x && lvl.spawn.x <= (p.x + p.w)) || plats[0];
      const goalPlat = plats.find(p => p.goal) || plats[plats.length - 1];

      // Breadth-First-Search from startPlat
      const reachable = new Set();
      const parent = new Map();
      const queue = [startPlat.id];
      reachable.add(startPlat.id);

      const platMap = new Map();
      plats.forEach(p => platMap.set(p.id, p));

      while (queue.length > 0) {
        const currId = queue.shift();
        const currPlat = platMap.get(currId);
        if (!currPlat) continue;

        for (const nextPlat of plats) {
          if (reachable.has(nextPlat.id)) continue;
          const jump = canJump(currPlat, nextPlat);
          if (jump.ok) {
            reachable.add(nextPlat.id);
            parent.set(nextPlat.id, { from: currId, reason: jump.reason });
            queue.push(nextPlat.id);
          }
        }
      }

      const isGoalReachable = reachable.has(goalPlat.id);

      // Furthest reachable platform by X + W
      let maxReachX = -Infinity;
      let furthestPlat = null;
      for (const id of reachable) {
        const p = platMap.get(id);
        if (p && (p.x + p.w) > maxReachX) {
          maxReachX = p.x + p.w;
          furthestPlat = p;
        }
      }

      // Find unreachable platforms sorted by X
      const unreachable = plats.filter(p => !reachable.has(p.id));
      unreachable.sort((a,b) => a.x - b.x);

      results.push({
        idx,
        name: lvl.name,
        short: lvl.short,
        totalWalkable: plats.length,
        reachableCount: reachable.size,
        isGoalReachable,
        startPlat: { id: startPlat.id, x: startPlat.x, right: startPlat.x + startPlat.w, y: startPlat.y },
        goalPlat: { id: goalPlat.id, x: goalPlat.x, right: goalPlat.x + goalPlat.w, y: goalPlat.y },
        furthestReached: furthestPlat ? { id: furthestPlat.id, x: furthestPlat.x, right: furthestPlat.x + furthestPlat.w, y: furthestPlat.y } : null,
        firstUnreached: unreachable.length > 0 ? {
          id: unreachable[0].id,
          x: unreachable[0].x,
          right: unreachable[0].x + unreachable[0].w,
          y: unreachable[0].y,
          gapFromFurthest: furthestPlat ? (unreachable[0].x - (furthestPlat.x + furthestPlat.w)) : null,
          dyFromFurthest: furthestPlat ? unreachable[0].y - furthestPlat.y : null
        } : null,
        unreachableList: unreachable.map(p => ({ id: p.id, x: p.x, right: p.x + p.w, y: p.y, kind: p.kind }))
      });
    }

    return results;
  });

  console.log(JSON.stringify(analysis, null, 2));
  fs.writeFileSync('tools/pathfinder_correct_bounds.json', JSON.stringify(analysis, null, 2));
  await browser.close();
})();
