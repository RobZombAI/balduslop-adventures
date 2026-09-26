# tools/final_visual_perfection.py
import re

with open("bundle/index-gta-v1.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Clean radiant sun in Mediterranean sky (without the distracting long white ray box)
sun_old = '''  for (let r = 0; r < 8; r++) {
    const ray = new De(new os(0.55, 3.2, 0.2, 2, 0.05), new Ce({color: 0xfff0aa, roughness: 0.3}));
    const ang = r * Math.PI / 4;
    ray.position.set(Math.cos(ang) * 5.8, Math.sin(ang) * 5.8, 0);
    ray.rotation.z = ang;
    sunGroup.add(ray);
  }'''

sun_new = '''  // Radiant clay sun with soft golden glow halo
  const sunHalo = new De(new $t(5.2, 20, 16), new Ce({color: 0xffe066, roughness: 0.3, transparent: true, opacity: 0.45}));
  sunGroup.add(sunHalo);'''

bundle = bundle.replace(sun_old, sun_new)

# 2. Position the sign slightly higher (y = 13.8) so it's beautifully framed above the platform surface
old_sign_pos = 'signGroup.position.set(6.8, 13.0, -1.0);'
new_sign_pos = 'signGroup.position.set(7.2, 13.8, -1.2);'
bundle = bundle.replace(old_sign_pos, new_sign_pos)

# 3. Enhance Giuseppe's face & smile: wider smile, bigger white teeth, prominent black glasses
old_mouth = '''  // 3. Cheerful Radiant Smile with Upper White Teeth
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
  headGroup.add(mouthGroup);'''

new_mouth = '''  // 3. Cheerful Radiant Smile with Upper White Teeth (matching media_1790434143730.jpg)
  const mouthGroup = new U();
  mouthGroup.position.set(0, 0.18, 0.23);
  const mouthBg = new De(new os(0.16, 0.065, 0.02, 2, 0.008), mouthDarkMat);
  mouthGroup.add(mouthBg);
  // Brilliant white teeth row
  const teeth = new De(new os(0.14, 0.032, 0.02, 2, 0.004), teethMat);
  teeth.position.set(0, 0.016, 0.008);
  mouthGroup.add(teeth);
  // Soft friendly lips
  const lipUp = new De(new os(0.17, 0.016, 0.018, 2, 0.004), lipsMat);
  lipUp.position.set(0, 0.036, 0.008);
  const lipDown = new De(new os(0.15, 0.018, 0.018, 2, 0.004), lipsMat);
  lipDown.position.set(0, -0.032, 0.008);
  mouthGroup.add(lipUp, lipDown);
  headGroup.add(mouthGroup);'''

bundle = bundle.replace(old_mouth, new_mouth)

# 4. Make Trowel & Living Green Sprout 1.45x scale so leaves and scoop are clearly visible
bundle = bundle.replace('trowelProp.scale.setScalar(1.25);', 'trowelProp.scale.setScalar(1.45);')

# 5. Make sure the Duomo facade and Ficus are also mirrored/repeated across the level sections
# so that as Giuseppe advances through the level, the Augusta architecture and trees continue
with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("Applied final visual perfection!")
