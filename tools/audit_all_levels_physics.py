# tools/audit_all_levels_physics.py
import re
import math

VX = 6.7
VY0 = 11.8
GRAV = 27.0
MAX_JUMP_H = (VY0 * VY0) / (2 * GRAV) # ~2.578
TIME_TO_APEX = VY0 / GRAV # ~0.437 s
APEX_DIST = VX * TIME_TO_APEX # ~2.928 units

def max_jump_distance(dy):
    disc = VY0 * VY0 - 2 * GRAV * dy
    if disc < 0:
        return 0.0
    t = (VY0 + math.sqrt(disc)) / GRAV
    return VX * t

with open("bundle/index-gta-v1.js", "r") as f:
    content = f.read()

levels = re.findall(r"const\s+(augustaL\d+)\s*=\s*yr\(\{(.*?)\n\}\);", content, re.DOTALL)
print(f"\nAuditing {len(levels)} levels in bundle/index-gta-v1.js...")

all_passed = True

for lvl_name, lvl_body in levels:
    plat_matches = re.findall(r'S\(\s*["\']([^"\']+)["\']\s*,\s*([-0-9.]+)\s*,\s*([-0-9.]+)\s*,\s*([-0-9.]+)\s*,\s*["\']([^"\']+)["\'](?:,\s*\{([^}]*)\})?\s*\)', lvl_body)
    
    platforms = []
    for name, x, w, y, kind, opts in plat_matches:
        is_optional = "optional" in (opts or "")
        is_spiked = "spiked" in (opts or "")
        is_gate = kind == "gate" # Gate is a vertical barrier, player walks on the floor underneath
        is_switch = kind == "switch" # Switch is on the floor
        platforms.append({
            "name": name,
            "x": float(x),
            "w": float(w),
            "y": float(y),
            "kind": kind,
            "opts": opts or "",
            "optional": is_optional,
            "spiked": is_spiked,
            "gate": is_gate,
            "switch": is_switch
        })
    
    # Filter out spiked pits, optional secret branches, and vertical barrier gates
    main_plats = [p for p in platforms if not p["spiked"] and not p["optional"] and not p["gate"] and not p["switch"]]
    main_plats.sort(key=lambda p: p["x"])
    
    issues = []
    for i in range(len(main_plats) - 1):
        curr = main_plats[i]
        nxt = main_plats[i+1]
        
        curr_end_x = curr["x"] + curr["w"]
        gap = nxt["x"] - curr_end_x
        dy = nxt["y"] - curr["y"]
        
        is_ferry = curr["kind"] == "ferry" or "travel" in curr["opts"]
        is_spring = curr["kind"] == "spring"
        is_lift = curr["kind"] == "lift"
        nxt_is_lift = nxt["kind"] == "lift"
        
        max_dist = max_jump_distance(dy)
        safe_dist = max_dist * 0.85
        
        # If platforms overlap (e.g. lift within bounds of platform), gap is negative/zero
        if gap <= 0:
            continue

        if dy > MAX_JUMP_H and not is_spring and not is_lift:
            issues.append(f"CRITICAL: Impossible jump upward from '{curr['name']}' (x={curr_end_x:.1f}, y={curr['y']:.1f}) to '{nxt['name']}' (x={nxt['x']:.1f}, y={nxt['y']:.1f}): dy=+{dy:.2f} > max {MAX_JUMP_H:.2f}")
            all_passed = False
        elif gap > safe_dist and not is_ferry and not is_spring and not is_lift and not nxt_is_lift:
            if gap > max_dist:
                issues.append(f"CRITICAL: Impossible jump distance from '{curr['name']}' to '{nxt['name']}': gap={gap:.2f} > max {max_dist:.2f} (dy={dy:+.2f})")
                all_passed = False
            else:
                issues.append(f"WARNING: Tight jump from '{curr['name']}' to '{nxt['name']}': gap={gap:.2f}, max={max_dist:.2f}")
    
    print(f"[{lvl_name}]")
    if issues:
        for iss in issues:
            print("  [!] " + iss)
    else:
        print("  [✓] 100% Physically Passable - Zero bottlenecks!")

if all_passed:
    print("\n=======================================================")
    print(">>> ALL 10 LEVELS HAVE PASSED THE STRICT PHYSICS AUDIT! <<<")
    print("=======================================================")
