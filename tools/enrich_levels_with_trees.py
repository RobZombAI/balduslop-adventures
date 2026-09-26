# tools/enrich_levels_with_trees.py
import re

with open("tools/gta_all_10_levels.py", "r", encoding="utf-8") as f:
    text = f.read()

tree_additions = {
    1: [
        '{kind: "ficus-centenario", x: 8.0, y: 13.0, size: 14.0, z: -1.2}',
        '{kind: "palma-augusta", x: 28.0, y: 15.2, size: 8.5, z: -1.0}',
        '{kind: "arancio-siciliano", x: 38.0, y: 15.2, size: 6.0, z: -0.8}',
        '{kind: "tree-sapling", x: 68.0, y: 14.2, size: 4.0, z: -0.6}',
        '{kind: "olivo-secolare", x: 100.0, y: 13.8, size: 7.0, z: -1.2}',
        '{kind: "arancio-siciliano", x: 112.0, y: 11.2, size: 6.0, z: -0.8}',
        '{kind: "ficus-centenario", x: 140.0, y: 16.2, size: 13.0, z: -1.5}',
        '{kind: "palma-augusta", x: 182.0, y: 15.6, size: 9.0, z: -1.0}',
        '{kind: "olivo-secolare", x: 215.0, y: 15.8, size: 7.5, z: -1.2}',
        '{kind: "tree-sapling", x: 228.0, y: 17.8, size: 4.2, z: -0.6}'
    ],
    2: [
        '{kind: "palma-augusta", x: 8.0, y: 11.0, size: 8.5, z: -1.0}',
        '{kind: "palma-augusta", x: 28.0, y: 12.6, size: 8.5, z: -1.0}',
        '{kind: "tree-sapling", x: 45.0, y: 13.8, size: 3.8, z: -0.6}',
        '{kind: "olivo-secolare", x: 68.0, y: 12.6, size: 6.5, z: -1.2}',
        '{kind: "ficus-centenario", x: 92.0, y: 14.2, size: 13.0, z: -1.5}',
        '{kind: "palma-augusta", x: 115.0, y: 13.8, size: 9.0, z: -1.0}',
        '{kind: "arancio-siciliano", x: 135.0, y: 16.0, size: 6.0, z: -0.8}',
        '{kind: "tree-sapling", x: 160.0, y: 15.0, size: 4.0, z: -0.6}',
        '{kind: "palma-augusta", x: 185.0, y: 15.5, size: 8.5, z: -1.0}',
        '{kind: "ficus-rinascita", x: 215.0, y: 16.6, size: 5.5, z: -0.8}'
    ],
    3: [
        '{kind: "olivo-secolare", x: 10.0, y: 12.0, size: 7.0, z: -1.0}',
        '{kind: "ficus-centenario", x: 28.0, y: 12.8, size: 13.5, z: -1.5}',
        '{kind: "tree-sapling", x: 50.0, y: 12.5, size: 4.0, z: -0.6}',
        '{kind: "palma-augusta", x: 75.0, y: 13.2, size: 8.5, z: -1.0}',
        '{kind: "olivo-secolare", x: 98.0, y: 14.0, size: 6.5, z: -1.2}',
        '{kind: "arancio-siciliano", x: 125.0, y: 15.2, size: 6.0, z: -0.8}',
        '{kind: "tree-sapling", x: 145.0, y: 15.0, size: 4.0, z: -0.6}',
        '{kind: "ficus-centenario", x: 170.0, y: 15.0, size: 12.0, z: -1.5}',
        '{kind: "palma-augusta", x: 200.0, y: 15.8, size: 8.5, z: -1.0}',
        '{kind: "ficus-rinascita", x: 225.0, y: 16.0, size: 5.5, z: -0.8}'
    ],
    4: [
        '{kind: "ficus-centenario", x: 15.0, y: 12.0, size: 14.0, z: -1.5}',
        '{kind: "palma-augusta", x: 32.0, y: 12.6, size: 9.0, z: -1.0}',
        '{kind: "olivo-secolare", x: 55.0, y: 13.5, size: 7.0, z: -1.2}',
        '{kind: "tree-sapling", x: 75.0, y: 14.0, size: 4.0, z: -0.6}',
        '{kind: "arancio-siciliano", x: 100.0, y: 14.5, size: 6.0, z: -0.8}',
        '{kind: "ficus-centenario", x: 125.0, y: 15.0, size: 13.0, z: -1.5}',
        '{kind: "palma-augusta", x: 155.0, y: 15.5, size: 8.5, z: -1.0}',
        '{kind: "olivo-secolare", x: 180.0, y: 16.0, size: 6.8, z: -1.2}',
        '{kind: "tree-sapling", x: 205.0, y: 16.5, size: 4.2, z: -0.6}',
        '{kind: "ficus-rinascita", x: 230.0, y: 17.0, size: 5.5, z: -0.8}'
    ],
    5: [
        '{kind: "arancio-siciliano", x: 15.0, y: 24.0, size: 6.5, z: -0.8}',
        '{kind: "palma-augusta", x: 35.0, y: 24.5, size: 9.0, z: -1.0}',
        '{kind: "olivo-secolare", x: 60.0, y: 25.0, size: 7.2, z: -1.2}',
        '{kind: "ficus-centenario", x: 85.0, y: 25.5, size: 14.0, z: -1.5}',
        '{kind: "tree-sapling", x: 110.0, y: 26.0, size: 4.0, z: -0.6}',
        '{kind: "arancio-siciliano", x: 135.0, y: 26.0, size: 6.0, z: -0.8}',
        '{kind: "palma-augusta", x: 165.0, y: 26.5, size: 8.5, z: -1.0}',
        '{kind: "olivo-secolare", x: 190.0, y: 27.0, size: 7.0, z: -1.2}',
        '{kind: "tree-sapling", x: 215.0, y: 27.5, size: 4.2, z: -0.6}',
        '{kind: "ficus-rinascita", x: 235.0, y: 28.0, size: 5.5, z: -0.8}'
    ],
    6: [
        '{kind: "palma-augusta", x: 16.0, y: 15.0, size: 8.5, z: -1.0}',
        '{kind: "olivo-secolare", x: 38.0, y: 16.0, size: 7.0, z: -1.2}',
        '{kind: "palma-augusta", x: 62.0, y: 16.5, size: 9.0, z: -1.0}',
        '{kind: "tree-sapling", x: 85.0, y: 17.0, size: 4.0, z: -0.6}',
        '{kind: "ficus-centenario", x: 110.0, y: 17.5, size: 13.0, z: -1.5}',
        '{kind: "arancio-siciliano", x: 135.0, y: 17.5, size: 6.0, z: -0.8}',
        '{kind: "olivo-secolare", x: 160.0, y: 18.0, size: 6.8, z: -1.2}',
        '{kind: "palma-augusta", x: 185.0, y: 18.5, size: 8.5, z: -1.0}',
        '{kind: "tree-sapling", x: 210.0, y: 19.0, size: 4.2, z: -0.6}',
        '{kind: "ficus-rinascita", x: 235.0, y: 19.5, size: 5.5, z: -0.8}'
    ],
    7: [
        '{kind: "palma-augusta", x: 14.0, y: 15.0, size: 8.5, z: -1.0}',
        '{kind: "olivo-secolare", x: 36.0, y: 15.8, size: 6.8, z: -1.2}',
        '{kind: "tree-sapling", x: 58.0, y: 16.2, size: 4.0, z: -0.6}',
        '{kind: "ficus-centenario", x: 82.0, y: 16.8, size: 13.5, z: -1.5}',
        '{kind: "palma-augusta", x: 108.0, y: 17.0, size: 9.0, z: -1.0}',
        '{kind: "arancio-siciliano", x: 132.0, y: 17.5, size: 6.0, z: -0.8}',
        '{kind: "olivo-secolare", x: 158.0, y: 18.0, size: 7.0, z: -1.2}',
        '{kind: "tree-sapling", x: 182.0, y: 18.5, size: 4.0, z: -0.6}',
        '{kind: "palma-augusta", x: 208.0, y: 19.0, size: 8.5, z: -1.0}',
        '{kind: "ficus-rinascita", x: 232.0, y: 19.5, size: 5.5, z: -0.8}'
    ],
    8: [
        '{kind: "palma-augusta", x: 12.0, y: 12.5, size: 8.5, z: -1.0}',
        '{kind: "arancio-siciliano", x: 30.0, y: 13.0, size: 6.2, z: -0.8}',
        '{kind: "ficus-centenario", x: 52.0, y: 13.6, size: 13.0, z: -1.5}',
        '{kind: "tree-sapling", x: 72.0, y: 14.0, size: 4.0, z: -0.6}',
        '{kind: "olivo-secolare", x: 96.0, y: 14.5, size: 7.0, z: -1.2}',
        '{kind: "palma-augusta", x: 120.0, y: 15.0, size: 9.0, z: -1.0}',
        '{kind: "arancio-siciliano", x: 148.0, y: 15.5, size: 6.0, z: -0.8}',
        '{kind: "olivo-secolare", x: 172.0, y: 16.0, size: 6.8, z: -1.2}',
        '{kind: "tree-sapling", x: 198.0, y: 16.5, size: 4.2, z: -0.6}',
        '{kind: "ficus-rinascita", x: 226.0, y: 17.0, size: 5.5, z: -0.8}'
    ],
    9: [
        '{kind: "ficus-centenario", x: 15.0, y: 15.0, size: 14.0, z: -1.2}',
        '{kind: "palma-augusta", x: 35.0, y: 15.8, size: 8.5, z: -1.0}',
        '{kind: "arancio-siciliano", x: 55.0, y: 16.2, size: 6.0, z: -0.8}',
        '{kind: "tree-sapling", x: 75.0, y: 16.6, size: 4.0, z: -0.6}',
        '{kind: "ficus-centenario", x: 102.0, y: 17.0, size: 13.5, z: -1.5}',
        '{kind: "olivo-secolare", x: 128.0, y: 17.5, size: 7.0, z: -1.2}',
        '{kind: "palma-augusta", x: 152.0, y: 18.0, size: 9.0, z: -1.0}',
        '{kind: "arancio-siciliano", x: 176.0, y: 18.5, size: 6.0, z: -0.8}',
        '{kind: "tree-sapling", x: 202.0, y: 19.0, size: 4.2, z: -0.6}',
        '{kind: "ficus-rinascita", x: 228.0, y: 19.5, size: 5.5, z: -0.8}'
    ],
    10: [
        '{kind: "ficus-centenario", x: 15.0, y: 16.0, size: 14.0, z: -1.2}',
        '{kind: "palma-augusta", x: 25.0, y: 16.8, size: 9.0, z: -0.8}',
        '{kind: "arancio-siciliano", x: 38.0, y: 17.2, size: 6.5, z: -0.8}',
        '{kind: "tree-sapling", x: 50.0, y: 17.6, size: 4.2, z: -0.6}',
        '{kind: "ficus-centenario", x: 72.0, y: 18.0, size: 14.5, z: -1.5}',
        '{kind: "olivo-secolare", x: 92.0, y: 18.5, size: 7.5, z: -1.2}',
        '{kind: "palma-augusta", x: 112.0, y: 19.0, size: 9.5, z: -0.8}',
        '{kind: "ficus-centenario", x: 135.0, y: 19.5, size: 15.0, z: -1.5}',
        '{kind: "arancio-siciliano", x: 158.0, y: 20.0, size: 6.5, z: -0.8}',
        '{kind: "tree-sapling", x: 178.0, y: 20.5, size: 4.5, z: -0.6}',
        '{kind: "ficus-centenario", x: 200.0, y: 21.0, size: 14.0, z: -1.2}',
        '{kind: "palma-augusta", x: 215.0, y: 21.5, size: 9.0, z: -0.8}'
    ]
}

matches = list(re.finditer(r"decor:\s*\[", text))
print("Found decor matches:", len(matches))

# Process from last to first so indices do not shift!
for lvl in range(10, 0, -1):
    m = matches[lvl - 1]
    idx = m.end()
    trees = tree_additions[lvl]
    tree_str = "\n    " + ",\n    ".join(trees) + ","
    text = text[:idx] + tree_str + text[idx:]

with open("tools/gta_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully injected 10-12 foreground trees into all 10 levels of tools/gta_all_10_levels.py!")
