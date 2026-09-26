# tools/snap_all_level_trees.py
import re

with open("tools/gta_all_10_levels.py", "r", encoding="utf-8") as f:
    text = f.read()

def snap_level_decor(lvl_code):
    plat_match = re.search(r"platforms:\s*\[([\s\S]*?)\]\s*,\s*decor:", lvl_code)
    if not plat_match:
        return lvl_code
    
    plats = []
    for p in re.finditer(r"S\(\"([^\"]+)\",\s*(-?[\d\.]+),\s*([\d\.]+),\s*([\d\.]+)", plat_match.group(1)):
        name, px, pw, py = p.group(1), float(p.group(2)), float(p.group(3)), float(p.group(4))
        if "pit" not in name and "spikes" not in name:
            plats.append((px - pw/2, px + pw/2, py))
            
    def get_ground_y(x):
        for x0, x1, y in plats:
            if x0 - 0.5 <= x <= x1 + 0.5:
                return y
        # fallback nearest platform
        best_d = 9999
        best_y = 14.0
        for x0, x1, y in plats:
            d = min(abs(x - x0), abs(x - x1))
            if d < best_d:
                best_d = d
                best_y = y
        return best_y

    def replace_decor_y(match):
        kind = match.group(1)
        x = float(match.group(2))
        old_y = float(match.group(3))
        rest = match.group(4)
        # Preserve background / sky objects
        if any(sky_word in kind for sky_word in ["fumo", "ciminiera", "torcia", "hangar-arch", "gozzo", "chiatta"]):
            return match.group(0)
        target_y = get_ground_y(x)
        return f'{{kind: "{kind}", x: {x:.1f}, y: {target_y:.1f}{rest}}}'

    decor_match = re.search(r"decor:\s*\[([\s\S]*?)\]\s*,\s*(?:stamps|coins|hazards)", lvl_code)
    if not decor_match:
        return lvl_code
    
    old_decor = decor_match.group(1)
    new_decor = re.sub(r'\{kind:\s*"([^"]+)",\s*x:\s*(-?[\d\.]+),\s*y:\s*(-?[\d\.]+)([^}]*)\}', replace_decor_y, old_decor)
    return lvl_code[:decor_match.start(1)] + new_decor + lvl_code[decor_match.end(1):]

# Process each level definition
level_blocks = re.split(r"(def get_level_\d+\(\):)", text)
for i in range(1, len(level_blocks), 2):
    header = level_blocks[i]
    body = level_blocks[i+1]
    level_blocks[i+1] = snap_level_decor(body)

new_text = "".join(level_blocks)
with open("tools/gta_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully snapped all ground decor and trees to exact platform heights across all 10 levels!")
