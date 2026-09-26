# tools/apply_perfect_gta.py
import re

with open("bundle/index-gta-v1.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# -------------------------------------------------------------------
# 1. REMOVE LANDMARK "beacon" FROM LEVEL 1 TO PREVENT BLUE CLAY DRUM
# -------------------------------------------------------------------
bundle = bundle.replace('S("start", -8, 16, 13, "stone", {landmark: "beacon"})', 'S("start", -8, 16, 13, "stone")')
bundle = bundle.replace('S("start", -8, 16, 13, "stone", {landmark: "beacon"})', 'S("start", -8, 16, 13, "stone")')
bundle = bundle.replace('{x: -8, name: "1. L\'Ingresso della Villa & Il Cartello Civico", landmark: "beacon"}', '{x: -8, name: "1. L\'Ingresso della Villa & Il Cartello Civico"}')
print("Removed landmark beacon from Level 1 spawn!")

# -------------------------------------------------------------------
# 2. IMPLEMENT 100% FAITHFUL GIUSEPPE 3D CLAY MODEL
# -------------------------------------------------------------------
giuseppe_faithful_code = '''function applyGiuseppeCustomization(scene, choice) {
  if (!choice || (choice.id !== "giuseppe" && choice.id !== "baldu" && choice.id !== "explorer")) return;
  const head = scene.getObjectByName("Head");
  if (!head || head.getObjectByName("giuseppe-head-root")) return;

  // 1. COMPLETELY HIDE the legacy anime explorer model
  scene.traverse(p => {
    if (p.isMesh && (p.name === "explorer" || p.name === "explorer-mesh" || p.isSkinnedMesh)) {
      p.visible = false;
      p.castShadow = false;
      p.receiveShadow = false;
    }
  });

  // 2. Proportions & Materials: Authentic Stop-Motion Claymation (Aardman style)
  const skinMat = new Ce({color: 0xf2be9e, roughness: 0.88, metalness: 0});
  const lipsMat = new Ce({color: 0xd87a70, roughness: 0.75, metalness: 0});
  const mouthDarkMat = new Ce({color: 0x3d1212, roughness: 0.9, metalness: 0});
  const teethMat = new Ce({color: 0xffffff, roughness: 0.3, metalness: 0});
  const eyeWhiteMat = new Ce({color: 0xffffff, roughness: 0.2, metalness: 0});
  const pupilMat = new Ce({color: 0x1f140e, roughness: 0.3, metalness: 0});
  const browMat = new Ce({color: 0x3d2719, roughness: 0.9, metalness: 0});

  // Bold black glasses
  const frameMat = new Ce({color: 0x111111, roughness: 0.25, metalness: 0.15});
  const lensMat = new Ce({color: 0xffffff, roughness: 0.05, metalness: 0.1, transparent: true, opacity: 0.35});

  // Sky-blue button-down shirt
  const shirtMat = new Ce({color: 0x72aadc, roughness: 0.86, metalness: 0});
  const buttonMat = new Ce({color: 0xfafafa, roughness: 0.25, metalness: 0.3});

  // Dark charcoal trousers & belt
  const pantsMat = new Ce({color: 0x222a36, roughness: 0.88, metalness: 0});
  const beltMat = new Ce({color: 0x1c1510, roughness: 0.85, metalness: 0});
  const buckleMat = new Ce({color: 0xd5d8dc, roughness: 0.2, metalness: 0.75});
  const shoeMat = new Ce({color: 0x161514, roughness: 0.82, metalness: 0});

  // Gardening Trowel & Living Green Sprout
  const woodMat = new Ce({color: 0x9b5a28, roughness: 0.82, metalness: 0});
  const metalMat = new Ce({color: 0xd0d5dd, roughness: 0.22, metalness: 0.75});
  const leafMat = new Ce({color: 0x389a24, roughness: 0.78, metalness: 0});
  const twigMat = new Ce({color: 0x6e4624, roughness: 0.85, metalness: 0});

  // Leather Wristwatch
  const strapMat = new Ce({color: 0x482816, roughness: 0.82, metalness: 0});
  const dialMat = new Ce({color: 0xffffff, roughness: 0.25, metalness: 0.15});
  const watchCaseMat = new Ce({color: 0xcccccc, roughness: 0.2, metalness: 0.8});

  // Slight 3/4 turn towards the camera (22 degrees) so face, glasses, smile and trowel are always clearly visible!
  const charMount = scene.parent;
  if (charMount && charMount.name === "Normalized custom character") {
    charMount.rotation.y = -0.38;
  }

  // -----------------------------------------------------------
  // A. HEAD & FACIAL FEATURES (Attached to Head bone)
  // Scale: 1.35x for bold, expressive claymation character
  // -----------------------------------------------------------
  const headGroup = new U();
  headGroup.name = "giuseppe-head-root";
  headGroup.scale.setScalar(1.35);

  // 1. Smooth Bald Scalp (Egg/Pear shaped clay cranium)
  const scalp = new De(new $t(1, 24, 20), skinMat);
  scalp.position.set(0, 0.28, 0.03);
  scalp.scale.set(0.23, 0.265, 0.235);
  headGroup.add(scalp);

  // Cheeks (plump, smiling clay cheeks)
  const cheekL = new De(new $t(1, 14, 12), skinMat);
  cheekL.position.set(-0.135, 0.21, 0.16);
  cheekL.scale.set(0.095, 0.095, 0.085);
  const cheekR = new De(new $t(1, 14, 12), skinMat);
  cheekR.position.set(0.135, 0.21, 0.16);
  cheekR.scale.set(0.095, 0.095, 0.085);
  headGroup.add(cheekL, cheekR);

  // Rounded friendly chin
  const chin = new De(new $t(1, 14, 12), skinMat);
  chin.position.set(0, 0.12, 0.14);
  chin.scale.set(0.12, 0.095, 0.12);
  headGroup.add(chin);

  // Ears
  const earL = new De(new $t(1, 12, 10), skinMat);
  earL.position.set(-0.235, 0.26, 0.02);
  earL.scale.set(0.045, 0.085, 0.06);
  const earR = new De(new $t(1, 12, 10), skinMat);
  earR.position.set(0.235, 0.26, 0.02);
  earR.scale.set(0.045, 0.085, 0.06);
  headGroup.add(earL, earR);

  // Friendly rounded nose
  const nose = new De(new $t(1, 14, 12), skinMat);
  nose.position.set(0, 0.26, 0.25);
  nose.scale.set(0.075, 0.075, 0.085);
  headGroup.add(nose);

  // Eyebrows (warm arched brown clay)
  const browL = new De(new os(0.07, 0.018, 0.02, 2, 0.005), browMat);
  browL.position.set(-0.085, 0.36, 0.22);
  browL.rotation.z = -0.16;
  const browR = new De(new os(0.07, 0.018, 0.02, 2, 0.005), browMat);
  browR.position.set(0.085, 0.36, 0.22);
  browR.rotation.z = 0.16;
  headGroup.add(browL, browR);

  // Eyes (White clay eyeballs + dark pupils + specular highlight)
  for (const side of [-1, 1]) {
    const eyeX = side * 0.085;
    const eye = new De(new $t(0.048, 16, 12), eyeWhiteMat);
    eye.position.set(eyeX, 0.295, 0.205);
    const pupil = new De(new $t(0.025, 12, 10), pupilMat);
    pupil.position.set(eyeX, 0.295, 0.245);
    const specular = new De(new $t(0.008, 8, 6), eyeWhiteMat);
    specular.position.set(eyeX - side * 0.008, 0.305, 0.262);
    headGroup.add(eye, pupil, specular);
  }

  // 2. Thick Black Rounded Glasses (Identical to reference image)
  const glasses = new U();
  glasses.position.set(0, 0.295, 0.245);
  const frameW = 0.075, frameH = 0.058, thick = 0.014;
  for (const side of [-1, 1]) {
    const gx = side * 0.085;
    const fTop = new De(new os(frameW*2, thick, 0.02, 2, 0.003), frameMat);
    fTop.position.set(gx, frameH, 0);
    const fBot = new De(new os(frameW*2, thick, 0.02, 2, 0.003), frameMat);
    fBot.position.set(gx, -frameH, 0);
    const fL = new De(new os(thick, frameH*2, 0.02, 2, 0.003), frameMat);
    fL.position.set(gx - frameW, 0, 0);
    const fR = new De(new os(thick, frameH*2, 0.02, 2, 0.003), frameMat);
    fR.position.set(gx + frameW, 0, 0);
    const lens = new De(new an(frameW*1.8, frameH*1.8), lensMat);
    lens.position.set(gx, 0, 0.002);
    glasses.add(fTop, fBot, fL, fR, lens);

    // Temple arms going back to ears
    const arm = new De(new os(0.009, 0.013, 0.25, 2, 0.002), frameMat);
    arm.position.set(gx + side * (frameW - 0.005), 0.01, -0.11);
    arm.rotation.y = -side * 0.12;
    glasses.add(arm);
  }
  // Bridge connecting rims over nose
  const gBridge = new De(new os(0.045, 0.016, 0.018, 2, 0.004), frameMat);
  gBridge.position.set(0, 0.01, 0.002);
  glasses.add(gBridge);
  headGroup.add(glasses);

  // 3. Cheerful Radiant Smile with Upper White Teeth
  const mouthGroup = new U();
  mouthGroup.position.set(0, 0.175, 0.22);
  const mouthBg = new De(new os(0.13, 0.05, 0.02, 2, 0.008), mouthDarkMat);
  mouthGroup.add(mouthBg);
  // White upper teeth row
  const teeth = new De(new os(0.11, 0.025, 0.018, 2, 0.004), teethMat);
  teeth.position.set(0, 0.014, 0.008);
  mouthGroup.add(teeth);
  // Lips
  const lipUp = new De(new os(0.135, 0.013, 0.016, 2, 0.004), lipsMat);
  lipUp.position.set(0, 0.028, 0.007);
  const lipDown = new De(new os(0.12, 0.015, 0.016, 2, 0.004), lipsMat);
  lipDown.position.set(0, -0.024, 0.007);
  mouthGroup.add(lipUp, lipDown);
  headGroup.add(mouthGroup);

  head.add(headGroup);

  // -----------------------------------------------------------
  // B. NECK (Attached to Neck bone)
  // -----------------------------------------------------------
  const neckBone = scene.getObjectByName("Neck");
  if (neckBone) {
    const neckMesh = new De(new li(0.13, 0.14, 0.14, 14), skinMat);
    neckMesh.position.set(0, 0.05, 0);
    neckBone.add(neckMesh);
  }

  // -----------------------------------------------------------
  // C. UPPER TORSO & OPEN COLLAR SKY-BLUE SHIRT (Attached to Spine2)
  // -----------------------------------------------------------
  const spine2 = scene.getObjectByName("Spine2");
  if (spine2) {
    const chestGroup = new U();
    // Sky-blue shirt chest volume
    const chest = new De(new os(0.48, 0.26, 0.35, 4, 0.04), shirtMat);
    chest.position.set(0, 0.08, 0.02);
    chestGroup.add(chest);

    // V-neck cutout exposing upper clay neck/chest
    const neckCutout = new De(new os(0.18, 0.18, 0.10, 2, 0.01), skinMat);
    neckCutout.position.set(0, 0.14, 0.16);
    chestGroup.add(neckCutout);

    // Collar lapels spread open
    const lapelL = new De(new os(0.10, 0.12, 0.028, 2, 0.008), shirtMat);
    lapelL.position.set(-0.10, 0.11, 0.195);
    lapelL.rotation.set(0.32, 0.26, -0.38);
    const lapelR = new De(new os(0.10, 0.12, 0.028, 2, 0.008), shirtMat);
    lapelR.position.set(0.10, 0.11, 0.195);
    lapelR.rotation.set(0.32, -0.26, 0.38);
    chestGroup.add(lapelL, lapelR);

    // Mother-of-pearl buttons down front placket
    for (let b = 0; b < 2; b++) {
      const btn = new De(new li(0.016, 0.016, 0.01, 10), buttonMat);
      btn.position.set(0, 0.02 - b * 0.09, 0.20);
      btn.rotation.x = Math.PI / 2;
      chestGroup.add(btn);
    }
    spine2.add(chestGroup);
  }

  // -----------------------------------------------------------
  // D. MID TORSO / BELLY (Attached to Spine)
  // -----------------------------------------------------------
  const spine = scene.getObjectByName("Spine");
  if (spine) {
    const bellyGroup = new U();
    const belly = new De(new os(0.46, 0.24, 0.33, 4, 0.035), shirtMat);
    belly.position.set(0, 0.06, 0.02);
    bellyGroup.add(belly);

    const btn = new De(new li(0.016, 0.016, 0.01, 10), buttonMat);
    btn.position.set(0, 0.04, 0.19);
    btn.rotation.x = Math.PI / 2;
    bellyGroup.add(btn);

    spine.add(bellyGroup);
  }

  // -----------------------------------------------------------
  // E. HIPS, BELT & BUCKLE (Attached to Hips bone)
  // -----------------------------------------------------------
  const hips = scene.getObjectByName("Hips");
  if (hips) {
    const hipsGroup = new U();
    // Pelvis in dark charcoal trousers
    const pelvis = new De(new os(0.44, 0.20, 0.30, 4, 0.03), pantsMat);
    pelvis.position.set(0, -0.04, 0.01);
    hipsGroup.add(pelvis);

    // Dark leather belt around waist
    const belt = new De(new os(0.455, 0.06, 0.315, 3, 0.015), beltMat);
    belt.position.set(0, 0.03, 0.01);
    hipsGroup.add(belt);

    // Silver metal buckle at center front
    const buckle = new De(new os(0.095, 0.07, 0.026, 2, 0.005), buckleMat);
    buckle.position.set(0, 0.03, 0.175);
    const buckleHole = new De(new os(0.05, 0.038, 0.03, 1, 0.002), beltMat);
    buckleHole.position.set(0, 0.03, 0.175);
    hipsGroup.add(buckle, buckleHole);

    hips.add(hipsGroup);
  }

  // -----------------------------------------------------------
  // F. ARMS, SHORT SLEEVES, WRISTWATCH & TROWEL
  // -----------------------------------------------------------
  const leftArm = scene.getObjectByName("LeftArm");
  if (leftArm) {
    const sleeveL = new De(new li(0.105, 0.098, 0.15, 12), shirtMat);
    sleeveL.position.set(0, 0.07, 0);
    leftArm.add(sleeveL);
  }
  const rightArm = scene.getObjectByName("RightArm");
  if (rightArm) {
    const sleeveR = new De(new li(0.105, 0.098, 0.15, 12), shirtMat);
    sleeveR.position.set(0, 0.07, 0);
    rightArm.add(sleeveR);
  }

  // Left Forearm (skin tone + WRISTWATCH)
  const leftForeArm = scene.getObjectByName("LeftForeArm");
  if (leftForeArm) {
    const armL = new De(new li(0.082, 0.072, 0.17, 12), skinMat);
    armL.position.set(0, 0.08, 0);
    leftForeArm.add(armL);

    // WRISTWATCH on left wrist (matching reference)
    const watchGroup = new U();
    watchGroup.position.set(0, 0.14, 0);
    const strap = new De(new li(0.080, 0.080, 0.035, 14), strapMat);
    watchGroup.add(strap);
    const wCase = new De(new li(0.042, 0.042, 0.02, 14), watchCaseMat);
    wCase.position.set(0, 0, 0.08);
    wCase.rotation.x = Math.PI / 2;
    const wDial = new De(new li(0.035, 0.035, 0.006, 14), dialMat);
    wDial.position.set(0, 0, 0.092);
    wDial.rotation.x = Math.PI / 2;
    watchGroup.add(wCase, wDial);
    leftForeArm.add(watchGroup);
  }

  const leftHand = scene.getObjectByName("LeftHand");
  if (leftHand) {
    const handL = new De(new $t(1, 10, 8), skinMat);
    handL.position.set(0, 0.08, 0);
    handL.scale.set(0.07, 0.09, 0.055);
    leftHand.add(handL);
  }

  const rightForeArm = scene.getObjectByName("RightForeArm");
  if (rightForeArm) {
    const armR = new De(new li(0.082, 0.072, 0.17, 12), skinMat);
    armR.position.set(0, 0.08, 0);
    rightForeArm.add(armR);
  }

  // Right Hand & GARDENING TROWEL WITH LIVING SPROUT
  const rightHand = scene.getObjectByName("RightHand");
  if (rightHand) {
    const handR = new De(new $t(1, 10, 8), skinMat);
    handR.position.set(0, 0.08, 0);
    handR.scale.set(0.07, 0.09, 0.055);
    rightHand.add(handR);

    // TROWEL PROP (Identical to reference artwork)
    const trowelProp = new U();
    trowelProp.name = "giuseppe-trowel-prop";
    trowelProp.position.set(0.05, 0.10, 0.06);
    trowelProp.rotation.set(-0.35, 0.25, 0.45);
    trowelProp.scale.setScalar(1.25);

    // Wooden handle
    const handle = new De(new li(0.028, 0.024, 0.20, 10), woodMat);
    handle.position.set(0, -0.07, 0);
    trowelProp.add(handle);

    // Metal neck
    const neckMetal = new De(new li(0.018, 0.018, 0.07, 8), metalMat);
    neckMetal.position.set(0, 0.06, 0.018);
    neckMetal.rotation.x = -0.4;
    trowelProp.add(neckMetal);

    // Pointed metal scoop blade
    const scoop = new De(new os(0.12, 0.22, 0.022, 3, 0.005), metalMat);
    scoop.position.set(0, 0.17, 0.05);
    scoop.rotation.x = -0.3;
    trowelProp.add(scoop);

    // LIVING GREEN CLAY SPROUT (wooden twig + 3 green leaves)
    const sproutGroup = new U();
    sproutGroup.position.set(0, 0.18, 0.07);

    const twig = new De(new li(0.015, 0.011, 0.18, 8), twigMat);
    twig.position.set(0, 0.08, 0);
    sproutGroup.add(twig);

    const leafTop = new De(new $t(1, 10, 8), leafMat);
    leafTop.position.set(0, 0.18, 0.01);
    leafTop.scale.set(0.04, 0.075, 0.014);
    leafTop.rotation.x = -0.3;
    sproutGroup.add(leafTop);

    const leafL = new De(new $t(1, 10, 8), leafMat);
    leafL.position.set(-0.05, 0.12, 0);
    leafL.scale.set(0.036, 0.065, 0.014);
    leafL.rotation.set(0.2, 0, 0.7);
    sproutGroup.add(leafL);

    const leafR = new De(new $t(1, 10, 8), leafMat);
    leafR.position.set(0.05, 0.10, 0);
    leafR.scale.set(0.036, 0.065, 0.014);
    leafR.rotation.set(-0.2, 0, -0.7);
    sproutGroup.add(leafR);

    trowelProp.add(sproutGroup);
    rightHand.add(trowelProp);
  }

  // -----------------------------------------------------------
  // G. LEGS & SHOES
  // -----------------------------------------------------------
  const leftUpLeg = scene.getObjectByName("LeftUpLeg");
  if (leftUpLeg) {
    const thighL = new De(new li(0.12, 0.105, 0.24, 12), pantsMat);
    thighL.position.set(0, 0.10, 0);
    leftUpLeg.add(thighL);
  }
  const leftLeg = scene.getObjectByName("LeftLeg");
  if (leftLeg) {
    const calfL = new De(new li(0.105, 0.095, 0.22, 12), pantsMat);
    calfL.position.set(0, 0.10, 0);
    leftLeg.add(calfL);
  }
  const leftFoot = scene.getObjectByName("LeftFoot");
  if (leftFoot) {
    const shoeL = new De(new os(0.13, 0.09, 0.24, 3, 0.02), shoeMat);
    shoeL.position.set(0, 0.04, 0.07);
    leftFoot.add(shoeL);
  }

  const rightUpLeg = scene.getObjectByName("RightUpLeg");
  if (rightUpLeg) {
    const thighR = new De(new li(0.12, 0.105, 0.24, 12), pantsMat);
    thighR.position.set(0, 0.10, 0);
    rightUpLeg.add(thighR);
  }
  const rightLeg = scene.getObjectByName("RightLeg");
  if (rightLeg) {
    const calfR = new De(new li(0.105, 0.095, 0.22, 12), pantsMat);
    calfR.position.set(0, 0.10, 0);
    rightLeg.add(calfR);
  }
  const rightFoot = scene.getObjectByName("RightFoot");
  if (rightFoot) {
    const shoeR = new De(new os(0.13, 0.09, 0.24, 3, 0.02), shoeMat);
    shoeR.position.set(0, 0.04, 0.07);
    rightFoot.add(shoeR);
  }
}
'''

start_custom = bundle.find('function applyGiuseppeCustomization')
if start_custom != -1:
    idx = bundle.find('{', start_custom)
    depth = 1
    i = idx + 1
    while depth > 0 and i < len(bundle):
        if bundle[i] == '{': depth += 1
        elif bundle[i] == '}': depth -= 1
        i += 1
    bundle = bundle[:start_custom] + giuseppe_faithful_code + bundle[i:]
    print("Replaced applyGiuseppeCustomization with 100% faithful 3D clay model!")

# -------------------------------------------------------------------
# 3. BUILD AUTHENTIC AUGUSTA DIORAMA BACKDROP (Duomo, Ficus, Sea, Sign)
# -------------------------------------------------------------------
augusta_backdrop_func = '''function buildAugustaBackdrop(world, level) {
  const root = world.backRoot;
  const augustaGroup = new U();
  augustaGroup.name = "Augusta Authentic Diorama Backdrop";

  // A. Deep Mediterranean Azure Sky & Radiant Golden Sun
  const sunGroup = new U();
  sunGroup.position.set(16, 22, -32);
  const sunCore = new De(new $t(3.8, 20, 16), new Ce({color: 0xffeb77, emissive: 0xffd233, emissiveIntensity: 0.85, roughness: 0.2}));
  sunGroup.add(sunCore);
  for (let r = 0; r < 8; r++) {
    const ray = new De(new os(0.55, 3.2, 0.2, 2, 0.05), new Ce({color: 0xfff0aa, roughness: 0.3}));
    const ang = r * Math.PI / 4;
    ray.position.set(Math.cos(ang) * 5.8, Math.sin(ang) * 5.8, 0);
    ray.rotation.z = ang;
    sunGroup.add(ray);
  }
  augustaGroup.add(sunGroup);

  // Soft white clay clouds
  const cloudCoords = [[-6, 21, -30, 1.2], [10, 23, -33, 1.4], [32, 21, -32, 1.1], [65, 23, -34, 1.3]];
  const cloudMat = new Ce({color: 0xffffff, roughness: 0.92, metalness: 0});
  for (const [cx, cy, cz, cs] of cloudCoords) {
    const cl = new U();
    cl.position.set(cx, cy, cz);
    cl.scale.setScalar(cs);
    const b1 = new De(new $t(2.8, 16, 12), cloudMat);
    const b2 = new De(new $t(2.2, 14, 10), cloudMat); b2.position.set(-1.8, -0.4, 0.2);
    const b3 = new De(new $t(2.4, 14, 10), cloudMat); b3.position.set(1.9, -0.3, -0.1);
    cl.add(b1, b2, b3);
    augustaGroup.add(cl);
  }

  // B. Sparkling Golfo Xifonio (Azure Sea Plane)
  const seaMat = new Ce({color: 0x196eb8, roughness: 0.35, metalness: 0.1});
  const sea = new De(new an(280, 26), seaMat);
  sea.position.set(60, 6, -28);
  sea.rotation.x = -Math.PI / 2.35;
  augustaGroup.add(sea);

  // Traditional Sicilian fishing boats (Gozzi) on the bay
  const boatCoords = [[3, 7.0, -25, 0x1d70b8], [12, 6.6, -27, 0xd83a3a], [28, 6.8, -26, 0xf0b828], [55, 6.4, -28, 0x228833]];
  for (const [bx, by, bz, bcol] of boatCoords) {
    const boat = new U();
    boat.position.set(bx, by, bz);
    const hull = new De(new os(2.4, 0.55, 0.9, 2, 0.08), new Ce({color: bcol, roughness: 0.8}));
    hull.position.y = 0.25;
    const mast = new De(new li(0.045, 0.045, 2.4, 8), new Ce({color: 0x885533, roughness: 0.8}));
    mast.position.set(0, 1.3, 0);
    boat.add(hull, mast);
    augustaGroup.add(boat);
  }

  // C. BAROQUE DUOMO DI AUGUSTA (Chiesa Madre Santa Maria Assunta)
  // Majestically framed on the left of spawn (x = -4, y = 11, z = -18)
  const duomoGroup = new U();
  duomoGroup.name = "Duomo di Augusta Facciata Barocca";
  duomoGroup.position.set(-3.5, 11, -18);

  const stoneMat = new Ce({color: 0xd49b56, roughness: 0.85, metalness: 0});
  const stoneShadeMat = new Ce({color: 0xb57c3d, roughness: 0.88, metalness: 0});
  const doorWoodMat = new Ce({color: 0x4a2a16, roughness: 0.85, metalness: 0});
  const bellBronzeMat = new Ce({color: 0xbfa040, roughness: 0.3, metalness: 0.7});
  const crossMat = new Ce({color: 0xf5f5f5, roughness: 0.2, metalness: 0.4});

  // Base tier facade block
  const tier1 = new De(new os(13, 9.5, 3.2, 3, 0.15), stoneMat);
  tier1.position.set(0, 4.75, 0);
  duomoGroup.add(tier1);

  // Grand Portale Maggiore (central portal)
  const portalArch = new De(new os(3.2, 5.8, 0.4, 2, 0.1), stoneShadeMat);
  portalArch.position.set(0, 3.0, 1.7);
  const portalDoor = new De(new os(2.4, 4.8, 0.3, 2, 0.05), doorWoodMat);
  portalDoor.position.set(0, 2.6, 1.75);
  const portalPediment = new De(new os(3.8, 0.75, 0.55, 2, 0.05), stoneMat);
  portalPediment.position.set(0, 6.2, 1.8);
  duomoGroup.add(portalArch, portalDoor, portalPediment);

  // Side portals
  for (const side of [-1, 1]) {
    const sPortal = new De(new os(1.7, 3.6, 0.3, 2, 0.05), doorWoodMat);
    sPortal.position.set(side * 4.3, 2.0, 1.7);
    duomoGroup.add(sPortal);
  }

  // 6 Corinthian pilasters on tier 1
  for (let p = 0; p < 6; p++) {
    const px = -5.4 + p * 2.16;
    const pilaster = new De(new os(0.52, 9.2, 0.38, 2, 0.04), stoneMat);
    pilaster.position.set(px, 4.8, 1.75);
    duomoGroup.add(pilaster);
  }

  // Entablature cornice
  const cornice1 = new De(new os(14.2, 1.0, 3.8, 2, 0.08), stoneMat);
  cornice1.position.set(0, 9.8, 0);
  duomoGroup.add(cornice1);

  // Tier 2 with large Baroque scroll volutes
  const tier2 = new De(new os(8.6, 7.0, 2.8, 3, 0.12), stoneMat);
  tier2.position.set(0, 13.8, 0);
  duomoGroup.add(tier2);

  // Volutes
  for (const side of [-1, 1]) {
    const volute = new De(new os(2.0, 4.8, 0.7, 3, 0.2), stoneMat);
    volute.position.set(side * 5.2, 12.4, 0.7);
    volute.rotation.z = side * 0.35;
    duomoGroup.add(volute);
  }

  // Central baroque window
  const win2 = new De(new os(2.0, 3.4, 0.3, 2, 0.06), stoneShadeMat);
  win2.position.set(0, 13.6, 1.45);
  duomoGroup.add(win2);

  // Belfry with 3 arches & bronze bells
  const belfry = new De(new os(6.0, 3.8, 2.0, 2, 0.1), stoneMat);
  belfry.position.set(0, 19.0, 0);
  duomoGroup.add(belfry);

  for (let b = 0; b < 3; b++) {
    const bx = -1.6 + b * 1.6;
    const bArch = new De(new os(1.0, 2.4, 0.45, 2, 0.04), stoneShadeMat);
    bArch.position.set(bx, 18.8, 1.0);
    const bell = new De(new li(0.28, 0.14, 0.55, 12), bellBronzeMat);
    bell.position.set(bx, 19.0, 1.0);
    duomoGroup.add(bArch, bell);
  }

  // Summit Pediment & Latin Cross
  const pediment = new De(new os(6.2, 1.3, 2.2, 2, 0.08), stoneMat);
  pediment.position.set(0, 21.4, 0);
  const crossV = new De(new os(0.18, 2.2, 0.18, 1, 0.02), crossMat);
  crossV.position.set(0, 23.0, 0);
  const crossH = new De(new os(1.3, 0.18, 0.18, 1, 0.02), crossMat);
  crossH.position.set(0, 23.4, 0);
  duomoGroup.add(pediment, crossV, crossH);

  // Adjoining Sicilian Townhouses
  const houseMat = new Ce({color: 0xdeb887, roughness: 0.9});
  const roofMat = new Ce({color: 0xa84a28, roughness: 0.85});
  const house = new De(new os(11, 11, 4.0, 2, 0.1), houseMat);
  house.position.set(-11.5, 5.5, -1);
  const roof = new De(new os(12, 2.0, 4.6, 2, 0.1), roofMat);
  roof.position.set(-11.5, 11.8, -1);
  duomoGroup.add(house, roof);

  augustaGroup.add(duomoGroup);

  // D. MONUMENTAL CENTENARY FICUS TREE (Ficus macrophylla)
  // Positioned on the right of spawn (x = 22, y = 11, z = -14)
  const ficusGroup = new U();
  ficusGroup.name = "Ficus Centenario Villa Comunale";
  ficusGroup.position.set(22, 11, -14);

  const trunkMat = new Ce({color: 0x583e26, roughness: 0.88});
  const foliageMat = new Ce({color: 0x2e7526, roughness: 0.85});
  const foliageLightMat = new Ce({color: 0x489632, roughness: 0.82});

  // Massive main trunk & buttress root columns
  const mainTrunk = new De(new li(1.5, 2.4, 9.0, 14), trunkMat);
  mainTrunk.position.set(0, 4.5, 0);
  ficusGroup.add(mainTrunk);

  for (let r = 0; r < 6; r++) {
    const ang = r * Math.PI / 3;
    const dist = 1.8 + (r % 2) * 0.7;
    const rootCol = new De(new li(0.40, 0.70, 8.0, 10), trunkMat);
    rootCol.position.set(Math.cos(ang) * dist, 4.0, Math.sin(ang) * dist);
    rootCol.rotation.set(Math.sin(ang) * 0.15, 0, -Math.cos(ang) * 0.15);
    ficusGroup.add(rootCol);
  }

  // Aerial Root Tendrils cascading down
  for (let t = 0; t < 8; t++) {
    const ang = t * Math.PI / 4 + 0.3;
    const rDist = 2.6 + (t % 3) * 0.8;
    const tendril = new De(new li(0.07, 0.12, 7.0, 8), trunkMat);
    tendril.position.set(Math.cos(ang) * rDist, 3.5, Math.sin(ang) * rDist);
    ficusGroup.add(tendril);
  }

  // Giant clay foliage canopy
  const canopyNodes = [
    [0, 9.2, 0, 5.0, 3.0, 4.6, foliageMat],
    [-3.0, 8.4, 1.2, 4.0, 2.5, 3.6, foliageLightMat],
    [3.2, 8.8, -1.0, 4.2, 2.6, 4.0, foliageMat],
    [-1.4, 10.8, -1.2, 3.8, 2.4, 3.4, foliageLightMat],
    [2.0, 11.2, 1.0, 4.0, 2.5, 3.6, foliageMat]
  ];
  for (const [cx, cy, cz, sx, sy, sz, cmat] of canopyNodes) {
    const clump = new De(new $t(1, 16, 12), cmat);
    clump.position.set(cx, cy, cz);
    clump.scale.set(sx, sy, sz);
    ficusGroup.add(clump);
  }

  augustaGroup.add(ficusGroup);

  // E. ICONIC SIGNBOARD "SALVIAMO IL VERDE DI AUGUSTA" (in the foreground!)
  const signGroup = new U();
  signGroup.name = "Cartello Civico Salviamo Il Verde Di Augusta";
  signGroup.position.set(8.5, 13.0, -1.0);

  const postMat = new Ce({color: 0x3d2716, roughness: 0.9});
  const postL = new De(new os(0.18, 2.8, 0.18, 2, 0.02), postMat);
  postL.position.set(-1.2, 1.4, 0);
  const postR = new De(new os(0.18, 2.8, 0.18, 2, 0.02), postMat);
  postR.position.set(1.2, 1.4, 0);
  signGroup.add(postL, postR);

  // Dynamic Canvas Texture for crisp embossed text matching the reference artwork!
  let boardMat = new Ce({color: 0x5a3922, roughness: 0.88});
  try {
    const sCanvas = document.createElement("canvas");
    sCanvas.width = 1024;
    sCanvas.height = 512;
    const sctx = sCanvas.getContext("2d");
    sctx.fillStyle = "#52331c";
    sctx.fillRect(0, 0, 1024, 512);
    // Plank grooves
    sctx.fillStyle = "#38200e";
    sctx.fillRect(0, 168, 1024, 8);
    sctx.fillRect(0, 340, 1024, 8);
    // Wood grain
    sctx.strokeStyle = "rgba(0,0,0,0.18)";
    sctx.lineWidth = 3;
    for (let gy = 20; gy < 512; gy += 28) {
      sctx.beginPath(); sctx.moveTo(0, gy); sctx.lineTo(1024, gy); sctx.stroke();
    }
    // High-visibility clay lettering
    sctx.textAlign = "center";
    sctx.textBaseline = "middle";
    sctx.font = "900 102px 'Arial Rounded MT Bold', sans-serif";
    // SALVIAMO (ivory white)
    sctx.fillStyle = "rgba(20,10,5,0.6)";
    sctx.fillText("SALVIAMO", 515, 94);
    sctx.fillStyle = "#fcf6e8";
    sctx.fillText("SALVIAMO", 512, 88);
    // IL VERDE (bright leaf green!)
    sctx.fillStyle = "rgba(10,35,8,0.7)";
    sctx.fillText("IL VERDE", 515, 260);
    sctx.fillStyle = "#7ae234";
    sctx.fillText("IL VERDE", 512, 254);
    // DI AUGUSTA (ivory white)
    sctx.fillStyle = "rgba(20,10,5,0.6)";
    sctx.fillText("DI AUGUSTA", 515, 430);
    sctx.fillStyle = "#fcf6e8";
    sctx.fillText("DI AUGUSTA", 512, 424);

    const signTex = new Uo(sCanvas);
    signTex.colorSpace = xn;
    signTex.needsUpdate = true;
    boardMat = new Ce({map: signTex, roughness: 0.85});
  } catch(e) { console.warn("Sign tex", e); }

  const board = new De(new os(3.8, 1.9, 0.18, 3, 0.04), boardMat);
  board.position.set(0, 2.2, 0.06);
  signGroup.add(board);

  // Stone base & Terracotta Agave Planter beside sign
  const baseStone = new De(new os(3.8, 0.35, 1.2, 2, 0.08), stoneMat);
  baseStone.position.set(0, 0.18, 0);
  const agavePot = new De(new li(0.35, 0.22, 0.5, 12), new Ce({color: 0xbf5b30, roughness: 0.85}));
  agavePot.position.set(-1.6, 0.5, 0.2);
  const agavePlant = new De(new $t(0.45, 12, 10), new Ce({color: 0x3d8248, roughness: 0.8}));
  agavePlant.position.set(-1.6, 0.9, 0.2);
  agavePlant.scale.set(1.2, 0.6, 1.2);
  signGroup.add(baseStone, agavePot, agavePlant);

  augustaGroup.add(signGroup);

  // F. Park bench along the promenade
  const benchGroup = new U();
  benchGroup.name = "Panchina Villa Comunale";
  benchGroup.position.set(14.5, 13.0, -1.2);
  const ironMat = new Ce({color: 0x224428, roughness: 0.7, metalness: 0.3});
  const slatMat = new Ce({color: 0x7c4c28, roughness: 0.85});
  for (const bx of [-1.1, 1.1]) {
    const bLeg = new De(new os(0.08, 0.65, 0.55, 2, 0.02), ironMat);
    bLeg.position.set(bx, 0.35, 0);
    benchGroup.add(bLeg);
  }
  for (let s = 0; s < 4; s++) {
    const slat = new De(new os(2.4, 0.045, 0.10, 1, 0.01), slatMat);
    slat.position.set(0, 0.55, -0.18 + s * 0.12);
    benchGroup.add(slat);
  }
  for (let s = 0; s < 3; s++) {
    const bSlat = new De(new os(2.4, 0.08, 0.04, 1, 0.01), slatMat);
    bSlat.position.set(0, 0.75 + s * 0.13, -0.22);
    benchGroup.add(bSlat);
  }
  augustaGroup.add(benchGroup);

  // Add the entire authentic Augusta diorama to world's backRoot
  root.add(augustaGroup);
}
'''

# Replace buildAugustaBackdrop definition
pos_aug = bundle.find('function buildAugustaBackdrop')
if pos_aug != -1:
    pos_bae = bundle.find('function bae(t,e){', pos_aug)
    bundle = bundle[:pos_aug] + augusta_backdrop_func + "\n" + bundle[pos_bae:]
    print("Replaced buildAugustaBackdrop with enhanced Augusta diorama!")

with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("Applied perfect GTA Giuseppe & Augusta scenery!")
