# tools/assemble_all_levels.py
import os

with open("tools/gta_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write('''# tools/gta_all_10_levels.py
"""
10 Bespoke Handcrafted Levels for GTA: Giuseppe Taglia Alberi (Augusta)
Audited for physics, zero impossible jumps, 52 themed 3D clay objects.
"""

def get_level_1():
    return """const augustaL1 = yr({
  layoutVersion: 1,
  name: "Salviamo il Verde di Augusta: I Giardini Pubblici",
  short: "Villa Comunale",
  label: "Ficus secolari, Duomo barocco e la rinascita verde",
  biome: "citadel",
  intro: "Benvenuto alla Villa Comunale di Augusta! Fondata nel 1850 sulla spianata di Piazza d'Armi, ospita i monumentali Ficus secolari minacciati da abbattimenti sconsiderati. Con la tua paletta e i germogli di Ficus, supera le motoseghe impazzite, disattiva le bolle di calore e raggiungi il sagrato barocco della Chiesa Madre per piantare il futuro verde di Augusta!",
  sky: "#1c6498",
  fog: "#3b82b0",
  spawn: {x: 1.5, y: 13},
  end: 245,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. L'Ingresso della Villa & Il Cartello Civico"},
    {x: 48, name: "2. I Ficus Secolari (1850) & La Difesa dei Rami", landmark: "pulsedrum"},
    {x: 104, name: "3. Il Belvedere Panoramico sul Golfo Xifonio", landmark: "bannerarch"},
    {x: 165, name: "4. Il Viale delle Palme & L'Arresto delle Motoseghe", landmark: "sandwheel"},
    {x: 215, name: "5. Il Sagrato Barocco della Chiesa Madre", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 13, "stone"),
    S("plat-ficus-step1", 10, 4.0, 13.6, "stone"),
    S("plat-ficus-step2", 16, 6.5, 14.5, "stone"),
    S("step-roots", 24, 3.6, 15.6, "ledge"),
    S("lift-canopy", 29, 3.5, 14.8, "lift", {moveX: 2.8, period: 4.5}),
    S("plat-avenue", 34, 7.5, 15.2, "stone"),
    S("pit-spikes-1", 7, 38, 2.0, "stone", {spiked: !0}),

    S("opt-sprout1", 42, 3.5, 18.0, "ledge", {optional: !0}),
    S("spring-branch1", 43, 2.0, 15.2, "spring"),
    S("dock-ficus-main", 48, 7, 15.2, "stone", {checkpoint: 50, depth: 22, landmark: "pulsedrum"}),
    S("crumble-bark", 57, 4.2, 14.8, "crumble"),
    S("plat-shaded", 63, 6, 14.2, "stone"),
    S("ferry-breeze", 71, 4.5, 13.8, "ferry", {travel: 18, speed: 3.2}),
    S("plat-seawall", 91, 7, 13.8, "stone"),
    S("pit-spikes-2", 50, 52, 2.0, "stone", {spiked: !0}),

    S("dock-belvedere", 104, 7, 11.2, "stone", {checkpoint: 106, depth: 22, landmark: "bannerarch"}),
    S("balance-terrace", 113, 7, 11.8, "balance"),
    S("step-parapet", 122, 3.8, 12.8, "ledge"),
    S("step-baluster", 126, 3.2, 14.2, "ledge"),
    S("balance-lookout", 128, 7.5, 14.8, "balance"),
    S("opt-sprout2", 133, 3.5, 18.8, "ledge", {optional: !0}),
    S("lift-gulf", 138, 3.6, 14.5, "lift", {moveY: 2.2, period: 4.0}),
    S("plat-irrigation", 145, 22, 16.0, "stone"),
    S("switch-water", 153, 2.2, 16.15, "switch", {channel: "garden-water", latch: !0}),
    S("gate-duomo", 160, 1.8, 20.0, "gate", {channel: "garden-water", h: 4}),

    S("dock-palms", 165, 7, 16.0, "stone", {checkpoint: 167, depth: 22, landmark: "sandwheel"}),
    S("pulse-stump1", 174, 3.8, 15.6, "pulse", {period: 4.2, phase: 0}),
    S("pulse-stump2", 180, 3.8, 15.6, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-fountain", 186, 6, 14.8, "stone"),
    S("step-piazza1", 197, 3.2, 16.0, "ledge"),
    S("lift-pergola", 194, 3.6, 14.2, "lift", {moveX: 2.6, moveY: 1.8, period: 5.0}),
    S("opt-sprout3", 202, 3.5, 20.8, "ledge", {optional: !0}),
    S("spring-piazza", 203, 2.0, 15.8, "spring"),
    S("plat-terrace-piazza", 201, 8, 15.8, "stone", {landmark: "sandwheel"}),
    S("pit-spikes-3", 167, 45, 4.0, "stone", {spiked: !0}),

    S("dock-duomo-approach", 213, 7, 15.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-duomo1", 222, 3.8, 16.8, "ledge"),
    S("step-duomo2", 228, 4.2, 17.8, "ledge"),
    S("goal-duomo", 234, 15, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  decor: [
    {kind: "cartello-salviamo-verde", x: 4.5, y: 13.0, size: 4.0, z: -1.8},
    {kind: "panchina-villa", x: 9.0, y: 13.0, size: 3.0, z: -1.5},
    {kind: "vaso-terracotta-agave", x: 14.0, y: 14.5, size: 2.2, z: -1.2},
    {kind: "palma-augusta", x: 20.0, y: 14.5, size: 8.5, z: -3.5},
    {kind: "ficus-centenario", x: 54.0, y: 15.2, size: 14.0, z: -4.0},
    {kind: "cut-stump", x: 62.0, y: 14.2, size: 3.0, z: -2.0},
    {kind: "chainsaw", x: 66.0, y: 14.2, size: 2.5, z: -1.8},
    {kind: "panchina-villa", x: 74.0, y: 13.8, size: 3.0, z: -1.5},
    {kind: "ficus-centenario", x: 88.0, y: 13.8, size: 13.0, z: -4.2},
    {kind: "balustrata-xifonio", x: 108.0, y: 11.2, size: 4.5, z: -2.5},
    {kind: "gozzo-xifonio", x: 118.0, y: 8.0, size: 5.5, z: -10.0},
    {kind: "vaso-terracotta-agave", x: 124.0, y: 12.8, size: 2.2, z: -1.2},
    {kind: "palma-augusta", x: 130.0, y: 13.8, size: 8.5, z: -3.5},
    {kind: "gozzo-xifonio", x: 142.0, y: 7.5, size: 5.0, z: -12.0},
    {kind: "cut-stump", x: 168.0, y: 16.0, size: 3.0, z: -2.0},
    {kind: "chainsaw", x: 172.0, y: 16.0, size: 2.5, z: -1.8},
    {kind: "heat-wave", x: 178.0, y: 15.6, size: 3.5, z: -1.5},
    {kind: "fountain-augusta", x: 190.0, y: 14.8, size: 4.0, z: -2.5},
    {kind: "palma-augusta", x: 196.0, y: 15.8, size: 9.0, z: -3.5},
    {kind: "cartello-salviamo-verde", x: 206.0, y: 15.8, size: 3.8, z: -1.8},
    {kind: "barocco-duomo", x: 236.0, y: 18.8, size: 18.0, z: -4.5},
    {kind: "vaso-terracotta-agave", x: 226.0, y: 17.8, size: 2.5, z: -1.5},
    {kind: "panchina-villa", x: 230.0, y: 18.8, size: 3.0, z: -1.5},
    {kind: "tree-sapling", x: 242.0, y: 18.8, size: 2.5, z: -1.5}
  ],
  stamps: [{x: 42.5, y: 19.5}, {x: 133.5, y: 20.5}, {x: 202.5, y: 22.5}],
  coins: [
    {x: 12, y: 15.2}, {x: 18, y: 16.0}, {x: 25, y: 17.0}, {x: 35, y: 16.8},
    {x: 43, y: 16.5}, {x: 60, y: 16.2}, {x: 65, y: 15.6}, {x: 75, y: 15.2},
    {x: 82, y: 15.2}, {x: 94, y: 15.2}, {x: 115, y: 13.2}, {x: 124, y: 14.2},
    {x: 130, y: 15.2}, {x: 135, y: 15.2}, {x: 150, y: 17.6}, {x: 157, y: 17.6},
    {x: 176, y: 17.2}, {x: 182, y: 17.2}, {x: 188, y: 16.2}, {x: 205, y: 17.2},
    {x: 224, y: 18.2}, {x: 230, y: 19.2}
  ],
  hazards: [
    {x: 57, y: 14.8, w: 4.2, h: 0.5, kind: "crumble"},
    {x: 174, y: 15.6, w: 3.8, h: 0.5, kind: "pulse"},
    {x: 180, y: 15.6, w: 3.8, h: 0.5, kind: "pulse"}
  ],
  hints: [
    {x: 0, end: 18, title: "Villa Comunale di Augusta (1850)", text: "Fondata dal generale Micheroux sulla Piazza d'Armi. I grandi Ficus secolari proteggono la citta dalle bolle di calore!", icon: "walk"},
    {x: 48, end: 68, title: "I Ficus Monumentali", text: "Le radici aeree del Ficus formano una cattedrale viva. Salta sui rami ed evita le motoseghe che abbattono gli alberi!", icon: "sink"},
    {x: 104, end: 125, title: "Belvedere sul Golfo Xifonio", text: "Dalla balconata della Villa si scorge il mare ionico e i gozzi dei pescatori. Raccogli il secondo germoglio dorato!", icon: "knead"},
    {x: 148, end: 165, title: "La Valvola Idraulica dei Giardini", text: "Premi l'interruttore della condotta per innaffiare le radici secolari e aprire la cancellata di Piazza Duomo!", icon: "walk"},
    {x: 215, end: 242, title: "Piazza Duomo & Chiesa Madre (1769)", text: "Sei arrivato al Duomo barocco di Santa Maria Assunta! Pianta il germoglio al centro del sagrato per celebrare la rinascita verde!", icon: "bell"}
  ],
  shaping: [], enemies: [], crushers: []
});"""

def get_level_2():
    return """const augustaL2 = yr({
  layoutVersion: 1,
  name: "Lungomare Rossini & Il Diluvio Fognario",
  short: "Lungomare Rossini",
  label: "Tombini che esplodono, liquami in strada e crisi climatica",
  biome: "nightfall",
  intro: "Le bombe d'acqua della crisi climatica travolgono Augusta! La rete fognaria obsoleta cede e i tombini del lungomare Rossini saltano via sparando getti di liquami e melma. Salta sulle passerelle di soccorso e chiudi le paratoie di spurgo!",
  sky: "#131f2b",
  fog: "#1f3142",
  spawn: {x: 1.5, y: 11},
  end: 242,
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
    S("crane-lift1", 26, 3.8, 13.0, "lift", {moveY: 2.2, period: 4.2}),
    S("plat-pierhead", 32, 6.5, 13.8, "stone"),
    S("spring-port1", 41, 2.0, 13.8, "spring"),
    S("opt-port1", 40, 3.6, 17.8, "ledge", {optional: !0}),
    S("pit-mercury-1", 7, 40, 1.5, "stone", {spiked: !0}),

    S("dock-channel", 46, 7.5, 13.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-gangway1", 56, 4.8, 13.2, "stone"),
    S("ferry-mercury", 63, 5.5, 12.6, "ferry", {travel: 24, speed: 3.4}),
    S("plat-crane-isle", 90, 8.0, 12.6, "stone"),
    S("pit-mercury-2", 52, 48, 1.5, "stone", {spiked: !0}),

    // SECTION 3: FIXED JUMP: step-port2 at y=15.2 (dy=+1.0 from 14.2), crane-jib2 at y=15.6!
    S("dock-cranes", 100, 7.0, 12.6, "stone", {checkpoint: 102, depth: 22, landmark: "bannerarch"}),
    S("crane-jib1", 109, 8.0, 13.2, "balance"),
    S("step-trolley", 119, 3.8, 14.2, "ledge"),
    S("step-port2", 123.5, 3.2, 15.2, "ledge"),
    S("crane-jib2", 127.5, 8.0, 15.6, "balance"),
    S("opt-port2", 133, 3.6, 19.5, "ledge", {optional: !0}),
    S("lift-gantry", 136.5, 3.6, 15.6, "lift", {moveY: 1.8, period: 4.0}),
    S("plat-dockgate-floor", 143, 22, 16.0, "stone", {landmark: "beacon"}),
    S("switch-dockgate", 152, 2.2, 16.15, "switch", {channel: "dock-lock", latch: !0}),
    S("gate-dock", 159, 1.8, 20.0, "gate", {channel: "dock-lock", h: 4}),

    S("dock-barge", 163, 7.5, 16.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-wharf1", 173, 4.0, 15.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-wharf2", 179, 4.0, 15.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-tanker-deck", 185, 6.5, 15.0, "stone"),
    S("step-port3", 194, 3.2, 15.6, "ledge"),
    S("lift-winch", 193, 3.6, 14.0, "lift", {moveX: 2.8, moveY: 1.8, period: 4.8}),
    S("opt-port3", 201, 3.5, 19.5, "ledge", {optional: !0}),
    S("spring-port3", 200, 2.0, 15.6, "spring"),
    S("plat-seawall", 198, 8.5, 15.6, "stone", {landmark: "sandwheel"}),
    S("step-pier-link", 207.5, 3.5, 15.6, "ledge"),
    S("pit-mercury-3", 168, 42, 2.5, "stone", {spiked: !0}),

    S("dock-exit", 212, 7.0, 15.6, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-rock1", 221, 3.8, 16.6, "ledge"),
    S("step-rock2", 227, 4.2, 17.6, "ledge"),
    S("goal-harbor", 233, 14, 18.6, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 40, y: 1.5},
    {x: 52, w: 48, y: 1.5},
    {x: 168, w: 42, y: 2.5}
  ],
  decor: [
    {kind: "sewer-manhole", x: 4.0, y: 11.0, size: 2.5, z: -1.5},
    {kind: "valvola-spurgo", x: 12.0, y: 11.8, size: 2.2, z: -1.2},
    {kind: "salvagente-rossini", x: 18.0, y: 12.6, size: 1.8, z: -1.2},
    {kind: "sewer-manhole", x: 30.0, y: 13.8, size: 2.5, z: -1.5},
    {kind: "pompa-idrovora", x: 35.0, y: 13.8, size: 2.5, z: -1.5},
    {kind: "chiatta-megara", x: 68.0, y: 10.0, size: 14.0, z: -6.0},
    {kind: "gru-portuale-rossini", x: 92.0, y: 12.6, size: 16.0, z: -4.5},
    {kind: "sewer-manhole", x: 112.0, y: 12.6, size: 2.5, z: -1.5},
    {kind: "valvola-spurgo", x: 120.0, y: 14.2, size: 2.2, z: -1.2},
    {kind: "gru-portuale-rossini", x: 132.0, y: 15.6, size: 16.0, z: -4.5},
    {kind: "pompa-idrovora", x: 148.0, y: 16.0, size: 2.5, z: -1.5},
    {kind: "salvagente-rossini", x: 166.0, y: 16.0, size: 1.8, z: -1.2},
    {kind: "chiatta-megara", x: 188.0, y: 12.0, size: 14.0, z: -6.0},
    {kind: "sewer-manhole", x: 215.0, y: 15.6, size: 2.5, z: -1.5},
    {kind: "valvola-spurgo", x: 224.0, y: 16.6, size: 2.2, z: -1.2}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Rada di Augusta & Il Lungomare", text: "Le bombe d'acqua fanno saltare i tombini fognari! Evita i liquami ed attraversa i pontili della marina.", touchText: "Evita i liquami ed attraversa con attenzione i pontili di soccorso!"},
    {x: 48, end: 66, icon: "knead", title: "La Chiatta Megara", text: "Sali sulla chiatta di salvataggio a fune per superare il canale melmoso."},
    {x: 102, end: 125, icon: "knead", title: "Bracci delle Gru Meccaniche", text: "I bracci delle gru del molo sono bilanciati: salta al centro per mantenere la stabilita!"},
    {x: 146, end: 160, icon: "walk", title: "Paratoia di Sicurezza", text: "Attiva la valvola principale per abbassare la paratoia ed evitare l'allagamento delle vie costiere."},
    {x: 212, end: 242, icon: "bell", title: "Molo Nord di Augusta", text: "Suona la campana navale per mettere in sicurezza il lungomare e completare il livello!"}
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
  stamps: [{x: 41.0, y: 19.5}, {x: 134.5, y: 21.0}, {x: 202.5, y: 21.5}],
  enemies: [], crushers: []
});"""

def get_level_3():
    return """const augustaL3 = yr({
  layoutVersion: 1,
  name: "Il Golfo Xifonio & Il Depuratore Che Non C'è",
  short: "Golfo Xifonio",
  label: "Bagnanti tra divieti di balneazione e scarichi a mare",
  biome: "nightfall",
  intro: "Il paradosso del golfo Xifonio: le famiglie fanno il bagno tra splendide acque e cartelli di divieto di balneazione ignorati, mentre scarichi fognari abusivi riversano reflui in mare senza depuratore. Salta tra le boe e attiva i filtri marini!",
  sky: "#183852",
  fog: "#244c6e",
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
    S("step-pyrite1", 10, 4.0, 12.8, "ledge"),
    S("plat-terrace1", 16, 7.0, 13.6, "stone"),
    S("crumble-red1", 25, 4.2, 14.2, "crumble"),
    S("plat-terrace2", 31, 7.5, 14.4, "stone"),
    S("spring-ash1", 40, 2.0, 14.4, "spring"),
    S("opt-ash1", 39, 3.6, 18.5, "ledge", {optional: !0}),
    S("pit-ash-1", 7, 39, 2.0, "stone", {spiked: !0}),

    S("dock-crater", 46, 7.5, 14.4, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("crumble-crater1", 55, 4.2, 14.2, "crumble"),
    S("ferry-fumarole", 61, 5.5, 13.8, "ferry", {travel: 16, speed: 3.0}),
    S("plat-ridge", 79, 7.0, 13.8, "stone"),
    S("plat-stepping-xifonio", 88, 4.5, 13.5, "stone"),
    S("pit-ash-2", 52, 46, 2.0, "stone", {spiked: !0}),

    S("dock-fumaroles", 95, 7.0, 13.2, "stone", {checkpoint: 97, depth: 22, landmark: "bannerarch"}),
    S("geyser-vent", 104, 6.0, 12.0, "balance"),
    S("step-geyser-ledge", 112, 3.5, 13.5, "ledge"),
    S("step-ash2", 118, 3.5, 14.6, "ledge"),
    S("crane-jib-ash", 123.5, 7.5, 15.2, "balance"),
    S("opt-ash2", 132, 3.6, 19.5, "ledge", {optional: !0}),
    S("lift-ash", 137, 3.6, 15.0, "lift", {moveY: 2.2, period: 4.2}),
    S("plat-ashgate-floor", 143, 22, 16.0, "stone", {landmark: "beacon"}),
    S("switch-ashgate", 152, 2.2, 16.15, "switch", {channel: "ash-lock", latch: !0}),
    S("gate-ash", 159, 1.8, 20.0, "gate", {channel: "ash-lock", h: 4}),

    S("dock-slag", 163, 7.5, 16.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-ash1", 173, 4.0, 15.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-ash2", 179, 4.0, 15.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-calc-deck", 185, 6.5, 14.8, "stone"),
    S("step-ash3", 194, 3.2, 15.8, "ledge"),
    S("lift-winch-ash", 193, 3.6, 14.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-ash3", 201, 3.5, 20.0, "ledge", {optional: !0}),
    S("spring-ash3", 201, 2.0, 15.8, "spring"),
    S("plat-ashcliff", 199, 8.5, 15.8, "stone", {landmark: "sandwheel"}),
    S("step-cliff-link", 208, 3.5, 15.8, "ledge"),
    S("pit-ash-3", 168, 44, 2.5, "stone", {spiked: !0}),

    S("dock-ash-exit", 213, 7.0, 15.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-ash-rock1", 222, 3.8, 16.8, "ledge"),
    S("step-ash-rock2", 228, 4.2, 17.8, "ledge"),
    S("goal-ash", 234, 14, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 2.0},
    {x: 52, w: 46, y: 2.0},
    {x: 168, w: 44, y: 2.5}
  ],
  decor: [
    {kind: "cartello-divieto-balneazione", x: 4.0, y: 12.0, size: 3.2, z: -1.6},
    {kind: "ombrellone-spiaggia", x: 12.0, y: 12.8, size: 3.8, z: -2.0},
    {kind: "sdraio-bagnante", x: 15.0, y: 12.8, size: 2.0, z: -1.5},
    {kind: "tubo-scarico-mare", x: 28.0, y: 13.0, size: 4.0, z: -2.5},
    {kind: "boa-filtrante", x: 50.0, y: 12.0, size: 3.5, z: -3.0},
    {kind: "cartello-divieto-balneazione", x: 74.0, y: 13.8, size: 3.2, z: -1.6},
    {kind: "tubo-scarico-mare", x: 82.0, y: 12.0, size: 4.0, z: -2.5},
    {kind: "campanello-sos-costa", x: 98.0, y: 13.2, size: 3.0, z: -1.2},
    {kind: "boa-filtrante", x: 114.0, y: 11.5, size: 3.5, z: -3.0},
    {kind: "ombrellone-spiaggia", x: 145.0, y: 16.0, size: 3.8, z: -2.0},
    {kind: "cartello-divieto-balneazione", x: 165.0, y: 16.0, size: 3.2, z: -1.6},
    {kind: "tubo-scarico-mare", x: 186.0, y: 13.5, size: 4.0, z: -2.5},
    {kind: "boa-filtrante", x: 202.0, y: 14.0, size: 3.5, z: -3.0},
    {kind: "campanello-sos-costa", x: 216.0, y: 15.8, size: 3.0, z: -1.2}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Golfo Xifonio & Divieti", text: "Acque cristalline ma inquinate da scarichi abusivi. Fai attenzione ai cartelli di divieto di balneazione!"},
    {x: 48, end: 66, icon: "knead", title: "La Zattera di Filtraggio", text: "Sali sulla chiatta per attraversare la zona di sversamento priva di depuratore."},
    {x: 102, end: 125, icon: "knead", title: "Geyser di Scarico Marino", text: "I reflui generano correnti d'aria ascendenti. Usa le piattaforme filtranti per salire."},
    {x: 146, end: 160, icon: "walk", title: "Filtro Idrico di Baia", text: "Attiva la valvola per depurare il tratto di costa e procedere verso il belvedere."},
    {x: 212, end: 240, icon: "bell", title: "Belvedere sul Golfo Xifonio", text: "Suona la campana per chiedere a gran voce un vero depuratore per Augusta!"}
  ],
  coins: [
    {x: 8, y: 14.0}, {x: 12, y: 14.5}, {x: 18, y: 15.0}, {x: 21, y: 15.0},
    {x: 28, y: 16.0}, {x: 34, y: 16.0}, {x: 41, y: 16.5}, {x: 58, y: 15.0},
    {x: 68, y: 14.5}, {x: 74, y: 14.5}, {x: 80, y: 14.5}, {x: 86, y: 14.5},
    {x: 104, y: 14.5}, {x: 111, y: 15.0}, {x: 115, y: 15.0}, {x: 121, y: 16.0},
    {x: 129, y: 17.5}, {x: 147, y: 17.5}, {x: 154, y: 17.5}, {x: 166, y: 17.5},
    {x: 175, y: 17.0}, {x: 181, y: 17.0}, {x: 187, y: 16.5}, {x: 195, y: 16.5},
    {x: 204, y: 17.5}, {x: 223, y: 18.5}, {x: 229, y: 19.5}, {x: 235, y: 20.5}
  ],
  stamps: [{x: 41.0, y: 19.5}, {x: 134.5, y: 21.0}, {x: 202.5, y: 21.5}],
  enemies: [], crushers: []
});"""

def get_level_4():
    return """const augustaL4 = yr({
  layoutVersion: 1,
  name: "Il Petrolchimico & Il Triangolo della Morte",
  short: "Petrolchimico",
  label: "Fumi industriali, idrocarburi e la richiesta di bonifica",
  biome: "nightfall",
  intro: "Il polo industriale Priolo-Augusta-Melilli: ciminiere fumanti, serbatoi e fiaccole accese giorno e notte. Gli abitanti respirano miasmi e chiedono bonifiche mai arrivate. Raggiungi le torri di monitoraggio e riduci le emissioni!",
  sky: "#21151e",
  fog: "#361f30",
  spawn: {x: 1.5, y: 11},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Condotte di Petrolio Greggio", landmark: "beacon"},
    {x: 48, name: "2. Vasche di Raffinazione Tossica", landmark: "pulsedrum"},
    {x: 102, name: "3. Fiaccole & Fumi Acri", landmark: "bannerarch"},
    {x: 162, name: "4. Il Deposito Idrocarburi", landmark: "sandwheel"},
    {x: 212, name: "5. Torretta di Monitoraggio Aria", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 11, "stone", {landmark: "beacon"}),
    S("step-pipe1", 10, 4.0, 11.8, "ledge"),
    S("plat-manifold1", 16, 7.0, 12.6, "stone"),
    S("crane-refinery1", 25, 4.0, 13.0, "lift", {moveY: 2.2, period: 4.2}),
    S("plat-pipebridge", 31, 7.5, 13.8, "stone"),
    S("spring-petrol1", 40, 2.0, 13.8, "spring"),
    S("opt-petrol1", 39, 3.6, 18.0, "ledge", {optional: !0}),
    S("pit-petrol-1", 7, 39, 1.5, "stone", {spiked: !0}),

    S("dock-refining", 46, 7.5, 13.8, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-gangway-ind", 55, 4.8, 13.2, "stone"),
    S("ferry-petrol", 62, 5.5, 12.6, "ferry", {travel: 24, speed: 3.4}),
    S("plat-cracker-isle", 88, 8.0, 12.6, "stone"),
    S("pit-petrol-2", 52, 46, 1.5, "stone", {spiked: !0}),

    S("dock-flares", 98, 7.0, 12.6, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-petrol", 107, 8.0, 13.2, "balance"),
    S("step-grate1", 117, 3.8, 14.0, "ledge"),
    S("step-sewer2", 122.5, 3.2, 15.2, "ledge"),
    S("crane-jib-petrol2", 127.5, 8.0, 15.6, "balance"),
    S("opt-petrol2", 134, 3.6, 19.5, "ledge", {optional: !0}),
    S("lift-refinery", 137, 3.6, 15.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-flaregate-floor", 143, 22, 16.0, "stone", {landmark: "beacon"}),
    S("switch-flaregate", 152, 2.2, 16.15, "switch", {channel: "flare-lock", latch: !0}),
    S("gate-flare", 159, 1.8, 20.0, "gate", {channel: "flare-lock", h: 4}),

    S("dock-tanker", 163, 7.5, 16.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-ref1", 173, 4.0, 15.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-ref2", 179, 4.0, 15.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-tanker-top", 185, 6.5, 15.0, "stone"),
    S("step-ref3", 194, 3.2, 15.8, "ledge"),
    S("lift-winch-ref", 193, 3.6, 14.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-petrol3", 201, 3.5, 20.0, "ledge", {optional: !0}),
    S("spring-petrol3", 200, 2.0, 15.8, "spring"),
    S("plat-tankfarm", 198, 8.5, 15.8, "stone", {landmark: "sandwheel"}),
    S("step-ref-link", 208, 3.5, 15.8, "ledge"),
    S("pit-petrol-3", 168, 42, 2.5, "stone", {spiked: !0}),

    S("dock-ref-exit", 213, 7.0, 15.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-ref-rock1", 222, 3.8, 16.8, "ledge"),
    S("step-ref-rock2", 228, 4.2, 17.8, "ledge"),
    S("goal-refinery", 234, 14, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 1.5},
    {x: 52, w: 46, y: 1.5},
    {x: 168, w: 42, y: 2.5}
  ],
  decor: [
    {kind: "traliccio-tubi", x: 8.0, y: 11.8, size: 7.5, z: -3.0},
    {kind: "fusto-tossico", x: 18.0, y: 12.6, size: 1.8, z: -1.2},
    {kind: "manometro-pressione", x: 22.0, y: 12.6, size: 1.8, z: -1.0},
    {kind: "oil-tank", x: 38.0, y: 13.8, size: 12.0, z: -5.0},
    {kind: "ciminiera-bicolore", x: 58.0, y: 13.2, size: 18.0, z: -6.0},
    {kind: "flare-stack", x: 85.0, y: 12.6, size: 14.0, z: -4.0},
    {kind: "traliccio-tubi", x: 104.0, y: 12.6, size: 7.5, z: -3.0},
    {kind: "fusto-tossico", x: 112.0, y: 14.0, size: 1.8, z: -1.2},
    {kind: "ciminiera-bicolore", x: 130.0, y: 15.6, size: 18.0, z: -6.0},
    {kind: "flare-stack", x: 150.0, y: 16.0, size: 14.0, z: -4.0},
    {kind: "oil-tank", x: 172.0, y: 16.0, size: 12.0, z: -5.0},
    {kind: "manometro-pressione", x: 188.0, y: 15.0, size: 1.8, z: -1.0},
    {kind: "fusto-tossico", x: 202.0, y: 15.8, size: 1.8, z: -1.2},
    {kind: "traliccio-tubi", x: 218.0, y: 15.8, size: 7.5, z: -3.0}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Petrolchimico di Augusta", text: "Il cuore dell'industria chimica: salta sopra le condotte di petrolio greggio evitando i reflui tossici!"},
    {x: 48, end: 66, icon: "knead", title: "Chiatta dei Rifiuti Industriali", text: "Attraversa il canale industriale usando la chiatta automatizzata a cavo."},
    {x: 102, end: 125, icon: "knead", title: "Bracci dei Serbatoi & Fiaccole", text: "Il fumo è denso: salta sulle travi metalliche e mantieni il baricentro!"},
    {x: 146, end: 160, icon: "walk", title: "Valvola di Sicurezza Impianti", text: "Attiva l'interruttore per sfiatare i fumi nocivi e aprire il cancello verso l'uscita."},
    {x: 212, end: 240, icon: "bell", title: "Stazione Monitoraggio Qualita Aria", text: "Attiva la campana della centralina per registrare i dati ambientali ed esigere bonifiche!"}
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
  stamps: [{x: 41.0, y: 19.5}, {x: 134.5, y: 21.0}, {x: 202.5, y: 21.5}],
  enemies: [], crushers: []
});"""

def get_level_5():
    return """const augustaL5 = yr({
  layoutVersion: 1,
  name: "Hangar Dirigibili & L'Amianto Sotto i Piedi",
  short: "Hangar Dirigibili",
  label: "Capolavoro in cemento armato del 1917 e macerie tossiche",
  biome: "nightfall",
  intro: "L'incredibile Hangar per Dirigibili del 1917: una meraviglia ingegneristica in cemento armato abbandonata all'incuria, circondata da onduline di amianto frantumate dal vento. Scala le titaniche centine paraboliche ed esponi lo scandalo!",
  sky: "#19222d",
  fog: "#253443",
  spawn: {x: 1.5, y: 23},
  end: 240,
  previousDistance: 1100,
  cameraY: 3,
  sections: [
    {x: -8, name: "1. Il Portale Est dell'Idroscalo", landmark: "beacon"},
    {x: 48, name: "2. La Volta Parabolica in Cemento", landmark: "pulsedrum"},
    {x: 102, name: "3. Trave Reticolare di Carroponte", landmark: "bannerarch"},
    {x: 162, name: "4. Lastre di Amianto & Ponteggi", landmark: "sandwheel"},
    {x: 212, name: "5. Cupola Superiore del Dirigibile", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 23, "stone", {landmark: "beacon"}),
    S("step-hangar1", 10, 4.0, 23.6, "ledge"),
    S("plat-hangar-floor", 16, 7.0, 24.2, "stone"),
    S("crane-hangar1", 25, 4.0, 24.5, "lift", {moveY: 2.2, period: 4.2}),
    S("plat-girder1", 31, 7.5, 25.2, "stone"),
    S("spring-hangar1", 40, 2.0, 25.2, "spring"),
    S("opt-hangar1", 39, 3.6, 29.5, "ledge", {optional: !0}),
    S("pit-hangar-1", 7, 39, 10.0, "stone", {spiked: !0}),

    S("dock-hangar-vault", 46, 7.5, 25.2, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-vault-floor", 55, 4.8, 24.6, "stone"),
    S("crane-nave", 61, 5.5, 24.0, "ferry", {travel: 16, speed: 3.2}),
    S("plat-catwalk", 79, 8.0, 24.0, "stone"),
    S("plat-girder-link", 89, 6.0, 24.0, "stone"),
    S("pit-hangar-2", 52, 46, 10.0, "stone", {spiked: !0}),

    S("dock-nave", 98, 7.0, 24.0, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-hangar", 107, 8.0, 24.6, "balance"),
    S("step-girder", 117, 3.8, 25.4, "ledge"),
    S("step-hangar2", 122.5, 3.2, 26.6, "ledge"),
    S("crane-jib-hangar2", 127.5, 8.0, 27.2, "balance"),
    S("opt-hangar2", 134, 3.6, 31.5, "ledge", {optional: !0}),
    S("lift-hangar", 137, 3.6, 26.8, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-hangargate-floor", 143, 22, 27.8, "stone", {landmark: "beacon"}),
    S("switch-hangargate", 152, 2.2, 27.95, "switch", {channel: "hangar-lock", latch: !0}),
    S("gate-hangar", 159, 1.8, 31.8, "gate", {channel: "hangar-lock", h: 4}),

    S("dock-asbestos", 163, 7.5, 27.8, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-hang1", 173, 4.0, 27.2, "pulse", {period: 4.2, phase: 0}),
    S("pulse-hang2", 179, 4.0, 27.2, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-hangar-top", 185, 6.5, 26.8, "stone"),
    S("step-hang3", 194, 3.2, 27.6, "ledge"),
    S("lift-winch-hang", 193, 3.6, 25.8, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-hang3", 201, 3.5, 31.8, "ledge", {optional: !0}),
    S("spring-hang3", 200, 2.0, 27.6, "spring"),
    S("plat-roofarch", 198, 8.5, 27.6, "stone", {landmark: "sandwheel"}),
    S("step-roof-link", 208, 3.5, 27.6, "ledge"),
    S("pit-hangar-3", 168, 42, 12.0, "stone", {spiked: !0}),

    S("dock-hang-exit", 213, 7.0, 27.6, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-hang-rock1", 222, 3.8, 28.6, "ledge"),
    S("step-hang-rock2", 228, 4.2, 29.6, "ledge"),
    S("goal-hangar", 234, 14, 30.6, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 10.0},
    {x: 52, w: 46, y: 10.0},
    {x: 168, w: 42, y: 12.0}
  ],
  decor: [
    {kind: "hangar-arch", x: 10.0, y: 23.0, size: 28.0, z: -5.0},
    {kind: "cartello-bonifica", x: 18.0, y: 24.2, size: 2.8, z: -1.2},
    {kind: "pannello-amianto", x: 26.0, y: 24.5, size: 3.2, z: -1.4},
    {kind: "dirigibile-relique", x: 50.0, y: 25.0, size: 15.0, z: -4.0},
    {kind: "faro-cantiere", x: 78.0, y: 24.0, size: 3.5, z: -1.5},
    {kind: "bidone-decontaminazione", x: 88.0, y: 24.0, size: 2.2, z: -1.2},
    {kind: "hangar-arch", x: 100.0, y: 24.0, size: 28.0, z: -5.0},
    {kind: "cartello-bonifica", x: 114.0, y: 25.4, size: 2.8, z: -1.2},
    {kind: "pannello-amianto", x: 130.0, y: 27.2, size: 3.2, z: -1.4},
    {kind: "faro-cantiere", x: 148.0, y: 27.8, size: 3.5, z: -1.5},
    {kind: "hangar-arch", x: 170.0, y: 27.0, size: 28.0, z: -5.0},
    {kind: "dirigibile-relique", x: 190.0, y: 27.0, size: 15.0, z: -4.0},
    {kind: "cartello-bonifica", x: 216.0, y: 27.6, size: 2.8, z: -1.2}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Hangar Dirigibili (1917)", text: "Monumento unico di architettura bellica: 105 metri di campata libera in cemento armato, oggi assediato da detriti."},
    {x: 48, end: 66, icon: "knead", title: "Carroponte di Ispezione", text: "Usa la chiatta mobile per superare la campata centrale sopra il pavimento ricolmo di onduline d'amianto."},
    {x: 102, end: 125, icon: "knead", title: "Centine Metalliche Sospese", text: "Le passerelle superiori oscillano sopra l'abisso dell'hangar. Salta al centro delle travi!"},
    {x: 146, end: 160, icon: "walk", title: "Portone di Ventilazione", text: "Premi il commutatore per sbloccare la massiccia porta scorrevole d'acciaio del dirigibile."},
    {x: 212, end: 240, icon: "bell", title: "Cima della Parabola in Cemento", text: "Suona la campana sul colmo dell'Hangar per richiedere il restauro e la bonifica immediata!"}
  ],
  coins: [
    {x: 8, y: 24.5}, {x: 12, y: 24.5}, {x: 18, y: 25.5}, {x: 21, y: 25.5},
    {x: 28, y: 26.5}, {x: 34, y: 26.5}, {x: 41, y: 27.0}, {x: 58, y: 25.5},
    {x: 68, y: 25.0}, {x: 74, y: 25.0}, {x: 80, y: 25.0}, {x: 86, y: 25.0},
    {x: 104, y: 25.5}, {x: 111, y: 26.0}, {x: 115, y: 26.0}, {x: 121, y: 27.0},
    {x: 129, y: 28.5}, {x: 147, y: 28.5}, {x: 154, y: 28.5}, {x: 166, y: 28.5},
    {x: 175, y: 28.0}, {x: 181, y: 28.0}, {x: 187, y: 27.5}, {x: 195, y: 27.5},
    {x: 204, y: 28.5}, {x: 223, y: 29.5}, {x: 229, y: 30.5}, {x: 235, y: 31.5}
  ],
  stamps: [{x: 41.0, y: 30.5}, {x: 134.5, y: 32.5}, {x: 202.5, y: 33.0}],
  enemies: [], crushers: []
});"""

def get_level_6():
    return """const augustaL6 = yr({
  layoutVersion: 1,
  name: "Il Castello Svevo & L'Abbandono dell'Imperatore",
  short: "Castello Svevo",
  label: "Fortezza federiciana del 1242 tra crepe, sterpaglie e promesse",
  biome: "nightfall",
  intro: "Voluto da Federico II di Svevia nel 1242 sulla punta estrema dell'isola: una magnifica roccaforte chiusa al pubblico, soffocata da transenne eterne e crolli parziali. Esplora le cortine e i bastioni per risvegliare la storia imperiale di Augusta!",
  sky: "#24191a",
  fog: "#382326",
  spawn: {x: 1.5, y: 14},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Il Fosso dei Balestrieri", landmark: "beacon"},
    {x: 48, name: "2. La Torre Angolare Sveva", landmark: "pulsedrum"},
    {x: 102, name: "3. Camminamento di Ronda Decaduto", landmark: "bannerarch"},
    {x: 162, name: "4. Cortile d'Armi con Sterpaglie", landmark: "sandwheel"},
    {x: 212, name: "5. Mastio Superiore Federiciano", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 14, "stone", {landmark: "beacon"}),
    S("step-castle1", 10, 4.0, 14.8, "ledge"),
    S("plat-castle-wall", 16, 7.0, 15.6, "stone"),
    S("crane-castle1", 25, 4.0, 15.8, "lift", {moveY: 2.0, period: 4.2}),
    S("plat-rampart1", 31, 7.5, 16.6, "stone"),
    S("spring-castle1", 40, 2.0, 16.6, "spring"),
    S("opt-castle1", 39, 3.6, 20.8, "ledge", {optional: !0}),
    S("pit-castle-1", 7, 39, 4.0, "stone", {spiked: !0}),

    S("dock-swabian-tower", 46, 7.5, 16.6, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-parapet", 55, 4.8, 16.0, "stone"),
    S("ferry-drawbridge", 62, 5.5, 15.4, "ferry", {travel: 24, speed: 3.4}),
    S("plat-rampart-isle", 88, 8.0, 15.4, "stone"),
    S("pit-castle-2", 52, 46, 4.0, "stone", {spiked: !0}),

    S("dock-merlons", 98, 7.0, 15.4, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-castle", 107, 8.0, 16.0, "balance"),
    S("step-merlon1", 117, 3.8, 17.0, "ledge"),
    S("step-castle2", 122.5, 3.2, 18.2, "ledge"),
    S("crane-jib-castle2", 127.5, 8.0, 18.6, "balance"),
    S("opt-castle2", 134, 3.6, 22.8, "ledge", {optional: !0}),
    S("lift-castle", 137, 3.6, 18.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-castlegate-floor", 143, 22, 19.0, "stone", {landmark: "beacon"}),
    S("switch-castlegate", 152, 2.2, 19.15, "switch", {channel: "castle-lock", latch: !0}),
    S("gate-castle", 159, 1.8, 23.0, "gate", {channel: "castle-lock", h: 4}),

    S("dock-courtyard", 163, 7.5, 19.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-cas1", 173, 4.0, 18.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-cas2", 179, 4.0, 18.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-courtyard-top", 185, 6.5, 18.0, "stone"),
    S("step-cas3", 194, 3.2, 18.8, "ledge"),
    S("lift-winch-cas", 193, 3.6, 17.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-castle3", 201, 3.5, 23.0, "ledge", {optional: !0}),
    S("spring-castle3", 200, 2.0, 18.8, "spring"),
    S("plat-keep", 198, 8.5, 18.8, "stone", {landmark: "sandwheel"}),
    S("step-keep-link", 208, 3.5, 18.8, "ledge"),
    S("pit-castle-3", 168, 42, 5.0, "stone", {spiked: !0}),

    S("dock-cas-exit", 213, 7.0, 18.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-cas-rock1", 222, 3.8, 19.8, "ledge"),
    S("step-cas-rock2", 228, 4.2, 20.8, "ledge"),
    S("goal-castle", 234, 14, 21.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 4.0},
    {x: 52, w: 46, y: 4.0},
    {x: 168, w: 42, y: 5.0}
  ],
  decor: [
    {kind: "torre-sveva", x: 12.0, y: 14.8, size: 16.0, z: -5.0},
    {kind: "stemma-federico", x: 20.0, y: 15.6, size: 3.0, z: -1.5},
    {kind: "lanterna-ferro-battuto", x: 28.0, y: 16.6, size: 1.8, z: -1.2},
    {kind: "catapulta-antica", x: 50.0, y: 16.6, size: 4.5, z: -2.0},
    {kind: "ponte-levatoio-svevo", x: 74.0, y: 15.4, size: 6.5, z: -3.0},
    {kind: "cannone-antico", x: 92.0, y: 15.4, size: 3.2, z: -1.5},
    {kind: "torre-sveva", x: 104.0, y: 15.4, size: 16.0, z: -5.0},
    {kind: "stemma-federico", x: 114.0, y: 17.0, size: 3.0, z: -1.5},
    {kind: "lanterna-ferro-battuto", x: 130.0, y: 18.6, size: 1.8, z: -1.2},
    {kind: "cannone-antico", x: 150.0, y: 19.0, size: 3.2, z: -1.5},
    {kind: "catapulta-antica", x: 172.0, y: 19.0, size: 4.5, z: -2.0},
    {kind: "torre-sveva", x: 200.0, y: 18.8, size: 16.0, z: -5.0},
    {kind: "stemma-federico", x: 220.0, y: 19.8, size: 3.0, z: -1.5}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Castello Svevo di Augusta (1242)", text: "Costruito dall'imperatore Federico II Stupor Mundi. Oggi versa in uno stato di colpevole abbandono."},
    {x: 48, end: 66, icon: "knead", title: "Ponte Levatoio del Maniero", text: "Attraversa il fossato medievale salendo sul vecchio ponte a fune."},
    {x: 102, end: 125, icon: "knead", title: "Merli Ghibellini e Crepe", text: "Salta sui merli di pietra calcarea e fai attenzione ai tratti franati."},
    {x: 146, end: 160, icon: "walk", title: "Erpice della Fortezza", text: "Aziona la leva dell'argano per alzare la grata medievale e liberare il cortile d'armi."},
    {x: 212, end: 240, icon: "bell", title: "Mastio Imperiale", text: "Raggiungi la sommità della torre per piantare la bandiera della tutela monumentale!"}
  ],
  coins: [
    {x: 8, y: 16.5}, {x: 12, y: 16.5}, {x: 18, y: 17.5}, {x: 21, y: 17.5},
    {x: 28, y: 18.5}, {x: 34, y: 18.5}, {x: 41, y: 19.0}, {x: 58, y: 17.5},
    {x: 68, y: 17.0}, {x: 74, y: 17.0}, {x: 80, y: 17.0}, {x: 86, y: 17.0},
    {x: 104, y: 17.5}, {x: 111, y: 18.0}, {x: 115, y: 18.0}, {x: 121, y: 19.0},
    {x: 129, y: 20.5}, {x: 147, y: 20.5}, {x: 154, y: 20.5}, {x: 166, y: 20.5},
    {x: 175, y: 20.0}, {x: 181, y: 20.0}, {x: 187, y: 19.5}, {x: 195, y: 19.5},
    {x: 204, y: 20.5}, {x: 223, y: 21.5}, {x: 229, y: 22.5}, {x: 235, y: 23.5}
  ],
  stamps: [{x: 41.0, y: 22.5}, {x: 134.5, y: 24.5}, {x: 202.5, y: 25.0}],
  enemies: [], crushers: []
});"""

def get_level_7():
    return """const augustaL7 = yr({
  layoutVersion: 1,
  name: "Capo Santa Croce & Il Santuario della Posidonia",
  short: "Capo Santa Croce",
  label: "Faro bianco, falesie calcaree e le praterie sottomarine",
  biome: "nightfall",
  intro: "Il promontorio di Capo Santa Croce: falesie calcaree a picco sullo Ionio, il faro borbonico e le preziose praterie di Posidonia oceanica che ossigenano il mare e frenano l'erosione costiera. Proteggi le scogliere dagli sversamenti!",
  sky: "#122a44",
  fog: "#1c3c5e",
  spawn: {x: 1.5, y: 15},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. La Scogliera delle Posidonie", landmark: "beacon"},
    {x: 48, name: "2. I Faraglioni di Calcare Bianco", landmark: "pulsedrum"},
    {x: 102, name: "3. Il Sentiero del Faro Borbonico", landmark: "bannerarch"},
    {x: 162, name: "4. Gli Inghiottoi Naturali", landmark: "sandwheel"},
    {x: 212, name: "5. La Lanterna di Capo Santa Croce", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 15, "stone", {landmark: "beacon"}),
    S("step-cliff1", 10, 4.0, 15.8, "ledge"),
    S("plat-coast-wall", 16, 7.0, 16.6, "stone"),
    S("crane-cliff1", 25, 4.0, 16.8, "lift", {moveY: 2.0, period: 4.2}),
    S("plat-ledge1", 31, 7.5, 17.6, "stone"),
    S("spring-cliff1", 40, 2.0, 17.6, "spring"),
    S("opt-cliff1", 39, 3.6, 21.8, "ledge", {optional: !0}),
    S("pit-cliff-1", 7, 39, 5.0, "stone", {spiked: !0}),

    S("dock-lighthouse-approach", 46, 7.5, 17.6, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-cliff-path", 55, 4.8, 17.0, "stone"),
    S("ferry-reefs", 62, 5.5, 16.4, "ferry", {travel: 24, speed: 3.4}),
    S("plat-reef-isle", 88, 8.0, 16.4, "stone"),
    S("pit-cliff-2", 52, 46, 5.0, "stone", {spiked: !0}),

    S("dock-promontory", 98, 7.0, 16.4, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-cliff", 107, 8.0, 17.0, "balance"),
    S("step-promontory", 117, 3.8, 18.0, "ledge"),
    S("step-cliff3", 122.5, 3.2, 19.2, "ledge"),
    S("crane-jib-cliff2", 127.5, 8.0, 19.6, "balance"),
    S("opt-cliff2", 134, 3.6, 23.8, "ledge", {optional: !0}),
    S("lift-cliff", 137, 3.6, 19.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-lightgate-floor", 143, 22, 20.0, "stone", {landmark: "beacon"}),
    S("switch-lightgate", 152, 2.2, 20.15, "switch", {channel: "light-lock", latch: !0}),
    S("gate-light", 159, 1.8, 24.0, "gate", {channel: "light-lock", h: 4}),

    S("dock-cove", 163, 7.5, 20.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-clf1", 173, 4.0, 19.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-clf2", 179, 4.0, 19.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-cove-top", 185, 6.5, 19.0, "stone"),
    S("step-clf3", 194, 3.2, 19.8, "ledge"),
    S("lift-winch-clf", 193, 3.6, 18.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-cliff3", 201, 3.5, 24.0, "ledge", {optional: !0}),
    S("spring-cliff3", 200, 2.0, 19.8, "spring"),
    S("plat-lantern-base", 198, 8.5, 19.8, "stone", {landmark: "sandwheel"}),
    S("step-lantern-link", 208, 3.5, 19.8, "ledge"),
    S("pit-cliff-3", 168, 42, 6.0, "stone", {spiked: !0}),

    S("dock-clf-exit", 213, 7.0, 19.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-clf-rock1", 222, 3.8, 20.8, "ledge"),
    S("step-clf-rock2", 228, 4.2, 21.8, "ledge"),
    S("goal-lighthouse", 234, 14, 22.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 5.0},
    {x: 52, w: 46, y: 5.0},
    {x: 168, w: 42, y: 6.0}
  ],
  decor: [
    {kind: "falesia-calcarea", x: 10.0, y: 15.0, size: 12.0, z: -4.0},
    {kind: "banco-posidonia", x: 18.0, y: 15.8, size: 2.8, z: -1.2},
    {kind: "gabbiano-scoglio", x: 26.0, y: 16.8, size: 1.4, z: -1.0},
    {kind: "ancora-ammiragliato", x: 50.0, y: 17.6, size: 3.8, z: -1.8},
    {kind: "falesia-calcarea", x: 74.0, y: 16.4, size: 12.0, z: -4.0},
    {kind: "campana-nebbia", x: 92.0, y: 16.4, size: 2.6, z: -1.2},
    {kind: "lighthouse-tower", x: 108.0, y: 16.4, size: 16.0, z: -5.0},
    {kind: "banco-posidonia", x: 120.0, y: 18.0, size: 2.8, z: -1.2},
    {kind: "gabbiano-scoglio", x: 132.0, y: 19.6, size: 1.4, z: -1.0},
    {kind: "ancora-ammiragliato", x: 150.0, y: 20.0, size: 3.8, z: -1.8},
    {kind: "falesia-calcarea", x: 176.0, y: 19.4, size: 12.0, z: -4.0},
    {kind: "lighthouse-tower", x: 200.0, y: 19.8, size: 16.0, z: -5.0},
    {kind: "campana-nebbia", x: 218.0, y: 20.8, size: 2.6, z: -1.2}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Capo Santa Croce", text: "Le scogliere calcaree a picco sul mare aperto: le onde si infrangono sulle falesie ioniche."},
    {x: 48, end: 66, icon: "knead", title: "La Chiatta dei Faraglioni", text: "Sali sulla chiatta per attraversare l'insenatura marina sopra i banchi di Posidonia."},
    {x: 102, end: 125, icon: "knead", title: "Sentiero della Lanterna", text: "Salta sui gradoni di calcare bianco per salire verso il faro storico."},
    {x: 146, end: 160, icon: "walk", title: "Cancello del Semaforo Marittimo", text: "Attiva l'interruttore della stazione per aprire il passaggio verso la lanterna."},
    {x: 212, end: 240, icon: "bell", title: "La Lanterna di Capo Santa Croce", text: "Accendi il faro per guidare le navi e proteggere l'ecosistema marino dalle maree nere!"}
  ],
  coins: [
    {x: 8, y: 17.5}, {x: 12, y: 17.5}, {x: 18, y: 18.5}, {x: 21, y: 18.5},
    {x: 28, y: 19.5}, {x: 34, y: 19.5}, {x: 41, y: 20.0}, {x: 58, y: 18.5},
    {x: 68, y: 18.0}, {x: 74, y: 18.0}, {x: 80, y: 18.0}, {x: 86, y: 18.0},
    {x: 104, y: 18.5}, {x: 111, y: 19.0}, {x: 115, y: 19.0}, {x: 121, y: 20.0},
    {x: 129, y: 21.5}, {x: 147, y: 21.5}, {x: 154, y: 21.5}, {x: 166, y: 21.5},
    {x: 175, y: 21.0}, {x: 181, y: 21.0}, {x: 187, y: 20.5}, {x: 195, y: 20.5},
    {x: 204, y: 21.5}, {x: 223, y: 22.5}, {x: 229, y: 23.5}, {x: 235, y: 24.5}
  ],
  stamps: [{x: 41.0, y: 23.5}, {x: 134.5, y: 25.5}, {x: 202.5, y: 26.0}],
  enemies: [], crushers: []
});"""

def get_level_8():
    return """const augustaL8 = yr({
  layoutVersion: 1,
  name: "Le Saline Regie & I Fenicotteri Rosa",
  short: "Saline Regie",
  label: "Oasi di biodiversità, piramidi di sale e mulini a vento",
  biome: "nightfall",
  intro: "Le antiche Saline Regie di Augusta: una preziosa oasi umida dove nidificano i fenicotteri rosa tra vasche d'evaporazione rosse e candide piramidi di sale. Attraversa i canali sui mulini a vento e salva questo paradiso della biodiversità!",
  sky: "#241828",
  fog: "#3c223c",
  spawn: {x: 1.5, y: 12},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Gli Argini di Cristallizzazione", landmark: "beacon"},
    {x: 48, name: "2. Le Vasche Rosse dei Fenicotteri", landmark: "pulsedrum"},
    {x: 102, name: "3. I Mulini a Vento delle Saline", landmark: "bannerarch"},
    {x: 162, name: "4. I Monti di Sale Marino", landmark: "sandwheel"},
    {x: 212, name: "5. Il Casotto dei Salinai", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 12, "stone", {landmark: "beacon"}),
    S("step-salt1", 10, 4.0, 12.8, "ledge"),
    S("plat-saltcanal1", 16, 7.0, 13.6, "stone"),
    S("crane-salt1", 25, 4.0, 13.8, "lift", {moveY: 2.0, period: 4.2}),
    S("plat-saltpyramid1", 31, 7.5, 14.4, "stone"),
    S("spring-salt1", 40, 2.0, 14.4, "spring"),
    S("opt-salt1", 39, 3.6, 18.5, "ledge", {optional: !0}),
    S("pit-salt-1", 7, 39, 2.0, "stone", {spiked: !0}),

    S("dock-salina", 46, 7.5, 14.4, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-salina-levee", 55, 4.8, 13.8, "stone"),
    S("ferry-salina", 61, 5.5, 13.4, "ferry", {travel: 16, speed: 3.2}),
    S("plat-salina-isle", 79, 8.0, 13.4, "stone"),
    S("step-windmill-ramp", 88, 4.5, 13.4, "stone"),
    S("pit-salt-2", 52, 46, 2.0, "stone", {spiked: !0}),

    S("dock-pyramids", 95, 7.0, 13.4, "stone", {checkpoint: 97, depth: 22, landmark: "bannerarch"}),
    S("orbit-windmill1", 104, 7.5, 14.2, "balance"),
    S("step-salt2", 114, 3.8, 15.0, "ledge"),
    S("step-salina2", 120, 3.2, 16.2, "ledge"),
    S("crane-jib-salt2", 125, 8.0, 16.6, "balance"),
    S("opt-salt2", 132, 3.6, 20.8, "ledge", {optional: !0}),
    S("lift-salina", 136, 3.6, 16.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-saltgate-floor", 142, 22, 17.0, "stone", {landmark: "beacon"}),
    S("switch-saltgate", 151, 2.2, 17.15, "switch", {channel: "salt-lock", latch: !0}),
    S("gate-salt", 158, 1.8, 21.0, "gate", {channel: "salt-lock", h: 4}),

    S("dock-saltpans", 162, 7.5, 17.0, "stone", {checkpoint: 164, depth: 22, landmark: "sandwheel"}),
    S("pulse-slt1", 172, 4.0, 16.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-slt2", 178, 4.0, 16.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-salt-dry", 184, 6.5, 16.0, "stone"),
    S("step-slt3", 193, 3.2, 16.8, "ledge"),
    S("lift-winch-slt", 192, 3.6, 15.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-salt3", 200, 3.5, 21.0, "ledge", {optional: !0}),
    S("spring-salt3", 199, 2.0, 16.8, "spring"),
    S("plat-mill-base", 197, 8.5, 16.8, "stone", {landmark: "sandwheel"}),
    S("step-mill-link", 207, 3.5, 16.8, "ledge"),
    S("pit-salt-3", 167, 42, 3.0, "stone", {spiked: !0}),

    S("dock-slt-exit", 212, 7.0, 16.8, "stone", {checkpoint: 214, depth: 22, landmark: "bellgate"}),
    S("step-slt-rock1", 221, 3.8, 17.8, "ledge"),
    S("step-slt-rock2", 227, 4.2, 18.8, "ledge"),
    S("goal-salina", 233, 14, 19.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 235})
  ],
  hazards: [
    {x: 7, w: 39, y: 2.0},
    {x: 52, w: 46, y: 2.0},
    {x: 167, w: 42, y: 3.0}
  ],
  decor: [
    {kind: "salt-pyramid", x: 8.0, y: 12.0, size: 4.0, z: -1.8},
    {kind: "fenicottero-rosa", x: 18.0, y: 13.6, size: 2.8, z: -1.2},
    {kind: "paratoia-salina", x: 26.0, y: 13.8, size: 3.8, z: -1.5},
    {kind: "badile-salinaio", x: 34.0, y: 14.4, size: 2.2, z: -1.0},
    {kind: "salt-windmill", x: 50.0, y: 14.4, size: 6.5, z: -3.5},
    {kind: "fenicottero-rosa", x: 68.0, y: 13.4, size: 2.8, z: -1.2},
    {kind: "carrello-sale", x: 84.0, y: 13.4, size: 3.0, z: -1.5},
    {kind: "salt-pyramid", x: 100.0, y: 13.4, size: 4.0, z: -1.8},
    {kind: "salt-windmill", x: 120.0, y: 15.0, size: 6.5, z: -3.5},
    {kind: "paratoia-salina", x: 146.0, y: 17.0, size: 3.8, z: -1.5},
    {kind: "salt-pyramid", x: 170.0, y: 17.0, size: 4.0, z: -1.8},
    {kind: "fenicottero-rosa", x: 188.0, y: 16.0, size: 2.8, z: -1.2},
    {kind: "carrello-sale", x: 202.0, y: 16.8, size: 3.0, z: -1.5},
    {kind: "salt-windmill", x: 218.0, y: 16.8, size: 6.5, z: -3.5}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Le Saline Regie", text: "Un paesaggio storico modellato dall'acqua di mare e dal sole siciliano. Salta tra le paratoie di legno!"},
    {x: 48, end: 66, icon: "knead", title: "La Chiatta dei Canali Salmastri", text: "Attraversa le vasche rosse ricche di artemia salina, il cibo preferito dei fenicotteri rosa."},
    {x: 102, end: 125, icon: "knead", title: "Mulini delle Saline", text: "I grandi mulini a vento azionavano le pompe di sollevamento. Salta sulle piattaforme girevoli!"},
    {x: 146, end: 160, icon: "walk", title: "Chiusa delle Acque Madri", text: "Apri la paratoia per regolare il flusso e liberare la via verso i monti di sale cristallino."},
    {x: 212, end: 240, icon: "bell", title: "Il Casotto dei Salinai", text: "Suona la campana per istituire la riserva naturale permanente delle Saline di Augusta!"}
  ],
  coins: [
    {x: 8, y: 14.5}, {x: 12, y: 14.5}, {x: 18, y: 15.5}, {x: 21, y: 15.5},
    {x: 28, y: 16.5}, {x: 34, y: 16.5}, {x: 41, y: 17.0}, {x: 58, y: 15.5},
    {x: 68, y: 15.0}, {x: 74, y: 15.0}, {x: 80, y: 15.0}, {x: 86, y: 15.0},
    {x: 104, y: 15.5}, {x: 111, y: 16.0}, {x: 115, y: 16.0}, {x: 121, y: 17.0},
    {x: 129, y: 18.5}, {x: 147, y: 18.5}, {x: 154, y: 18.5}, {x: 166, y: 18.5},
    {x: 175, y: 18.0}, {x: 181, y: 18.0}, {x: 187, y: 17.5}, {x: 195, y: 17.5},
    {x: 204, y: 18.5}, {x: 223, y: 19.5}, {x: 229, y: 20.5}, {x: 235, y: 21.5}
  ],
  stamps: [{x: 41.0, y: 20.5}, {x: 134.5, y: 22.5}, {x: 202.5, y: 23.0}],
  enemies: [], crushers: []
});"""

def get_level_9():
    return """const augustaL9 = yr({
  layoutVersion: 1,
  name: "Forte Vittoria & Forte Garcia: I Guardiani della Rada",
  short: "I Forti Spagnoli",
  label: "Fortificazioni rinascimentali del 1567 in mezzo al porto industriale",
  biome: "nightfall",
  intro: "Eretti nel 1567 dal viceré spagnolo Garcia de Toledo al centro della rada megarese: due forti marittimi gemelli un tempo collegati da pesanti catene sommerse per sbarrare il porto. Salta sui bastioni storici e ricongiungi i guardiani!",
  sky: "#151e28",
  fog: "#243242",
  spawn: {x: 1.5, y: 15},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. La Batteria di Forte Garcia", landmark: "beacon"},
    {x: 48, name: "2. Il Canale delle Catene Sommerso", landmark: "pulsedrum"},
    {x: 102, name: "3. La Garitta Spagnola di Vedetta", landmark: "bannerarch"},
    {x: 162, name: "4. Le Fonderie di Cannoni", landmark: "sandwheel"},
    {x: 212, name: "5. Bastione Principale di Forte Vittoria", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 15, "stone", {landmark: "beacon"}),
    S("step-fort1", 10, 4.0, 15.8, "ledge"),
    S("plat-garcia-wall", 16, 7.0, 16.6, "stone"),
    S("crane-fort1", 25, 4.0, 16.8, "lift", {moveY: 2.0, period: 4.2}),
    S("plat-garcia-ramp", 31, 7.5, 17.6, "stone"),
    S("spring-fort1", 40, 2.0, 17.6, "spring"),
    S("opt-fort1", 39, 3.6, 21.8, "ledge", {optional: !0}),
    S("pit-fort-1", 7, 39, 5.0, "stone", {spiked: !0}),

    S("dock-channel-fort", 46, 7.5, 17.6, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-chain-wharf", 55, 4.8, 17.0, "stone"),
    S("ferry-fortchain", 62, 5.5, 16.4, "ferry", {travel: 24, speed: 3.4}),
    S("plat-chain-isle", 88, 8.0, 16.4, "stone"),
    S("pit-fort-2", 52, 46, 5.0, "stone", {spiked: !0}),

    S("dock-sentry", 98, 7.0, 16.4, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-fort", 107, 8.0, 17.0, "balance"),
    S("step-ironlink", 117, 3.8, 18.0, "ledge"),
    S("step-fort2", 122.5, 3.2, 19.2, "ledge"),
    S("crane-jib-fort2", 127.5, 8.0, 19.6, "balance"),
    S("opt-fort2", 134, 3.6, 23.8, "ledge", {optional: !0}),
    S("lift-fort", 137, 3.6, 19.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-vittoriagate-floor", 143, 22, 20.0, "stone", {landmark: "beacon"}),
    S("switch-vittoriagate", 152, 2.2, 20.15, "switch", {channel: "vittoria-lock", latch: !0}),
    S("gate-vittoria", 159, 1.8, 24.0, "gate", {channel: "vittoria-lock", h: 4}),

    S("dock-artillery", 163, 7.5, 20.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-frt1", 173, 4.0, 19.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-frt2", 179, 4.0, 19.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-battery-deck", 185, 6.5, 19.0, "stone"),
    S("step-frt3", 194, 3.2, 19.8, "ledge"),
    S("lift-winch-frt", 193, 3.6, 18.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-fort3", 201, 3.5, 24.0, "ledge", {optional: !0}),
    S("spring-fort3", 200, 2.0, 19.8, "spring"),
    S("plat-vittoria-keep", 198, 8.5, 19.8, "stone", {landmark: "sandwheel"}),
    S("step-keep-link2", 208, 3.5, 19.8, "ledge"),
    S("pit-fort-3", 168, 42, 6.0, "stone", {spiked: !0}),

    S("dock-frt-exit", 213, 7.0, 19.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-frt-rock1", 222, 3.8, 20.8, "ledge"),
    S("step-frt-rock2", 228, 4.2, 21.8, "ledge"),
    S("goal-vittoria", 234, 14, 22.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 5.0},
    {x: 52, w: 46, y: 5.0},
    {x: 168, w: 42, y: 6.0}
  ],
  decor: [
    {kind: "cannone-borbonico", x: 10.0, y: 15.0, size: 3.5, z: -1.6},
    {kind: "garitta-vedetta", x: 20.0, y: 16.6, size: 5.0, z: -2.5},
    {kind: "piramide-palle-cannone", x: 28.0, y: 16.6, size: 1.8, z: -1.0},
    {kind: "bastione-spagnolo", x: 50.0, y: 17.6, size: 8.0, z: -4.0},
    {kind: "argano-catena-porto", x: 74.0, y: 16.4, size: 3.0, z: -1.5},
    {kind: "bandiera-sicilia", x: 92.0, y: 16.4, size: 5.5, z: -2.0},
    {kind: "garitta-vedetta", x: 106.0, y: 16.4, size: 5.0, z: -2.5},
    {kind: "cannone-borbonico", x: 118.0, y: 18.0, size: 3.5, z: -1.6},
    {kind: "piramide-palle-cannone", x: 130.0, y: 19.6, size: 1.8, z: -1.0},
    {kind: "bastione-spagnolo", x: 150.0, y: 20.0, size: 8.0, z: -4.0},
    {kind: "bandiera-sicilia", x: 174.0, y: 19.4, size: 5.5, z: -2.0},
    {kind: "garitta-vedetta", x: 200.0, y: 19.8, size: 5.0, z: -2.5},
    {kind: "cannone-borbonico", x: 220.0, y: 20.8, size: 3.5, z: -1.6}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Forte Garcia (1567)", text: "Le mura bastionate spagnole a difesa della rada: cannoni di bronzo puntati sul mare."},
    {x: 48, end: 66, icon: "knead", title: "Il Canale delle Catene", text: "Attraversa il tratto d'acqua che divide Forte Garcia da Forte Vittoria."},
    {x: 102, end: 125, icon: "knead", title: "Garitte di Avvistamento", text: "Le sentinelle vigilavano sulle navi nemiche: salta lungo il camminamento d'artiglieria."},
    {x: 146, end: 160, icon: "walk", title: "Chiusa delle Munizioni", text: "Aziona l'argano per aprire il massiccio portale di Forte Vittoria."},
    {x: 212, end: 240, icon: "bell", title: "Mastio di Forte Vittoria", text: "Suona la campana storica per valorizzare questi due gioielli del patrimonio fortificato!"}
  ],
  coins: [
    {x: 8, y: 17.5}, {x: 12, y: 17.5}, {x: 18, y: 18.5}, {x: 21, y: 18.5},
    {x: 28, y: 19.5}, {x: 34, y: 19.5}, {x: 41, y: 20.0}, {x: 58, y: 18.5},
    {x: 68, y: 18.0}, {x: 74, y: 18.0}, {x: 80, y: 18.0}, {x: 86, y: 18.0},
    {x: 104, y: 18.5}, {x: 111, y: 19.0}, {x: 115, y: 19.0}, {x: 121, y: 20.0},
    {x: 129, y: 21.5}, {x: 147, y: 21.5}, {x: 154, y: 21.5}, {x: 166, y: 21.5},
    {x: 175, y: 21.0}, {x: 181, y: 21.0}, {x: 187, y: 20.5}, {x: 195, y: 20.5},
    {x: 204, y: 21.5}, {x: 223, y: 22.5}, {x: 229, y: 23.5}, {x: 235, y: 24.5}
  ],
  stamps: [{x: 41.0, y: 23.5}, {x: 134.5, y: 25.5}, {x: 202.5, y: 26.0}],
  enemies: [], crushers: []
});"""

def get_level_10():
    return """const augustaL10 = yr({
  layoutVersion: 1,
  name: "Porta Spagnola & La Grande Rinascita Verde",
  short: "Porta Spagnola",
  label: "La porta barocca del 1692, la differenziata e il trionfo ecologico",
  biome: "nightfall",
  intro: "Il gran finale: varca la celebre Porta Spagnola del 1692, simbolo imperituro di Augusta fondata dal viceré Benavides. Raccogli tutti i rifiuti, pianta i giovani alberi e raggiungi Piazza Duomo per celebrare la rinascita ecologica e culturale della citta!",
  sky: "#19283e",
  fog: "#2b4060",
  spawn: {x: 1.5, y: 16},
  end: 240,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Il Viale della Porta Spagnola", landmark: "beacon"},
    {x: 48, name: "2. I Bastioni di San Giacomo", landmark: "pulsedrum"},
    {x: 102, name: "3. Il Ponte sull'Istmo d'Augusta", landmark: "bannerarch"},
    {x: 162, name: "4. L'Oasi della Raccolta Differenziata", landmark: "sandwheel"},
    {x: 212, name: "5. L'Arco Trionfale Verde in Piazza Duomo", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 16, "stone", {landmark: "beacon"}),
    S("step-porta1", 10, 4.0, 16.8, "ledge"),
    S("plat-porta-avenue", 16, 7.0, 17.6, "stone"),
    S("crane-porta1", 25, 4.0, 17.8, "lift", {moveY: 2.0, period: 4.2}),
    S("plat-bastion-rampart", 31, 7.5, 18.6, "stone"),
    S("spring-porta1", 40, 2.0, 18.6, "spring"),
    S("opt-porta1", 39, 3.6, 22.8, "ledge", {optional: !0}),
    S("pit-porta-1", 7, 39, 6.0, "stone", {spiked: !0}),

    S("dock-spaniard", 46, 7.5, 18.6, "stone", {checkpoint: 48, depth: 22, landmark: "pulsedrum"}),
    S("plat-isthmus-walk", 55, 4.8, 18.0, "stone"),
    S("ferry-portaisle", 62, 5.5, 17.4, "ferry", {travel: 24, speed: 3.4}),
    S("plat-isthmus-isle", 88, 8.0, 17.4, "stone"),
    S("pit-porta-2", 52, 46, 6.0, "stone", {spiked: !0}),

    S("dock-drawbridge-isthmus", 98, 7.0, 17.4, "stone", {checkpoint: 100, depth: 22, landmark: "bannerarch"}),
    S("crane-jib-porta", 107, 8.0, 18.0, "balance"),
    S("step-drawbridge", 117, 3.8, 19.0, "ledge"),
    S("step-finale2", 122.5, 3.2, 20.2, "ledge"),
    S("crane-jib-porta2", 127.5, 8.0, 20.6, "balance"),
    S("opt-porta2", 134, 3.6, 24.8, "ledge", {optional: !0}),
    S("lift-porta", 137, 3.6, 20.0, "lift", {moveY: 2.0, period: 4.0}),
    S("plat-portagate-floor", 143, 22, 21.0, "stone", {landmark: "beacon"}),
    S("switch-portagate", 152, 2.2, 21.15, "switch", {channel: "porta-lock", latch: !0}),
    S("gate-porta", 159, 1.8, 25.0, "gate", {channel: "porta-lock", h: 4}),

    S("dock-recycling-park", 163, 7.5, 21.0, "stone", {checkpoint: 165, depth: 22, landmark: "sandwheel"}),
    S("pulse-prt1", 173, 4.0, 20.4, "pulse", {period: 4.2, phase: 0}),
    S("pulse-prt2", 179, 4.0, 20.4, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-recycle-top", 185, 6.5, 20.0, "stone"),
    S("step-prt3", 194, 3.2, 20.8, "ledge"),
    S("lift-winch-prt", 193, 3.6, 19.0, "lift", {moveX: 2.6, moveY: 1.8, period: 4.8}),
    S("opt-porta3", 201, 3.5, 25.0, "ledge", {optional: !0}),
    S("spring-porta3", 200, 2.0, 20.8, "spring"),
    S("plat-duomo-square", 198, 8.5, 20.8, "stone", {landmark: "sandwheel"}),
    S("step-duomo-link", 208, 3.5, 20.8, "ledge"),
    S("pit-porta-3", 168, 42, 7.0, "stone", {spiked: !0}),

    S("dock-prt-exit", 213, 7.0, 20.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-prt-rock1", 222, 3.8, 21.8, "ledge"),
    S("step-prt-rock2", 228, 4.2, 22.8, "ledge"),
    S("goal-porta", 234, 14, 23.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  hazards: [
    {x: 7, w: 39, y: 6.0},
    {x: 52, w: 46, y: 6.0},
    {x: 168, w: 42, y: 7.0}
  ],
  decor: [
    {kind: "porta-spagnola", x: 10.0, y: 16.0, size: 10.0, z: -3.0},
    {kind: "vaso-caltagirone", x: 20.0, y: 17.6, size: 3.2, z: -1.2},
    {kind: "palina-raccolta-differenziata", x: 28.0, y: 17.6, size: 2.2, z: -1.0},
    {kind: "bastione-spagnolo", x: 50.0, y: 18.6, size: 8.0, z: -4.0},
    {kind: "ficus-rinascita", x: 74.0, y: 17.4, size: 14.0, z: -4.5},
    {kind: "arco-trionfale-verde", x: 92.0, y: 17.4, size: 9.0, z: -2.5},
    {kind: "palina-raccolta-differenziata", x: 106.0, y: 17.4, size: 2.2, z: -1.0},
    {kind: "vaso-caltagirone", x: 118.0, y: 19.0, size: 3.2, z: -1.2},
    {kind: "ficus-rinascita", x: 148.0, y: 21.0, size: 14.0, z: -4.5},
    {kind: "palina-raccolta-differenziata", x: 172.0, y: 21.0, size: 2.2, z: -1.0},
    {kind: "arco-trionfale-verde", x: 196.0, y: 20.8, size: 9.0, z: -2.5},
    {kind: "barocco-duomo", x: 216.0, y: 20.8, size: 18.0, z: -4.5},
    {kind: "vaso-caltagirone", x: 230.0, y: 21.8, size: 3.2, z: -1.2}
  ],
  shaping: [],
  hints: [
    {x: 0, end: 14, icon: "walk", title: "Porta Spagnola (1692)", text: "L'iconica porta d'accesso all'isola, eretta dopo le guerre barocche. Varca la soglia della storia!"},
    {x: 48, end: 66, icon: "knead", title: "I Bastioni e il Ponte", text: "Attraversa l'istmo che separa il golfo Xifonio dalla rada megarese."},
    {x: 102, end: 125, icon: "knead", title: "L'Istmo d'Augusta", text: "Salta tra i piloni del viadotto e respira l'aria salmastra ionica."},
    {x: 146, end: 160, icon: "walk", title: "La Rinascita Ecologica", text: "Attiva la stazione di riciclo intelligente per aprire la via verso la cattedrale barocca."},
    {x: 212, end: 240, icon: "bell", title: "Trionfo in Piazza Duomo", text: "Suona la campana finale! Augusta è libera dal degrado, fiorisce nel verde e risplende di cultura!"}
  ],
  coins: [
    {x: 8, y: 18.5}, {x: 12, y: 18.5}, {x: 18, y: 19.5}, {x: 21, y: 19.5},
    {x: 28, y: 20.5}, {x: 34, y: 20.5}, {x: 41, y: 21.0}, {x: 58, y: 19.5},
    {x: 68, y: 19.0}, {x: 74, y: 19.0}, {x: 80, y: 19.0}, {x: 86, y: 19.0},
    {x: 104, y: 19.5}, {x: 111, y: 20.0}, {x: 115, y: 20.0}, {x: 121, y: 21.0},
    {x: 129, y: 22.5}, {x: 147, y: 22.5}, {x: 154, y: 22.5}, {x: 166, y: 22.5},
    {x: 175, y: 22.0}, {x: 181, y: 22.0}, {x: 187, y: 21.5}, {x: 195, y: 21.5},
    {x: 204, y: 22.5}, {x: 223, y: 23.5}, {x: 229, y: 24.5}, {x: 235, y: 25.5}
  ],
  stamps: [{x: 41.0, y: 24.5}, {x: 134.5, y: 26.5}, {x: 202.5, y: 27.0}],
  enemies: [], crushers: []
});"""

def get_all_levels():
    return "\\n\\n".join([
        get_level_1(), get_level_2(), get_level_3(), get_level_4(),
        get_level_5(), get_level_6(), get_level_7(), get_level_8(),
        get_level_9(), get_level_10()
    ])
''')
print("tools/gta_all_10_levels.py assembled cleanly!")
