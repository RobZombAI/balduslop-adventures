# tools/cerignola_decor_and_level.py
"""
Cerignola Handcrafted Procedural 3D Decor Models & Complete Level Definition
for BalduSlop / GTA Giuseppe Taglia Alberi: Edizione Cerignola
"""

def get_cerignola_decor_models():
    return '''
,"duomo-tonti-cerignola"(t,e,n){
  const o=oo(e,n,20.0);
  // Cattedrale di San Pietro Apostolo (Duomo Tonti di Cerignola)
  // Colossal late-19th century basilica with one of the largest domes in Southern Italy
  // Raised podium & marble steps
  t.box(18, 1.8, 12, "cream", o, 0, 0.9, 0);
  t.box(16, 0.8, 10, "terrain", o, 0, 1.8, 0);
  // Main cathedral basilica body (tufo pugliese & stone)
  t.box(14, 11, 8.5, "cream", o, 0, 7.5, 0);
  // Three portal arches on facade (arched entryways in dark clay)
  t.box(2.4, 3.6, 0.4, "dark", o, 0, 3.8, 4.3);
  t.cylinder(1.2, 0.4, "dark", o, 0, 5.6, 4.3);
  t.box(1.6, 2.8, 0.4, "dark", o, -4.5, 3.2, 4.3);
  t.cylinder(0.8, 0.4, "dark", o, -4.5, 4.6, 4.3);
  t.box(1.6, 2.8, 0.4, "dark", o, 4.5, 3.2, 4.3);
  t.cylinder(0.8, 0.4, "dark", o, 4.5, 4.6, 4.3);
  // Rose window (Grande Rosone)
  t.cylinder(2.2, 0.45, "gold", o, 0, 10.2, 4.3);
  t.ball(1.2, 1.2, 0.3, "blueLight", o, 0, 10.2, 4.4);
  // Giant octagonal drum
  t.cylinder(5.2, 4.0, "cream", o, 0, 14.5, 0);
  for(let i=0; i<8; i++){
    const ang = i * Math.PI / 4;
    t.box(0.6, 2.2, 0.3, "dark", o, Math.sin(ang)*5.0, 14.5, Math.cos(ang)*5.0);
  }
  // Colossal copper cupola (dome)
  t.ball(5.8, 5.0, 5.8, "blueLight", o, 0, 18.2, 0);
  // Top lantern & cross
  t.cylinder(1.4, 2.8, "cream", o, 0, 21.5, 0);
  t.cylinder(0.2, 2.0, "gold", o, 0, 23.5, 0);
  t.box(1.2, 0.2, 0.2, "gold", o, 0, 23.8, 0);
  // Twin bell towers
  t.box(3.2, 18.0, 3.2, "cream", o, -7.0, 10.5, 3.2);
  t.cylinder(1.6, 4.0, "blueLight", o, -7.0, 21.0, 3.2);
  t.box(3.2, 18.0, 3.2, "cream", o, 7.0, 10.5, 3.2);
  t.cylinder(1.6, 4.0, "blueLight", o, 7.0, 21.0, 3.2);
}
,"blindato-portavalori"(t,e,n){
  const o=oo(e,n,8.0);
  // Assalto al Portavalori - Heavy armored security van
  // 4 Heavy reinforced wheels
  t.cylinder(0.7, 0.5, "dark", o, -2.0, 0.7, 1.4);
  t.cylinder(0.7, 0.5, "dark", o, 2.0, 0.7, 1.4);
  t.cylinder(0.7, 0.5, "dark", o, -2.0, 0.7, -1.4);
  t.cylinder(0.7, 0.5, "dark", o, 2.0, 0.7, -1.4);
  // Steel undercarriage
  t.box(6.2, 0.7, 2.8, "dark", o, 0, 0.9, 0);
  // Armored transport body (deep blue security plating)
  t.box(6.0, 2.3, 2.7, "blue", o, 0, 2.2, 0);
  // Front armor cabin & bulletproof sloped glass slit
  t.box(2.2, 1.8, 2.6, "blueLight", o, -2.0, 2.2, 0);
  t.box(0.2, 0.6, 2.2, "dark", o, -3.05, 2.4, 0);
  // Rear security vault doors (blown open by commando explosives)
  t.box(0.12, 1.9, 1.3, "dark", o, 3.4, 2.1, 1.3);
  t.box(0.12, 1.9, 1.3, "dark", o, 3.5, 1.9, -1.2);
  // Inside open vault: gold bars & security lockbox
  t.box(0.7, 0.3, 0.4, "gold", o, 2.2, 1.4, 0.3);
  t.box(0.7, 0.3, 0.4, "gold", o, 2.4, 1.7, 0.25);
  // Scattered loot on ground
  t.box(0.65, 0.25, 0.35, "gold", o, 3.8, 0.2, 0.4);
  t.box(0.65, 0.25, 0.35, "gold", o, 4.2, 0.4, 0.3);
  t.box(0.5, 0.2, 0.3, "gold", o, 4.6, 0.15, -0.6);
  t.ball(0.45, 0.4, 0.45, "cream", o, 4.4, 0.3, 0.9);
  // Flashing security beacons
  t.cylinder(0.2, 0.25, "orangeLight", o, -1.6, 3.45, 0.9);
  t.cylinder(0.2, 0.25, "blueLight", o, 1.8, 3.45, -0.9);
}
,"ruspa-ariete-commando"(t,e,n){
  const o=oo(e,n,8.5);
  // Heavy caterpillar wheel loader used as battering ram in Cerignola heists
  // Giant grooved tires
  t.cylinder(1.15, 0.75, "dark", o, -1.7, 1.15, 1.5);
  t.cylinder(1.15, 0.75, "dark", o, 1.7, 1.15, 1.5);
  t.cylinder(1.15, 0.75, "dark", o, -1.7, 1.15, -1.5);
  t.cylinder(1.15, 0.75, "dark", o, 1.7, 1.15, -1.5);
  // Heavy body (construction yellow/orange)
  t.box(4.4, 1.9, 2.5, "orange", o, 0.2, 2.2, 0);
  // Enclosed safety cab
  t.box(2.0, 2.0, 2.1, "dark", o, 0.1, 4.0, 0);
  t.box(2.2, 0.25, 2.3, "orange", o, 0.1, 5.0, 0);
  t.cylinder(0.22, 0.35, "orangeLight", o, 0.1, 5.25, 0);
  // Hydraulic boom arms reaching forward
  t.cylinder(0.24, 3.4, "dark", o, -2.5, 2.3, 1.15);
  t.cylinder(0.24, 3.4, "dark", o, -2.5, 2.3, -1.15);
  // Heavy steel front shovel bucket (ariete)
  t.box(1.3, 1.8, 3.4, "dark", o, -4.2, 1.3, 0);
  t.box(0.2, 0.4, 3.3, "gold", o, -4.8, 0.5, 0);
}
,"chiodi-quattro-punte"(t,e,n){
  const o=oo(e,n,4.0);
  // Artisanal 4-pointed tire caltrops (ricci a 4 punte)
  t.box(3.4, 0.06, 0.06, "dark", o, 0, 0.05, 0);
  // Spikes welded in tetrahedron shape
  t.cylinder(0.08, 0.65, "dark", o, 0, 0.32, 0);
  t.cylinder(0.07, 0.55, "gold", o, 0.15, 0.2, 0.2);
  t.cylinder(0.08, 0.65, "dark", o, -1.2, 0.32, 0.25);
  t.cylinder(0.07, 0.55, "dark", o, -1.0, 0.22, -0.3);
  t.cylinder(0.08, 0.65, "dark", o, 1.2, 0.32, -0.2);
  t.cylinder(0.07, 0.55, "gold", o, 1.4, 0.22, 0.35);
  t.cylinder(0.07, 0.55, "dark", o, -0.6, 0.25, -0.15);
  t.cylinder(0.07, 0.55, "dark", o, 0.6, 0.25, 0.15);
}
,"auto-cannibalizzata-cerignola"(t,e,n){
  const o=oo(e,n,6.5);
  // Stolen vehicle stripped to bare metal in 30 seconds
  // Cinder blocks (mattoni forati) under the four corners
  t.box(0.55, 0.45, 0.55, "orange", o, -1.6, 0.22, 1.0);
  t.box(0.55, 0.45, 0.55, "orange", o, 1.6, 0.22, 1.0);
  t.box(0.55, 0.45, 0.55, "orange", o, -1.6, 0.22, -1.0);
  t.box(0.55, 0.45, 0.55, "orange", o, 1.6, 0.22, -1.0);
  // Naked chassis floorpan
  t.box(4.5, 0.3, 1.9, "dark", o, 0, 0.55, 0);
  // Exposed empty engine compartment
  t.box(1.2, 0.7, 1.3, "dark", o, -1.8, 0.9, 0);
  t.cylinder(0.25, 0.5, "gold", o, -1.8, 1.3, 0);
  // Skeleton door frames & pillars
  t.cylinder(0.09, 1.2, "dark", o, -1.0, 1.4, 0.9);
  t.cylinder(0.09, 1.2, "dark", o, 0.2, 1.4, 0.9);
  t.cylinder(0.09, 1.2, "dark", o, 1.4, 1.4, 0.9);
  t.cylinder(0.09, 1.2, "dark", o, -1.0, 1.4, -0.9);
  t.cylinder(0.09, 1.2, "dark", o, 0.2, 1.4, -0.9);
  t.cylinder(0.09, 1.2, "dark", o, 1.4, 1.4, -0.9);
  // Stripped roof panel
  t.box(2.6, 0.08, 1.9, "blue", o, 0.2, 2.0, 0);
  // Discarded rims beside the chassis
  t.cylinder(0.55, 0.35, "dark", o, 2.5, 0.18, 0.9);
}
,"officina-smontaggio-capannone"(t,e,n){
  const o=oo(e,n,10.0);
  // Clandestine chop shop shed
  t.box(0.45, 6.5, 0.45, "dark", o, -4.0, 3.25, 0);
  t.box(0.45, 6.5, 0.45, "dark", o, 4.0, 3.25, 0);
  // Overhead crane steel beam
  t.box(8.6, 0.55, 0.65, "orange", o, 0, 6.2, 0);
  // Hanging engine hoist
  t.cylinder(0.08, 2.2, "dark", o, 0, 4.8, 0);
  t.box(0.85, 0.7, 0.85, "gold", o, 0, 3.6, 0);
  // Stacks of confiscated tires
  t.cylinder(0.65, 1.9, "dark", o, -2.8, 0.95, -0.9);
  t.cylinder(0.65, 1.3, "dark", o, -1.4, 0.65, -0.9);
  t.cylinder(0.65, 1.6, "dark", o, 2.6, 0.8, -0.9);
}
,"gazzella-carabinieri-polizia"(t,e,n){
  const o=oo(e,n,7.0);
  // Italian law enforcement patrol sedan (Gazzella / Pantera)
  // Wheels
  t.cylinder(0.58, 0.38, "dark", o, -1.5, 0.58, 1.1);
  t.cylinder(0.58, 0.38, "dark", o, 1.5, 0.58, 1.1);
  t.cylinder(0.58, 0.38, "dark", o, -1.5, 0.58, -1.1);
  t.cylinder(0.58, 0.38, "dark", o, 1.5, 0.58, -1.1);
  // Carabinieri deep blue body
  t.box(4.6, 1.05, 2.1, "blue", o, 0, 1.0, 0);
  // White police livery stripe
  t.box(4.4, 0.22, 2.15, "cream", o, 0, 1.1, 0);
  // Aerodynamic cockpit & windows
  t.box(2.3, 0.9, 1.9, "blueLight", o, 0.1, 1.85, 0);
  // Emergency flashing LED lightbar
  t.box(0.35, 0.12, 1.5, "dark", o, 0.1, 2.35, 0);
  t.box(0.28, 0.22, 0.55, "blueLight", o, 0.1, 2.46, 0.55);
  t.box(0.22, 0.18, 0.25, "cream", o, 0.1, 2.46, 0);
  t.box(0.28, 0.22, 0.55, "blueLight", o, 0.1, 2.46, -0.55);
  // Headlamps
  t.box(0.1, 0.3, 0.5, "cream", o, -2.32, 0.95, 0.65);
  t.box(0.1, 0.3, 0.5, "cream", o, -2.32, 0.95, -0.65);
}
,"bustina-polvere-bianca"(t,e,n){
  const o=oo(e,n,3.2);
  // Transparent ziploc baggie with white powder / crystal
  t.box(1.3, 1.5, 0.35, "blueLight", o, 0, 0.75, 0);
  // White powder filling inside
  t.box(1.1, 0.9, 0.26, "cream", o, 0, 0.52, 0);
  // Blue zip seal
  t.box(1.35, 0.14, 0.38, "blue", o, 0, 1.42, 0);
  // Fine powder glow aura
  t.ball(0.55, 0.45, 0.55, "cream", o, 0.4, 0.35, 0.2);
}
,"panetto-sigillato-sequestro"(t,e,n){
  const o=oo(e,n,3.5);
  // Contraband brick sealed with brown packaging tape
  t.box(1.7, 0.75, 1.1, "bark", o, 0, 0.38, 0);
  // Cross tape
  t.box(1.75, 0.78, 0.22, "gold", o, 0, 0.38, 0);
  t.box(0.22, 0.78, 1.15, "gold", o, 0, 0.38, 0);
  // Slash showing white test cut
  t.box(0.45, 0.12, 0.35, "cream", o, 0.45, 0.78, 0.15);
}
,"fossa-granaria-cerignola"(t,e,n){
  const o=oo(e,n,5.0);
  // Ancient underground wheat storage pit of Piano San Rocco (Fosse Granarie)
  t.cylinder(2.0, 0.38, "cream", o, 0, 0.19, 0);
  t.cylinder(1.4, 0.42, "dark", o, 0, 0.22, 0);
  // Stone boundary marker cippo
  t.cylinder(0.42, 1.15, "cream", o, 0.9, 0.65, 0.9);
  // Golden durum wheat ears
  t.cylinder(0.12, 0.85, "gold", o, -0.45, 0.45, 0.35);
  t.cylinder(0.12, 0.85, "gold", o, 0.25, 0.45, -0.55);
}
,"pusher-cerignolano"(t,e,n){
  const o=oo(e,n,4.5);
  // Shady street dealer standing by the alley corner
  t.cylinder(0.32, 1.15, "dark", o, -0.24, 0.58, 0);
  t.cylinder(0.32, 1.15, "dark", o, 0.24, 0.58, 0);
  // Dark puffer jacket
  t.box(1.0, 1.15, 0.7, "dark", o, 0, 1.68, 0);
  // Hood up
  t.ball(0.5, 0.55, 0.52, "dark", o, 0, 2.48, 0);
  // Dark sunglasses
  t.box(0.38, 0.12, 0.16, "dark", o, 0, 2.48, 0.4);
  // Discreet white packet in hand
  t.box(0.26, 0.22, 0.12, "cream", o, 0.6, 1.35, 0.38);
}
,"carabiniere-posto-blocco"(t,e,n){
  const o=oo(e,n,4.5);
  // Carabiniere officer at checkpoint
  t.cylinder(0.3, 1.25, "dark", o, -0.24, 0.62, 0);
  t.cylinder(0.3, 1.25, "dark", o, 0.24, 0.62, 0);
  // Navy uniform jacket
  t.box(0.95, 1.15, 0.65, "blue", o, 0, 1.78, 0);
  // White reflective bandolier cross-belt
  t.cylinder(0.08, 1.35, "cream", o, 0, 1.78, 0.34);
  // Service peaked cap with gold flame
  t.cylinder(0.48, 0.28, "blue", o, 0, 2.65, 0);
  t.box(0.52, 0.07, 0.32, "dark", o, 0, 2.54, 0.26);
  t.ball(0.12, 0.12, 0.08, "gold", o, 0, 2.7, 0.36);
  // Red 'ALT' traffic paddle
  t.cylinder(0.06, 1.25, "cream", o, 0.65, 1.25, 0.32);
  t.cylinder(0.38, 0.07, "orange", o, 0.65, 1.88, 0.32);
}
,"furgone-in-fiamme"(t,e,n){
  const o=oo(e,n,7.5);
  // Overturned vehicle barricade ablaze
  t.box(5.2, 2.3, 2.1, "dark", o, 0, 1.15, 0);
  // Vibrant clay flames
  t.ball(0.95, 1.9, 0.95, "orange", o, -1.3, 2.6, 0.2);
  t.ball(0.85, 2.3, 0.85, "orangeLight", o, 0.3, 2.9, -0.3);
  t.ball(1.15, 2.1, 1.05, "orange", o, 1.5, 2.7, 0.1);
  t.ball(0.65, 1.6, 0.65, "gold", o, -0.2, 2.4, 0.4);
  // Black smoke cloud
  t.ball(1.5, 1.9, 1.5, "dark", o, 0.2, 4.6, 0);
  t.ball(1.9, 2.3, 1.9, "dark", o, 0.5, 6.5, 0.2);
}
,"olivo-bella-di-cerignola"(t,e,n){
  const o=oo(e,n,6.5);
  // Gnarled olive tree of the Tavoliere
  t.cylinder(1.5, 2.9, "bark", o, 0, 1.45, 0);
  // Spreading canopy
  t.ball(3.8, 1.9, 3.8, "foliage", o, 0, 3.9, 0);
  t.ball(2.9, 1.6, 2.9, "leafLight", o, 0.8, 4.5, -0.5);
  // Big DOP green olives of Cerignola
  t.ball(0.3, 0.4, 0.3, "leafLight", o, -1.3, 2.8, 1.0);
  t.ball(0.3, 0.4, 0.3, "leafLight", o, 1.5, 2.9, -0.8);
  t.ball(0.3, 0.4, 0.3, "leafLight", o, 0.3, 2.7, 1.5);
  t.ball(0.3, 0.4, 0.3, "leafLight", o, -0.9, 3.0, -1.2);
}
'''

