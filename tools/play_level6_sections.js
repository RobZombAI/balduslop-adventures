const puppeteer = require("puppeteer-core");

(async () => {
  const browser = await puppeteer.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });
  const page = await browser.newPage();
  await page.goto("http://localhost:8080/?nocache=" + Date.now(), { waitUntil: "networkidle2" });

  const results = await page.evaluate(async () => {
    await window.__START_LEVEL__(5);
    await new Promise(r => setTimeout(r, 400));
    const ce = window.__GAME_CE__;

    const sections = [
      { name: "Section 0: The Crooked Garden", startX: 1.5, startY: 0, endX: 97, groundId: "start" },
      { name: "Section 1: The Folding Path", startX: 99.0, startY: 0, endX: 207, groundId: "folding-entry" },
      { name: "Section 2: The Upside-Down Orchard", startX: 209.0, startY: 0, endX: 282, groundId: "orchard-entry" },
      { name: "Section 3: The Breathing Corridor", startX: 284.0, startY: 0, endX: 365, groundId: "corridor-entry" },
      { name: "Section 4: The Infinite Room", startX: 367.0, startY: 0, endX: 485, groundId: "room-entry" },
      { name: "Section 5: The Dream Knot", startX: 487.0, startY: 0, endX: 580, groundId: "knot-entry" }
    ];

    const report = [];

    for (const sec of sections) {
      ce.checkpoint = { x: sec.startX, y: sec.startY };
      ce.player.x = sec.startX;
      ce.player.y = sec.startY;
      ce.player.vx = 0;
      ce.player.vy = 0;
      ce.player.groundId = sec.groundId;
      ce.player.coyote = 0.135;
      ce.deaths = 0;

      let reached = false;
      let maxX = sec.startX;
      let failurePoint = null;

      // Smart traversal: look ahead to find target platforms and jump/move towards them
      for (let f = 0; f < 1800; f++) {
        const px = ce.player.x;
        const py = ce.player.y;
        if (px > maxX) maxX = px;

        if (px >= sec.endX) {
          reached = true;
          break;
        }

        // Find upcoming platforms
        const ahead = ce.level.platforms
          .filter(p => p.kind !== "wall" && p.kind !== "hazard" && !p.spiked && p.x + p.w > px - 1 && p.x < px + 15)
          .sort((a, b) => a.x - b.x);

        const currentGround = ce.level.platforms.find(p => p.id === ce.player.groundId);
        const nextPlat = ahead.find(p => p.x > (currentGround ? currentGround.x + 0.5 : px));

        let jumpPressed = false;
        let jumpHeld = ce.player.vy > 0;
        let dir = 1;

        if (nextPlat) {
          const dist = nextPlat.x - px;
          const dy = nextPlat.y - py;
          // Jump if approaching edge or if target is higher
          if (dist > 0.5 && dist < 4.0 && dy > -1.0) {
            jumpPressed = dist < 2.5 || (currentGround && px > currentGround.x + currentGround.w - 1.2);
          } else if (dist <= 0.5 && dy > 0.5) {
            jumpPressed = true;
          }
        } else {
          jumpPressed = f % 30 === 0;
        }

        // Periodic jump if stuck
        if (ce.player.groundId && Math.abs(ce.player.vx) < 0.2) {
          jumpPressed = true;
        }

        ce.tick(1/60, {
          right: dir > 0,
          left: dir < 0,
          jumpPressed,
          jumpHeld
        });

        if (ce.deaths > 5) {
          failurePoint = { x: ce.player.x, y: ce.player.y, groundId: ce.player.groundId, reason: "Excessive deaths" };
          break;
        }
      }

      if (!reached && !failurePoint) {
        failurePoint = { x: ce.player.x, y: ce.player.y, groundId: ce.player.groundId, reason: "Timed out / blocked" };
      }

      report.push({
        section: sec.name,
        reached,
        maxX: Math.round(maxX * 10) / 10,
        targetX: sec.endX,
        failurePoint
      });
    }

    return report;
  });

  console.log("SECTION RESULTS:\n", JSON.stringify(results, null, 2));
  await browser.close();
})();
