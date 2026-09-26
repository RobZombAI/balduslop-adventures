# tools/generate_gta_game.py
"""
Builds GTA: Giuseppe Taglia Alberi
Full standalone game with custom 3D character, 14 custom environmental models,
and 10 handcrafted satirical and educational levels about Augusta (SR).
"""

import os
import re

def get_character_customization_code():
    return """
function applyGiuseppeCustomization(scene, choice) {
  if (!choice || (choice.id !== "giuseppe" && choice.id !== "baldu" && choice.id !== "explorer")) return;
  const head = scene.getObjectByName("Head");
  if (!head || head.getObjectByName("giuseppe-head-features")) return;

  const features = new U();
  features.name = "giuseppe-head-features";

  // Materials for Giuseppe (from reference portrait)
  const skinMat = new Ce({color: 0xf1be9c, roughness: 0.88, metalness: 0});
  const scalpMat = new Ce({color: 0xf3c2a2, roughness: 0.90, metalness: 0});
  const frameMat = new Ce({color: 0x111111, roughness: 0.22, metalness: 0.15}); // Black glossy frames
  const lensMat = new Ce({color: 0xffffff, roughness: 0.05, metalness: 0.1, transparent: true, opacity: 0.4});
  const teethMat = new Ce({color: 0xffffff, roughness: 0.4, metalness: 0});
  const lipsMat = new Ce({color: 0xd67d73, roughness: 0.7, metalness: 0});
  const shirtMat = new Ce({color: 0x82b4dc, roughness: 0.92, metalness: 0}); // Light blue dress shirt
  const collarDark = new Ce({color: 0x2b3848, roughness: 0.85, metalness: 0}); // Dark inner collar band
  const buttonMat = new Ce({color: 0xf7f7f7, roughness: 0.3, metalness: 0.4}); // Pearl white buttons
  const sashGreen = new Ce({color: 0x008c45, roughness: 0.8, metalness: 0}); // Italian tricolor sash
  const sashWhite = new Ce({color: 0xf4f5f0, roughness: 0.8, metalness: 0});
  const sashRed = new Ce({color: 0xcd212a, roughness: 0.8, metalness: 0});

  // 1. Bald Scalp volume (smooth, cheerful, rounded cranium)
  const scalp = new De(new $t(1, 16, 14), scalpMat);
  scalp.position.set(0, 0.30, -0.02);
  scalp.scale.set(0.185, 0.155, 0.19);
  features.add(scalp);

  const forehead = new De(new $t(1, 14, 12), skinMat);
  forehead.position.set(0, 0.24, 0.10);
  forehead.scale.set(0.165, 0.13, 0.15);
  features.add(forehead);

  // 2. Black glasses frames (matching portrait)
  const glasses = new U();
  glasses.name = "giuseppe-glasses";
  glasses.position.set(0, 0.145, 0.225);

  // Left frame rim (rounded rectangle)
  const rimL = new De(new os(0.068, 0.052, 0.012, 3, 0.016), frameMat);
  rimL.position.set(-0.068, 0, 0);
  glasses.add(rimL);

  // Left lens
  const lensL = new De(new os(0.056, 0.040, 0.004, 2, 0.01), lensMat);
  lensL.position.set(-0.068, 0, 0.003);
  glasses.add(lensL);

  // Right frame rim (rounded rectangle)
  const rimR = new De(new os(0.068, 0.052, 0.012, 3, 0.016), frameMat);
  rimR.position.set(0.068, 0, 0);
  glasses.add(rimR);

  // Right lens
  const lensR = new De(new os(0.056, 0.040, 0.004, 2, 0.01), lensMat);
  lensR.position.set(0.068, 0, 0.003);
  glasses.add(lensR);

  // Nose bridge
  const bridge = new De(new os(0.028, 0.010, 0.012, 2, 0.003), frameMat);
  bridge.position.set(0, 0.008, 0.001);
  glasses.add(bridge);

  // Left temple arm (going back to ear)
  const armL = new De(new os(0.008, 0.010, 0.20, 2, 0.002), frameMat);
  armL.position.set(-0.112, 0.006, -0.095);
  armL.rotation.y = 0.08;
  glasses.add(armL);

  // Right temple arm (going back to ear)
  const armR = new De(new os(0.008, 0.010, 0.20, 2, 0.002), frameMat);
  armR.position.set(0.112, 0.006, -0.095);
  armR.rotation.y = -0.08;
  glasses.add(armR);

  features.add(glasses);

  // 3. Wide cheerful smile with white teeth
  const mouth = new U();
  mouth.position.set(0, 0.058, 0.218);

  const lips = new De(new os(0.075, 0.022, 0.018, 3, 0.008), lipsMat);
  mouth.add(lips);

  const teeth = new De(new os(0.060, 0.012, 0.014, 2, 0.004), teethMat);
  teeth.position.set(0, 0.002, 0.003);
  mouth.add(teeth);

  features.add(mouth);

  // 4. Mayoral Light Blue Shirt Collar & Buttons
  const collarGroup = new U();
  collarGroup.position.set(0, -0.11, 0.12);

  // Inner contrast collar band (like in photo)
  const innerBand = new De(new os(0.16, 0.04, 0.08, 2, 0.01), collarDark);
  innerBand.position.set(0, 0.02, -0.02);
  collarGroup.add(innerBand);

  // Left collar wing
  const collarL = new De(new os(0.07, 0.06, 0.025, 2, 0.01), shirtMat);
  collarL.position.set(-0.065, 0, 0.035);
  collarL.rotation.set(0.3, 0.2, -0.3);
  collarGroup.add(collarL);

  // Right collar wing
  const collarR = new De(new os(0.07, 0.06, 0.025, 2, 0.01), shirtMat);
  collarR.position.set(0.065, 0, 0.035);
  collarR.rotation.set(0.3, -0.2, 0.3);
  collarGroup.add(collarR);

  // Small white buttons on placket
  for (let b = 0; b < 3; b++) {
    const btn = new De(new $t(0.008, 8, 8), buttonMat);
    btn.position.set(0, -0.04 - b * 0.06, 0.048);
    btn.rotation.x = Math.PI / 2;
    collarGroup.add(btn);
  }

  // 5. Tricolor Mayoral Sash (fascia tricolore da sindaco)
  const sash = new U();
  sash.position.set(0, -0.15, 0.05);
  const bandG = new De(new os(0.022, 0.32, 0.015, 2, 0.004), sashGreen);
  bandG.position.set(-0.025, -0.10, 0.03);
  bandG.rotation.z = 0.42;
  const bandW = new De(new os(0.022, 0.32, 0.015, 2, 0.004), sashWhite);
  bandW.position.set(0, -0.10, 0.032);
  bandW.rotation.z = 0.42;
  const bandR = new De(new os(0.022, 0.32, 0.015, 2, 0.004), sashRed);
  bandR.position.set(0.025, -0.10, 0.03);
  bandR.rotation.z = 0.42;
  sash.add(bandG, bandW, bandR);
  collarGroup.add(sash);

  features.add(collarGroup);

  head.add(features);

  // Recolor clothes of base mesh to light blue mayoral shirt and dark trousers
  scene.traverse(p => {
    if (p.isMesh && p.material) {
      for (const m of (Array.isArray(p.material) ? p.material : [p.material])) {
        if (m.name && m.name.toLowerCase().includes("top") || m.name.toLowerCase().includes("shirt") || m.name.toLowerCase().includes("jacket")) {
          m.color.setHex(0x82b4dc);
          m.needsUpdate = true;
        } else if (m.name && m.name.toLowerCase().includes("bottom") || m.name.toLowerCase().includes("pant")) {
          m.color.setHex(0x22262b);
          m.needsUpdate = true;
        }
      }
    }
  });
}
"""

