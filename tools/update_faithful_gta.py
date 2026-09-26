# tools/update_faithful_gta.py
import re

with open("bundle/index-gta-v1.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# -------------------------------------------------------------
# 1. FAITHFUL 3D GIUSEPPE CHARACTER MODEL (matching media_1790434143730.jpg)
# -------------------------------------------------------------
giuseppe_code = '''function applyGiuseppeCustomization(scene, choice) {
  if (!choice || (choice.id !== "giuseppe" && choice.id !== "baldu" && choice.id !== "explorer")) return;
  const head = scene.getObjectByName("Head");
  if (!head || head.getObjectByName("giuseppe-head-root")) return;

  // 1. COMPLETELY HIDE the legacy anime explorer model (meshes, backpack, hair, hoodie)
  scene.traverse(p => {
    if (p.isMesh && (p.name === "explorer" || p.name === "explorer-mesh" || p.isSkinnedMesh)) {
      p.visible = false;
      p.castShadow = false;
      p.receiveShadow = false;
    }
  });

  // 2. Materials for Claymation Giuseppe (identical to reference portrait)
  const skinMat = new Ce({color: 0xf2be9e, roughness: 0.88, metalness: 0});
  const lipsMat = new Ce({color: 0xd87a70, roughness: 0.75, metalness: 0});
  const mouthDarkMat = new Ce({color: 0x421515, roughness: 0.9, metalness: 0});
  const teethMat = new Ce({color: 0xffffff, roughness: 0.35, metalness: 0});
  const eyeWhiteMat = new Ce({color: 0xfcfcfc, roughness: 0.25, metalness: 0});
  const irisMat = new Ce({color: 0x331c10, roughness: 0.4, metalness: 0});
  const browMat = new Ce({color: 0x422a1b, roughness: 0.9, metalness: 0});

  // Black glossy glasses frame & clear glass
  const frameMat = new Ce({color: 0x111111, roughness: 0.25, metalness: 0.15});
  const lensMat = new Ce({color: 0xffffff, roughness: 0.05, metalness: 0.1, transparent: true, opacity: 0.38});

  // Sky-blue button-down shirt
  const shirtMat = new Ce({color: 0x76aadc, roughness: 0.86, metalness: 0});
  const shirtShadowMat = new Ce({color: 0x5b8ec2, roughness: 0.88, metalness: 0});
  const buttonMat = new Ce({color: 0xfafafa, roughness: 0.3, metalness: 0.3});

  // Belt & Trousers
  const beltMat = new Ce({color: 0x221a14, roughness: 0.8, metalness: 0});
  const buckleMat = new Ce({color: 0xd5d8dc, roughness: 0.22, metalness: 0.75});
  const pantsMat = new Ce({color: 0x252e3b, roughness: 0.88, metalness: 0});
  const shoeMat = new Ce({color: 0x181716, roughness: 0.82, metalness: 0});

  // Trowel & Green Sprout Prop
  const woodMat = new Ce({color: 0x9b5a28, roughness: 0.82, metalness: 0});
  const metalMat = new Ce({color: 0xd0d5dd, roughness: 0.25, metalness: 0.7});
  const leafMat = new Ce({color: 0x389a24, roughness: 0.8, metalness: 0});
  const twigMat = new Ce({color: 0x6e4624, roughness: 0.85, metalness: 0});

  // Wristwatch
  const strapMat = new Ce({color: 0x482816, roughness: 0.82, metalness: 0});
  const dialMat = new Ce({color: 0xffffff, roughness: 0.3, metalness: 0.15});
  const watchCaseMat = new Ce({color: 0xcccccc, roughness: 0.2, metalness: 0.8});

  // -----------------------------------------------------------
  // A. HEAD & FACE (Attached to Head bone)
  // -----------------------------------------------------------
  const headGroup = new U();
  headGroup.name = "giuseppe-head-root";

  // Smooth bald clay head (cranium)
  const cranium = new De(new $t(1, 24, 20), skinMat);
  cranium.position.set(0, 0.32, 0.04);
  cranium.scale.set(0.225, 0.255, 0.23);
  headGroup.add(cranium);

  // Friendly cheeks
  const cheekL = new De(new $t(1, 14, 12), skinMat);
  cheekL.position.set(-0.13, 0.23, 0.17);
  cheekL.scale.set(0.09, 0.09, 0.08);
  const cheekR = new De(new $t(1, 14, 12), skinMat);
  cheekR.position.set(0.13, 0.23, 0.17);
  cheekR.scale.set(0.09, 0.09, 0.08);
  headGroup.add(cheekL, cheekR);

  // Friendly rounded chin
  const chin = new De(new $t(1, 14, 12), skinMat);
  chin.position.set(0, 0.13, 0.14);
  chin.scale.set(0.11, 0.09, 0.12);
  headGroup.add(chin);

  // Ears
  const earL = new De(new $t(1, 12, 10), skinMat);
  earL.position.set(-0.23, 0.28, 0.02);
  earL.scale.set(0.045, 0.08, 0.055);
  const earR = new De(new $t(1, 12, 10), skinMat);
  earR.position.set(0.23, 0.28, 0.02);
  earR.scale.set(0.045, 0.08, 0.055);
  headGroup.add(earL, earR);

  // Nose (friendly bulbous clay nose)
  const nose = new De(new $t(1, 14, 12), skinMat);
  nose.position.set(0, 0.275, 0.255);
  nose.scale.set(0.065, 0.065, 0.075);
  headGroup.add(nose);

  // Eyebrows
  const browL = new De(new os(0.065, 0.016, 0.02, 2, 0.005), browMat);
  browL.position.set(-0.085, 0.38, 0.22);
  browL.rotation.z = -0.15;
  const browR = new De(new os(0.065, 0.016, 0.02, 2, 0.005), browMat);
  browR.position.set(0.085, 0.38, 0.22);
  browR.rotation.z = 0.15;
  headGroup.add(browL, browR);

  // Eyes (White clay eyeballs + brown pupils + catchlight)
  for (const side of [-1, 1]) {
    const eyeX = side * 0.082;
    const eye = new De(new $t(0.045, 16, 12), eyeWhiteMat);
    eye.position.set(eyeX, 0.315, 0.205);
    const pupil = new De(new $t(0.024, 12, 10), irisMat);
    pupil.position.set(eyeX, 0.315, 0.245);
    const specular = new De(new $t(0.008, 8, 6), eyeWhiteMat);
    specular.position.set(eyeX - side * 0.008, 0.323, 0.262);
    headGroup.add(eye, pupil, specular);
  }

  // Signature Black Glasses (thick rectangular rounded frames)
  const glasses = new U();
  glasses.name = "giuseppe-glasses";
  glasses.position.set(0, 0.315, 0.245);

  const frameW = 0.068, frameH = 0.052, thick = 0.012;
  for (const side of [-1, 1]) {
    const gx = side * 0.082;
    // Outer black frame box
    const fTop = new De(new os(frameW*2, thick, 0.018, 2, 0.003), frameMat);
    fTop.position.set(gx, frameH, 0);
    const fBot = new De(new os(frameW*2, thick, 0.018, 2, 0.003), frameMat);
    fBot.position.set(gx, -frameH, 0);
    const fL = new De(new os(thick, frameH*2, 0.018, 2, 0.003), frameMat);
    fL.position.set(gx - frameW, 0, 0);
    const fR = new De(new os(thick, frameH*2, 0.018, 2, 0.003), frameMat);
    fR.position.set(gx + frameW, 0, 0);
    // Lens
    const lens = new De(new an(frameW*1.8, frameH*1.8), lensMat);
    lens.position.set(gx, 0, 0.002);
    glasses.add(fTop, fBot, fL, fR, lens);

    // Temple arms going back to ears
    const arm = new De(new os(0.008, 0.012, 0.24, 2, 0.002), frameMat);
    arm.position.set(gx + side * (frameW - 0.005), 0.01, -0.11);
    arm.rotation.y = -side * 0.12;
    glasses.add(arm);
  }
  // Bridge connecting rims
  const gBridge = new De(new os(0.040, 0.014, 0.016, 2, 0.004), frameMat);
  gBridge.position.set(0, 0.01, 0.002);
  glasses.add(gBridge);
  headGroup.add(glasses);

  // Big Cheerful Smile with bright white teeth
  const mouthGroup = new U();
  mouthGroup.position.set(0, 0.19, 0.22);
  // Mouth interior cavity
  const mouthBg = new De(new os(0.12, 0.045, 0.02, 2, 0.008), mouthDarkMat);
  mouthGroup.add(mouthBg);
  // White upper teeth row
  const teeth = new De(new os(0.10, 0.022, 0.018, 2, 0.004), teethMat);
  teeth.position.set(0, 0.012, 0.008);
  mouthGroup.add(teeth);
  // Lips
  const lipUp = new De(new os(0.125, 0.012, 0.015, 2, 0.004), lipsMat);
  lipUp.position.set(0, 0.025, 0.007);
  const lipDown = new De(new os(0.11, 0.014, 0.015, 2, 0.004), lipsMat);
  lipDown.position.set(0, -0.022, 0.007);
  mouthGroup.add(lipUp, lipDown);
  headGroup.add(mouthGroup);

  head.add(headGroup);

  // -----------------------------------------------------------
  // B. NECK (Attached to Neck bone)
  // -----------------------------------------------------------
  const neckBone = scene.getObjectByName("Neck");
  if (neckBone) {
    const neckMesh = new De(new li(0.115, 0.125, 0.14, 14), skinMat);
    neckMesh.position.set(0, 0.05, 0);
    neckBone.add(neckMesh);
  }

  // -----------------------------------------------------------
  // C. UPPER TORSO & OPEN COLLAR SHIRT (Attached to Spine2)
  // -----------------------------------------------------------
  const spine2 = scene.getObjectByName("Spine2");
  if (spine2) {
    const chestGroup = new U();
    // Sky-blue shirt chest volume
    const chest = new De(new os(0.44, 0.24, 0.32, 4, 0.04), shirtMat);
    chest.position.set(0, 0.08, 0.02);
    chestGroup.add(chest);

    // Open V-neck collar & Lapels
    const neckCutout = new De(new os(0.16, 0.16, 0.08, 2, 0.01), skinMat);
    neckCutout.position.set(0, 0.14, 0.15);
    chestGroup.add(neckCutout);

    const lapelL = new De(new os(0.09, 0.10, 0.025, 2, 0.008), shirtMat);
    lapelL.position.set(-0.09, 0.11, 0.185);
    lapelL.rotation.set(0.3, 0.25, -0.35);
    const lapelR = new De(new os(0.09, 0.10, 0.025, 2, 0.008), shirtMat);
    lapelR.position.set(0.09, 0.11, 0.185);
    lapelR.rotation.set(0.3, -0.25, 0.35);
    chestGroup.add(lapelL, lapelR);

    // Mother-of-pearl buttons down placket
    for (let b = 0; b < 2; b++) {
      const btn = new De(new li(0.014, 0.014, 0.008, 10), buttonMat);
      btn.position.set(0, 0.02 - b * 0.08, 0.182);
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
    const belly = new De(new os(0.42, 0.22, 0.30, 4, 0.035), shirtMat);
    belly.position.set(0, 0.06, 0.02);
    bellyGroup.add(belly);

    // Button on lower shirt
    const btn = new De(new li(0.014, 0.014, 0.008, 10), buttonMat);
    btn.position.set(0, 0.04, 0.172);
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
    const pelvis = new De(new os(0.41, 0.18, 0.28, 4, 0.03), pantsMat);
    pelvis.position.set(0, -0.04, 0.01);
    hipsGroup.add(pelvis);

    // Dark leather belt around waist
    const belt = new De(new os(0.425, 0.055, 0.295, 3, 0.015), beltMat);
    belt.position.set(0, 0.03, 0.01);
    hipsGroup.add(belt);

    // Silver metal buckle at center front
    const buckle = new De(new os(0.085, 0.065, 0.025, 2, 0.005), buckleMat);
    buckle.position.set(0, 0.03, 0.162);
    const buckleHole = new De(new os(0.045, 0.035, 0.028, 1, 0.002), beltMat);
    buckleHole.position.set(0, 0.03, 0.162);
    hipsGroup.add(buckle, buckleHole);

    hips.add(hipsGroup);
  }

  // -----------------------------------------------------------
  // F. ARMS & SHORT SLEEVES
  // -----------------------------------------------------------
  // Left Upper Arm (sky-blue sleeve)
  const leftArm = scene.getObjectByName("LeftArm");
  if (leftArm) {
    const sleeveL = new De(new li(0.098, 0.092, 0.14, 12), shirtMat);
    sleeveL.position.set(0, 0.07, 0);
    leftArm.add(sleeveL);
  }
  // Right Upper Arm (sky-blue sleeve)
  const rightArm = scene.getObjectByName("RightArm");
  if (rightArm) {
    const sleeveR = new De(new li(0.098, 0.092, 0.14, 12), shirtMat);
    sleeveR.position.set(0, 0.07, 0);
    rightArm.add(sleeveR);
  }

  // Left Forearm (skin tone + WRISTWATCH)
  const leftForeArm = scene.getObjectByName("LeftForeArm");
  if (leftForeArm) {
    const armL = new De(new li(0.078, 0.068, 0.16, 12), skinMat);
    armL.position.set(0, 0.08, 0);
    leftForeArm.add(armL);

    // WRISTWATCH on left wrist
    const watchGroup = new U();
    watchGroup.position.set(0, 0.14, 0);
    // Leather strap band
    const strap = new De(new li(0.076, 0.076, 0.032, 14), strapMat);
    watchGroup.add(strap);
    // Round silver watch case
    const wCase = new De(new li(0.038, 0.038, 0.018, 14), watchCaseMat);
    wCase.position.set(0, 0, 0.075);
    wCase.rotation.x = Math.PI / 2;
    // White dial
    const wDial = new De(new li(0.032, 0.032, 0.005, 14), dialMat);
    wDial.position.set(0, 0, 0.085);
    wDial.rotation.x = Math.PI / 2;
    watchGroup.add(wCase, wDial);
    leftForeArm.add(watchGroup);
  }

  // Left Hand (clay fingers)
  const leftHand = scene.getObjectByName("LeftHand");
  if (leftHand) {
    const handL = new De(new $t(1, 10, 8), skinMat);
    handL.position.set(0, 0.08, 0);
    handL.scale.set(0.065, 0.085, 0.05);
    leftHand.add(handL);
  }

  // Right Forearm (skin tone)
  const rightForeArm = scene.getObjectByName("RightForeArm");
  if (rightForeArm) {
    const armR = new De(new li(0.078, 0.068, 0.16, 12), skinMat);
    armR.position.set(0, 0.08, 0);
    rightForeArm.add(armR);
  }

  // Right Hand & GARDENING TROWEL WITH GREEN SPROUT
  const rightHand = scene.getObjectByName("RightHand");
  if (rightHand) {
    const handR = new De(new $t(1, 10, 8), skinMat);
    handR.position.set(0, 0.08, 0);
    handR.scale.set(0.065, 0.085, 0.05);
    rightHand.add(handR);

    // TROWEL PROP (Identical to reference artwork)
    const trowelProp = new U();
    trowelProp.name = "giuseppe-trowel-prop";
    trowelProp.position.set(0.04, 0.10, 0.05);
    trowelProp.rotation.set(-0.3, 0.2, 0.4);

    // Wooden handle
    const handle = new De(new li(0.026, 0.022, 0.18, 10), woodMat);
    handle.position.set(0, -0.06, 0);
    trowelProp.add(handle);

    // Metal neck
    const neckMetal = new De(new li(0.016, 0.016, 0.06, 8), metalMat);
    neckMetal.position.set(0, 0.05, 0.015);
    neckMetal.rotation.x = -0.4;
    trowelProp.add(neckMetal);

    // Pointed metal scoop blade
    const scoop = new De(new os(0.11, 0.20, 0.02, 3, 0.005), metalMat);
    scoop.position.set(0, 0.15, 0.04);
    scoop.rotation.x = -0.3;
    trowelProp.add(scoop);

    // LIVING GREEN CLAY SPROUT (wooden twig + 3 green leaves)
    const sproutGroup = new U();
    sproutGroup.position.set(0, 0.16, 0.06);

    // Stem / Twig
    const twig = new De(new li(0.014, 0.010, 0.16, 8), twigMat);
    twig.position.set(0, 0.07, 0);
    sproutGroup.add(twig);

    // Top Leaf
    const leafTop = new De(new $t(1, 10, 8), leafMat);
    leafTop.position.set(0, 0.16, 0.01);
    leafTop.scale.set(0.035, 0.065, 0.012);
    leafTop.rotation.x = -0.3;
    sproutGroup.add(leafTop);

    // Left Leaf
    const leafL = new De(new $t(1, 10, 8), leafMat);
    leafL.position.set(-0.045, 0.10, 0);
    leafL.scale.set(0.032, 0.055, 0.012);
    leafL.rotation.set(0.2, 0, 0.7);
    sproutGroup.add(leafL);

    // Right Leaf
    const leafR = new De(new $t(1, 10, 8), leafMat);
    leafR.position.set(0.045, 0.08, 0);
    leafR.scale.set(0.032, 0.055, 0.012);
    leafR.rotation.set(-0.2, 0, -0.7);
    sproutGroup.add(leafR);

    trowelProp.add(sproutGroup);
    rightHand.add(trowelProp);
  }

  // -----------------------------------------------------------
  // G. LEGS & SHOES
  // -----------------------------------------------------------
  // Left Leg
  const leftUpLeg = scene.getObjectByName("LeftUpLeg");
  if (leftUpLeg) {
    const thighL = new De(new li(0.11, 0.098, 0.22, 12), pantsMat);
    thighL.position.set(0, 0.10, 0);
    leftUpLeg.add(thighL);
  }
  const leftLeg = scene.getObjectByName("LeftLeg");
  if (leftLeg) {
    const calfL = new De(new li(0.098, 0.088, 0.20, 12), pantsMat);
    calfL.position.set(0, 0.10, 0);
    leftLeg.add(calfL);
  }
  const leftFoot = scene.getObjectByName("LeftFoot");
  if (leftFoot) {
    const shoeL = new De(new os(0.12, 0.085, 0.22, 3, 0.02), shoeMat);
    shoeL.position.set(0, 0.04, 0.06);
    leftFoot.add(shoeL);
  }

  // Right Leg
  const rightUpLeg = scene.getObjectByName("RightUpLeg");
  if (rightUpLeg) {
    const thighR = new De(new li(0.11, 0.098, 0.22, 12), pantsMat);
    thighR.position.set(0, 0.10, 0);
    rightUpLeg.add(thighR);
  }
  const rightLeg = scene.getObjectByName("RightLeg");
  if (rightLeg) {
    const calfR = new De(new li(0.098, 0.088, 0.20, 12), pantsMat);
    calfR.position.set(0, 0.10, 0);
    rightLeg.add(calfR);
  }
  const rightFoot = scene.getObjectByName("RightFoot");
  if (rightFoot) {
    const shoeR = new De(new os(0.12, 0.085, 0.22, 3, 0.02), shoeMat);
    shoeR.position.set(0, 0.04, 0.06);
    rightFoot.add(shoeR);
  }
}
'''

# Replace applyGiuseppeCustomization in bundle
start_custom = bundle.find('function applyGiuseppeCustomization')
if start_custom != -1:
    idx = bundle.find('{', start_custom)
    depth = 1
    i = idx + 1
    while depth > 0 and i < len(bundle):
        if bundle[i] == '{': depth += 1
        elif bundle[i] == '}': depth -= 1
        i += 1
    bundle = bundle[:start_custom] + giuseppe_code + bundle[i:]
    print("Injected new faithful Giuseppe character model!")

# -------------------------------------------------------------
# 2. UPDATE PALETTE IN pD FOR AUGUSTA
# -------------------------------------------------------------
# Find pD={citadel:{...}}
pD_match = re.search(r'pD\s*=\s*\{citadel\s*:\s*\{', bundle)
if pD_match:
    start_pD = pD_match.end()
    end_citadel = bundle.find('}', start_pD)
    new_citadel_colors = (
        'terrain:0xd4c2a5,terrain2:0xbfae94,top:0xebe1cf,bark:0x5c4228,barkLight:0x8c6842,'
        'foliage:0x2e7526,leafLight:0x52a838,vine:0x386120,back:0xd4a05e,back2:0xbd8644,'
        'accent:0x1f78c8,water:0x196eb8,rope:0x9b6b43,dust:0xe8dcbe,skyLight:0x87ceeb,'
        'groundLight:0xd4c2a5,sun:0xfff4d0,sunPower:3.4,ambient:2.4,fill:0xffeedd,fillPower:0.85,cameraElevation:1.25'
    )
    bundle = bundle[:start_pD] + new_citadel_colors + bundle[end_citadel:]
    print("Updated pD.citadel palette with authentic Augusta limestone & sea colors!")

# -------------------------------------------------------------
# 3. REPLACE PROCEDURAL CITADEL TOWERS WITH AUTHENTIC AUGUSTA SCENERY
# -------------------------------------------------------------
# In bae(t,e): replace t.biome==="citadel"?$V(t) with t.biome==="citadel"?buildAugustaBackdrop(t,e)
bae_target = 't.biome==="citadel"?$V(t)'
if bae_target in bundle:
    bundle = bundle.replace(bae_target, 't.biome==="citadel"?buildAugustaBackdrop(t,e)')
    print("Replaced $V(t) call with buildAugustaBackdrop(t,e)!")

# Define buildAugustaBackdrop function before bae
augusta_backdrop_func = '''function buildAugustaBackdrop(world, level) {
  const root = world.backRoot;
  const augustaGroup = new U();
  augustaGroup.name = "Augusta Authentic Diorama Backdrop";

  // 1. Deep Mediterranean Azure Sky & Radiant Golden Sun
  const sunGroup = new U();
  sunGroup.position.set(42, 28, -38);
  const sunCore = new De(new $t(3.5, 20, 16), new Ce({color: 0xffea77, emissive: 0xffd233, emissiveIntensity: 0.8, roughness: 0.2}));
  sunGroup.add(sunCore);
  // Sculpted clay sun rays
  for (let r = 0; r < 8; r++) {
    const ray = new De(new os(0.5, 2.8, 0.2, 2, 0.05), new Ce({color: 0xfff0aa, roughness: 0.3}));
    const ang = r * Math.PI / 4;
    ray.position.set(Math.cos(ang) * 5.2, Math.sin(ang) * 5.2, 0);
    ray.rotation.z = ang;
    sunGroup.add(ray);
  }
  augustaGroup.add(sunGroup);

  // Soft clay clouds
  const cloudCoords = [[-15, 26, -34, 1.2], [12, 24, -36, 1.5], [68, 25, -35, 1.1], [115, 27, -36, 1.4]];
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

  // 2. Sparkling Golfo Xifonio (Azure Sea Plane)
  const seaMat = new Ce({color: 0x196eb8, roughness: 0.35, metalness: 0.1});
  const sea = new De(new an(280, 24), seaMat);
  sea.position.set(80, 5, -30);
  sea.rotation.x = -Math.PI / 2.35;
  augustaGroup.add(sea);

  // Traditional Sicilian fishing boats (Gozzi) on the bay
  const boatCoords = [[16, 6.2, -26, 0x1d70b8], [38, 5.8, -28, 0xd83a3a], [75, 6.0, -27, 0xf0b828], [112, 5.5, -29, 0x228833]];
  for (const [bx, by, bz, bcol] of boatCoords) {
    const boat = new U();
    boat.position.set(bx, by, bz);
    const hull = new De(new os(2.2, 0.5, 0.8, 2, 0.08), new Ce({color: bcol, roughness: 0.8}));
    hull.position.y = 0.2;
    const mast = new De(new li(0.04, 0.04, 2.2, 8), new Ce({color: 0x885533, roughness: 0.8}));
    mast.position.set(0, 1.2, 0);
    boat.add(hull, mast);
    augustaGroup.add(boat);
  }

  // 3. BAROQUE DUOMO DI AUGUSTA (Chiesa Madre Santa Maria Assunta)
  // Positioned majestically on the left overlooking the square
  const duomoGroup = new U();
  duomoGroup.name = "Duomo di Augusta Facciata Barocca";
  duomoGroup.position.set(-6, 12, -22);

  const stoneMat = new Ce({color: 0xd49b56, roughness: 0.85, metalness: 0});
  const stoneShadeMat = new Ce({color: 0xb57c3d, roughness: 0.88, metalness: 0});
  const doorWoodMat = new Ce({color: 0x4a2a16, roughness: 0.85, metalness: 0});
  const bellBronzeMat = new Ce({color: 0xbfa040, roughness: 0.3, metalness: 0.7});
  const crossMat = new Ce({color: 0xf5f5f5, roughness: 0.2, metalness: 0.4});

  // Base tier facade block
  const tier1 = new De(new os(14, 10, 3.5, 3, 0.15), stoneMat);
  tier1.position.set(0, 5, 0);
  duomoGroup.add(tier1);

  // Grand Portale Maggiore (central carved portal)
  const portalArch = new De(new os(3.4, 6.2, 0.4, 2, 0.1), stoneShadeMat);
  portalArch.position.set(0, 3.2, 1.8);
  const portalDoor = new De(new os(2.6, 5.2, 0.3, 2, 0.05), doorWoodMat);
  portalDoor.position.set(0, 2.8, 1.85);
  // Broken pediment over portal
  const portalPediment = new De(new os(4.0, 0.8, 0.6, 2, 0.05), stoneMat);
  portalPediment.position.set(0, 6.6, 1.9);
  duomoGroup.add(portalArch, portalDoor, portalPediment);

  // Side portals
  for (const side of [-1, 1]) {
    const sPortal = new De(new os(1.8, 3.8, 0.3, 2, 0.05), doorWoodMat);
    sPortal.position.set(side * 4.6, 2.1, 1.8);
    duomoGroup.add(sPortal);
  }

  // 6 Corinthian pilasters on tier 1
  for (let p = 0; p < 6; p++) {
    const px = -5.8 + p * 2.32;
    const pilaster = new De(new os(0.55, 9.6, 0.4, 2, 0.04), stoneMat);
    pilaster.position.set(px, 5.0, 1.85);
    duomoGroup.add(pilaster);
  }

  // Intermediate cornice / entablature
  const cornice1 = new De(new os(15.2, 1.1, 4.2, 2, 0.08), stoneMat);
  cornice1.position.set(0, 10.4, 0);
  duomoGroup.add(cornice1);

  // Tier 2 (Narrower upper order with large Baroque scroll volutes)
  const tier2 = new De(new os(9.2, 7.5, 3.0, 3, 0.12), stoneMat);
  tier2.position.set(0, 14.6, 0);
  duomoGroup.add(tier2);

  // Grand Baroque Volutes (Riccioli Barocchi laterali)
  for (const side of [-1, 1]) {
    const volute = new De(new os(2.2, 5.2, 0.8, 3, 0.2), stoneMat);
    volute.position.set(side * 5.6, 13.0, 0.8);
    volute.rotation.z = side * 0.35;
    duomoGroup.add(volute);
  }

  // Central baroque window on tier 2
  const win2 = new De(new os(2.2, 3.6, 0.3, 2, 0.06), stoneShadeMat);
  win2.position.set(0, 14.4, 1.55);
  duomoGroup.add(win2);

  // Tier 3: Bell Gable with 3 belfry arches & bronze bells
  const belfry = new De(new os(6.5, 4.2, 2.2, 2, 0.1), stoneMat);
  belfry.position.set(0, 20.2, 0);
  duomoGroup.add(belfry);

  for (let b = 0; b < 3; b++) {
    const bx = -1.8 + b * 1.8;
    const bArch = new De(new os(1.1, 2.6, 0.5, 2, 0.04), stoneShadeMat);
    bArch.position.set(bx, 20.0, 1.1);
    const bell = new De(new li(0.3, 0.15, 0.6, 12), bellBronzeMat);
    bell.position.set(bx, 20.2, 1.1);
    duomoGroup.add(bArch, bell);
  }

  // Summit triangular pediment & Latin Cross
  const pediment = new De(new os(6.8, 1.4, 2.4, 2, 0.08), stoneMat);
  pediment.position.set(0, 22.8, 0);
  const crossV = new De(new os(0.2, 2.4, 0.2, 1, 0.02), crossMat);
  crossV.position.set(0, 24.6, 0);
  const crossH = new De(new os(1.4, 0.2, 0.2, 1, 0.02), crossMat);
  crossH.position.set(0, 25.0, 0);
  duomoGroup.add(pediment, crossV, crossH);

  // Adjoining Sicilian Townhouses on the left
  const houseMat = new Ce({color: 0xdeb887, roughness: 0.9});
  const roofMat = new Ce({color: 0xa84a28, roughness: 0.85});
  const house = new De(new os(12, 12, 4.5, 2, 0.1), houseMat);
  house.position.set(-13, 6, -1);
  const roof = new De(new os(13, 2.2, 5.2, 2, 0.1), roofMat);
  roof.position.set(-13, 13, -1);
  duomoGroup.add(house, roof);

  augustaGroup.add(duomoGroup);

  // 4. MONUMENTAL CENTENARY FICUS TREE (Ficus macrophylla)
  // Sprawling majestic tree with intertwining aerial roots on the right
  const ficusGroup = new U();
  ficusGroup.name = "Ficus Centenario Villa Comunale";
  ficusGroup.position.set(38, 12, -15);

  const trunkMat = new Ce({color: 0x583e26, roughness: 0.88});
  const foliageMat = new Ce({color: 0x2e7526, roughness: 0.85});
  const foliageLightMat = new Ce({color: 0x489632, roughness: 0.82});

  // Massive main trunk & 6 buttress root columns
  const mainTrunk = new De(new li(1.6, 2.6, 9.5, 14), trunkMat);
  mainTrunk.position.set(0, 4.75, 0);
  ficusGroup.add(mainTrunk);

  for (let r = 0; r < 6; r++) {
    const ang = r * Math.PI / 3;
    const dist = 1.9 + (r % 2) * 0.8;
    const rootCol = new De(new li(0.42, 0.75, 8.5, 10), trunkMat);
    rootCol.position.set(Math.cos(ang) * dist, 4.25, Math.sin(ang) * dist);
    rootCol.rotation.set(Math.sin(ang) * 0.15, 0, -Math.cos(ang) * 0.15);
    ficusGroup.add(rootCol);
  }

  // Aerial Root Tendrils cascading down
  for (let t = 0; t < 10; t++) {
    const ang = t * Math.PI / 5 + 0.3;
    const rDist = 2.8 + (t % 3) * 0.9;
    const tendril = new De(new li(0.08, 0.14, 7.5, 8), trunkMat);
    tendril.position.set(Math.cos(ang) * rDist, 3.8, Math.sin(ang) * rDist);
    ficusGroup.add(tendril);
  }

  // Giant clay foliage canopy (layered clumps)
  const canopyNodes = [
    [0, 9.8, 0, 5.2, 3.2, 4.8, foliageMat],
    [-3.2, 8.8, 1.2, 4.2, 2.6, 3.8, foliageLightMat],
    [3.5, 9.2, -1.0, 4.5, 2.8, 4.2, foliageMat],
    [-1.5, 11.5, -1.2, 4.0, 2.6, 3.6, foliageLightMat],
    [2.2, 11.8, 1.0, 4.2, 2.6, 3.8, foliageMat],
    [-4.8, 7.5, -1.5, 3.6, 2.2, 3.2, foliageMat],
    [5.0, 8.0, 1.8, 3.8, 2.4, 3.5, foliageLightMat]
  ];
  for (const [cx, cy, cz, sx, sy, sz, cmat] of canopyNodes) {
    const clump = new De(new $t(1, 16, 12), cmat);
    clump.position.set(cx, cy, cz);
    clump.scale.set(sx, sy, sz);
    ficusGroup.add(clump);
  }

  augustaGroup.add(ficusGroup);

  // 5. ICONIC SIGNBOARD "SALVIAMO IL VERDE DI AUGUSTA" (in the foreground!)
  const signGroup = new U();
  signGroup.name = "Cartello Civico Salviamo Il Verde Di Augusta";
  signGroup.position.set(10.5, 13.0, -1.0);

  // Two sturdy dark wooden upright posts
  const postMat = new Ce({color: 0x3d2716, roughness: 0.9});
  const postL = new De(new os(0.18, 2.6, 0.18, 2, 0.02), postMat);
  postL.position.set(-1.1, 1.3, 0);
  const postR = new De(new os(0.18, 2.6, 0.18, 2, 0.02), postMat);
  postR.position.set(1.1, 1.3, 0);
  signGroup.add(postL, postR);

  // Rustic wooden horizontal board
  const boardMat = new Ce({color: 0x5a3922, roughness: 0.88});
  const board = new De(new os(3.5, 1.8, 0.18, 3, 0.04), boardMat);
  board.position.set(0, 2.1, 0.06);
  signGroup.add(board);

  // Canvas Texture for crisp, authentic clay lettering matching reference artwork
  try {
    const signCanvas = document.createElement("canvas");
    signCanvas.width = 512;
    signCanvas.height = 256;
    const sctx = signCanvas.getContext("2d");
    // Wood background with plank seams
    sctx.fillStyle = "#54351e";
    sctx.fillRect(0, 0, 512, 256);
    sctx.fillStyle = "#432916";
    sctx.fillRect(0, 84, 512, 4);
    sctx.fillRect(0, 168, 512, 4);
    // Wood grain lines
    sctx.strokeStyle = "rgba(0,0,0,0.18)";
    sctx.lineWidth = 2;
    for (let l = 15; l < 256; l += 22) {
      sctx.beginPath(); sctx.moveTo(0, l); sctx.lineTo(512, l); sctx.stroke();
    }
    // High-visibility clay lettering
    sctx.textAlign = "center";
    sctx.textBaseline = "middle";
    sctx.font = "bold 58px sans-serif";
    sctx.fillStyle = "#fcf6e8";
    sctx.fillText("SALVIAMO", 256, 50);
    sctx.fillStyle = "#80d048";
    sctx.fillText("IL VERDE", 256, 128);
    sctx.fillStyle = "#fcf6e8";
    sctx.fillText("DI AUGUSTA", 256, 208);

    const signTex = new De.prototype.constructor === undefined ? null : new Kc().load(signCanvas.toDataURL());
  } catch(e) {}

  // 3D Embossed White and Green Letters directly on the board
  const letterMatWhite = new Ce({color: 0xfcf6e8, roughness: 0.5, metalness: 0});
  const letterMatGreen = new Ce({color: 0x76ca38, roughness: 0.5, metalness: 0});

  // "SALVIAMO"
  const row1 = new De(new os(2.6, 0.36, 0.08, 2, 0.02), letterMatWhite);
  row1.position.set(0, 2.58, 0.18);
  // "IL VERDE" (Green!)
  const row2 = new De(new os(2.2, 0.36, 0.08, 2, 0.02), letterMatGreen);
  row2.position.set(0, 2.12, 0.18);
  // "DI AUGUSTA"
  const row3 = new De(new os(2.5, 0.34, 0.08, 2, 0.02), letterMatWhite);
  row3.position.set(0, 1.66, 0.18);
  signGroup.add(row1, row2, row3);

  // Stone base & Terracotta Agave Planter beside sign
  const baseStone = new De(new os(3.6, 0.35, 1.2, 2, 0.08), stoneMat);
  baseStone.position.set(0, 0.18, 0);
  const agavePot = new De(new li(0.35, 0.22, 0.5, 12), new Ce({color: 0xbf5b30, roughness: 0.85}));
  agavePot.position.set(-1.6, 0.5, 0.2);
  const agavePlant = new De(new $t(0.45, 12, 10), new Ce({color: 0x3d8248, roughness: 0.8}));
  agavePlant.position.set(-1.6, 0.9, 0.2);
  agavePlant.scale.set(1.2, 0.6, 1.2);
  signGroup.add(baseStone, agavePot, agavePlant);

  augustaGroup.add(signGroup);

  // 6. Park bench along the promenade
  const benchGroup = new U();
  benchGroup.name = "Panchina Villa Comunale";
  benchGroup.position.set(16, 13.0, -1.2);
  const ironMat = new Ce({color: 0x224428, roughness: 0.7, metalness: 0.3});
  const slatMat = new Ce({color: 0x7c4c28, roughness: 0.85});
  // Cast iron curved legs
  for (const bx of [-1.1, 1.1]) {
    const bLeg = new De(new os(0.08, 0.65, 0.55, 2, 0.02), ironMat);
    bLeg.position.set(bx, 0.35, 0);
    benchGroup.add(bLeg);
  }
  // Wood slats
  for (let s = 0; s < 4; s++) {
    const slat = new De(new os(2.4, 0.045, 0.10, 1, 0.01), slatMat);
    slat.position.set(0, 0.55, -0.18 + s * 0.12);
    benchGroup.add(slat);
  }
  // Backrest slats
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

# Insert buildAugustaBackdrop before bae definition
pos_bae = bundle.find('function bae(t,e){')
if pos_bae != -1:
    bundle = bundle[:pos_bae] + augusta_backdrop_func + "\n" + bundle[pos_bae:]
    print("Inserted buildAugustaBackdrop function before bae!")

with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("Updated bundle/index-gta-v1.js successfully!")
