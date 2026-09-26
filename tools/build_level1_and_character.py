# tools/build_level1_and_character.py
import re
import os

with open("tools/generate_gta_game.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

# 1. Update Character Customization Code to include Trowel with green sprout, Wristwatch, Belt, Glasses, Scalp, Smile
new_char_code = '''function applyGiuseppeCustomization(scene, choice) {
  if (!choice || (choice.id !== "giuseppe" && choice.id !== "baldu" && choice.id !== "explorer")) return;
  const head = scene.getObjectByName("Head");
  if (!head || head.getObjectByName("giuseppe-head-features")) return;

  const features = new U();
  features.name = "giuseppe-head-features";

  // Materials for Giuseppe (from reference artwork)
  const skinMat = new Ce({color: 0xf1be9c, roughness: 0.88, metalness: 0});
  const scalpMat = new Ce({color: 0xf3c2a2, roughness: 0.90, metalness: 0});
  const frameMat = new Ce({color: 0x111111, roughness: 0.22, metalness: 0.15}); // Black glossy frames
  const lensMat = new Ce({color: 0xffffff, roughness: 0.05, metalness: 0.1, transparent: true, opacity: 0.45});
  const teethMat = new Ce({color: 0xffffff, roughness: 0.4, metalness: 0});
  const lipsMat = new Ce({color: 0xd67d73, roughness: 0.7, metalness: 0});
  const shirtMat = new Ce({color: 0x78abdc, roughness: 0.90, metalness: 0}); // Sky-blue dress shirt
  const collarDark = new Ce({color: 0x223040, roughness: 0.85, metalness: 0});
  const buttonMat = new Ce({color: 0xf7f7f7, roughness: 0.3, metalness: 0.4});
  const woodMat = new Ce({color: 0xb57842, roughness: 0.85, metalness: 0});
  const metalMat = new Ce({color: 0xd0d5dd, roughness: 0.25, metalness: 0.7});
  const leafMat = new Ce({color: 0x3a9d23, roughness: 0.8, metalness: 0});
  const leatherMat = new Ce({color: 0x4a2c16, roughness: 0.85, metalness: 0});
  const dialMat = new Ce({color: 0xffffff, roughness: 0.3, metalness: 0.2});
  const beltMat = new Ce({color: 0x251c16, roughness: 0.8, metalness: 0});
  const buckleMat = new Ce({color: 0xcccccc, roughness: 0.25, metalness: 0.8});

  // 1. Bald Scalp volume (smooth, cheerful, rounded cranium)
  const scalp = new De(new $t(1, 16, 14), scalpMat);
  scalp.position.set(0, 0.30, -0.02);
  scalp.scale.set(0.185, 0.155, 0.19);
  features.add(scalp);

  const forehead = new De(new $t(1, 14, 12), skinMat);
  forehead.position.set(0, 0.24, 0.10);
  forehead.scale.set(0.165, 0.13, 0.15);
  features.add(forehead);

  // 2. Black glasses frames matching reference portrait
  const glasses = new U();
  glasses.name = "giuseppe-glasses";
  glasses.position.set(0, 0.145, 0.225);

  const rimL = new De(new os(0.068, 0.052, 0.012, 3, 0.016), frameMat);
  rimL.position.set(-0.068, 0, 0);
  const lensL = new De(new os(0.056, 0.040, 0.004, 2, 0.01), lensMat);
  lensL.position.set(-0.068, 0, 0.003);
  glasses.add(rimL, lensL);

  const rimR = new De(new os(0.068, 0.052, 0.012, 3, 0.016), frameMat);
  rimR.position.set(0.068, 0, 0);
  const lensR = new De(new os(0.056, 0.040, 0.004, 2, 0.01), lensMat);
  lensR.position.set(0.068, 0, 0.003);
  glasses.add(rimR, lensR);

  const bridge = new De(new os(0.028, 0.010, 0.012, 2, 0.003), frameMat);
  bridge.position.set(0, 0.008, 0.001);
  glasses.add(bridge);

  const armL = new De(new os(0.008, 0.010, 0.20, 2, 0.002), frameMat);
  armL.position.set(-0.112, 0.006, -0.095);
  armL.rotation.y = 0.08;
  const armR = new De(new os(0.008, 0.010, 0.20, 2, 0.002), frameMat);
  armR.position.set(0.112, 0.006, -0.095);
  armR.rotation.y = -0.08;
  glasses.add(armL, armR);

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

  // 4. Sky-Blue Shirt Collar & Front Buttons (no sash, matching new image)
  const collarGroup = new U();
  collarGroup.position.set(0, -0.11, 0.12);
  const innerBand = new De(new os(0.16, 0.04, 0.08, 2, 0.01), collarDark);
  innerBand.position.set(0, 0.02, -0.02);
  collarGroup.add(innerBand);

  const collarL = new De(new os(0.075, 0.065, 0.025, 2, 0.01), shirtMat);
  collarL.position.set(-0.068, 0, 0.035);
  collarL.rotation.set(0.3, 0.2, -0.3);
  const collarR = new De(new os(0.075, 0.065, 0.025, 2, 0.01), shirtMat);
  collarR.position.set(0.068, 0, 0.035);
  collarR.rotation.set(0.3, -0.2, 0.3);
  collarGroup.add(collarL, collarR);

  for (let b = 0; b < 3; b++) {
    const btn = new De(new $t(0.008, 8, 8), buttonMat);
    btn.position.set(0, -0.04 - b * 0.06, 0.048);
    btn.rotation.x = Math.PI / 2;
    collarGroup.add(btn);
  }
  features.add(collarGroup);
  head.add(features);

  // 5. Right Hand: Gardening Trowel with Living Green Clay Sapling
  const rightHand = scene.getObjectByName("RightHand");
  if (rightHand && !rightHand.getObjectByName("giuseppe-trowel")) {
    const trowel = new U();
    trowel.name = "giuseppe-trowel";
    trowel.position.set(0.02, -0.04, 0.02);
    trowel.rotation.set(Math.PI / 4, 0, -Math.PI / 6);

    // Wooden handle
    const handle = new De(new os(0.018, 0.09, 0.018, 2, 0.006), woodMat);
    handle.position.set(0, 0, 0);
    trowel.add(handle);

    // Metal neck and scoop
    const neck = new De(new os(0.008, 0.04, 0.008, 2, 0.002), metalMat);
    neck.position.set(0, 0.06, 0.01);
    neck.rotation.x = -0.3;
    trowel.add(neck);

    const scoop = new De(new os(0.045, 0.08, 0.010, 2, 0.003), metalMat);
    scoop.position.set(0, 0.11, 0.025);
    scoop.rotation.x = -0.2;
    trowel.add(scoop);

    // Sprouting green twig with leaves (Il Germoglio di Ficus)
    const twig = new De(new os(0.008, 0.08, 0.008, 2, 0.002), woodMat);
    twig.position.set(0, 0.15, 0.035);
    trowel.add(twig);

    const leaf1 = new De(new $t(0.018, 8, 8), leafMat);
    leaf1.scale.set(1.4, 0.3, 0.8);
    leaf1.position.set(-0.02, 0.16, 0.04);
    leaf1.rotation.set(0.3, -0.4, 0.5);

    const leaf2 = new De(new $t(0.018, 8, 8), leafMat);
    leaf2.scale.set(1.4, 0.3, 0.8);
    leaf2.position.set(0.02, 0.18, 0.04);
    leaf2.rotation.set(-0.3, 0.4, -0.5);

    const leafTop = new De(new $t(0.015, 8, 8), leafMat);
    leafTop.scale.set(1.2, 0.3, 0.7);
    leafTop.position.set(0, 0.20, 0.04);
    leafTop.rotation.set(0.2, 0, 0);

    trowel.add(leaf1, leaf2, leafTop);
    rightHand.add(trowel);
  }

  // 6. Left Wrist: Leather Wristwatch with Round Dial Face
  const leftWrist = scene.getObjectByName("LeftForeArm") || scene.getObjectByName("LeftHand");
  if (leftWrist && !leftWrist.getObjectByName("giuseppe-watch")) {
    const watch = new U();
    watch.name = "giuseppe-watch";
    watch.position.set(0.01, -0.16, 0.03);

    // Leather band
    const band = new De(new os(0.048, 0.025, 0.048, 2, 0.005), leatherMat);
    watch.add(band);

    // Round metallic silver case
    const caseMesh = new De(new $t(0.022, 12, 10), metalMat);
    caseMesh.scale.set(1, 0.3, 1);
    caseMesh.position.set(0, 0, 0.025);
    caseMesh.rotation.x = Math.PI / 2;
    watch.add(caseMesh);

    // White dial face
    const dial = new De(new $t(0.018, 12, 8), dialMat);
    dial.scale.set(1, 0.05, 1);
    dial.position.set(0, 0, 0.028);
    dial.rotation.x = Math.PI / 2;
    watch.add(dial);

    leftWrist.add(watch);
  }

  // 7. Waist Belt with Silver Buckle
  const spine = scene.getObjectByName("Hips") || scene.getObjectByName("Spine");
  if (spine && !spine.getObjectByName("giuseppe-belt")) {
    const beltGroup = new U();
    beltGroup.name = "giuseppe-belt";
    beltGroup.position.set(0, 0.04, 0);

    // Belt strap
    const strap = new De(new os(0.23, 0.038, 0.17, 3, 0.01), beltMat);
    beltGroup.add(strap);

    // Silver Buckle at center
    const buckle = new De(new os(0.052, 0.042, 0.016, 2, 0.004), buckleMat);
    buckle.position.set(0, 0, 0.088);
    beltGroup.add(buckle);

    spine.add(beltGroup);
  }

  // 8. Clothing Recolor: Sky-Blue Shirt & Dark Trousers
  scene.traverse(p => {
    if (p.isMesh && p.material) {
      for (const m of (Array.isArray(p.material) ? p.material : [p.material])) {
        if (m.name && (m.name.toLowerCase().includes("top") || m.name.toLowerCase().includes("shirt") || m.name.toLowerCase().includes("jacket"))) {
          m.color.setHex(0x78abdc);
          m.needsUpdate = true;
        } else if (m.name && (m.name.toLowerCase().includes("bottom") || m.name.toLowerCase().includes("pant"))) {
          m.color.setHex(0x242830);
          m.needsUpdate = true;
        }
      }
    }
  });
}'''

# Replace get_character_customization_code()
old_char_marker = 'def get_character_customization_code():'
end_char_marker = 'def get_gta_3d_decor_builders():'
idx1 = gen_code.find(old_char_marker)
idx2 = gen_code.find(end_char_marker)
if idx1 != -1 and idx2 != -1:
    gen_code = gen_code[:idx1] + 'def get_character_customization_code():\n    return """' + new_char_code + '\n"""\n\n' + gen_code[idx2:]
    print("Replaced character customization code in generator!")

# 2. Update 3D Environmental Models in get_gta_3d_decor_builders()
new_decor_code = '''def get_gta_3d_decor_builders():
    return """
,"ficus-centenario"(t,e,n){
  const o=oo(e,n,14.0);
  // Monumental Ficus macrophylla of Villa Comunale di Augusta (1850)
  // Main ancient fluted trunk
  t.cylinder(2.2,5.5,"rope",o,0,2.75,0);
  // 4 massive buttress pillar roots
  t.cylinder(0.9,5.0,"rope",o,-1.8,2.5,0.9);
  t.cylinder(0.8,5.2,"rope",o,1.7,2.6,-0.8);
  t.cylinder(0.7,4.8,"rope",o,0.9,2.4,1.6);
  t.cylinder(0.75,4.9,"rope",o,-1.5,2.4,-1.4);
  // Spreading root flare base
  t.ball(3.2,0.8,3.2,"rope",o,0,0.4,0);
  // Hanging aerial roots descending to soil
  t.cylinder(0.12,4.2,"rope",o,-3.2,4.2,1.2);
  t.cylinder(0.10,4.0,"rope",o,3.0,4.1,-1.2);
  t.cylinder(0.14,4.5,"rope",o,-1.2,4.3,2.8);
  t.cylinder(0.11,4.1,"rope",o,2.4,4.1,2.2);
  // Magnificent layered cathedral canopy
  t.ball(5.8,2.6,5.8,"foliage",o,0,7.2,0);
  t.ball(4.2,2.2,4.2,"moss",o,-3.2,7.8,1.5);
  t.ball(4.4,2.3,4.4,"foliage",o,3.0,7.6,-1.4);
  t.ball(3.6,2.0,3.6,"moss",o,0.8,8.4,2.2);
  t.ball(3.8,2.1,3.8,"foliage",o,-1.6,8.2,-2.6);
  t.ball(3.0,1.8,3.0,"foliage",o,0,9.6,0.4);
}
,"secular-ficus"(t,e,n){
  // Alias for ficus-centenario
  _D["ficus-centenario"](t,e,n);
}
,"barocco-duomo"(t,e,n){
  const o=oo(e,n,18.0);
  // Chiesa Madre di Augusta (Santa Maria Assunta in Cielo, 1693-1769)
  // Ground Floor (First Order) - warm Sicilian limestone
  t.box(14.0,1.2,3.0,"cream",o,0,0.6,0);
  t.box(15.0,0.4,3.6,"top",o,0,0.2,0.2); // steps
  t.box(12.5,7.5,2.4,"cream",o,0,4.95,0);
  // 4 Corinthian pilasters
  t.cylinder(0.45,7.6,"cream",o,-5.2,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,-2.4,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,2.4,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,5.2,5.0,1.25);
  // Column capitals
  t.box(1.2,0.6,1.2,"gold",o,-5.2,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,-2.4,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,2.4,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,5.2,8.9,1.25);
  // Central Main Portal: arched recessed entrance & broken pediment
  t.box(2.8,5.2,1.2,"dark",o,0,3.8,0.8);
  t.cylinder(1.4,1.2,"dark",o,0,6.4,0.8);
  t.box(3.4,0.4,0.6,"gold",o,0,7.4,1.3);
  // Side niches with carved statues
  t.box(1.4,3.2,0.6,"dark",o,-3.8,4.5,1.15);
  t.box(1.4,3.2,0.6,"dark",o,3.8,4.5,1.15);
  t.cylinder(0.3,1.8,"cream",o,-3.8,4.2,1.2);
  t.cylinder(0.3,1.8,"cream",o,3.8,4.2,1.2);
  // Intermediate entablature separating orders
  t.box(13.6,1.0,2.8,"cream",o,0,9.2,0);
  t.box(14.2,0.4,3.0,"gold",o,0,9.7,0);
  // Second Order (Upper tier)
  t.box(8.2,6.0,2.2,"cream",o,0,12.7,-0.1);
  // Baroque S-curved scroll volutes (ampie volute a ricciolo)
  t.cylinder(1.8,2.0,"cream",o,-5.2,11.2,0.8);
  t.cylinder(1.8,2.0,"cream",o,5.2,11.2,0.8);
  t.ball(1.2,1.2,1.2,"gold",o,-5.8,12.6,0.9);
  t.ball(1.2,1.2,1.2,"gold",o,5.8,12.6,0.9);
  // Upper pilasters
  t.cylinder(0.4,5.8,"cream",o,-2.8,12.6,1.05);
  t.cylinder(0.4,5.8,"cream",o,2.8,12.6,1.05);
  // Central Baroque upper window with pediment
  t.box(2.2,3.6,0.8,"dark",o,0,12.8,1.0);
  t.cylinder(1.1,0.8,"dark",o,0,14.6,1.0);
  t.box(2.8,0.4,0.6,"gold",o,0,15.3,1.1);
  // Top Entablature & Bell Gable (Cella campanaria)
  t.box(9.2,0.8,2.4,"cream",o,0,16.1,-0.1);
  t.box(5.4,3.4,1.8,"cream",o,0,18.2,-0.2);
  // Belfry arched openings
  t.box(1.2,2.0,1.9,"dark",o,-1.3,18.0,-0.2);
  t.box(1.2,2.0,1.9,"dark",o,1.3,18.0,-0.2);
  // Bronze bells
  t.cylinder(0.35,0.8,"gold",o,-1.3,18.2,-0.2);
  t.cylinder(0.35,0.8,"gold",o,1.3,18.2,-0.2);
  // Triangular pediment
  t.box(6.0,0.6,2.0,"cream",o,0,20.2,-0.2);
  // Elevated Latin Stone Cross at top summit
  t.box(0.3,2.4,0.3,"gold",o,0,21.6,-0.2);
  t.box(1.6,0.3,0.3,"gold",o,0,22.1,-0.2);
  // Flanking historic townhouses with balconies (from artwork)
  t.box(7.0,12.0,5.0,"top",o,-10.0,6.0,-1.5);
  t.box(2.4,0.3,1.2,"dark",o,-9.5,7.0,1.2);
  t.cylinder(0.06,0.9,"dark",o,-9.5,7.5,1.7);
  t.box(7.0,12.0,5.0,"top",o,10.0,6.0,-1.5);
  t.box(2.4,0.3,1.2,"dark",o,9.5,7.0,1.2);
  t.cylinder(0.06,0.9,"dark",o,9.5,7.5,1.7);
}
,"duomo-facade"(t,e,n){
  _D["barocco-duomo"](t,e,n);
}
,"cartello-salviamo-verde"(t,e,n){
  const o=oo(e,n,4.0);
  // The wooden signpost from the reference artwork
  // Stone base & small agave
  t.box(2.6,0.4,1.4,"cream",o,0,0.2,0);
  t.ball(0.5,0.3,0.5,"foliage",o,-0.9,0.4,0.4);
  // Two dark wooden upright posts
  t.box(0.18,2.8,0.18,"dark",o,-0.85,1.4,0);
  t.box(0.18,2.8,0.18,"dark",o,0.85,1.4,0);
  // Horizontal wooden sign board (dark timber planks)
  t.box(2.8,1.4,0.16,"rope",o,0,2.3,0.08);
  t.box(2.7,0.06,0.18,"dark",o,0,2.75,0.09);
  t.box(2.7,0.06,0.18,"dark",o,0,2.3,0.09);
  t.box(2.7,0.06,0.18,"dark",o,0,1.85,0.09);
  // White embossed letters: "SALVIAMO" / "IL VERDE" / "DI AUGUSTA"
  t.box(2.2,0.28,0.08,"cream",o,0,2.62,0.18);
  t.box(1.9,0.26,0.08,"foliage",o,0,2.28,0.18);
  t.box(2.1,0.24,0.08,"cream",o,0,1.94,0.18);
}
,"palma-augusta"(t,e,n){
  const o=oo(e,n,8.0);
  // Curved ringed Mediterranean palm trunk
  t.cylinder(0.42,6.0,"rope",o,0,3.0,0);
  for(let r=1;r<6;r++){
    t.cylinder(0.48,0.12,"dark",o,0,r*1.0,0);
  }
  // Fan fronds canopy
  t.ball(2.4,0.6,2.4,"foliage",o,0,6.2,0);
  t.ball(3.4,0.4,1.4,"foliage",o,1.2,6.0,0);
  t.ball(3.4,0.4,1.4,"foliage",o,-1.2,6.0,0);
  t.ball(1.4,0.4,3.4,"foliage",o,0,6.0,1.2);
  t.ball(1.4,0.4,3.4,"foliage",o,0,6.0,-1.2);
  // Golden dates
  t.ball(0.5,0.7,0.5,"gold",o,0.4,5.7,0.3);
  t.ball(0.4,0.6,0.4,"gold",o,-0.4,5.7,-0.3);
}
,"panchina-villa"(t,e,n){
  const o=oo(e,n,3.0);
  // Park bench with green cast-iron legs and wooden slats
  t.box(0.12,1.0,0.9,"moss",o,-1.2,0.5,0);
  t.box(0.12,1.0,0.9,"moss",o,1.2,0.5,0);
  t.cylinder(0.08,0.8,"dark",o,-1.2,0.85,0);
  t.cylinder(0.08,0.8,"dark",o,1.2,0.85,0);
  t.box(2.4,0.08,0.22,"rope",o,0,0.52,0.2);
  t.box(2.4,0.08,0.22,"rope",o,0,0.52,-0.05);
  t.box(2.4,0.18,0.08,"rope",o,0,0.82,-0.32);
  t.box(2.4,0.18,0.08,"rope",o,0,1.08,-0.36);
}
,"balustrata-xifonio"(t,e,n){
  const o=oo(e,n,4.0);
  // Coastal stone balustrade on the Gulf of Augusta
  t.box(3.8,0.35,0.6,"cream",o,0,0.18,0);
  for(let b=-2;b<=2;b++){
    t.cylinder(0.15,0.9,"cream",o,b*0.75,0.8,0);
    t.ball(0.22,0.22,0.22,"cream",o,b*0.75,0.7,0);
  }
  t.box(3.9,0.25,0.7,"cream",o,0,1.35,0);
}
,"vaso-terracotta-agave"(t,e,n){
  const o=oo(e,n,2.0);
  // Terracotta urn with succulent agave
  t.cylinder(0.5,0.8,"coral",o,0,0.4,0);
  t.cylinder(0.6,0.15,"orange",o,0,0.85,0);
  t.cylinder(0.52,0.08,"dark",o,0,0.88,0);
  t.ball(0.2,0.7,0.2,"foliage",o,0,1.3,0);
  t.ball(0.18,0.6,0.18,"foliage",o,0.35,1.15,0.2);
  t.ball(0.18,0.6,0.18,"foliage",o,-0.35,1.15,-0.2);
  t.ball(0.18,0.6,0.18,"foliage",o,-0.2,1.15,0.35);
  t.ball(0.18,0.6,0.18,"foliage",o,0.2,1.15,-0.35);
}
,"gozzo-xifonio"(t,e,n){
  const o=oo(e,n,5.0);
  // Sicilian wooden fishing boat on Golfo Xifonio
  t.box(3.8,1.0,1.6,"cream",o,0,0.5,0);
  t.box(3.85,0.3,1.65,"blue",o,0,0.85,0);
  t.box(3.9,0.15,0.15,"coral",o,0,0.2,0);
  t.cylinder(0.8,1.0,"cream",o,-1.9,0.5,0);
  t.cylinder(0.8,1.0,"cream",o,1.9,0.5,0);
  t.box(0.3,0.1,1.5,"rope",o,0,0.75,0);
  t.cylinder(0.06,3.2,"rope",o,0.3,1.0,0.5);
}
,"paletta-germoglio"(t,e,n){
  const o=oo(e,n,1.8);
  // Collectible golden trowel with sprouting green twig
  t.ball(0.9,0.9,0.9,"gold",o,0,0.6,0);
  t.box(0.35,0.5,0.08,"top",o,0,0.45,0);
  t.cylinder(0.08,0.5,"rope",o,0,0.1,0);
  t.cylinder(0.05,0.6,"rope",o,0,0.8,0);
  t.ball(0.2,0.12,0.25,"foliage",o,0.2,0.95,0.1);
  t.ball(0.2,0.12,0.25,"foliage",o,-0.2,1.05,-0.1);
  t.ball(0.18,0.10,0.22,"foliage",o,0,1.2,0);
}
,"cut-stump"(t,e,n){
  const o=oo(e,n,2.5);
  // Freshly cut tree stump
  t.cylinder(1.2,1.2,"rope",o,0,0.6,0);
  t.cylinder(1.15,0.06,"top",o,0,1.21,0);
  t.ball(1.6,0.15,1.6,"gold",o,0,0.08,0);
}
,"chainsaw"(t,e,n){
  const o=oo(e,n,2.0);
  // Motorized chainsaw hazard
  t.box(0.9,0.55,0.5,"orange",o,0,0.4,0);
  t.cylinder(0.06,0.6,"dark",o,-0.4,0.6,0);
  t.box(1.2,0.22,0.06,"dark",o,0.9,0.35,0);
  t.box(1.22,0.24,0.08,"gold",o,0.9,0.35,0);
}
,"waste-bin"(t,e,n){
  const o=oo(e,n,2.2);
  t.box(0.5,0.8,0.5,"rope",o,-0.8,0.4,0);
  t.box(0.5,0.8,0.5,"blue",o,-0.25,0.4,0);
  t.box(0.5,0.8,0.5,"gold",o,0.3,0.4,0);
  t.box(0.5,0.8,0.5,"foliage",o,0.85,0.4,0);
  t.box(0.52,0.08,0.52,"dark",o,-0.8,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,-0.25,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,0.3,0.84,0);
  t.box(0.52,0.08,0.52,"dark",o,0.85,0.84,0);
}
,"sewer-manhole"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.9,0.12,"dark",o,0,0.06,0);
  t.cylinder(0.75,0.08,"dark",o,0.1,0.25,0.1);
  t.cylinder(1.2,0.05,"blueLight",o,0,0.03,0);
  t.ball(0.4,0.5,0.4,"foliage",o,0,0.35,0);
}
,"stage-speaker"(t,e,n){
  const o=oo(e,n,4.5);
  t.box(1.4,3.2,1.2,"dark",o,0,1.6,0);
  for(let y of[0.6,1.3,2.0,2.7]){
    t.cylinder(0.24,0.05,"cream",o,0,y,0.61);
    t.cylinder(0.12,0.06,"dark",o,0,y,0.62);
  }
}
,"stage-light"(t,e,n){
  const o=oo(e,n,3.5);
  t.box(0.12,3.0,0.12,"dark",o,0,1.5,0);
  t.box(1.5,0.15,0.15,"dark",o,0,2.9,0);
  t.cylinder(0.2,0.35,"gold",o,-0.5,2.7,0.1);
  t.cylinder(0.2,0.35,"blueLight",o,0.5,2.7,0.1);
}
,"burning-tire"(t,e,n){
  const o=oo(e,n,2.8);
  t.cylinder(0.7,0.35,"dark",o,0,0.18,0);
  t.cylinder(0.65,0.35,"dark",o,0.4,0.45,0.1);
  t.ball(0.5,0.8,0.5,"gold",o,0.2,0.8,0);
  t.ball(0.35,0.6,0.35,"orange",o,-0.1,0.7,0.1);
  t.ball(0.8,0.7,0.8,"dark",o,0.1,1.5,0);
  t.ball(1.1,0.9,1.1,"dark",o,0.3,2.3,0);
}
,"cement-mixer"(t,e,n){
  const o=oo(e,n,4.0);
  t.box(1.6,1.4,1.4,"orange",o,-0.6,0.7,0);
  t.cylinder(0.9,1.8,"cream",o,0.7,1.2,0);
  t.box(2.2,0.1,1.8,"terrain2",o,0.5,0.05,0);
}
,"fountain-augusta"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(1.6,0.6,"cream",o,0,0.3,0);
  t.cylinder(1.45,0.1,"blueLight",o,0,0.55,0);
  t.cylinder(0.4,1.2,"cream",o,0,0.8,0);
  t.ball(0.6,0.3,0.6,"cream",o,0,1.4,0);
}
,"tree-sapling"(t,e,n){
  const o=oo(e,n,2.0);
  t.cylinder(0.06,1.8,"rope",o,0,0.9,0);
  t.cylinder(0.04,1.4,"top",o,0.12,0.7,0);
  t.ball(0.5,0.7,0.5,"foliage",o,0,1.7,0);
}
,"heat-wave"(t,e,n){
  const o=oo(e,n,3.5);
  t.ball(1.8,1.4,1.8,"orangeLight",o,0,1.0,0);
  t.ball(1.2,1.8,1.2,"gold",o,0,1.4,0);
}
"""'''

old_decor_marker = 'def get_gta_3d_decor_builders():'
end_decor_marker = 'def generate_gta_levels_code():'
idx_d1 = gen_code.find(old_decor_marker)
idx_d2 = gen_code.find(end_decor_marker)
if idx_d1 != -1 and idx_d2 != -1:
    gen_code = gen_code[:idx_d1] + new_decor_code + '\n\n' + gen_code[idx_d2:]
    print("Replaced 3D environmental decor models in generator!")

# 3. Handcraft Level 1 in generate_gta_levels_code()
level1_custom_code = '''def get_handcrafted_level_1():
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
    {x: -8, name: "1. L'Ingresso della Villa & Il Cartello Civico", landmark: "beacon"},
    {x: 48, name: "2. I Ficus Secolari (1850) & La Difesa dei Rami", landmark: "pulsedrum"},
    {x: 104, name: "3. Il Belvedere Panoramico sul Golfo Xifonio", landmark: "bannerarch"},
    {x: 165, name: "4. Il Viale delle Palme & L'Arresto delle Motoseghe", landmark: "sandwheel"},
    {x: 215, name: "5. Il Sagrato Barocco della Chiesa Madre", landmark: "bellgate"}
  ],
  platforms: [
    // Section 1: Ingresso della Villa & Cartello
    S("start", -8, 16, 13, "stone", {landmark: "beacon"}),
    S("plat-ficus-step1", 10, 4.0, 13.6, "stone"),
    S("plat-ficus-step2", 16, 6.5, 14.5, "stone"),
    S("step-roots", 24, 3.6, 15.6, "ledge"),
    S("lift-canopy", 29, 3.5, 14.8, "lift", {moveX: 2.8, period: 4.5}),
    S("plat-avenue", 34, 7.5, 15.2, "stone"),
    S("pit-spikes-1", 7, 38, 2.0, "stone", {spiked: !0}),

    // Section 2: Ficus Secolari & Chiome
    S("opt-sprout1", 42, 3.5, 18.0, "ledge", {optional: !0}),
    S("spring-branch1", 43, 2.0, 15.2, "spring"),
    S("dock-ficus-main", 48, 7, 15.2, "stone", {checkpoint: 50, depth: 22, landmark: "pulsedrum"}),
    S("crumble-bark", 57, 4.2, 14.8, "crumble"),
    S("plat-shaded", 63, 6, 14.2, "stone"),
    S("ferry-breeze", 71, 4.5, 13.8, "ferry", {travel: 18, speed: 3.2}),
    S("plat-seawall", 91, 7, 13.8, "stone"),
    S("pit-spikes-2", 50, 52, 2.0, "stone", {spiked: !0}),

    // Section 3: Belvedere sul Golfo Xifonio & Balustrata
    S("dock-belvedere", 104, 7, 11.2, "stone", {checkpoint: 106, depth: 22, landmark: "bannerarch"}),
    S("balance-terrace", 113, 7, 11.8, "balance"),
    S("step-parapet", 122, 3.8, 12.8, "ledge"),
    S("step-baluster", 126, 3.2, 15.5, "ledge"),
    S("balance-lookout", 128, 7.5, 13.8, "balance"),
    S("opt-sprout2", 133, 3.5, 18.8, "ledge", {optional: !0}),
    S("lift-gulf", 138, 3.6, 13.5, "lift", {moveY: 2.6, period: 4.0}),
    S("plat-irrigation", 145, 22, 16.2, "stone", {landmark: "beacon"}),
    S("switch-water", 153, 2.2, 16.35, "switch", {channel: "garden-water", latch: !0}),
    S("gate-duomo", 160, 1.8, 20.2, "gate", {channel: "garden-water", h: 4}),

    // Section 4: Viale delle Palme & Stop Motoseghe
    S("dock-palms", 165, 7, 16.2, "stone", {checkpoint: 167, depth: 22, landmark: "sandwheel"}),
    S("pulse-stump1", 174, 3.8, 15.6, "pulse", {period: 4.2, phase: 0}),
    S("pulse-stump2", 180, 3.8, 15.6, "pulse", {period: 4.2, phase: 0.5}),
    S("plat-fountain", 186, 6, 14.8, "stone"),
    S("step-piazza1", 197, 3.2, 18.2, "ledge"),
    S("lift-pergola", 194, 3.6, 14.2, "lift", {moveX: 2.6, moveY: 1.8, period: 5.0}),
    S("opt-sprout3", 202, 3.5, 20.8, "ledge", {optional: !0}),
    S("spring-piazza", 203, 2.0, 15.8, "spring"),
    S("plat-terrace-piazza", 201, 8, 15.8, "stone", {landmark: "sandwheel"}),
    S("pit-spikes-3", 167, 45, 4.0, "stone", {spiked: !0}),

    // Section 5: Piazza Duomo & Sagrato della Chiesa Madre Barocca
    S("dock-duomo-approach", 213, 7, 15.8, "stone", {checkpoint: 215, depth: 22, landmark: "bellgate"}),
    S("step-duomo1", 222, 3.8, 16.8, "ledge"),
    S("step-duomo2", 228, 4.2, 17.8, "ledge"),
    S("goal-duomo", 234, 15, 18.8, "stone", {landmark: "bellgate", goal: !0, checkpoint: 236})
  ],
  decor: [
    // Entrance: Signpost "SALVIAMO IL VERDE DI AUGUSTA", benches, agaves, palms
    {kind: "cartello-salviamo-verde", x: 4.5, y: 13.0, size: 4.0, z: -1.8},
    {kind: "panchina-villa", x: 9.0, y: 13.0, size: 3.0, z: -1.5},
    {kind: "vaso-terracotta-agave", x: 14.0, y: 14.5, size: 2.2, z: -1.2},
    {kind: "palma-augusta", x: 20.0, y: 14.5, size: 8.5, z: -3.5},

    // Grand Ficus trees with aerial roots & chainsaw/stump hazards
    {kind: "ficus-centenario", x: 54.0, y: 15.2, size: 14.0, z: -4.0},
    {kind: "cut-stump", x: 62.0, y: 14.2, size: 3.0, z: -2.0},
    {kind: "chainsaw", x: 66.0, y: 14.2, size: 2.5, z: -1.8},
    {kind: "panchina-villa", x: 74.0, y: 13.8, size: 3.0, z: -1.5},
    {kind: "ficus-centenario", x: 88.0, y: 13.8, size: 13.0, z: -4.2},

    // Gulf of Xifonio Belvedere: balustrade, agaves, and fishing boats on the sea
    {kind: "balustrata-xifonio", x: 108.0, y: 11.2, size: 4.5, z: -2.5},
    {kind: "gozzo-xifonio", x: 118.0, y: 8.0, size: 5.5, z: -10.0},
    {kind: "vaso-terracotta-agave", x: 124.0, y: 12.8, size: 2.2, z: -1.2},
    {kind: "palma-augusta", x: 130.0, y: 13.8, size: 8.5, z: -3.5},
    {kind: "gozzo-xifonio", x: 142.0, y: 7.5, size: 5.0, z: -12.0},

    // Palms Avenue, irrigation switch & heat wave
    {kind: "cut-stump", x: 168.0, y: 16.2, size: 3.0, z: -2.0},
    {kind: "chainsaw", x: 172.0, y: 16.2, size: 2.5, z: -1.8},
    {kind: "heat-wave", x: 178.0, y: 15.6, size: 3.5, z: -1.5},
    {kind: "fountain-augusta", x: 190.0, y: 14.8, size: 4.0, z: -2.5},
    {kind: "palma-augusta", x: 196.0, y: 15.8, size: 9.0, z: -3.5},
    {kind: "cartello-salviamo-verde", x: 206.0, y: 15.8, size: 3.8, z: -1.8},

    // Grand Baroque Piazza Duomo Finish: Chiesa Madre, benches, agaves, new saplings
    {kind: "barocco-duomo", x: 236.0, y: 18.8, size: 18.0, z: -4.5},
    {kind: "vaso-terracotta-agave", x: 226.0, y: 17.8, size: 2.5, z: -1.5},
    {kind: "panchina-villa", x: 230.0, y: 18.8, size: 3.0, z: -1.5},
    {kind: "tree-sapling", x: 242.0, y: 18.8, size: 2.5, z: -1.5}
  ],
  stamps: [
    {x: 42.5, y: 19.5},
    {x: 133.5, y: 20.5},
    {x: 202.5, y: 22.5}
  ],
  coins: [
    {x: 12, y: 15.2},
    {x: 18, y: 16.0},
    {x: 25, y: 17.0},
    {x: 35, y: 16.8},
    {x: 43, y: 16.5},
    {x: 60, y: 16.2},
    {x: 65, y: 15.6},
    {x: 75, y: 15.2},
    {x: 82, y: 15.2},
    {x: 94, y: 15.2},
    {x: 115, y: 13.2},
    {x: 124, y: 14.2},
    {x: 130, y: 15.2},
    {x: 135, y: 15.2},
    {x: 150, y: 17.6},
    {x: 157, y: 17.6},
    {x: 176, y: 17.2},
    {x: 182, y: 17.2},
    {x: 188, y: 16.2},
    {x: 205, y: 17.2},
    {x: 224, y: 18.2},
    {x: 230, y: 19.2}
  ],
  hazards: [
    {x: 57, y: 14.8, w: 4.2, h: 0.5, kind: "crumble"},
    {x: 174, y: 15.6, w: 3.8, h: 0.5, kind: "pulse"},
    {x: 180, y: 15.6, w: 3.8, h: 0.5, kind: "pulse"}
  ],
  hints: [
    {x: 3, title: "Villa Comunale di Augusta (1850)", text: "Fondata dal generale Micheroux sulla Piazza d'Armi. I grandi Ficus secolari proteggono la citta dalle bolle di calore!", icon: "info"},
    {x: 52, title: "I Ficus Monumentali", text: "Le radici aeree del Ficus formano una cattedrale viva. Salta sui rami ed evita le motoseghe che abbattono gli alberi!", icon: "alert-triangle"},
    {x: 108, title: "Belvedere sul Golfo Xifonio", text: "Dalla balconata della Villa si scorge il mare ionico e i gozzi dei pescatori. Raccogli il secondo germoglio dorato!", icon: "compass"},
    {x: 150, title: "La Valvola Idraulica dei Giardini", text: "Premi l'interruttore della condotta per innaffiare le radici secolari e aprire la cancellata di Piazza Duomo!", icon: "check-circle"},
    {x: 218, title: "Piazza Duomo & Chiesa Madre (1769)", text: "Sei arrivato al Duomo barocco di Santa Maria Assunta! Pianta il germoglio al centro del sagrato per celebrare la rinascita verde!", icon: "sun"}
  ]
});"""
'''

# Update generate_gta_levels_code to use get_handcrafted_level_1
if "def get_handcrafted_level_1():" not in gen_code:
    gen_code = level1_custom_code + "\n\n" + gen_code
    gen_code = gen_code.replace("l1 = get_level_1()", "l1 = get_handcrafted_level_1()\n    levels.append(l1)\n    # L1 Handcrafted done\n    if False:")
    print("Injected handcrafted Level 1 into generator!")

with open("tools/generate_gta_game.py", "w", encoding="utf-8") as f:
    f.write(gen_code)

print("Updated tools/generate_gta_game.py successfully!")