def get_gta_3d_decor_builders():
    return """
,"secular-ficus"(t,e,n){
  const o=oo(e,n,12.0);
  // Massive ancient ficus tree of Villa Comunale di Augusta
  // Twisted trunk & aerial roots
  t.cylinder(1.8,5.0,"rope",o,0,2.5,0);
  t.cylinder(0.6,4.5,"rope",o,-1.4,2.2,0.6);
  t.cylinder(0.5,4.5,"rope",o,1.3,2.2,-0.5);
  t.cylinder(0.4,4.2,"rope",o,0.8,2.1,1.1);
  // Lush expansive green shade canopy
  t.ball(4.8,2.2,4.8,"foliage",o,0,5.8,0);
  t.ball(3.5,1.8,3.5,"foliage",o,-2.2,6.4,1.2);
  t.ball(3.6,1.9,3.6,"foliage",o,2.0,6.2,-1.0);
  t.ball(2.8,1.6,2.8,"foliage",o,0,7.2,0.8);
  // Hanging aerial roots
  t.cylinder(0.08,3.2,"rope",o,-2.2,3.5,1.0);
  t.cylinder(0.08,3.0,"rope",o,1.8,3.5,-0.8);
}
,"cut-stump"(t,e,n){
  const o=oo(e,n,2.5);
  // Freshly cut tree stump (satirical symbol of deforestation)
  t.cylinder(1.2,1.2,"rope",o,0,0.6,0);
  t.cylinder(1.15,0.06,"top",o,0,1.21,0); // Growth rings top
  // Yellow wood chips & sawdust
  t.ball(1.6,0.15,1.6,"gold",o,0,0.08,0);
}
,"chainsaw"(t,e,n){
  const o=oo(e,n,2.0);
  // Orange/yellow motorized chainsaw
  t.box(0.9,0.55,0.5,"orange",o,0,0.4,0);
  t.cylinder(0.06,0.6,"dark",o,-0.4,0.6,0); // Rear handle
  t.box(1.2,0.22,0.06,"dark",o,0.9,0.35,0); // Guide bar
  t.box(1.22,0.24,0.08,"gold",o,0.9,0.35,0); // Chain teeth
}
,"waste-bin"(t,e,n){
  const o=oo(e,n,2.2);
  // Cluster of recycling bins (mastelli della differenziata)
  // Brown (organico), Blue (carta), Yellow (plastica), Green (vetro)
  t.box(0.5,0.8,0.5,"rope",o,-0.8,0.4,0); // Umido
  t.box(0.5,0.8,0.5,"blue",o,-0.25,0.4,0); // Carta
  t.box(0.5,0.8,0.5,"gold",o,0.3,0.4,0); // Plastica
  t.box(0.5,0.8,0.5,"foliage",o,0.85,0.4,0); // Vetro
  // Open lids
  t.box(0.52,0.08,0.52,"dark",o,-0.8,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,-0.25,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,0.3,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,0.85,0.84,0);
}
,"sewer-manhole"(t,e,n){
  const o=oo(e,n,2.2);
  // Overflowing flooded cast-iron manhole (Lungomare Rossini)
  t.cylinder(0.9,0.12,"dark",o,0,0.06,0); // Manhole rim
  t.cylinder(0.75,0.08,"dark",o,0.1,0.25,0.1); // Displaced lid
  t.cylinder(1.2,0.05,"blueLight",o,0,0.03,0); // Puddle of sewage overflow
  t.ball(0.4,0.5,0.4,"foliage",o,0,0.35,0); // Bubbling green foam
}
,"stage-speaker"(t,e,n){
  const o=oo(e,n,4.5);
  // Giant concert festival speaker stack (propaganda mega-concert)
  t.box(1.4,3.2,1.2,"dark",o,0,1.6,0);
  // 4 Speaker woofers
  for(let y of[0.6,1.3,2.0,2.7]){
    t.cylinder(0.24,0.05,"cream",o,0,y,0.61);
    t.cylinder(0.12,0.06,"dark",o,0,y,0.62);
  }
}
,"stage-light"(t,e,n){
  const o=oo(e,n,3.5);
  // Concert truss with colorful rotating spotlights
  t.box(0.12,3.0,0.12,"dark",o,0,1.5,0);
  t.box(1.5,0.15,0.15,"dark",o,0,2.9,0);
  t.cylinder(0.2,0.35,"gold",o,-0.5,2.7,0.1);
  t.cylinder(0.2,0.35,"blueLight",o,0.5,2.7,0.1);
}
,"burning-tire"(t,e,n){
  const o=oo(e,n,2.8);
  // Burning pile of toxic waste & tires (discariche abusive)
  t.cylinder(0.7,0.35,"dark",o,0,0.18,0);
  t.cylinder(0.65,0.35,"dark",o,0.4,0.45,0.1);
  // Orange flames
  t.ball(0.5,0.8,0.5,"gold",o,0.2,0.8,0);
  t.ball(0.35,0.6,0.35,"orange",o,-0.1,0.7,0.1);
  // Billowing black smoke plume
  t.ball(0.8,0.7,0.8,"dark",o,0.1,1.5,0);
  t.ball(1.1,0.9,1.1,"dark",o,0.3,2.3,0);
}
,"cement-mixer"(t,e,n){
  const o=oo(e,n,4.0);
  // Concrete cement mixer pouring wet gray cement over soil
  t.box(1.6,1.4,1.4,"orange",o,-0.6,0.7,0);
  t.cylinder(0.9,1.8,"cream",o,0.7,1.2,0);
  // Wet cement pool on ground
  t.box(2.2,0.1,1.8,"terrain2",o,0.5,0.05,0);
}
,"duomo-facade"(t,e,n){
  const o=oo(e,n,14.0);
  // Sicilian Baroque Chiesa Madre facade in Piazza Duomo
  t.box(10,8.5,2.0,"cream",o,0,4.25,0,0.2);
  t.box(7.5,4.5,1.8,"cream",o,0,10.5,0,0.2);
  t.box(2.2,3.5,0.4,"rope",o,0,1.75,1.02); // Main wooden door
  t.box(3.2,0.8,0.6,"cream",o,0,3.6,1.05); // Portal pediment
  t.cylinder(0.7,1.4,"gold",o,0,13.5,0); // Cross pediment
}
,"fountain-augusta"(t,e,n){
  const o=oo(e,n,3.2);
  // Historic stone fountain with splashing clear water
  t.cylinder(1.6,0.6,"terrain",o,0,0.3,0);
  t.cylinder(1.45,0.1,"blueLight",o,0,0.55,0); // Water surface
  t.cylinder(0.4,1.2,"terrain2",o,0,0.8,0);
  t.ball(0.6,0.3,0.6,"terrain",o,0,1.4,0);
}
,"tree-sapling"(t,e,n){
  const o=oo(e,n,2.0);
  // Young leafy tree sapling with wooden stake support
  t.cylinder(0.06,1.8,"rope",o,0,0.9,0);
  t.cylinder(0.04,1.4,"top",o,0.12,0.7,0); // Wooden stake
  t.ball(0.5,0.7,0.5,"foliage",o,0,1.7,0); // Green foliage crown
}
,"heat-wave"(t,e,n){
  const o=oo(e,n,3.5);
  // Shimmering orange heat bubble aura
  t.ball(1.8,1.4,1.8,"orangeLight",o,0,1.0,0);
  t.ball(1.2,1.8,1.2,"gold",o,0,1.4,0);
}
"""