def get_cerignola_level_code():
    return '''const cerignolaL1 = yr({
  layoutVersion: 1,
  name: "Cerignola: La Città di Baldu — Tra Fosse Granarie e Duomo Tonti",
  short: "Cerignola",
  label: "Assalti ai portavalori, auto cannibalizzate, pusher e legalità",
  biome: "desert",
  intro: "Benvenuto a Cerignola, la leggendaria città natale di Baldu nel cuore del Tavoliere delle Puglie! Fatti strada tra le storiche fosse granarie, i commando dei portavalori sventrati dalle ruspe, i capannoni delle auto cannibalizzate e i vicoli dei pusher. Sfuggi ai posti di blocco delle Forze dell'Ordine e raggiungi il mastodontico Duomo Tonti per riscattare l'onore e la bellezza di Cerignola!",
  moralTitle: "Cerignola oltre il Pregiudizio: Il Riscatto, il Lavoro e la Bellezza del Tavoliere",
  moralStory: "Cerignola è una terra dal cuore antico e generoso, custode del Piano delle Fosse Granarie e della maestosa Cattedrale di San Pietro Apostolo. Troppo spesso le cronache riducono questa città agli assalti ai portavalori, allo smontaggio delle auto o allo spaccio. Ma la vera anima di Cerignola sono i braccianti che all'alba raccolgono l'oliva 'Bella di Cerignola', gli artigiani onesti, i giovani che scelgono la legalità e chi lotta ogni giorno per il riscatto sociale della propria comunità. La legalità non è un traguardo lontano: cresce ogni volta che diciamo no al crimine facile e costruiamo insieme una città più giusta, pulita e fiera!",
  sky: "#f59e0b",
  fog: "#d97706",
  spawn: {x: 1.5, y: 13.0},
  end: 245,
  previousDistance: 1100,
  cameraY: 2,
  sections: [
    {x: -8, name: "1. Le Fosse Granarie & La Periferia dei Capannoni", landmark: "beacon"},
    {x: 48, name: "2. L'Assalto al Blindato Portavalori (Commando Cerignolano)", landmark: "pulsedrum"},
    {x: 102, name: "3. I Capannoni dello Smontaggio (Auto Cannibalizzate)", landmark: "bannerarch"},
    {x: 165, name: "4. I Vicoli dei Pusher & Il Posto di Blocco", landmark: "sandwheel"},
    {x: 213, name: "5. Il Sagrato Monumentale del Duomo Tonti", landmark: "bellgate"}
  ],
  platforms: [
    S("start", -8, 16, 13.0, "stone", {landmark: "beacon"}),
    S("plat-fosse-step1", 6, 6.0, 13.6, "stone"),
    S("plat-fosse-step2", 15, 6.5, 14.2, "stone"),
    S("step-capannoni-root", 21.5, 3.5, 14.8, "ledge"),
    S("lift-paranco-officina", 27.5, 4.2, 14.8, "lift", {moveX: 2.2, period: 4.0}),
    S("plat-tetto-capannone", 33.5, 8.5, 15.2, "stone"),
    S("spring-copertoni-gomme", 41.5, 2.2, 15.2, "spring"),
    S("step-crossing-tetti", 44.0, 3.5, 15.4, "stone"),
    S("pit-chiodi-1", 7, 36, 3.0, "stone", {spiked: !0}),

    S("dock-portavalori-main", 48, 8.0, 15.2, "stone", {checkpoint: 50, depth: 22, landmark: "pulsedrum"}),
    S("crumble-lamiere-blindato", 56, 4.2, 14.8, "crumble"),
    S("plat-blocco-stradale", 63, 7.0, 14.2, "stone"),
    S("switch-chiave-portavalori", 65.5, 2.2, 14.35, "switch", {channel: "portavalori-open", latch: !0}),
    S("plat-ruspa-benna1", 70.0, 5.0, 14.2, "timed", {channel: "portavalori-open"}),
    S("plat-blindato-tetto", 76.5, 8.5, 14.4, "timed", {channel: "portavalori-open"}),
    S("plat-ruspa-braccio", 86.0, 4.5, 14.0, "timed", {channel: "portavalori-open"}),
    S("plat-asfalto-breccia", 91.5, 8.5, 13.8, "stone"),
    S("pit-chiodi-2", 50, 52, 2.5, "stone", {spiked: !0}),

    S("dock-autodemolizioni", 102, 8.0, 11.4, "stone", {checkpoint: 104, depth: 22, landmark: "bannerarch"}),
    S("balance-ponte-sollevatore", 111, 7.0, 11.8, "balance"),
    S("step-scocca-auto1", 118.5, 3.8, 12.8, "ledge"),
    S("step-scocca-auto2", 124, 3.4, 13.8, "ledge"),
    S("balance-carrello-officina", 130, 6.5, 14.6, "balance"),
    S("lift-gru-motore", 137, 3.6, 14.5, "lift", {moveY: 2.0, period: 4.0}),
    S("step-trave-capannone", 141.5, 3.8, 15.2, "ledge"),
    S("plat-nastro-ricambi", 146, 18.5, 16.0, "stone"),
    S("switch-posto-blocco", 153, 2.2, 16.15, "switch", {channel: "cancello-duomo", latch: !0}),
    S("gate-posto-blocco", 158, 1.8, 20.0, "gate", {channel: "cancello-duomo", h: 4}),

    S("dock-vicoli-spaccio", 165, 8.0, 16.0, "stone", {checkpoint: 167, depth: 22, landmark: "sandwheel"}),
    S("plat-vicoli-balcone1", 174.0, 5.5, 15.8, "stone"),
    S("plat-vicoli-balcone2", 180.5, 5.5, 15.5, "stone"),
    S("plat-posto-blocco-auto", 187.0, 7.5, 15.2, "stone"),
    S("lift-furgone-polizia", 195.5, 4.5, 15.0, "lift", {moveX: 1.8, period: 4.0}),
    S("plat-terrazza-corso", 202.5, 9.5, 16.0, "stone", {landmark: "sandwheel"}),
    S("pit-chiodi-3", 167, 45, 4.0, "stone", {spiked: !0}),

    S("dock-corso-duomo", 213, 8.0, 16.5, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-scalinata-duomo1", 222, 3.8, 17.2, "ledge"),
    S("step-scalinata-duomo2", 227, 4.0, 18.0, "ledge"),
    S("step-scalinata-duomo3", 232.0, 3.5, 18.4, "ledge"),
    S("goal-duomo-tonti", 236.5, 16.0, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 237})
  ],
  decor: [
    {kind: "fossa-granaria-cerignola", x: -4.0, y: 13.0, size: 5.0, z: -1.2},
    {kind: "olivo-bella-di-cerignola", x: 1.0, y: 13.0, size: 6.5, z: -1.0},
    {kind: "fossa-granaria-cerignola", x: 8.5, y: 13.6, size: 4.8, z: -0.8},
    {kind: "auto-cannibalizzata-cerignola", x: 16.0, y: 14.2, size: 5.5, z: -1.2},
    {kind: "bustina-polvere-bianca", x: 22.0, y: 14.8, size: 2.8, z: -0.5},
    {kind: "officina-smontaggio-capannone", x: 33.5, y: 15.2, size: 8.5, z: -2.0},
    {kind: "chiodi-quattro-punte", x: 25.0, y: 3.0, size: 4.0, z: 0.0},

    {kind: "blindato-portavalori", x: 50.0, y: 15.2, size: 7.5, z: -1.2},
    {kind: "ruspa-ariete-commando", x: 58.0, y: 15.0, size: 7.5, z: -1.5},
    {kind: "furgone-in-fiamme", x: 63.0, y: 14.2, size: 7.0, z: -1.2},
    {kind: "bustina-polvere-bianca", x: 76.5, y: 14.4, size: 3.0, z: -0.5},
    {kind: "chiodi-quattro-punte", x: 75.0, y: 2.5, size: 4.5, z: 0.0},
    {kind: "olivo-bella-di-cerignola", x: 92.0, y: 13.8, size: 6.5, z: -1.2},

    {kind: "auto-cannibalizzata-cerignola", x: 104.0, y: 11.4, size: 6.0, z: -1.0},
    {kind: "officina-smontaggio-capannone", x: 115.0, y: 12.0, size: 8.5, z: -2.0},
    {kind: "auto-cannibalizzata-cerignola", x: 120.0, y: 12.8, size: 5.5, z: -1.0},
    {kind: "panetto-sigillato-sequestro", x: 146.0, y: 16.0, size: 3.2, z: -0.6},
    {kind: "auto-cannibalizzata-cerignola", x: 150.0, y: 16.0, size: 6.0, z: -1.2},

    {kind: "pusher-cerignolano", x: 167.0, y: 16.0, size: 4.2, z: -0.8},
    {kind: "bustina-polvere-bianca", x: 174.0, y: 15.8, size: 3.0, z: -0.5},
    {kind: "panetto-sigillato-sequestro", x: 180.5, y: 15.5, size: 3.0, z: -0.5},
    {kind: "gazzella-carabinieri-polizia", x: 187.0, y: 15.2, size: 6.5, z: -1.2},
    {kind: "carabiniere-posto-blocco", x: 191.0, y: 15.2, size: 4.2, z: -0.8},
    {kind: "pusher-cerignolano", x: 204.0, y: 16.0, size: 4.2, z: -0.8},
    {kind: "chiodi-quattro-punte", x: 185.0, y: 4.0, size: 4.5, z: 0.0},

    {kind: "fossa-granaria-cerignola", x: 215.0, y: 16.5, size: 5.0, z: -1.2},
    {kind: "olivo-bella-di-cerignola", x: 220.0, y: 17.0, size: 6.8, z: -1.5},
    {kind: "duomo-tonti-cerignola", x: 236.5, y: 18.8, size: 20.0, z: -5.0},
    {kind: "olivo-bella-di-cerignola", x: 242.0, y: 18.8, size: 6.5, z: -1.2}
  ],
  stamps: [{x: 41.5, y: 19.5}, {x: 124.0, y: 17.5}, {x: 180.5, y: 19.0}],
  coins: [
    {x: 2, y: 13.5}, {x: 9, y: 14.2}, {x: 18, y: 14.8}, {x: 31, y: 15.6},
    {x: 43, y: 16.5}, {x: 52, y: 15.8}, {x: 64, y: 15.0}, {x: 74, y: 15.2},
    {x: 84, y: 15.0}, {x: 94, y: 14.5}, {x: 106, y: 12.5}, {x: 115, y: 13.2},
    {x: 126, y: 14.5}, {x: 139, y: 15.8}, {x: 150, y: 16.8}, {x: 170, y: 16.8},
    {x: 182, y: 16.5}, {x: 193, y: 16.2}, {x: 206, y: 16.8}, {x: 226, y: 18.5}
  ],
  hazards: [],
  enemies: [
    {kind: "drifter", x: 62.0, y: 14.8, min: 60.5, max: 64.5, speed: 0.8, bob: 0.12, period: 4.0},
    {kind: "drifter", x: 167.5, y: 16.5, min: 165.5, max: 171.0, speed: 0.9, bob: 0.15, period: 4.5}
  ],
  hints: [
    {x: 0, end: 18, title: "Le Fosse Granarie", text: "Benvenuto a Cerignola, terra di Baldu! Attraversa le storiche fosse granarie e i capannoni della periferia!", icon: "walk"},
    {x: 48, end: 70, title: "Assalto al Blindato Portavalori", text: "La ruspa ha sventrato il blindato! Premi l'interruttore sul veicolo per aprire il varco sulle benne e le lamiere!", icon: "knead"},
    {x: 102, end: 125, title: "Capannoni dello Smontaggio", text: "Auto cannibalizzate in 30 secondi: salta sui ponti sollevatori e le gru d'officina per raggiungere i tetti!", icon: "sink"},
    {x: 165, end: 190, title: "Posto di Blocco & Pusher", text: "Attento ai pusher nei vicoli e supera la pattuglia delle Forze dell'Ordine con la Gazzella!", icon: "walk"},
    {x: 213, end: 242, title: "Il Duomo Tonti (San Pietro)", text: "Sali la scalinata della maestosa Cattedrale di Cerignola: suona la campana e riscatta la città!", icon: "bell"}
  ],
  shaping: [], crushers: []
});'''
