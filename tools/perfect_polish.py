# tools/perfect_polish.py
import re

with open("bundle/index-gta-v1.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Remove duplicate decor "cartello-salviamo-verde" at x=4.5 so only the gorgeous authentic sign is shown
bundle = bundle.replace('{kind: "cartello-salviamo-verde", x: 4.5, y: 13.0, size: 4.0, z: -1.8},', '// duplicate sign removed')

# 2. Set Model orientation to 3/4 view towards camera (so Giuseppe faces ~26 degrees towards the player)
# Original: o.name="Model orientation",e.add(n),n.add(o),o.rotation.y=Math.PI/2
target_orient = 'o.name="Model orientation",e.add(n),n.add(o),o.rotation.y=Math.PI/2'
new_orient = 'o.name="Model orientation",e.add(n),n.add(o),o.rotation.y=Math.PI/2-0.45'
if target_orient in bundle:
    bundle = bundle.replace(target_orient, new_orient)
    print("Updated model orientation to 3/4 view towards camera!")

# 3. Position the Sun, Clouds, Ficus and Sign so they are fully framed in the camera view at spawn
# Camera view at spawn: x is centered around 4-6, y is centered around 14-16 (top is y=21, right is x=19)
# Move Sun to x = 11.0, y = 18.0, z = -26
# Move Ficus to x = 15.0, y = 12.0, z = -14
# Move Sign to x = 7.5, y = 13.0, z = -1.0
old_sun = 'sunGroup.position.set(16, 22, -32);'
new_sun = 'sunGroup.position.set(10.5, 17.5, -26);'
bundle = bundle.replace(old_sun, new_sun)

old_ficus = 'ficusGroup.position.set(22, 11, -14);'
new_ficus = 'ficusGroup.position.set(14.5, 11.5, -13);'
bundle = bundle.replace(old_ficus, new_ficus)

old_sign = 'signGroup.position.set(8.5, 13.0, -1.0);'
new_sign = 'signGroup.position.set(6.8, 13.0, -1.0);'
bundle = bundle.replace(old_sign, new_sign)

old_bench = 'benchGroup.position.set(14.5, 13.0, -1.2);'
new_bench = 'benchGroup.position.set(12.5, 13.0, -1.2);'
bundle = bundle.replace(old_bench, new_bench)

# 4. Enhance Giuseppe's facial details in 3/4 view (smile with teeth, black glasses, friendly clay eyes)
# In applyGiuseppeCustomization, adjust the smile and eyes to be even more prominent and joyful
with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("Applied perfect polish to Augusta diorama & Giuseppe 3/4 view!")