def generate_gta_levels_code():
    # Load levels generator with custom GTA ecological narratives and mechanics
    from generate_all_10_levels import get_level_1, get_level_2, get_level_3, get_level_4, get_level_5, get_level_6, get_level_7, get_level_8, get_level_9, get_level_10
    
    # We will customize each of the 10 levels to match the GTA Giuseppe Taglia Alberi themes!
    # L1: I Giardini Pubblici & La Strage degli Alberi
    # L2: Lungomare Rossini & Il Diluvio Fognario
    # L3: Il Golfo Xifonio & Il Depuratore Che Non C'e
    # L4: La Giungla dei Mastelli (Raccolta Differenziata)
    # L5: I Roghi Tossici delle Discariche Abusive
    # L6: Il Monte Tauro & La Colata di Cemento
    # L7: Piazza Castello & Il Gran Concerto Propaganda
    # L8: Il Porto Megarese & La Bonifica Fantasma
    # L9: Le Saline Mulinello Sotto Fuoco
    # L10: La Rinascita Verde di Augusta (Gran Finale)
    
    levels = []
    
    # Level 1
    l1 = get_level_1()
    l1 = l1.replace("Il Polo Petrolchimico di Augusta", "I Giardini Pubblici & La Strage degli Alberi")
    l1 = l1.replace('"Petrolchimico"', '"Villa Comunale"')
    l1 = l1.replace("Ciminiere, torce e fumi industriali", "Ficus secolari, motoseghe e bolle di calore")
    l1 = l1.replace("Benvenuto al polo petrolchimico di Augusta-Priolo. Tra ciminiere fumanti, valvole di pressione e tubature di greggio, scappa dalla raffineria prima che la pressione salga al massimo!",
                    "Benvenuto ai Giardini Pubblici di Augusta! Gli alberi secolari vengono abbattuti senza sosta, lasciando piazze di cemento rovente e asfissianti bolle di calore. Schiva le motoseghe, difendi i ficus e raccogli i germogli per ripiantare il verde!")
    l1 = l1.replace('biome: "desert"', 'biome: "citadel"')
    l1 = l1.replace('sky: "#2d2016"', 'sky: "#2e5a38"')
    l1 = l1.replace('fog: "#453225"', 'fog: "#3d7048"')
    l1 = l1.replace('{kind: "flare-stack", x: 54, y: 15.2, size: 12, z: -4}', '{kind: "secular-ficus", x: 54, y: 15.2, size: 12, z: -4}')
    l1 = l1.replace('{kind: "oil-tank", x: 120, y: 11.8, size: 5, z: -4}', '{kind: "cut-stump", x: 120, y: 11.8, size: 3, z: -2}')
    l1 = l1.replace('{kind: "oil-tank", x: 172, y: 16.2, size: 5.5, z: -4}', '{kind: "chainsaw", x: 172, y: 16.2, size: 2.5, z: -2}')
    l1 = l1.replace('{kind: "furnace", x: 60, y: 10, size: 6, z: -4}', '{kind: "secular-ficus", x: 60, y: 14.0, size: 10, z: -4}')
    l1 = l1.replace('{kind: "furnace", x: 185, y: 13, size: 6, z: -4}', '{kind: "tree-sapling", x: 185, y: 14.8, size: 2.2, z: -1.5}')
    levels.append(l1)

    # Level 2
    l2 = get_level_2()
    l2 = l2.replace("La Rada di Augusta & Pontili al Mercurio", "Lungomare Rossini & Il Diluvio Fognario")
    l2 = l2.replace('"Porto Mercurio"', '"Lungomare Rossini"')
    l2 = l2.replace("Pontili sospesi, chiatte industriali e acque scure", "Tombini che esplodono, liquami in strada e crisi climatica")
    l2 = l2.replace("Sei fuggito dalla raffineria, ma ora devi attraversare la rada industriale di Augusta. Le acque sono sature di mercurio e cloro-soda: salta tra pontili di carico, chiatte a fune e imponenti gru navali!",
                    "Le bombe d'acqua della crisi climatica travolgono Augusta! La rete fognaria obsoleta cede e i tombini del lungomare Rossini saltano via sparando getti di liquami e melma. Salta sulle passerelle di soccorso e chiudi le paratoie di spurgo!")
    l2 = l2.replace('{kind: "crane-tower", x: 30, y: 13.8, size: 9, z: -3.5}', '{kind: "sewer-manhole", x: 30, y: 13.8, size: 2.5, z: -1.5}')
    l2 = l2.replace('{kind: "crane-tower", x: 112, y: 12.6, size: 9.5, z: -3.5}', '{kind: "sewer-manhole", x: 112, y: 12.6, size: 2.5, z: -1.5}')
    levels.append(l2)

    # Level 3
    l3 = get_level_3()
    l3 = l3.replace("La Penisola delle Ceneri di Pirite", "Il Golfo Xifonio & Il Depuratore Che Non C'è")
    l3 = l3.replace('"Ceneri di Pirite"', '"Golfo Xifonio"')
    l3 = l3.replace("Montagne rosse, fumarole e scorie solforose", "Bagnanti tra divieti di balneazione e scarichi a mare")
    l3 = l3.replace("La famigerata penisola delle ceneri di pirite: milioni di tonnellate di polvere rossa tossica e scorie ferrose affacciate sul mare. Le passerelle franano e dai crateri eruttano violenti geyser di vapore solforoso!",
                    "Il paradosso del golfo Xifonio: le famiglie fanno il bagno tra splendide acque e cartelli di divieto di balneazione ignorati, mentre scarichi fognari abusivi riversano reflui in mare senza depuratore. Salta tra le boe e attiva i filtri marini!")
    l3 = l3.replace('biome: "desert"', 'biome: "nightfall"')
    l3 = l3.replace('sky: "#4a1810"', 'sky: "#183852"')
    l3 = l3.replace('fog: "#682416"', 'fog: "#244c6e"')
    levels.append(l3)

    # Level 4
    l4 = get_level_4()
    l4 = l4.replace("Le Condotte Fognarie & Canali Industriali", "La Giungla dei Mastelli (Raccolta Differenziata)")
    l4 = l4.replace('"Fognature"', '"I Mastelli"')
    l4 = l4.replace("Collettori sotterranei, saracinesche e reflui chimici", "Cassonetti rovesciati, cumuli di plastica e gabbiani")
    l4 = l4.replace("Scendi nel ventre sotterraneo di Augusta: un labirinto di collettori in cemento armato e condotte di scarico chimico. Le chiuse idrauliche funzionano a tempo e la melma verde è altamente corrosiva!",
                    "I vicoli di Augusta sono invasi dall'anarchia della raccolta differenziata! Mastelli rovesciati, sacchetti abbandonati ovunque e gabbiani affamati che assediano le strade. Salta sui bidoni colorati, differenzia i rifiuti e ripristina il decoro urbano!")
    l4 = l4.replace('{kind: "pipe", x: 10, y: 10, size: 6, z: -3}', '{kind: "waste-bin", x: 10, y: 10.5, size: 2.5, z: -1.5}')
    l4 = l4.replace('{kind: "hazard-barrel", x: 34, y: 12.8, size: 1.2, z: -1.2}', '{kind: "waste-bin", x: 34, y: 12.8, size: 2.2, z: -1.2}')
    l4 = l4.replace('{kind: "pipe-elbow", x: 60, y: 13.0, size: 2.6, z: -3}', '{kind: "waste-bin", x: 60, y: 13.0, size: 2.5, z: -1.5}')
    levels.append(l4)

    # Level 5
    l5 = get_level_5()
    l5 = l5.replace("L'Hangar Dirigibili di Augusta (Monumento 1917)", "I Roghi Tossici delle Discariche Abusive")
    l5 = l5.replace('"Hangar Dirigibili"', '"Roghi Tossici"')
    l5 = l5.replace("La monumentale cattedrale di cemento armato (1917)", "Copertoni in fiamme, diossina e discariche clandestine")
    l5 = l5.replace("Il monumento futurista più spettacolare di Sicilia: l'imponente Hangar Dirigibili del 1917 in cemento armato, alto quasi 40 metri! Arrampicati tra gli archi parabolici, i boschi di eucalipti e le grandiose capriate sospese nel vuoto!",
                    "Le periferie di Augusta soffocano tra roghi tossici di pneumatici e discariche abusive che bruciano nella notte! Schiva le fiamme di diossina, aziona gli idranti di soccorso e spegni i roghi dolosi per salvare l'aria dei cittadini!")
    l5 = l5.replace('biome: "citadel"', 'biome: "desert"')
    l5 = l5.replace('sky: "#453625"', 'sky: "#3a1a12"')
    l5 = l5.replace('fog: "#604b34"', 'fog: "#52261a"')
    l5 = l5.replace('{kind: "hangar-arch", x: 50, y: 16.5, size: 14.0, z: -4.0}', '{kind: "burning-tire", x: 50, y: 16.5, size: 3.5, z: -2.0}')
    l5 = l5.replace('{kind: "hangar-arch", x: 104, y: 23.5, size: 14.0, z: -4.0}', '{kind: "burning-tire", x: 104, y: 23.5, size: 4.0, z: -2.0}')
    l5 = l5.replace('{kind: "hangar-arch", x: 166, y: 28.0, size: 14.0, z: -4.0}', '{kind: "burning-tire", x: 166, y: 28.0, size: 4.0, z: -2.0}')
    levels.append(l5)

    # Level 6
    l6 = get_level_6()
    l6 = l6.replace("Il Castello Svevo di Augusta (Forte Hohenstaufen)", "Il Monte Tauro & La Colata di Cemento")
    l6 = l6.replace('"Castello Svevo"', '"Monte Tauro"')
    l6 = l6.replace("Mura normanno-sveve, prigioni borboniche e fossati", "Consumo di suolo selvaggio, betoniere e uliveti distrutti")
    l6 = l6.replace("La titanica fortezza fondata da Federico II nel 1232 sull'estremità nord dell'isola: mura ciclopiche in pietra lavica e calcare siracusano, ex carcere borbonico e cortili d'armi affacciati sul mare!",
                    "Le verdi colline del Monte Tauro vengono divorate dal cemento selvaggio! Betoniere e ruspe abbattono muretti a secco e uliveti secolari per speculazioni edilizie. Salta tra i cantieri abusivi, proteggi il suolo naturale e ferma la colata grigia!")
    l6 = l6.replace('{kind: "spanish-bastion", x: 20, y: 12.6, size: 6.0, z: -2.5}', '{kind: "cement-mixer", x: 20, y: 12.6, size: 4.0, z: -2.0}')
    l6 = l6.replace('{kind: "spanish-bastion", x: 74, y: 15.0, size: 6.5, z: -2.5}', '{kind: "cement-mixer", x: 74, y: 15.0, size: 4.0, z: -2.0}')
    l6 = l6.replace('{kind: "spanish-bastion", x: 114, y: 16.2, size: 7.0, z: -3.0}', '{kind: "cement-mixer", x: 114, y: 16.2, size: 4.0, z: -2.0}')
    levels.append(l6)

    # Level 7
    l7 = get_level_7()
    l7 = l7.replace("Faro Santa Croce & Le Falesie di Brucoli", "Piazza Castello & Il Gran Concerto Propaganda")
    l7 = l7.replace('"Faro S. Croce"', '"Concertone"')
    l7 = l7.replace("Scogliere bianche, mare Ionio e vista sul vulcano Etna", "Muri di casse acustiche, fari stordenti e passerelle")
    l7 = l7.replace("La punta più spettacolare della costa augustana: il faro ottagonale di Santa Croce a picco sulle scogliere calcaree bianche di Brucoli, con i bunker della Seconda Guerra Mondiale e la magnifica vista sul vulcano Etna!",
                    "Piazza Castello viene trasformata nel mega-palco del concerto propaganda delle istituzioni per distrarre i cittadini dai problemi ecologici! Salta sulle gigantesche torri di altoparlanti, schiva i fari stroboscopici e stacca la spina del frastuono!")
    l7 = l7.replace('sky: "#1a3450"', 'sky: "#241038"')
    l7 = l7.replace('fog: "#284c72"', 'fog: "#341852"')
    l7 = l7.replace('{kind: "lighthouse-tower", x: 174, y: 19.8, size: 9.5, z: -3.5}', '{kind: "stage-speaker", x: 174, y: 19.8, size: 6.5, z: -3.0}')
    l7 = l7.replace('{kind: "bunker", x: 74, y: 15.5, size: 3.5, z: -2.0}', '{kind: "stage-light", x: 74, y: 15.5, size: 4.0, z: -2.0}')
    levels.append(l7)

    # Level 8
    l8 = get_level_8()
    l8 = l8.replace("Le Antiche Saline Regina di Augusta", "Il Porto Megarese & La Bonifica Fantasma")
    l8 = l8.replace('"Saline Regina"', '"Bonifica Fantasma"')
    l8 = l8.replace("Bacini rosa, croste di sale e mulini a vento salinari", "Miliardi svaniti, draghe arrugginite e fanghi al mercurio")
    l8 = l8.replace("Le storiche Saline Regina di Augusta: una scacchiera di canali d'acqua rosa e argini di terra scura. Le croste di sale bianco cristallizzato si spaccano sotto i piedi e i mulini a vento salinari azionano grandi piattaforme orbitanti!",
                    "I fondali del porto megarese custodiscono decenni di veleni industriali: i fondi per la bonifica sono scomparsi e le draghe arrugginiscono nel silenzio. Muoviti tra i piloni di carotaggio, preleva i campioni e inchioda i responsabili!")
    levels.append(l8)

    # Level 9
    l9 = get_level_9()
    l9 = l9.replace("I Forti Spagnoli della Rada (Garcia & Vittoria)", "Le Saline Mulinello Sotto Fuoco")
    l9 = l9.replace('"Forti Spagnoli"', '"Saline Mulinello"')
    l9 = l9.replace("Fortezze gemelle (1567), onde in tempesta e catene navali", "Canneti protetti, fenicotteri rosa e roghi dolosi")
    l9 = l9.replace("Le due fortezze gemelle del 1567 edificate dal viceré Garcia de Toledo su due isolotti sperduti al centro del golfo di Augusta. Una tempesta notturna scuote la rada: supera i marosi, i cannoni e la gigantesca catena navale di ferro!",
                    "L'oasi protetta delle Saline Mulinello è assediata dalle fiamme dei piromani! I canneti bruciano mettendo in fuga i fenicotteri rosa. Attraversa i canali salmastri, apri le chiuse d'acqua dolce e salva l'ultimo rifugio naturale di Augusta!")
    levels.append(l9)

    # Level 10
    l10 = get_level_10()
    l10 = l10.replace("La Porta Spagnola & Il Taglio dell'Isola", "La Rinascita Verde di Augusta (Gran Finale)")
    l10 = l10.replace('"Porta Spagnola"', '"Rinascita Verde"')
    l10 = l10.replace("Il gran finale: centro storico, tetti barocchi e la fuga trionfale!", "La grande marcia del verde, alberi in ogni piazza e vittoria!")
    l10 = l10.replace("Il gran finale di Augusta Slop Adventures! Corri sui tetti e balconi barocchi dell'Isola di Augusta, supera il fossato salmastro del Taglio dell'Isola, varca l'arco trionfale della monumentale Porta Spagnola del 1699 e suona la Campana della Libertà!",
                     "Il grande corteo civico per il futuro di Augusta! Da Porta Spagnola fino a Piazza Duomo, i cittadini piantano alberi, rigenerano le piazze contro le bolle di calore e abbattono la Motosega d'Oro. Suona la Campana Civica della Rinascita Ecologica!")
    l10 = l10.replace('{kind: "porta-spagnola", x: 160, y: 20.8, size: 10.0, z: -3.0}', '{kind: "duomo-facade", x: 160, y: 20.8, size: 14.0, z: -3.5}')
    l10 = l10.replace('{kind: "spanish-bastion", x: 80, y: 16.2, size: 7.0, z: -3.0}', '{kind: "fountain-augusta", x: 80, y: 16.2, size: 4.0, z: -2.0}')
    levels.append(l10)

    return "\n\n".join(levels)

