# tools/generate_all_10_levels.py
"""
Generates all 10 unique, authentic Augusta (SR) levels,
custom 3D decor models, and integrates them into bundle/index-augusta-v2.js.
"""

import re
import json

def get_level_1():
    return """const augustaL1 = yr({
  layoutVersion: 1,
  name: "Il Polo Petrolchimico di Augusta",
  short: "Petrolchimico",
  label: "Ciminiere, torce e fumi industriali",
  biome: "desert",
  intro: "Benvenuto al polo petrolchimico di Augusta-Priolo. Tra ciminiere fumanti, valvole di pressione e tubature di greggio, scappa dalla raffineria prima che la pressione salga al massimo!",
  sky: "#2d2016",
  fog: "#453225",
  spawn: {x: 1.5, y: 13},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Raffineria & Conduttura Greggio", landmark: "beacon"},
    {x: 50, name: "2. Le Torce di Combustione (Flares)", landmark: "pulsedrum"},
    {x: 105, name: "3. Pipe-Rack delle Tubature Aeree", landmark: "bannerarch"},
    {x: 165, name: "4. Serbatoi di Stoccaggio Petrolio", landmark: "sandwheel"},
    {x: 215, name: "5. Banchina di Scarico Raffineria", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 13, "stone", {landmark: "beacon"}),
    S("lift-pipe1", 10, 3.6, 13.5, "lift", {moveY: 2.4, period: 4.0}),
    S("plat-refinery", 15, 6.5, 14.5, "stone"),
    S("step-valves", 23, 3.4, 15.6, "ledge"),
    S("lift-worker", 28, 3.5, 14.8, "lift", {moveX: 2.8, period: 4.5}),
    S("plat-conduit", 33, 7.5, 15.2, "stone"),
    S("pit-spikes-1", 7, 38, 2.0, "stone", {spiked: !0}),

    S("opt-pr1", 42, 3.5, 17.5, "ledge", {optional: !0}),
    S("spring-pr1", 43, 2.0, 15.2, "spring"),
    S("dock-flares", 48, 7, 15.2, "stone", {checkpoint: 50, depth: 22, landmark: "pulsedrum"}),
    S("crumble-flare1", 57, 4.2, 14.8, "crumble"),
    S("plat-steam", 63, 6, 14.2, "stone"),
    S("ferry-slop", 71, 4.5, 13.8, "ferry", {travel: 18, speed: 3.2}),
    S("plat-dockside", 91, 7, 13.8, "stone"),
    S("pit-spikes-2", 50, 52, 2.0, "stone", {spiked: !0}),

    S("dock-piperack", 104, 7, 11.2, "stone", {checkpoint: 106, depth: 22, landmark: "bannerarch"}),
    S("balance-tank1", 113, 7, 11.8, "balance"),
    S("step-cross", 122, 3.8, 12.8, "ledge"),
    S("step-pr2", 126, 3.2, 15.5, "ledge"),
    S("balance-tank2", 128, 7.5, 13.8, "balance"),
    S("opt-pr2", 133, 3.5, 18.5, "ledge", {optional: !0}),
    S("lift-boiler", 138, 3.6, 13.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-valvefloor", 145, 22, 16.2, "stone", {landmark: "beacon"}),
    S("switch-safety", 153, 2.2, 16.35, "switch", {channel: "flare-lock", latch: !0}),
    S("gate-safety", 160, 1.8, 20.2, "gate", {channel: "flare-lock", h: 4}),

    S("dock-tanks", 165, 7, 16.2, "stone", {checkpoint: 167, depth: 22, landmark: "sandwheel"}),
    S("pulse-pipe1", 174, 3.8, 15.6, "pulse", {period: 4.2, phase: 0}),
    S("pulse-pipe2", 180, 3.8, 15.6, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-tanker", 186, 6, 14.8, "stone"),
    S("step-pr3", 197, 3.2, 18.2, "ledge"),
    S("lift-chimney", 194, 3.6, 14.2, "lift", {moveX: 2.6, moveY: 1.8, period: 5.0}),
    S("opt-pr3", 202, 3.5, 20.5, "ledge", {optional: !0}),
    S("spring-pr3", 203, 2.0, 15.8, "spring"),
    S("plat-dike", 201, 8, 15.8, "stone", {landmark: "sandwheel"}),
    S("pit-spikes-3", 167, 45, 4.0, "stone", {spiked: !0}),

    S("dock-jetty", 213, 7, 15.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-dock1", 222, 3.8, 16.8, "ledge"),
    S("step-dock2", 228, 4.2, 17.8, "ledge"),
    S("goal-production", 234, 14, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 38, y: 2.0},
    {x: 50, w: 52, y: 2.0},
    {x: 167, w: 45, y: 4.0}
  ],
  decor: [
    {kind: "pipe", x: 10, y: 13, size: 6, z: -3},
    {kind: "pipe-elbow", x: 25, y: 13.5, size: 2.6, z: -3},
    {kind: "pipe-arch", x: 48, y: 13.8, size: 10, z: -3.4},
    {kind: "flare-stack", x: 54, y: 15.2, size: 12, z: -4},
    {kind: "furnace", x: 60, y: 10, size: 6, z: -4},
    {kind: "furnace-vent", x: 62, y: 14.5, size: 2.5, z: -5},
    {kind: "smoke", x: 63, y: 16, size: 1.5, z: -4.5},
    {kind: "valve", x: 72, y: 11.2, size: 1.55, z: -2.2},
    {kind: "pipe", x: 80, y: 9, size: 6, z: -3},
    {kind: "pipe", x: 110, y: 11, size: 6, z: -3},
    {kind: "oil-tank", x: 120, y: 11.8, size: 5, z: -4},
    {kind: "smoke", x: 123, y: 17, size: 1.5, z: -4.5},
    {kind: "pipe-arch", x: 106, y: 11.2, size: 10, z: -3.4},
    {kind: "scaffold", x: 134, y: 13.5, size: 3, z: -2.4},
    {kind: "caged-lamp", x: 146, y: 16.2, size: 0.7, z: -1.6},
    {kind: "pipe", x: 150, y: 16.2, size: 6, z: -3},
    {kind: "oil-tank", x: 172, y: 16.2, size: 5.5, z: -4},
    {kind: "pipe-arch", x: 168, y: 16.2, size: 10, z: -3.4},
    {kind: "furnace", x: 185, y: 13, size: 6, z: -4},
    {kind: "smoke", x: 188, y: 19, size: 1.5, z: -4.5},
    {kind: "caged-lamp", x: 214, y: 15.8, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Fuga dal Petrolchimico", text: "Inizia la corsa tra gli impianti di Augusta! Salta sulle condutture di metallo con Spazio. Raccogli le gocce d'oro di carburante.", touchText: "Inizia la corsa tra gli impianti di Augusta! Usa il joystick e SALTA per superare le condutture."},
    {x: 50, end: 65, icon: "sink", title: "Torce e Passerelle Fragili", text: "Le passerelle esposte al calore delle ciminiere si sgretolano: non fermarti troppo a lungo! Usa la molla di vapore per il timbro segreto."},
    {x: 106, end: 125, icon: "knead", title: "Bilanciamento Cisterne", text: "Le piattaforme a bascula sopra i serbatoi oscillano con il tuo peso. Mantieni il baricentro!"},
    {x: 150, end: 164, icon: "walk", title: "Valvola di Sicurezza", text: "Premi l'interruttore sulla passerella (camminandoci sopra o saltando) per abbassare la paratia tagliafuoco."},
    {x: 167, end: 185, icon: "drop", title: "Valvole a Pressione", text: "Le piattaforme a vapore pulsano a intervalli regolari. Usa STOMP (S o tasto STOMP) per scendere rapidamente!", touchText: "Le piattaforme pulsano a intervalli regolari. Premi il tasto STOMP per scendere in picchiata!"},
    {x: 215, end: 242, icon: "bell", title: "Banchina di Scarico", text: "Suona la Campana della Raffineria per completare la fuga dal Petrolchimico!"}
  ],
  coins: [
    {x: 6, y: 15.5}, {x: 10, y: 15.5}, {x: 17, y: 16.5}, {x: 19, y: 16.5},
    {x: 24, y: 15}, {x: 29, y: 15.5}, {x: 37, y: 16}, {x: 39, y: 16},
    {x: 56, y: 15}, {x: 62, y: 14.5}, {x: 68, y: 13.5},
    {x: 76, y: 13.5}, {x: 82, y: 13.5}, {x: 88, y: 13.5}, {x: 95, y: 13.5},
    {x: 115, y: 14}, {x: 118, y: 14}, {x: 124, y: 15},
    {x: 130, y: 16}, {x: 134, y: 16}, {x: 147, y: 18}, {x: 150, y: 18},
    {x: 176, y: 17.5}, {x: 182, y: 17.5}, {x: 188, y: 17},
    {x: 196, y: 17}, {x: 204, y: 18}, {x: 224, y: 19}, {x: 230, y: 20},
    {x: 236, y: 21}, {x: 239, y: 21}
  ],
  stamps: [
    {x: 43.5, y: 19.5},
    {x: 134.5, y: 20.5},
    {x: 203.5, y: 22.5}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_2():
    return """const augustaL2 = yr({
  layoutVersion: 1,
  name: "La Rada di Augusta & Pontili al Mercurio",
  short: "Porto Mercurio",
  label: "Pontili sospesi, chiatte industriali e acque scure",
  biome: "nightfall",
  intro: "Sei fuggito dalla raffineria, ma ora devi attraversare la rada industriale di Augusta. Le acque sono sature di mercurio e cloro-soda: salta tra pontili di carico, chiatte a fune e imponenti gru navali!",
  sky: "#131f2b",
  fog: "#1f3142",
  spawn: {x: 1.5, y: 11},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Calata delle Navi Cisterna", landmark: "beacon"},
    {x: 48, name: "2. Il Canale al Mercurio", landmark: "pulsedrum"},
    {x: 102, name: "3. Gru Navali & Pontili Galleggianti", landmark: "bannerarch"},
    {x: 162, name: "4. La Chiatta Mercantile Megara", landmark: "sandwheel"},
    {x: 212, name: "5. Molo di Scarico Nord", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 11, "stone", {landmark: "beacon"}),
    S("step-pier1", 10, 4.2, 11.8, "ledge"),
    S("plat-quay", 16, 7.5, 12.6, "stone"),
    S("crane-lift1", 26, 3.8, 13.0, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-pierhead", 32, 6.5, 13.8, "stone"),
    S("spring-port1", 41, 2.0, 13.8, "spring"),
    S("opt-port1", 40, 3.6, 17.8, "ledge", {optional: !0}),
    S("pit-mercury-1", 7, 40, 1.5, "stone", {spiked: !0}),

    S("dock-channel", 46, 7.5, 13.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-gangway1", 56, 4.8, 13.2, "stone"),
    S("ferry-mercury", 63, 5.5, 12.6, "ferry", {travel: 24, speed: 3.4}),
    S("plat-crane-isle", 90, 8.0, 12.6, "stone"),
    S("pit-mercury-2", 52, 48, 1.5, "stone", {spiked: !0}),

    S("dock-cranes", 100, 7.0, 12.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("crane-jib1", 109, 8.0, 13.2, "balance"),
    S("step-trolley", 119, 3.8, 14.2, "ledge"),
    S("step-port2", 125, 3.2, 16.8, "ledge"),
    S("crane-jib2", 127, 8.0, 15.2, "balance"),
    S("opt-port2", 133, 3.6, 20.0, "ledge", {optional: !0}),
    S("lift-gantry", 138, 3.6, 14.8, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-dockgate-floor", 144, 22, 16.0, "stone", {landmark: "beacon"}),
    S("switch-dockgate", 152, 2.2, 16.15, "switch", {channel: "dock-lock", latch: !0}),
    S("gate-dock", 159, 1.8, 20.0, "gate", {channel: "dock-lock", h: 4}),

    S("dock-barge", 163, 7.5, 16.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-wharf1", 173, 4.0, 15.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-wharf2", 179, 4.0, 15.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-tanker-deck", 185, 6.5, 14.6, "stone"),
    S("step-port3", 196, 3.2, 17.8, "ledge"),
    S("lift-winch", 193, 3.6, 14.0, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-port3", 201, 3.5, 20.2, "ledge", {optional: !0}),
    S("spring-port3", 202, 2.0, 15.6, "spring"),
    S("plat-seawall", 200, 8.5, 15.6, "stone", {landmark: "sandwheel"}),
    S("pit-mercury-3", 168, 44, 2.5, "stone", {spiked: !0}),

    S("dock-exit", 212, 7.0, 15.6, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-rock1", 221, 3.8, 16.6, "ledge"),
    S("step-rock2", 227, 4.2, 17.6, "ledge"),
    S("goal-harbor", 233, 14, 18.6, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 1.5},
    {x: 52, w: 48, y: 1.5},
    {x: 168, w: 44, y: 2.5}
  ],
  decor: [
    {kind: "cargo-ship", x: 75, y: 8.5, size: 22, z: -14},
    {kind: "crane-tower", x: 30, y: 13.8, size: 9, z: -3.5},
    {kind: "crane-tower", x: 112, y: 12.6, size: 9.5, z: -3.5},
    {kind: "hazard-barrel", x: 18, y: 12.6, size: 1.2, z: -1.2},
    {kind: "hazard-barrel", x: 20, y: 12.6, size: 1.2, z: -1.0},
    {kind: "caged-lamp", x: 16, y: 12.6, size: 0.7, z: -1.6},
    {kind: "caged-lamp", x: 48, y: 13.8, size: 0.7, z: -1.6},
    {kind: "scaffold", x: 56, y: 13.2, size: 3, z: -2.4},
    {kind: "pipe-arch", x: 92, y: 12.6, size: 10, z: -3.4},
    {kind: "caged-lamp", x: 102, y: 12.6, size: 0.7, z: -1.6},
    {kind: "scaffold", x: 146, y: 16.0, size: 3, z: -2.4},
    {kind: "caged-lamp", x: 164, y: 16.0, size: 0.7, z: -1.6},
    {kind: "hazard-barrel", x: 186, y: 14.6, size: 1.2, z: -1.2},
    {kind: "caged-lamp", x: 214, y: 15.6, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Rada di Augusta", text: "Salta tra i pontili della rada. Le acque scure sono piene di mercurio chimico: un solo tuffo è letale!", touchText: "Salta tra i pontili della rada con cautela: non cadere nelle acque al mercurio!"},
    {x: 48, end: 66, icon: "knead", title: "La Chiatta Salmastra", text: "Sali sulla chiatta a fune: ti trasporterà automaticamente oltre il canale delle navi cisterna."},
    {x: 102, end: 125, icon: "knead", title: "Bracci delle Gru Meccaniche", text: "Le travi delle gru portuali oscillano sotto il tuo peso. Mantieni l'equilibrio al centro!"},
    {x: 146, end: 160, icon: "walk", title: "Chiusa del Molo", text: "Attiva l'interruttore metallico sul pontile per abbassare la pesante saracinesca d'ormeggio."},
    {x: 212, end: 240, icon: "bell", title: "Faro del Molo Nord", text: "Suona la campana navale per uscire dalla rada di mercurio e raggiungere la costa!"}
  ],
  coins: [
    {x: 8, y: 13.5}, {x: 12, y: 13.5}, {x: 18, y: 14.5}, {x: 21, y: 14.5},
    {x: 28, y: 15.5}, {x: 34, y: 15.5}, {x: 41, y: 16.0}, {x: 58, y: 14.5},
    {x: 68, y: 14.0}, {x: 74, y: 14.0}, {x: 80, y: 14.0}, {x: 86, y: 14.0},
    {x: 104, y: 14.5}, {x: 111, y: 15.0}, {x: 115, y: 15.0}, {x: 121, y: 16.0},
    {x: 129, y: 17.5}, {x: 147, y: 17.5}, {x: 154, y: 17.5}, {x: 166, y: 17.5},
    {x: 175, y: 17.0}, {x: 181, y: 17.0}, {x: 187, y: 16.5}, {x: 195, y: 16.5},
    {x: 204, y: 17.5}, {x: 223, y: 18.5}, {x: 229, y: 19.5}, {x: 235, y: 20.5}
  ],
  stamps: [
    {x: 41.0, y: 19.5},
    {x: 134.5, y: 21.8},
    {x: 202.5, y: 22.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_3():
    return """const augustaL3 = yr({
  layoutVersion: 1,
  name: "La Penisola delle Ceneri di Pirite",
  short: "Ceneri di Pirite",
  label: "Montagne rosse, fumarole e scorie solforose",
  biome: "desert",
  intro: "La famigerata penisola delle ceneri di pirite: milioni di tonnellate di polvere rossa tossica e scorie ferrose affacciate sul mare. Le passerelle franano e dai crateri eruttano violenti geyser di vapore solforoso!",
  sky: "#4a1810",
  fog: "#682416",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. I Gradoni di Cenere Rossa", landmark: "beacon"},
    {x: 48, name: "2. Il Cratere Solforoso", landmark: "pulsedrum"},
    {x: 102, name: "3. Fumarole & Geyser di Vapore", landmark: "bannerarch"},
    {x: 162, name: "4. Scivoli di Scorie Tossiche", landmark: "sandwheel"},
    {x: 212, name: "5. Il Belvedere sulle Colline Rosse", landmark: "bellgate"}
  ],
  winds: [
    {x: 108, w: 6, y: 12, h: 10, dir: "up"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-pyrite1", 10, 4.0, 13.0, "ledge"),
    S("plat-terrace1", 16, 7.0, 14.0, "stone"),
    S("crumble-red1", 25, 4.2, 14.5, "crumble"),
    S("plat-terrace2", 31, 7.5, 14.8, "stone"),
    S("spring-ash1", 40, 2.0, 14.8, "spring"),
    S("opt-ash1", 39, 3.6, 19.0, "ledge", {optional: !0}),
    S("pit-ash-1", 7, 39, 2.0, "stone", {spiked: !0}),

    S("dock-crater", 46, 7.5, 14.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("crumble-crater1", 56, 4.2, 14.5, "crumble"),
    S("crumble-crater2", 62, 4.2, 14.0, "crumble"),
    S("plat-geyser-base", 68, 6.5, 13.6, "stone"),
    S("lift-sulfur", 77, 3.8, 13.2, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-ridge", 83, 7.5, 13.6, "stone"),
    S("pit-ash-2", 52, 48, 2.0, "stone", {spiked: !0}),

    S("dock-fumaroles", 100, 7.0, 13.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("geyser-vent", 108, 6.0, 12.0, "stone"),
    S("step-ash2", 116, 3.8, 16.5, "ledge"),
    S("crumble-hot1", 122, 4.2, 15.8, "crumble"),
    S("balance-ash1", 128, 7.5, 15.0, "balance"),
    S("opt-ash2", 134, 3.5, 19.8, "ledge", {optional: !0}),
    S("lift-cinder", 138, 3.6, 14.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-ashgate-floor", 144, 22, 16.2, "stone", {landmark: "beacon"}),
    S("switch-ashgate", 152, 2.2, 16.35, "switch", {channel: "ash-lock", latch: !0}),
    S("gate-ash", 159, 1.8, 20.2, "gate", {channel: "ash-lock", h: 4}),

    S("dock-slags", 163, 7.5, 16.2, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-steam1", 173, 4.0, 15.6, "pulse", {period: 4.2, phase: 0}),
    S("pulse-steam2", 179, 4.0, 15.6, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-slag-dike", 185, 6.5, 15.0, "stone"),
    S("step-ash3", 196, 3.2, 18.2, "ledge"),
    S("lift-pyramid", 193, 3.6, 14.4, "lift", {moveX: 2.8, moveY: 1.8, period: 5.0}),
    S("opt-ash3", 201, 3.5, 20.5, "ledge", {optional: !0}),
    S("spring-ash3", 202, 2.0, 15.8, "spring"),
    S("plat-redhill", 200, 8.5, 15.8, "stone", {landmark: "sandwheel"}),
    S("pit-ash-3", 168, 44, 3.0, "stone", {spiked: !0}),

    S("dock-belvedere", 212, 7.0, 15.8, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-cinder1", 221, 3.8, 16.8, "ledge"),
    S("step-cinder2", 227, 4.2, 17.8, "ledge"),
    S("goal-pyrite", 233, 14, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 39, y: 2.0},
    {x: 52, w: 48, y: 2.0},
    {x: 168, w: 44, y: 3.0}
  ],
  decor: [
    {kind: "boulder", x: 18, y: 14.0, size: 2.5, z: -1.5},
    {kind: "pebbles", x: 22, y: 14.0, size: 1.5, z: 1.0},
    {kind: "hazard-barrel", x: 34, y: 14.8, size: 1.2, z: -1.2},
    {kind: "cactus-opuntia", x: 48, y: 14.8, size: 2.2, z: -1.5},
    {kind: "smoke", x: 50, y: 16.0, size: 1.5, z: -4.0},
    {kind: "smoke", x: 70, y: 15.0, size: 2.0, z: -3.5},
    {kind: "furnace-vent", x: 72, y: 13.6, size: 2.5, z: -5.0},
    {kind: "hazard-barrel", x: 86, y: 13.6, size: 1.2, z: -1.0},
    {kind: "boulder", x: 104, y: 13.6, size: 3.0, z: -2.0},
    {kind: "smoke", x: 110, y: 16.0, size: 2.5, z: -3.0},
    {kind: "cactus-opuntia", x: 146, y: 16.2, size: 2.2, z: -1.5},
    {kind: "caged-lamp", x: 165, y: 16.2, size: 0.7, z: -1.6},
    {kind: "hazard-barrel", x: 186, y: 15.0, size: 1.2, z: -1.2},
    {kind: "boulder", x: 204, y: 15.8, size: 2.8, z: -1.5},
    {kind: "cactus-opuntia", x: 214, y: 15.8, size: 2.2, z: -1.5}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Ceneri di Pirite", text: "Le colline rosse sono friabili: molte piattaforme crollano appena ci poggi i piedi. Muoviti senza esitazione!"},
    {x: 48, end: 68, icon: "sink", title: "Passerelle Franabili", text: "Le ceneri cedono sotto il tuo peso. Corri e salta rapidamente tra i gradoni di pirite."},
    {x: 102, end: 120, icon: "updraft", title: "Geyser di Vapore Solforoso", text: "Entra nella colonna di fumo del geyser: la violenta corrente calda ti sparerà in alto verso la cima!"},
    {x: 146, end: 160, icon: "walk", title: "Saracinesca Solforosa", text: "Premi l'interruttore sulla passerella per sbloccare la paratia antiriflusso."},
    {x: 212, end: 240, icon: "bell", title: "Belvedere sulle Montagne Rosse", text: "Suona la campana di vetta per completare la traversata delle ceneri tossiche!"}
  ],
  coins: [
    {x: 8, y: 14.5}, {x: 12, y: 14.5}, {x: 18, y: 15.5}, {x: 22, y: 15.5},
    {x: 27, y: 16.0}, {x: 33, y: 16.0}, {x: 40, y: 16.5}, {x: 58, y: 15.5},
    {x: 64, y: 15.0}, {x: 70, y: 15.0}, {x: 79, y: 15.0}, {x: 85, y: 15.0},
    {x: 104, y: 15.0}, {x: 110, y: 18.0}, {x: 112, y: 20.0}, {x: 118, y: 18.0},
    {x: 124, y: 17.5}, {x: 130, y: 17.0}, {x: 148, y: 17.5}, {x: 154, y: 17.5},
    {x: 166, y: 17.5}, {x: 175, y: 17.0}, {x: 181, y: 17.0}, {x: 187, y: 16.5},
    {x: 195, y: 16.5}, {x: 204, y: 17.5}, {x: 223, y: 18.5}, {x: 229, y: 19.5}, {x: 235, y: 20.5}
  ],
  stamps: [
    {x: 40.0, y: 20.5},
    {x: 135.5, y: 21.5},
    {x: 202.5, y: 22.2}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_4():
    return """const augustaL4 = yr({
  layoutVersion: 1,
  name: "Le Condotte Fognarie & Canali Industriali",
  short: "Fognature",
  label: "Collettori sotterranei, saracinesche e reflui chimici",
  biome: "cave",
  intro: "Scendi nel ventre sotterraneo di Augusta: un labirinto di collettori in cemento armato e condotte di scarico chimico. Le chiuse idrauliche funzionano a tempo e la melma verde è altamente corrosiva!",
  sky: "#0a120e",
  fog: "#12241a",
  spawn: {x: 1.5, y: 10},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Il Collettore Principale", landmark: "beacon"},
    {x: 48, name: "2. Le Chiuse a Paratia Temporizzata", landmark: "pulsedrum"},
    {x: 102, name: "3. La Vasca di Decantazione Melme", landmark: "bannerarch"},
    {x: 162, name: "4. Sifone di Scarico a Mare", landmark: "sandwheel"},
    {x: 212, name: "5. Lo Sbocco Fognario Costiero", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 10, "stone", {landmark: "beacon"}),
    S("step-sewer1", 10, 4.0, 11.0, "ledge"),
    S("plat-collector", 16, 7.5, 11.8, "stone"),
    S("lift-effluent", 26, 3.8, 12.0, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-pipewalk", 32, 6.5, 12.8, "stone"),
    S("spring-sewer1", 41, 2.0, 12.8, "spring"),
    S("opt-sewer1", 40, 3.6, 16.8, "ledge", {optional: !0}),
    S("pit-sludge-1", 7, 40, 1.0, "stone", {spiked: !0}),

    S("dock-sluice", 46, 7.5, 12.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-conduit-floor", 56, 18, 13.0, "stone"),
    S("switch-timed1", 62, 2.2, 13.15, "switch", {channel: "timed-sluice", duration: 8}),
    S("gate-sluice1", 71, 1.8, 17.0, "gate", {channel: "timed-sluice", h: 4}),
    S("plat-overflow", 76, 7.5, 13.0, "stone"),
    S("lift-sump", 86, 3.8, 12.5, "lift", {moveX: 2.8, period: 4.5}),
    S("plat-settling", 92, 7.5, 12.5, "stone"),
    S("pit-sludge-2", 52, 48, 1.0, "stone", {spiked: !0}),

    S("dock-basin", 100, 7.0, 12.5, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-sewer1", 109, 8.0, 13.0, "balance"),
    S("step-grate1", 119, 3.8, 14.0, "ledge"),
    S("step-sewer2", 125, 3.2, 16.6, "ledge"),
    S("balance-sewer2", 127, 8.0, 14.8, "balance"),
    S("opt-sewer2", 133, 3.6, 19.6, "ledge", {optional: !0}),
    S("lift-screen", 138, 3.6, 14.2, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-sewergate-floor", 144, 22, 15.5, "stone", {landmark: "beacon"}),
    S("switch-sewergate", 152, 2.2, 15.65, "switch", {channel: "sewer-lock", latch: !0}),
    S("gate-sewer", 159, 1.8, 19.5, "gate", {channel: "sewer-lock", h: 4}),

    S("dock-siphon", 163, 7.5, 15.5, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-sewer1", 173, 4.0, 14.8, "pulse", {period: 4.2, phase: 0}),
    S("pulse-sewer2", 179, 4.0, 14.8, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-outfall", 185, 6.5, 14.0, "stone"),
    S("step-sewer3", 196, 3.2, 17.2, "ledge"),
    S("lift-culvert", 193, 3.6, 13.5, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-sewer3", 201, 3.5, 19.5, "ledge", {optional: !0}),
    S("spring-sewer3", 202, 2.0, 15.0, "spring"),
    S("plat-coast-drain", 200, 8.5, 15.0, "stone", {landmark: "sandwheel"}),
    S("pit-sludge-3", 168, 44, 2.0, "stone", {spiked: !0}),

    S("dock-outlet", 212, 7.0, 15.0, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-out1", 221, 3.8, 16.0, "ledge"),
    S("step-out2", 227, 4.2, 17.0, "ledge"),
    S("goal-sewer", 233, 14, 18.0, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 1.0},
    {x: 52, w: 48, y: 1.0},
    {x: 168, w: 44, y: 2.0}
  ],
  decor: [
    {kind: "pipe", x: 10, y: 10, size: 6, z: -3},
    {kind: "pipe-arch", x: 18, y: 11.8, size: 10, z: -3.4},
    {kind: "caged-lamp", x: 16, y: 11.8, size: 0.7, z: -1.6},
    {kind: "hazard-barrel", x: 34, y: 12.8, size: 1.2, z: -1.2},
    {kind: "valve", x: 48, y: 12.8, size: 1.55, z: -2.2},
    {kind: "pipe-elbow", x: 60, y: 13.0, size: 2.6, z: -3},
    {kind: "pipe", x: 74, y: 13.0, size: 6, z: -3},
    {kind: "caged-lamp", x: 92, y: 12.5, size: 0.7, z: -1.6},
    {kind: "pipe-arch", x: 106, y: 12.5, size: 10, z: -3.4},
    {kind: "shelf", x: 120, y: 11.0, size: 4, z: 2.5},
    {kind: "hazard-barrel", x: 146, y: 15.5, size: 1.2, z: -1.2},
    {kind: "caged-lamp", x: 164, y: 15.5, size: 0.7, z: -1.6},
    {kind: "pipe", x: 186, y: 14.0, size: 6, z: -3},
    {kind: "valve", x: 202, y: 15.0, size: 1.55, z: -2.2},
    {kind: "caged-lamp", x: 214, y: 15.0, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Condotte Fognarie", text: "Sei nei canali di scolo sotterranei di Augusta. Le acque melmose sul fondo sono cariche di scarti chimici!"},
    {x: 48, end: 68, icon: "timer", title: "Chiusa a Tempo", text: "Premi l'interruttore della paratia: hai 8 secondi per superare la porta prima che si richiuda!"},
    {x: 102, end: 125, icon: "knead", title: "Vasche di Decantazione", text: "Le griglie metalliche oscillano sotto il flusso dei reflui. Salta con ritmo regolare."},
    {x: 146, end: 160, icon: "walk", title: "Valvola del Collettore", text: "Premi la valvola sulla passerella per abbassare la grata di sicurezza."},
    {x: 212, end: 240, icon: "bell", title: "Sbocco Costiero", text: "Suona la campana dello sbocco a mare per riemergere alla luce del sole!"}
  ],
  coins: [
    {x: 8, y: 12.5}, {x: 12, y: 12.5}, {x: 18, y: 13.5}, {x: 22, y: 13.5},
    {x: 28, y: 14.5}, {x: 34, y: 14.5}, {x: 41, y: 15.0}, {x: 58, y: 14.5},
    {x: 64, y: 14.5}, {x: 70, y: 14.5}, {x: 78, y: 14.5}, {x: 88, y: 14.0},
    {x: 104, y: 14.0}, {x: 111, y: 14.5}, {x: 115, y: 14.5}, {x: 121, y: 15.5},
    {x: 129, y: 16.5}, {x: 147, y: 17.0}, {x: 154, y: 17.0}, {x: 166, y: 17.0},
    {x: 175, y: 16.5}, {x: 181, y: 16.5}, {x: 187, y: 16.0}, {x: 195, y: 16.0},
    {x: 204, y: 17.0}, {x: 223, y: 17.5}, {x: 229, y: 18.5}, {x: 235, y: 19.5}
  ],
  stamps: [
    {x: 41.0, y: 18.5},
    {x: 134.5, y: 21.2},
    {x: 202.5, y: 21.5}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_5():
    return """const augustaL5 = yr({
  layoutVersion: 1,
  name: "L'Hangar Dirigibili di Augusta (Monumento 1917)",
  short: "Hangar Dirigibili",
  label: "La monumentale cattedrale di cemento armato (1917)",
  biome: "citadel",
  intro: "Il monumento futurista più spettacolare di Sicilia: l'imponente Hangar Dirigibili del 1917 in cemento armato, alto quasi 40 metri! Arrampicati tra gli archi parabolici, i boschi di eucalipti e le grandiose capriate sospese nel vuoto!",
  sky: "#453625",
  fog: "#604b34",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 4,
  sections: [
    {x: -8, name: "1. Il Bosco di Eucalipti dell'Hangar", landmark: "beacon"},
    {x: 48, name: "2. Contrafforti & Pilastri Parabolici", landmark: "pulsedrum"},
    {x: 102, name: "3. La Scalata della Grande Navata", landmark: "bannerarch"},
    {x: 162, name: "4. Capriate del Tetto Sospese nel Vuoto", landmark: "sandwheel"},
    {x: 212, name: "5. La Passerella di Vedetta Aerea", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-hangar1", 10, 4.2, 13.0, "ledge"),
    S("plat-eucalyptus", 16, 7.5, 14.2, "stone"),
    S("lift-mast", 26, 3.8, 15.0, "lift", {moveY: 3.2, period: 4.5}),
    S("plat-buttress1", 32, 6.5, 16.5, "stone"),
    S("spring-hangar1", 41, 2.0, 16.5, "spring"),
    S("opt-hangar1", 40, 3.6, 21.0, "ledge", {optional: !0}),
    S("pit-hangar-1", 7, 40, 3.0, "stone", {spiked: !0}),

    S("dock-archbase", 46, 7.5, 16.5, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("step-arch1", 56, 4.0, 18.2, "ledge"),
    S("step-arch2", 62, 4.0, 20.0, "ledge"),
    S("plat-archbeam", 68, 7.5, 21.5, "stone"),
    S("lift-gantry-hangar", 78, 3.8, 22.0, "lift", {moveY: 3.0, period: 4.2}),
    S("plat-vault-floor", 84, 8.0, 23.5, "stone"),
    S("pit-hangar-2", 52, 48, 4.0, "stone", {spiked: !0}),

    S("dock-nave", 100, 7.0, 23.5, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-truss1", 109, 8.0, 24.5, "balance"),
    S("step-girder", 119, 3.8, 25.8, "ledge"),
    S("step-hangar2", 125, 3.2, 28.5, "ledge"),
    S("balance-truss2", 127, 8.0, 26.8, "balance"),
    S("opt-hangar2", 133, 3.6, 31.5, "ledge", {optional: !0}),
    S("lift-winch-hangar", 138, 3.6, 26.5, "lift", {moveY: 3.0, period: 4.0}),
    S("plat-skygate-floor", 144, 22, 28.0, "stone", {landmark: "beacon"}),
    S("switch-hangargate", 152, 2.2, 28.15, "switch", {channel: "hangar-lock", latch: !0}),
    S("gate-hangar", 159, 1.8, 32.0, "gate", {channel: "hangar-lock", h: 4}),

    S("dock-roof", 163, 7.5, 28.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-roof1", 173, 4.0, 27.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-roof2", 179, 4.0, 27.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-crown", 185, 6.5, 26.5, "stone"),
    S("step-hangar3", 196, 3.2, 29.8, "ledge"),
    S("lift-apex", 193, 3.6, 26.0, "lift", {moveX: 2.8, moveY: 2.0, period: 4.8}),
    S("opt-hangar3", 201, 3.5, 32.5, "ledge", {optional: !0}),
    S("spring-hangar3", 202, 2.0, 27.5, "spring"),
    S("plat-walkway", 200, 8.5, 27.5, "stone", {landmark: "sandwheel"}),
    S("pit-hangar-3", 168, 44, 8.0, "stone", {spiked: !0}),

    S("dock-aerie", 212, 7.0, 27.5, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-tower1", 221, 3.8, 28.8, "ledge"),
    S("step-tower2", 227, 4.2, 30.0, "ledge"),
    S("goal-hangar", 233, 14, 31.2, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 3.0},
    {x: 52, w: 48, y: 4.0},
    {x: 168, w: 44, y: 8.0}
  ],
  decor: [
    {kind: "tree", x: 12, y: 12.0, size: 4.5, z: -2.5},
    {kind: "tree", x: 22, y: 12.0, size: 5.0, z: -3.0},
    {kind: "hangar-arch", x: 50, y: 16.5, size: 14.0, z: -4.0},
    {kind: "scaffold", x: 32, y: 16.5, size: 3.5, z: -2.4},
    {kind: "caged-lamp", x: 48, y: 16.5, size: 0.7, z: -1.6},
    {kind: "hangar-arch", x: 104, y: 23.5, size: 14.0, z: -4.0},
    {kind: "scaffold", x: 86, y: 23.5, size: 3.5, z: -2.4},
    {kind: "caged-lamp", x: 102, y: 23.5, size: 0.7, z: -1.6},
    {kind: "hangar-arch", x: 166, y: 28.0, size: 14.0, z: -4.0},
    {kind: "scaffold", x: 146, y: 28.0, size: 3.5, z: -2.4},
    {kind: "caged-lamp", x: 164, y: 28.0, size: 0.7, z: -1.6},
    {kind: "banner", x: 188, y: 29.0, size: 2.5, z: -2.4},
    {kind: "caged-lamp", x: 214, y: 27.5, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Hangar Dirigibili (1917)", text: "Inizia la grande scalata dell'Hangar! Arrampicati sui contrafforti in cemento armato fino alla sommità delle capriate."},
    {x: 48, end: 68, icon: "knead", title: "Archi Parabolici", text: "Gli archi alti 40 metri sfidano la gravità: usa le travi inclinate per salire a grandi altezze."},
    {x: 102, end: 125, icon: "knead", title: "Capriate del Tetto", text: "Sei a 25 metri d'altezza! Mantieni l'equilibrio sulle travi a traliccio sopra il vuoto."},
    {x: 146, end: 160, icon: "walk", title: "Cancello delle Capriate", text: "Premi l'interruttore sulla passerella d'acciaio per sbloccare la paratia sommitale."},
    {x: 212, end: 240, icon: "bell", title: "Campana dei Dirigibili", text: "Suona la campana storica dell'aeroporto per celebrare la scalata del monumento d'Augusta!"}
  ],
  coins: [
    {x: 8, y: 14.0}, {x: 12, y: 14.0}, {x: 18, y: 15.5}, {x: 22, y: 15.5},
    {x: 28, y: 17.5}, {x: 34, y: 18.0}, {x: 41, y: 18.5}, {x: 58, y: 19.5},
    {x: 64, y: 21.0}, {x: 70, y: 22.5}, {x: 80, y: 24.5}, {x: 86, y: 25.0},
    {x: 104, y: 25.5}, {x: 111, y: 26.5}, {x: 115, y: 26.5}, {x: 121, y: 27.5},
    {x: 129, y: 29.0}, {x: 147, y: 29.5}, {x: 154, y: 29.5}, {x: 166, y: 29.5},
    {x: 175, y: 29.0}, {x: 181, y: 28.5}, {x: 187, y: 28.0}, {x: 195, y: 28.0},
    {x: 204, y: 29.5}, {x: 223, y: 30.5}, {x: 229, y: 31.5}, {x: 235, y: 32.5}
  ],
  stamps: [
    {x: 41.0, y: 22.5},
    {x: 134.5, y: 33.0},
    {x: 202.5, y: 34.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_6():
    return """const augustaL6 = yr({
  layoutVersion: 1,
  name: "Il Castello Svevo di Augusta (Forte Hohenstaufen)",
  short: "Castello Svevo",
  label: "Mura normanno-sveve, prigioni borboniche e fossati",
  biome: "cave",
  intro: "La titanica fortezza fondata da Federico II nel 1232 sull'estremità nord dell'isola: mura ciclopiche in pietra lavica e calcare siracusano, ex carcere borbonico e cortili d'armi affacciati sul mare!",
  sky: "#202630",
  fog: "#303946",
  spawn: {x: 1.5, y: 11},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Il Rivellino & Fossato Svevo", landmark: "beacon"},
    {x: 48, name: "2. Corte delle Prigioni Borboniche", landmark: "pulsedrum"},
    {x: 102, name: "3. Camminamento di Ronda dei Cavalieri", landmark: "bannerarch"},
    {x: 162, name: "4. Torre Ottagonale di Federico II", landmark: "sandwheel"},
    {x: 212, name: "5. I Bastioni d'Artiglieria sul Mare", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 11, "stone", {landmark: "beacon"}),
    S("step-svevo1", 10, 4.0, 11.8, "ledge"),
    S("plat-barbican", 16, 7.5, 12.6, "stone"),
    S("lift-portcullis", 26, 3.8, 13.0, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-rampart1", 32, 6.5, 13.8, "stone"),
    S("spring-castle1", 41, 2.0, 13.8, "spring"),
    S("opt-castle1", 40, 3.6, 17.8, "ledge", {optional: !0}),
    S("pit-moat-1", 7, 40, 1.5, "stone", {spiked: !0}),

    S("dock-prison", 46, 7.5, 13.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("step-cell1", 56, 4.2, 14.5, "ledge"),
    S("plat-courtyard", 62, 7.5, 15.0, "stone"),
    S("lift-chains", 72, 3.8, 14.5, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-dungeon-exit", 78, 8.0, 14.5, "stone"),
    S("step-svevo2", 88, 4.0, 15.6, "ledge"),
    S("plat-tower-base", 94, 7.0, 15.6, "stone"),
    S("pit-moat-2", 52, 48, 2.0, "stone", {spiked: !0}),

    S("dock-rampart", 100, 7.0, 15.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-drawbridge1", 109, 8.0, 16.2, "balance"),
    S("step-merlon1", 119, 3.8, 17.2, "ledge"),
    S("step-castle2", 125, 3.2, 19.8, "ledge"),
    S("balance-drawbridge2", 127, 8.0, 18.2, "balance"),
    S("opt-castle2", 133, 3.6, 22.8, "ledge", {optional: !0}),
    S("lift-keep", 138, 3.6, 17.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-castlegate-floor", 144, 22, 18.8, "stone", {landmark: "beacon"}),
    S("switch-castlegate", 152, 2.2, 18.95, "switch", {channel: "castle-lock", latch: !0}),
    S("gate-castle", 159, 1.8, 22.8, "gate", {channel: "castle-lock", h: 4}),

    S("dock-keep", 163, 7.5, 18.8, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-keep1", 173, 4.0, 18.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-keep2", 179, 4.0, 18.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-battery", 185, 6.5, 17.4, "stone"),
    S("step-castle3", 196, 3.2, 20.6, "ledge"),
    S("lift-turret", 193, 3.6, 16.8, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-castle3", 201, 3.5, 23.0, "ledge", {optional: !0}),
    S("spring-castle3", 202, 2.0, 18.4, "spring"),
    S("plat-seawall-castle", 200, 8.5, 18.4, "stone", {landmark: "sandwheel"}),
    S("pit-moat-3", 168, 44, 5.0, "stone", {spiked: !0}),

    S("dock-citadel-exit", 212, 7.0, 18.4, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-bastion1", 221, 3.8, 19.4, "ledge"),
    S("step-bastion2", 227, 4.2, 20.4, "ledge"),
    S("goal-castle", 233, 14, 21.4, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 1.5},
    {x: 52, w: 48, y: 2.0},
    {x: 168, w: 44, y: 5.0}
  ],
  decor: [
    {kind: "spanish-bastion", x: 20, y: 12.6, size: 6.0, z: -2.5},
    {kind: "torch", x: 16, y: 13.0, size: 0.8, z: -1.0},
    {kind: "caged-lamp", x: 34, y: 13.8, size: 0.7, z: -1.6},
    {kind: "banner", x: 48, y: 14.5, size: 2.4, z: -2.4},
    {kind: "spanish-bastion", x: 74, y: 15.0, size: 6.5, z: -2.5},
    {kind: "doorway", x: 80, y: 14.5, size: 3.5, z: -2.0},
    {kind: "torch", x: 92, y: 16.0, size: 0.8, z: -1.0},
    {kind: "spanish-bastion", x: 114, y: 16.2, size: 7.0, z: -3.0},
    {kind: "banner", x: 146, y: 19.5, size: 2.4, z: -2.4},
    {kind: "spanish-bastion", x: 174, y: 18.8, size: 7.0, z: -3.0},
    {kind: "torch", x: 186, y: 18.0, size: 0.8, z: -1.0},
    {kind: "caged-lamp", x: 214, y: 18.4, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Castello Svevo (1232)", text: "Esplora la monumentale fortezza di Federico II. Attento ai fossati con spuntoni e alle merlature di pietra lavica!"},
    {x: 48, end: 68, icon: "knead", title: "Prigioni Borboniche", text: "Attraversa il cortile dell'antico bagno penale. Salta sui montacarichi a catena per salire ai camminamenti."},
    {x: 102, end: 125, icon: "knead", title: "Ponti Levatoi Medievali", text: "Le passerelle in legno e ferro oscillano sotto il tuo peso. Mantieni il baricentro al centro."},
    {x: 146, end: 160, icon: "walk", title: "Saracinesca Reale", text: "Premi il meccanismo dell'argano sulla passerella per sollevare la grata di ferro."},
    {x: 212, end: 240, icon: "bell", title: "Cannoniere Sveve", text: "Suona la campana di vedetta del forte per liberare le prigioni di Federico II!"}
  ],
  coins: [
    {x: 8, y: 13.5}, {x: 12, y: 13.5}, {x: 18, y: 14.5}, {x: 22, y: 14.5},
    {x: 28, y: 15.5}, {x: 34, y: 15.5}, {x: 41, y: 16.0}, {x: 58, y: 16.5},
    {x: 64, y: 17.0}, {x: 74, y: 16.5}, {x: 80, y: 16.5}, {x: 90, y: 17.5},
    {x: 104, y: 17.5}, {x: 111, y: 18.0}, {x: 115, y: 18.0}, {x: 121, y: 19.0},
    {x: 129, y: 20.5}, {x: 147, y: 20.5}, {x: 154, y: 20.5}, {x: 166, y: 20.5},
    {x: 175, y: 20.0}, {x: 181, y: 20.0}, {x: 187, y: 19.5}, {x: 195, y: 19.5},
    {x: 204, y: 20.5}, {x: 223, y: 21.5}, {x: 229, y: 22.5}, {x: 235, y: 23.5}
  ],
  stamps: [
    {x: 41.0, y: 19.8},
    {x: 134.5, y: 24.5},
    {x: 202.5, y: 25.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_7():
    return """const augustaL7 = yr({
  layoutVersion: 1,
  name: "Faro Santa Croce & Le Falesie di Brucoli",
  short: "Faro S. Croce",
  label: "Scogliere bianche, mare Ionio e vista sul vulcano Etna",
  biome: "nightfall",
  intro: "La punta più spettacolare della costa augustana: il faro ottagonale di Santa Croce a picco sulle scogliere calcaree bianche di Brucoli, con i bunker della Seconda Guerra Mondiale e la magnifica vista sul vulcano Etna!",
  sky: "#1a3450",
  fog: "#284c72",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. I Sentieri Costieri di Brucoli", landmark: "beacon"},
    {x: 48, name: "2. Le Falesie Bianche a Strapiombo", landmark: "pulsedrum"},
    {x: 102, name: "3. La Casamatta del Bunker Costiero", landmark: "bannerarch"},
    {x: 162, name: "4. Scogliera del Faro di Santa Croce", landmark: "sandwheel"},
    {x: 212, name: "5. La Lanterna Ottagonale del Faro", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-cliff1", 10, 4.0, 12.8, "ledge"),
    S("plat-falesia1", 16, 7.5, 13.6, "stone"),
    S("lift-gull", 26, 3.8, 14.0, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-falesia2", 32, 6.5, 14.8, "stone"),
    S("spring-cliff1", 41, 2.0, 14.8, "spring"),
    S("opt-cliff1", 40, 3.6, 18.8, "ledge", {optional: !0}),
    S("pit-sea-1", 7, 40, 2.0, "stone", {spiked: !0}),

    S("dock-falesie", 46, 7.5, 14.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("step-ledge1", 56, 4.2, 15.5, "ledge"),
    S("plat-bunker-access", 62, 7.5, 16.0, "stone"),
    S("lift-marine", 72, 3.8, 15.5, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-pillbox", 78, 8.0, 15.5, "stone"),
    S("step-cliff2", 88, 4.0, 16.6, "ledge"),
    S("plat-reef", 94, 7.0, 16.6, "stone"),
    S("pit-sea-2", 52, 48, 2.5, "stone", {spiked: !0}),

    S("dock-bunker", 100, 7.0, 16.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-cliff1", 109, 8.0, 17.2, "balance"),
    S("step-promontory", 119, 3.8, 18.2, "ledge"),
    S("step-cliff3", 125, 3.2, 20.8, "ledge"),
    S("balance-cliff2", 127, 8.0, 19.2, "balance"),
    S("opt-cliff2", 133, 3.6, 23.8, "ledge", {optional: !0}),
    S("lift-lighthouse-rock", 138, 3.6, 18.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-lightgate-floor", 144, 22, 19.8, "stone", {landmark: "beacon"}),
    S("switch-lightgate", 152, 2.2, 19.95, "switch", {channel: "light-lock", latch: !0}),
    S("gate-light", 159, 1.8, 23.8, "gate", {channel: "light-lock", h: 4}),

    S("dock-lighthouse", 163, 7.5, 19.8, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-light1", 173, 4.0, 19.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-light2", 179, 4.0, 19.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-lantern-base", 185, 6.5, 18.4, "stone"),
    S("step-cliff4", 196, 3.2, 21.6, "ledge"),
    S("lift-beacon-lamp", 193, 3.6, 17.8, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-cliff3", 201, 3.5, 24.0, "ledge", {optional: !0}),
    S("spring-cliff3", 202, 2.0, 19.4, "spring"),
    S("plat-faro-deck", 200, 8.5, 19.4, "stone", {landmark: "sandwheel"}),
    S("pit-sea-3", 168, 44, 5.0, "stone", {spiked: !0}),

    S("dock-faro-exit", 212, 7.0, 19.4, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-croce1", 221, 3.8, 20.4, "ledge"),
    S("step-croce2", 227, 4.2, 21.4, "ledge"),
    S("goal-santacroce", 233, 14, 22.4, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 2.0},
    {x: 52, w: 48, y: 2.5},
    {x: 168, w: 44, y: 5.0}
  ],
  decor: [
    {kind: "etna-silhouette", x: 120, y: 22.0, size: 24.0, z: -20.0},
    {kind: "lighthouse-tower", x: 174, y: 19.8, size: 9.5, z: -3.5},
    {kind: "bunker", x: 74, y: 15.5, size: 3.5, z: -2.0},
    {kind: "cactus-opuntia", x: 18, y: 13.6, size: 2.2, z: -1.5},
    {kind: "boulder", x: 34, y: 14.8, size: 2.5, z: -1.5},
    {kind: "pebbles", x: 48, y: 14.8, size: 1.5, z: 1.0},
    {kind: "cactus-opuntia", x: 92, y: 16.6, size: 2.2, z: -1.5},
    {kind: "caged-lamp", x: 102, y: 16.6, size: 0.7, z: -1.6},
    {kind: "boulder", x: 146, y: 19.8, size: 2.8, z: -1.5},
    {kind: "caged-lamp", x: 164, y: 19.8, size: 0.7, z: -1.6},
    {kind: "cactus-opuntia", x: 202, y: 19.4, size: 2.2, z: -1.5},
    {kind: "caged-lamp", x: 214, y: 19.4, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Falesie di Brucoli", text: "Ammira le scogliere a strapiombo sul mar Ionio e i fichi d'india. Salta tra le falesie calcaree bianche!"},
    {x: 48, end: 68, icon: "knead", title: "Casamatta della 2ª GM", text: "Supera il vecchio bunker militare costiero affacciato sul golfo. La vista dell'Etna è spettacolare!"},
    {x: 102, end: 125, icon: "knead", title: "Il Faro di Santa Croce", text: "In lontananza svetta il faro ottagonale bianco e nero. Mantieni l'equilibrio sugli scogli esposti al vento."},
    {x: 146, end: 160, icon: "walk", title: "Chiusa del Faro", text: "Attiva l'interruttore sulla passerella di pietra per aprire la saracinesca della lanterna."},
    {x: 212, end: 240, icon: "bell", title: "Campana della Lanterna", text: "Suona la campana di Santa Croce davanti allo spettacolo del mare e del vulcano Etna!"}
  ],
  coins: [
    {x: 8, y: 14.5}, {x: 12, y: 14.5}, {x: 18, y: 15.5}, {x: 22, y: 15.5},
    {x: 28, y: 16.5}, {x: 34, y: 16.5}, {x: 41, y: 17.0}, {x: 58, y: 17.5},
    {x: 64, y: 18.0}, {x: 74, y: 17.5}, {x: 80, y: 17.5}, {x: 90, y: 18.5},
    {x: 104, y: 18.5}, {x: 111, y: 19.0}, {x: 115, y: 19.0}, {x: 121, y: 20.0},
    {x: 129, y: 21.5}, {x: 147, y: 21.5}, {x: 154, y: 21.5}, {x: 166, y: 21.5},
    {x: 175, y: 21.0}, {x: 181, y: 21.0}, {x: 187, y: 20.5}, {x: 195, y: 20.5},
    {x: 204, y: 21.5}, {x: 223, y: 22.5}, {x: 229, y: 23.5}, {x: 235, y: 24.5}
  ],
  stamps: [
    {x: 41.0, y: 20.8},
    {x: 134.5, y: 25.5},
    {x: 202.5, y: 26.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_8():
    return """const augustaL8 = yr({
  layoutVersion: 1,
  name: "Le Antiche Saline Regina di Augusta",
  short: "Saline Regina",
  label: "Bacini rosa, croste di sale e mulini a vento salinari",
  biome: "citadel",
  intro: "Le storiche Saline Regina di Augusta: una scacchiera di canali d'acqua rosa e argini di terra scura. Le croste di sale bianco cristallizzato si spaccano sotto i piedi e i mulini a vento salinari azionano grandi piattaforme orbitanti!",
  sky: "#5a2838",
  fog: "#783648",
  spawn: {x: 1.5, y: 11},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Le Vasche di Decantazione Regina", landmark: "beacon"},
    {x: 48, name: "2. Gli Argini dei Canali Salmastri", landmark: "pulsedrum"},
    {x: 102, name: "3. Le Piramidi di Sale Marino", landmark: "bannerarch"},
    {x: 162, name: "4. Il Mulino Salinaro Tradizionale", landmark: "sandwheel"},
    {x: 212, name: "5. Il Pontile del Magazzino del Sale", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 11, "stone", {landmark: "beacon"}),
    S("step-salt1", 10, 4.0, 11.8, "ledge"),
    S("plat-salina1", 16, 7.5, 12.6, "stone"),
    S("crumble-salt1", 25, 4.2, 13.0, "crumble"),
    S("plat-salina2", 31, 7.5, 13.4, "stone"),
    S("spring-salt1", 40, 2.0, 13.4, "spring"),
    S("opt-salt1", 39, 3.6, 17.4, "ledge", {optional: !0}),
    S("pit-brine-1", 7, 39, 1.5, "stone", {spiked: !0}),

    S("dock-dikes", 46, 7.5, 13.4, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("crumble-salt2", 56, 4.2, 13.2, "crumble"),
    S("crumble-salt3", 62, 4.2, 13.0, "crumble"),
    S("plat-sluice-base", 68, 6.5, 12.8, "stone"),
    S("lift-brine", 77, 3.8, 12.5, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-saltpyramid1", 83, 7.5, 12.8, "stone"),
    S("pit-brine-2", 52, 48, 1.5, "stone", {spiked: !0}),

    S("dock-pyramids", 100, 7.0, 12.8, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("orbit-windmill1", 112, 4.0, 14.5, "orbit", {moveX: 3.2, moveY: 2.6, period: 5.5}),
    S("step-salt2", 120, 3.8, 15.5, "ledge"),
    S("step-salina2", 126, 3.2, 18.2, "ledge"),
    S("balance-salt1", 128, 7.5, 16.5, "balance"),
    S("opt-salt2", 134, 3.5, 21.2, "ledge", {optional: !0}),
    S("lift-crystal", 138, 3.6, 16.0, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-saltgate-floor", 144, 22, 17.2, "stone", {landmark: "beacon"}),
    S("switch-saltgate", 152, 2.2, 17.35, "switch", {channel: "salt-lock", latch: !0}),
    S("gate-salt", 159, 1.8, 21.2, "gate", {channel: "salt-lock", h: 4}),

    S("dock-mill", 163, 7.5, 17.2, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-salt1", 173, 4.0, 16.6, "pulse", {period: 4.2, phase: 0}),
    S("pulse-salt2", 179, 4.0, 16.6, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-wharf-salt", 185, 6.5, 15.8, "stone"),
    S("step-salina3", 196, 3.2, 19.0, "ledge"),
    S("lift-pan", 193, 3.6, 15.2, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-salt3", 201, 3.5, 21.4, "ledge", {optional: !0}),
    S("spring-salt3", 202, 2.0, 16.8, "spring"),
    S("plat-depot", 200, 8.5, 16.8, "stone", {landmark: "sandwheel"}),
    S("pit-brine-3", 168, 44, 3.0, "stone", {spiked: !0}),

    S("dock-salina-exit", 212, 7.0, 16.8, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-pan1", 221, 3.8, 17.8, "ledge"),
    S("step-pan2", 227, 4.2, 18.8, "ledge"),
    S("goal-saline", 233, 14, 19.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 39, y: 1.5},
    {x: 52, w: 48, y: 1.5},
    {x: 168, w: 44, y: 3.0}
  ],
  decor: [
    {kind: "salt-pyramid", x: 20, y: 12.6, size: 4.0, z: -2.0},
    {kind: "salt-pyramid", x: 86, y: 12.8, size: 4.5, z: -2.2},
    {kind: "salt-windmill", x: 110, y: 13.5, size: 5.5, z: -3.0},
    {kind: "salt-pyramid", x: 148, y: 17.2, size: 4.0, z: -2.0},
    {kind: "salt-windmill", x: 170, y: 17.2, size: 5.5, z: -3.0},
    {kind: "caged-lamp", x: 16, y: 12.6, size: 0.7, z: -1.6},
    {kind: "caged-lamp", x: 48, y: 13.4, size: 0.7, z: -1.6},
    {kind: "scaffold", x: 74, y: 12.8, size: 3.0, z: -2.4},
    {kind: "banner", x: 102, y: 14.5, size: 2.4, z: -2.4},
    {kind: "caged-lamp", x: 165, y: 17.2, size: 0.7, z: -1.6},
    {kind: "salt-pyramid", x: 202, y: 16.8, size: 4.0, z: -2.0},
    {kind: "caged-lamp", x: 214, y: 16.8, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Le Saline Regina", text: "Cammina tra i bacini di evaporazione del sale marino. Le croste bianche sono fragili e si rompono sotto i piedi!"},
    {x: 48, end: 68, icon: "sink", title: "Croste di Sale Fragili", text: "Le passerelle di sale cristallino cedono se ti fermi troppo a lungo: salta con decisione."},
    {x: 102, end: 125, icon: "knead", title: "Le Pale del Mulino Salinaro", text: "Salta sulla piattaforma orbitante che gira insieme alle pale del mulino a vento per attraversare il grande bacino."},
    {x: 146, end: 160, icon: "walk", title: "Chiusa delle Saline", text: "Premi l'interruttore salinaro per aprire la paratoia che regola l'acqua rosa."},
    {x: 212, end: 240, icon: "bell", title: "Campana del Magazzino del Sale", text: "Suona la campana per completare la traversata delle splendide Saline di Augusta!"}
  ],
  coins: [
    {x: 8, y: 13.5}, {x: 12, y: 13.5}, {x: 18, y: 14.5}, {x: 22, y: 14.5},
    {x: 28, y: 15.0}, {x: 34, y: 15.0}, {x: 41, y: 15.5}, {x: 58, y: 14.5},
    {x: 64, y: 14.0}, {x: 74, y: 14.0}, {x: 80, y: 14.0}, {x: 90, y: 14.5},
    {x: 104, y: 14.5}, {x: 111, y: 16.5}, {x: 115, y: 16.5}, {x: 121, y: 17.5},
    {x: 129, y: 18.5}, {x: 147, y: 19.0}, {x: 154, y: 19.0}, {x: 166, y: 19.0},
    {x: 175, y: 18.5}, {x: 181, y: 18.5}, {x: 187, y: 17.5}, {x: 195, y: 17.5},
    {x: 204, y: 18.5}, {x: 223, y: 19.5}, {x: 229, y: 20.5}, {x: 235, y: 21.5}
  ],
  stamps: [
    {x: 40.0, y: 19.0},
    {x: 135.5, y: 23.0},
    {x: 202.5, y: 23.2}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_9():
    return """const augustaL9 = yr({
  layoutVersion: 1,
  name: "I Forti Spagnoli della Rada (Garcia & Vittoria)",
  short: "Forti Spagnoli",
  label: "Fortezze gemelle (1567), onde in tempesta e catene navali",
  biome: "nightfall",
  intro: "Le due fortezze gemelle del 1567 edificate dal viceré Garcia de Toledo su due isolotti sperduti al centro del golfo di Augusta. Una tempesta notturna scuote la rada: supera i marosi, i cannoni e la gigantesca catena navale di ferro!",
  sky: "#0d141e",
  fog: "#14202e",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Lo Scoglio di Forte Garcia", landmark: "beacon"},
    {x: 48, name: "2. I Bastioni ad Asso di Picche", landmark: "pulsedrum"},
    {x: 102, name: "3. La Catena di Sbarramento Navale", landmark: "bannerarch"},
    {x: 162, name: "4. I Marosi del Forte Vittoria", landmark: "sandwheel"},
    {x: 212, name: "5. La Terrazza delle Polveriere & Bracieri", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-garcia1", 10, 4.0, 12.8, "ledge"),
    S("plat-bastion-garcia", 16, 7.5, 13.6, "stone"),
    S("lift-rigging", 26, 3.8, 14.0, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-rampart-garcia", 32, 6.5, 14.8, "stone"),
    S("spring-fort1", 41, 2.0, 14.8, "spring"),
    S("opt-fort1", 40, 3.6, 18.8, "ledge", {optional: !0}),
    S("pit-storm-1", 7, 40, 2.0, "stone", {spiked: !0}),

    S("dock-garcia-battery", 46, 7.5, 14.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("step-rampart1", 56, 4.2, 15.5, "ledge"),
    S("plat-chain-base", 62, 7.5, 16.0, "stone"),
    S("lift-pulley", 72, 3.8, 15.5, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-chain-tower", 78, 8.0, 15.5, "stone"),
    S("step-garcia2", 88, 4.0, 16.6, "ledge"),
    S("plat-reef-fort", 94, 7.0, 16.6, "stone"),
    S("pit-storm-2", 52, 48, 2.5, "stone", {spiked: !0}),

    S("dock-ironchain", 100, 7.0, 16.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-chain1", 109, 8.0, 17.2, "balance"),
    S("step-ironlink", 119, 3.8, 18.2, "ledge"),
    S("step-fort2", 125, 3.2, 20.8, "ledge"),
    S("balance-chain2", 127, 8.0, 19.2, "balance"),
    S("opt-fort2", 133, 3.6, 23.8, "ledge", {optional: !0}),
    S("lift-cannon-hoist", 138, 3.6, 18.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-vittoriagate-floor", 144, 22, 19.8, "stone", {landmark: "beacon"}),
    S("switch-vittoriagate", 152, 2.2, 19.95, "switch", {channel: "vittoria-lock", latch: !0}),
    S("gate-vittoria", 159, 1.8, 23.8, "gate", {channel: "vittoria-lock", h: 4}),

    S("dock-vittoria", 163, 7.5, 19.8, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-vittoria1", 173, 4.0, 19.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-vittoria2", 179, 4.0, 19.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-vittoria-dike", 185, 6.5, 18.4, "stone"),
    S("step-fort3", 196, 3.2, 21.6, "ledge"),
    S("lift-beacon-fort", 193, 3.6, 17.8, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-fort3", 201, 3.5, 24.0, "ledge", {optional: !0}),
    S("spring-fort3", 202, 2.0, 19.4, "spring"),
    S("plat-vittoria-crest", 200, 8.5, 19.4, "stone", {landmark: "sandwheel"}),
    S("pit-storm-3", 168, 44, 5.0, "stone", {spiked: !0}),

    S("dock-fort-exit", 212, 7.0, 19.4, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-garcia-end1", 221, 3.8, 20.4, "ledge"),
    S("step-garcia-end2", 227, 4.2, 21.4, "ledge"),
    S("goal-forts", 233, 14, 22.4, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 2.0},
    {x: 52, w: 48, y: 2.5},
    {x: 168, w: 44, y: 5.0}
  ],
  decor: [
    {kind: "spanish-bastion", x: 22, y: 13.6, size: 7.0, z: -3.0},
    {kind: "torch", x: 18, y: 14.0, size: 0.8, z: -1.0},
    {kind: "caged-lamp", x: 34, y: 14.8, size: 0.7, z: -1.6},
    {kind: "spanish-bastion", x: 74, y: 15.5, size: 7.5, z: -3.0},
    {kind: "banner", x: 48, y: 15.5, size: 2.4, z: -2.4},
    {kind: "torch", x: 80, y: 16.5, size: 0.8, z: -1.0},
    {kind: "spanish-bastion", x: 114, y: 17.2, size: 8.0, z: -3.5},
    {kind: "cargo-ship", x: 120, y: 10.0, size: 20.0, z: -18.0},
    {kind: "caged-lamp", x: 102, y: 16.6, size: 0.7, z: -1.6},
    {kind: "spanish-bastion", x: 174, y: 19.8, size: 7.5, z: -3.0},
    {kind: "torch", x: 186, y: 19.2, size: 0.8, z: -1.0},
    {kind: "caged-lamp", x: 214, y: 19.4, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Forte Garcia (1567)", text: "Sei sull'isolotto fortificato di Forte Garcia nel cuore della rada. Una tempesta notturna alza onde minacciose!"},
    {x: 48, end: 68, icon: "knead", title: "I Bastioni ad Asso di Picche", text: "Le mura cinquecentesche resistono ai marosi. Sali sui cannoni per raggiungere la torre della catena navale."},
    {x: 102, end: 125, icon: "knead", title: "La Catena di Sbarramento", text: "In bilico sulla colossale catena di ferro che chiudeva il porto di Augusta ai pirati e alle navi nemiche!"},
    {x: 146, end: 160, icon: "walk", title: "Portone di Forte Vittoria", text: "Premi il dispositivo a leva sulla passerella per aprire la pesante porta ferrata del Forte Vittoria."},
    {x: 212, end: 240, icon: "bell", title: "Campana delle Fortezze", text: "Suona la campana di Forte Vittoria per completare l'epica traversata notturna delle fortezze gemelle!"}
  ],
  coins: [
    {x: 8, y: 14.5}, {x: 12, y: 14.5}, {x: 18, y: 15.5}, {x: 22, y: 15.5},
    {x: 28, y: 16.5}, {x: 34, y: 16.5}, {x: 41, y: 17.0}, {x: 58, y: 17.5},
    {x: 64, y: 18.0}, {x: 74, y: 17.5}, {x: 80, y: 17.5}, {x: 90, y: 18.5},
    {x: 104, y: 18.5}, {x: 111, y: 19.0}, {x: 115, y: 19.0}, {x: 121, y: 20.0},
    {x: 129, y: 21.5}, {x: 147, y: 21.5}, {x: 154, y: 21.5}, {x: 166, y: 21.5},
    {x: 175, y: 21.0}, {x: 181, y: 21.0}, {x: 187, y: 20.5}, {x: 195, y: 20.5},
    {x: 204, y: 21.5}, {x: 223, y: 22.5}, {x: 229, y: 23.5}, {x: 235, y: 24.5}
  ],
  stamps: [
    {x: 41.0, y: 20.8},
    {x: 134.5, y: 25.5},
    {x: 202.5, y: 26.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_level_10():
    return """const augustaL10 = yr({
  layoutVersion: 1,
  name: "La Porta Spagnola & Il Taglio dell'Isola",
  short: "Porta Spagnola",
  label: "Il gran finale: centro storico, tetti barocchi e la fuga trionfale!",
  biome: "desert",
  intro: "Il gran finale di Augusta Slop Adventures! Corri sui tetti e balconi barocchi dell'Isola di Augusta, supera il fossato salmastro del Taglio dell'Isola, varca l'arco trionfale della monumentale Porta Spagnola del 1699 e suona la Campana della Libertà!",
  sky: "#4e381c",
  fog: "#6c4e28",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. I Tetti Barocchi dell'Isola", landmark: "beacon"},
    {x: 48, name: "2. I Vicoli della Città Vecchia", landmark: "pulsedrum"},
    {x: 102, name: "3. Il Fossato del Taglio dell'Isola", landmark: "bannerarch"},
    {x: 162, name: "4. L'Arco della Porta Spagnola (1699)", landmark: "sandwheel"},
    {x: 212, name: "5. La Campana della Libertà di Augusta", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-roof1", 10, 4.0, 13.0, "ledge"),
    S("plat-palazzo1", 16, 7.5, 14.0, "stone"),
    S("lift-balcony", 26, 3.8, 14.5, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-terrazza1", 32, 6.5, 15.5, "stone"),
    S("spring-finale1", 41, 2.0, 15.5, "spring"),
    S("opt-finale1", 40, 3.6, 19.8, "ledge", {optional: !0}),
    S("pit-alley-1", 7, 40, 2.0, "stone", {spiked: !0}),

    S("dock-alleys", 46, 7.5, 15.5, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("step-cornice1", 56, 4.2, 16.2, "ledge"),
    S("plat-piazza", 62, 7.5, 16.8, "stone"),
    S("lift-pulley-city", 72, 3.8, 16.2, "lift", {moveY: 2.8, period: 4.2}),
    S("plat-bridgehead", 78, 8.0, 16.2, "stone"),
    S("step-roof2", 88, 4.0, 17.5, "ledge"),
    S("plat-moat-edge", 94, 7.0, 17.5, "stone"),
    S("pit-moat-cut", 52, 48, 2.5, "stone", {spiked: !0}),

    S("dock-cut", 100, 7.0, 17.5, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("balance-span1", 109, 8.0, 18.2, "balance"),
    S("step-drawbridge", 119, 3.8, 19.2, "ledge"),
    S("step-finale2", 125, 3.2, 21.8, "ledge"),
    S("balance-span2", 127, 8.0, 20.2, "balance"),
    S("opt-finale2", 133, 3.6, 24.8, "ledge", {optional: !0}),
    S("lift-triumphal", 138, 3.6, 19.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-portagate-floor", 144, 22, 20.8, "stone", {landmark: "beacon"}),
    S("switch-portagate", 152, 2.2, 20.95, "switch", {channel: "porta-lock", latch: !0}),
    S("gate-porta", 159, 1.8, 24.8, "gate", {channel: "porta-lock", h: 4}),

    S("dock-porta-arch", 163, 7.5, 20.8, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-porta1", 173, 4.0, 20.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-porta2", 179, 4.0, 20.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-triumphal-way", 185, 6.5, 19.5, "stone"),
    S("step-finale3", 196, 3.2, 22.8, "ledge"),
    S("lift-victory-belfry", 193, 3.6, 19.0, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-finale3", 201, 3.5, 25.0, "ledge", {optional: !0}),
    S("spring-finale3", 202, 2.0, 20.5, "spring"),
    S("plat-belvedere-augusta", 200, 8.5, 20.5, "stone", {landmark: "sandwheel"}),
    S("pit-finale-3", 168, 44, 6.0, "stone", {spiked: !0}),

    S("dock-liberty", 212, 7.0, 20.5, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-liberty1", 221, 3.8, 21.5, "ledge"),
    S("step-liberty2", 227, 4.2, 22.5, "ledge"),
    S("goal-liberty", 233, 14, 23.5, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 2.0},
    {x: 52, w: 48, y: 2.5},
    {x: 168, w: 44, y: 6.0}
  ],
  decor: [
    {kind: "porta-spagnola", x: 160, y: 20.8, size: 10.0, z: -3.0},
    {kind: "spanish-bastion", x: 80, y: 16.2, size: 7.0, z: -3.0},
    {kind: "banner", x: 18, y: 16.0, size: 2.5, z: -2.4},
    {kind: "banner", x: 48, y: 17.5, size: 2.5, z: -2.4},
    {kind: "caged-lamp", x: 34, y: 15.5, size: 0.7, z: -1.6},
    {kind: "caged-lamp", x: 94, y: 17.5, size: 0.7, z: -1.6},
    {kind: "caged-lamp", x: 102, y: 17.5, size: 0.7, z: -1.6},
    {kind: "banner", x: 146, y: 22.0, size: 2.5, z: -2.4},
    {kind: "cactus-opuntia", x: 186, y: 19.5, size: 2.2, z: -1.5},
    {kind: "banner", x: 202, y: 22.0, size: 2.5, z: -2.4},
    {kind: "caged-lamp", x: 214, y: 20.5, size: 0.7, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Centro Storico di Augusta", text: "Corri sui tetti barocchi dell'Isola! Salta tra terrazze e cornicioni dorati dal sole siciliano."},
    {x: 48, end: 68, icon: "knead", title: "I Vicoli dell'Isola", text: "Attraversa le piazze della città vecchia. Preparati a scavalcare il canale del Taglio dell'Isola!"},
    {x: 102, end: 125, icon: "knead", title: "Il Taglio dell'Isola", text: "Il fossato che separa Augusta dalla terraferma: salta sul ponte levatoio basculante sopra il canale."},
    {x: 146, end: 160, icon: "walk", title: "La Porta Spagnola (1699)", text: "Premi il verricello per aprire la monumentale Porta Spagnola sormontata dall'aquila asburgica!"},
    {x: 212, end: 240, icon: "bell", title: "La Campana della Libertà", text: "Salta e suona la Campana d'Oro della Libertà per celebrare il trionfo e la salvezza di Augusta!"}
  ],
  coins: [
    {x: 8, y: 14.5}, {x: 12, y: 14.5}, {x: 18, y: 15.5}, {x: 22, y: 15.5},
    {x: 28, y: 17.0}, {x: 34, y: 17.0}, {x: 41, y: 18.0}, {x: 58, y: 18.0},
    {x: 64, y: 18.5}, {x: 74, y: 18.0}, {x: 80, y: 18.0}, {x: 90, y: 19.5},
    {x: 104, y: 19.5}, {x: 111, y: 20.0}, {x: 115, y: 20.0}, {x: 121, y: 21.0},
    {x: 129, y: 22.5}, {x: 147, y: 22.5}, {x: 154, y: 22.5}, {x: 166, y: 22.5},
    {x: 175, y: 22.0}, {x: 181, y: 22.0}, {x: 187, y: 21.5}, {x: 195, y: 21.5},
    {x: 204, y: 22.5}, {x: 223, y: 23.5}, {x: 229, y: 24.5}, {x: 235, y: 25.5}
  ],
  stamps: [
    {x: 41.0, y: 21.8},
    {x: 134.5, y: 26.5},
    {x: 202.5, y: 27.0}
  ],
  enemies: [],
  crushers: []
});"""

def get_3d_decor_builders():
    return """
,"oil-tank"(t,e,n){
  const o=oo(e,n,5.0);
  t.cylinder(2.2,3.6,"dark",o,0,1.8,0);
  t.ball(2.2,0.7,2.2,"orange",o,0,3.6,0);
  t.cylinder(2.35,0.14,"orangeLight",o,0,1.2,0);
  t.cylinder(2.35,0.14,"orangeLight",o,0,2.4,0);
  t.cylinder(0.18,4.0,"dark",o,1.8,2.0,0);
}
,"flare-stack"(t,e,n){
  const o=oo(e,n,12.0);
  t.cylinder(0.35,10,"dark",o,0,5,0);
  for(let y of[2,4,6,8])t.box(1.2,0.15,1.2,"orange",o,0,y,0);
  t.cylinder(0.65,0.7,"orange",o,0,10.2,0);
  t.ball(0.75,1.5,0.75,"gold",o,0,11.2,0);
  t.ball(0.45,1.0,0.45,"orangeLight",o,0,12.0,0);
  t.ball(0.9,0.8,0.9,"dark",o,0.2,13.0,0);
}
,"crane-tower"(t,e,n){
  const o=oo(e,n,9.0);
  t.box(0.9,8,0.9,"orange",o,0,4,0);
  t.box(1.8,1.4,1.5,"dark",o,0.3,7.8,0);
  t.box(8.5,0.6,0.7,"orange",o,2.5,8.4,0);
  t.box(2.0,1.5,1.2,"terrain",o,-2.4,8.4,0);
  t.cylinder(0.06,3.6,"rope",o,4.5,6.2,0);
  t.box(0.5,0.5,0.5,"dark",o,4.5,4.2,0);
}
,"hangar-arch"(t,e,n){
  const o=oo(e,n,14.0);
  t.box(1.2,7.5,1.6,"cream",o,-6,3.75,0,0.15);
  t.box(1.2,7.5,1.6,"cream",o,6,3.75,0,0.15);
  t.box(1.0,6,1.4,"cream",o,-4.2,9.5,0,0.15);
  t.box(1.0,6,1.4,"cream",o,4.2,9.5,0,0.15);
  t.box(5,1.2,1.4,"cream",o,0,13,0,0.15);
  t.box(11,0.35,0.8,"terrain2",o,0,6,0);
  t.box(8,0.35,0.8,"terrain2",o,0,9.8,0);
}
,"spanish-bastion"(t,e,n){
  const o=oo(e,n,6.0);
  t.box(7.5,5,2.4,"terrain",o,0,2.5,0,0.2);
  t.box(1.2,1.1,1.2,"terrain2",o,-2.8,5.4,0.6);
  t.box(1.2,1.1,1.2,"terrain2",o,0,5.4,0.6);
  t.box(1.2,1.1,1.2,"terrain2",o,2.8,5.4,0.6);
  t.cylinder(0.3,2.6,"dark",o,-1.4,5.2,1.1);
  t.box(1.0,1.3,0.25,"gold",o,0,3.2,1.25);
}
,"salt-pyramid"(t,e,n){
  const o=oo(e,n,4.0);
  t.box(5.5,1.1,4.2,"cream",o,0,0.55,0,0.2);
  t.box(3.8,1.1,2.9,"cream",o,0,1.65,0,0.2);
  t.ball(1.5,1.2,1.3,"cream",o,0,2.6,0);
}
,"salt-windmill"(t,e,n){
  const o=oo(e,n,5.5);
  t.cylinder(1.3,4.2,"cream",o,0,2.1,0);
  t.cylinder(1.5,1.1,"rope",o,0,4.8,0);
  t.ball(0.45,0.45,0.45,"dark",o,0,4.4,1.4);
  t.box(0.22,4.4,0.08,"rope",o,0,4.4,1.5);
  t.box(4.0,0.22,0.08,"rope",o,0,4.4,1.5);
}
,"lighthouse-tower"(t,e,n){
  const o=oo(e,n,9.5);
  t.cylinder(1.7,3.0,"cream",o,0,1.5,0);
  t.cylinder(1.5,2.0,"dark",o,0,4.0,0);
  t.cylinder(1.3,2.8,"cream",o,0,6.4,0);
  t.cylinder(1.8,0.3,"dark",o,0,8.0,0);
  t.cylinder(1.1,1.5,"gold",o,0,8.9,0);
  t.ball(1.2,0.6,1.2,"foliage",o,0,9.9,0);
}
,"cargo-ship"(t,e,n){
  const o=oo(e,n,18.0);
  t.box(22,4.2,3.8,"dark",o,0,2.1,0);
  t.box(4.5,3.8,3.2,"orange",o,12,2.3,0);
  t.box(5.5,3.8,3.0,"cream",o,-7,5.8,0);
  t.cylinder(0.28,14,"orangeLight",o,2,4.5,0);
  t.cylinder(0.8,2.2,"orange",o,-9,8.5,0);
}
,"porta-spagnola"(t,e,n){
  const o=oo(e,n,10.0);
  t.box(2.0,7.0,2.2,"cream",o,-3.5,3.5,0,0.15);
  t.box(2.0,7.0,2.2,"cream",o,3.5,3.5,0,0.15);
  t.box(5.8,1.5,2.0,"cream",o,0,6.6,0,0.15);
  t.box(3.0,2.0,0.7,"terrain2",o,0,8.3,0,0.2);
  t.box(4.5,0.28,0.18,"dark",o,0,4.8,0);
}
,"hazard-barrel"(t,e,n){
  const o=oo(e,n,1.2);
  t.cylinder(0.46,1.1,"orange",o,0,0.55,0);
  t.cylinder(0.5,0.08,"dark",o,0,1.1,0);
  t.cylinder(0.48,0.2,"gold",o,0,0.55,0);
}
,"bunker"(t,e,n){
  const o=oo(e,n,3.5);
  t.box(4.2,2.0,3.2,"terrain2",o,0,1.0,0,0.25);
  t.box(3.0,0.3,0.9,"dark",o,0,1.3,1.3);
  t.box(4.8,0.45,3.8,"terrain",o,0,2.2,0,0.2);
}
,"cactus-opuntia"(t,e,n){
  const o=oo(e,n,2.2);
  t.ball(0.65,0.85,0.18,"foliage",o,0,0.8,0);
  t.ball(0.55,0.65,0.16,"foliage",o,0.55,1.4,0.1);
  t.ball(0.5,0.6,0.16,"foliage",o,-0.38,1.6,-0.1);
  t.ball(0.12,0.16,0.12,"orange",o,0.75,2.0,0.1);
  t.ball(0.12,0.16,0.12,"orange",o,-0.45,2.1,-0.1);
}
,"etna-silhouette"(t,e,n){
  const o=oo(e,n,24.0);
  t.cylinder(18,10,"terrain",o,0,5,0);
  t.ball(6,2.6,6,"cream",o,0,10.2,0);
  t.ball(3.0,2.2,3.0,"cream",o,1.2,12.5,0);
}"""

def main():
    print("Reading bundle/index-augusta-v2.js...")
    with open("bundle/index-augusta-v2.js", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace the level definitions block
    start_marker = "// --- AUGUSTA LEVELS (PROVINCIA DI SIRACUSA) ---"
    end_marker = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5]"
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker)
    if start_pos == -1 or end_pos == -1:
        raise Exception(f"Markers not found: start_pos={start_pos}, end_pos={end_pos}")

    new_levels_code = f"""{start_marker}
{get_level_1()}

{get_level_2()}

{get_level_3()}

{get_level_4()}

{get_level_5()}

{get_level_6()}

{get_level_7()}

{get_level_8()}

{get_level_9()}

{get_level_10()}

"""
    new_sc_code = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10]"

    content = content[:start_pos] + new_levels_code + new_sc_code + content[end_pos + len(end_marker):]
    print("Levels 1-10 and Sc list replaced successfully!")

    # 2. Inject custom 3D decor builders into _D
    d_end_marker = "castle(t,e,n){sx(t,e,0,0,0,n)}};function kre"
    d_end_pos = content.find(d_end_marker)
    if d_end_pos == -1:
        raise Exception("Marker for _D end not found!")
    
    inject_pos = d_end_pos + len("castle(t,e,n){sx(t,e,0,0,0,n)}")
    decor_code = get_3d_decor_builders()
    content = content[:inject_pos] + decor_code + content[inject_pos:]
    print("Custom 3D decor models injected into _D successfully!")

    # 3. Update chapter count limit Ade = 5 to Ade = 10
    ade_marker = "const Ade=5,"
    ade_pos = content.find(ade_marker)
    if ade_pos != -1:
        content = content[:ade_pos] + "const Ade=10," + content[ade_pos + len(ade_marker):]
        print("Updated Ade=10 (unlocked all 10 chapters)!")
    else:
        print("Warning: Ade=5 marker not found, checking alternatives...")

    with open("bundle/index-augusta-v2.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Saved updated bundle/index-augusta-v2.js!")

if __name__ == "__main__":
    main()
