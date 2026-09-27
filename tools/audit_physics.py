import re
from tools.gta_all_10_levels import *

def check_physics(name, code):
    plat_pattern = re.compile(r'S\(["\']([^"\']+)["\'],\s*([-\d\.]+),\s*([-\d\.]+),\s*([-\d\.]+),\s*["\']([^"\']+)["\'](?:,\s*\{([^}]*)\})?\)')
    platforms = []
    for m in plat_pattern.finditer(code):
        pid, x, w, y, kind, extra = m.groups()
        x, w, y = float(x), float(w), float(y)
        if "spiked" in (extra or ""):
            continue
        if "optional" in (extra or ""):
            continue
        platforms.append({
            "id": pid, "x": x, "w": w, "y": y, "kind": kind,
            "x1": x - w/2.0, "x2": x + w/2.0, "extra": extra or ""
        })
    
    # Sort by x1
    platforms.sort(key=lambda p: p["x1"])
    print(f"=== PHYSICS AUDIT: {name} ({len(platforms)} platforms) ===")
    issues = []
    for i in range(len(platforms) - 1):
        p1 = platforms[i]
        p2 = platforms[i+1]
        gap_x = p2["x1"] - p1["x2"]
        delta_y = p2["y"] - p1["y"]
        
        # If platforms overlap in X, gap_x < 0
        # If gap_x > 4.5 and neither is a lift/ferry/spring
        has_mechanic = any(k in (p1["kind"], p2["kind"]) for k in ("lift", "ferry", "spring"))
        if gap_x > 4.5 and not has_mechanic:
            issues.append(f"GAP TOO WIDE: {p1['id']} -> {p2['id']} (gap_x={gap_x:.2f})")
            
        # Check vertical jump: if climbing without lift or spring
        if delta_y > 2.2 and not has_mechanic:
            issues.append(f"JUMP TOO HIGH: {p1['id']} -> {p2['id']} (dy={delta_y:.2f})")
            
    if issues:
        print(f"  [!] {len(issues)} ISSUES DETECTED:")
        for iss in issues:
            print("    ", iss)
    else:
        print("  [✓] All jumps strictly conform to athletic platforming physics!")
    return len(issues) == 0

levels = [
    ('L1', get_level_1()), ('L2', get_level_2()), ('L3', get_level_3()),
    ('L4', get_level_4()), ('L5', get_level_5()), ('L6', get_level_6()),
    ('L7', get_level_7()), ('L8', get_level_8()), ('L9', get_level_9()),
    ('L10', get_level_10())
]
ok = True
for name, code in levels:
    if not check_physics(name, code):
        ok = False
print("\nOVERALL PHYSICS AUDIT:", "PASSED 100%" if ok else "FAILED")