def main():
    print("Reading base bundle/index-augusta-v2.js...")
    with open("bundle/index-augusta-v2.js", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update character definition to Giuseppe
    char_marker = 'const S0=1.78,$d=['
    pos_d = content.find(char_marker)
    if pos_d != -1:
        end_d = content.find('],yD=', pos_d)
        new_d = 'const S0=1.78,$d=[{id:"giuseppe",name:"Giuseppe",note:"Il sindaco di Augusta con camicia celeste e occhiali neri.",model:"explorer.glb",motion:"explorer-motion.json",animation:"explorer-animation.json",height:S0*1.2,orangeSource:0,bonePrefix:"mixamorig"}'
        content = content[:pos_d] + new_d + content[end_d:]
        print("Updated character registry to Giuseppe!")
        content = content.replace('yD="baldu"', 'yD="giuseppe"')

    # 2. Add applyGiuseppeCustomization and replace call in ese()
    baldu_custom_marker = "applyBalduCustomization(e.scene,i)"
    if baldu_custom_marker in content:
        content = content.replace(baldu_custom_marker, "applyGiuseppeCustomization(e.scene,i)")
        print("Updated ese() call to applyGiuseppeCustomization!")

    # Inject applyGiuseppeCustomization definition
    func_marker = "function applyBalduCustomization("
    pos_func = content.find(func_marker)
    if pos_func != -1:
        content = content[:pos_func] + get_character_customization_code() + "\n" + content[pos_func:]
        print("Injected applyGiuseppeCustomization definition!")

    # 3. Inject GTA 3D environmental decor models into _D
    d_marker = 'castle(t,e,n){sx(t,e,0,0,0,n)}};'
    pos_d_end = content.find(d_marker)
    if pos_d_end != -1:
        inject_pos = pos_d_end + len('castle(t,e,n){sx(t,e,0,0,0,n)}')
        content = content[:inject_pos] + get_gta_3d_decor_builders() + content[inject_pos:]
        print("Injected GTA 3D environmental models into _D!")

    # 4. Replace levels with the 10 GTA bespoke levels
    start_marker = "// --- AUGUSTA LEVELS (PROVINCIA DI SIRACUSA) ---"
    end_marker = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10]"
    p_start = content.find(start_marker)
    p_end = content.find(end_marker)
    if p_start != -1 and p_end != -1:
        new_levels = "// --- GTA: GIUSEPPE TAGLIA ALBERI (10 LIVELLI ECOLOGICI E CIVICI) ---\n\n" + generate_gta_levels_code() + "\n\n"
        content = content[:p_start] + new_levels + end_marker + content[p_end + len(end_marker):]
        print("Replaced all 10 levels with GTA ecological levels!")

    # Save to bundle/index-gta-v1.js
    with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Saved bundle/index-gta-v1.js successfully!")

if __name__ == "__main__":
    main()
