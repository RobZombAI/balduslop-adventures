import json, re

def audit_level(level_name, code):
    # Parse platforms
    # S("start", -8, 16, 13, "stone")
    plat_pattern = re.compile(r'S\(["\']([^"\']+)["\'],\s*([-\d\.]+),\s*([-\d\.]+),\s*([-\d\.]+),\s*["\']([^"\']+)["\'](?:,\s*\{([^}]*)\})?\)')
    platforms = []
    for m in plat_pattern.finditer(code):
        pid, x, w, y, kind, extra = m.groups()
        x, w, y = float(x), float(w), float(y)
        platforms.append({
            "id": pid, "x": x, "w": w, "y": y, "kind": kind,
            "x1": x - w/2.0, "x2": x + w/2.0, "extra": extra or ""
        })
    
    # Parse trees
    tree_pattern = re.compile(r'\{kind:\s*["\'](ficus-centenario|palma-augusta|palma-dattilifera|arancio-siciliano|olivo-secolare|tree-sapling|ficus-rinascita|secular-ficus)["\'],\s*x:\s*([-\d\.]+),\s*y:\s*([-\d\.]+)')
    trees = []
    for m in tree_pattern.finditer(code):
        kind, tx, ty = m.groups()
        trees.append({"kind": kind, "x": float(tx), "y": float(ty)})
        
    print(f"=== {level_name} ===")
    print(f"Platforms: {len(platforms)}, Trees: {len(trees)}")
    
    # Verify trees
    tree_errors = []
    for t in trees:
        # Find solid stone platform
        found = False
        for p in platforms:
            if p["kind"] in ("stone", "terrain"):
                if p["x1"] - 0.2 <= t["x"] <= p["x2"] + 0.2:
                    if abs(t["y"] - p["y"]) < 0.3:
                        found = True
                        break
        if not found:
            tree_errors.append(f"UNANCHORED TREE: {t['kind']} at x={t['x']}, y={t['y']}")
            
    if tree_errors:
        print(f"  [!] {len(tree_errors)} TREE ERRORS:")
        for err in tree_errors[:5]:
            print("    ", err)
    else:
        print("  [✓] All trees perfectly grounded on solid stone platforms!")
        
    return len(tree_errors) == 0

