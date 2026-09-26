# tools/update_levels_with_hazards.py
import re

with open("tools/gta_all_10_levels.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Level 1: Update hint & decor
l1_decor_patch = '''    {kind: "barocco-duomo", x: 236.0, y: 18.8, size: 18.0, z: -4.5},
    {kind: "vaso-terracotta-agave", x: 226.0, y: 17.8, size: 2.5, z: -1.5},
    {kind: "panchina-villa", x: 230.0, y: 18.8, size: 3.0, z: -1.5},
    {kind: "tree-sapling", x: 242.0, y: 18.8, size: 2.5, z: -1.5},
    {kind: "discarica-abusiva", x: 78.0, y: 13.8, size: 5.5, z: -2.8},
    {kind: "fumo-petrolchimico-nube", x: 120.0, y: 26.0, size: 14.0, z: -15.0},
    {kind: "scarico-fogna-liquami", x: 148.0, y: 16.0, size: 4.5, z: -2.5},
    {kind: "liquame-tossico-pozza", x: 156.0, y: 16.0, size: 3.5, z: -1.2},
    {kind: "ciminiera-fumo-animata", x: 180.0, y: 14.0, size: 20.0, z: -20.0}'''

code = code.replace(
    '''    {kind: "barocco-duomo", x: 236.0, y: 18.8, size: 18.0, z: -4.5},
    {kind: "vaso-terracotta-agave", x: 226.0, y: 17.8, size: 2.5, z: -1.5},
    {kind: "panchina-villa", x: 230.0, y: 18.8, size: 3.0, z: -1.5},
    {kind: "tree-sapling", x: 242.0, y: 18.8, size: 2.5, z: -1.5}''',
    l1_decor_patch
)

code = code.replace(
    'text: "Premi l\'interruttore della condotta per innaffiare le radici secolari e aprire la cancellata di Piazza Duomo!"',
    'text: "Cammina o salta sopra la valvola a terra per irrigare le radici secolari e aprire la cancellata di Piazza Duomo!"'
)

# 2. Level 2: Update sky, fog & decor
code = code.replace('sky: "#131f2b",\n  fog: "#1f3142",', 'sky: "#141e28",\n  fog: "#223140",')
l2_decor_patch = '''    {kind: "valvola-spurgo", x: 224.0, y: 16.6, size: 2.2, z: -1.2},
    {kind: "scarico-fogna-liquami", x: 22.0, y: 12.6, size: 5.0, z: -2.5},
    {kind: "fusto-tossico-sversato", x: 38.0, y: 13.8, size: 3.0, z: -1.2},
    {kind: "discarica-abusiva", x: 80.0, y: 12.6, size: 6.0, z: -3.0},
    {kind: "liquame-tossico-pozza", x: 146.0, y: 16.0, size: 4.0, z: -1.2},
    {kind: "rifiuti-plastica-costa", x: 172.0, y: 15.0, size: 4.5, z: -2.0},
    {kind: "fumo-petrolchimico-nube", x: 95.0, y: 24.0, size: 15.0, z: -14.0},
    {kind: "ciminiera-fumo-animata", x: 200.0, y: 14.0, size: 22.0, z: -18.0}'''

code = code.replace(
    '    {kind: "valvola-spurgo", x: 224.0, y: 16.6, size: 2.2, z: -1.2}',
    l2_decor_patch,
    1
)

# 3. Level 3: Update sky, fog & decor
code = code.replace('sky: "#183852",\n  fog: "#244c6e",', 'sky: "#193246",\n  fog: "#284660",')
l3_decor_patch = '''    {kind: "campanello-sos-costa", x: 216.0, y: 15.8, size: 3.0, z: -1.2},
    {kind: "scarico-fogna-liquami", x: 34.0, y: 13.0, size: 5.5, z: -2.8},
    {kind: "rifiuti-plastica-costa", x: 60.0, y: 12.5, size: 4.8, z: -2.2},
    {kind: "fumo-petrolchimico-nube", x: 105.0, y: 25.0, size: 15.0, z: -15.0},
    {kind: "torcia-petrolchimico-fiamma", x: 155.0, y: 14.0, size: 22.0, z: -18.0},
    {kind: "discarica-abusiva", x: 178.0, y: 15.0, size: 6.0, z: -3.0},
    {kind: "fusto-tossico-sversato", x: 194.0, y: 13.5, size: 3.0, z: -1.5}'''

code = code.replace(
    '    {kind: "campanello-sos-costa", x: 216.0, y: 15.8, size: 3.0, z: -1.2}',
    l3_decor_patch,
    1
)

# 4. Level 4: Update sky, fog & decor
code = code.replace('sky: "#21151e",\n  fog: "#361f30",', 'sky: "#261713",\n  fog: "#42281e",')
l4_decor_patch = '''    {kind: "traliccio-tubi", x: 218.0, y: 15.8, size: 7.5, z: -3.0},
    {kind: "ciminiera-fumo-animata", x: 42.0, y: 13.8, size: 22.0, z: -8.0},
    {kind: "torcia-petrolchimico-fiamma", x: 75.0, y: 12.6, size: 24.0, z: -7.0},
    {kind: "fusto-tossico-sversato", x: 92.0, y: 12.6, size: 3.2, z: -1.2},
    {kind: "liquame-tossico-pozza", x: 114.0, y: 14.0, size: 4.5, z: -1.4},
    {kind: "discarica-abusiva", x: 160.0, y: 16.0, size: 6.5, z: -3.5},
    {kind: "fumo-petrolchimico-nube", x: 60.0, y: 26.0, size: 16.0, z: -12.0},
    {kind: "fumo-petrolchimico-nube", x: 180.0, y: 27.0, size: 18.0, z: -14.0}'''

code = code.replace(
    '    {kind: "traliccio-tubi", x: 218.0, y: 15.8, size: 7.5, z: -3.0}',
    l4_decor_patch,
    1
)

# 5. Level 5: Update sky, fog & decor
code = code.replace('sky: "#19222d",\n  fog: "#253443",', 'sky: "#1a232e",\n  fog: "#2a3746",')
l5_decor_patch = '''    {kind: "cartello-bonifica", x: 216.0, y: 27.6, size: 2.8, z: -1.2},
    {kind: "discarica-abusiva", x: 26.0, y: 24.5, size: 6.5, z: -3.0},
    {kind: "scarico-fogna-liquami", x: 70.0, y: 24.0, size: 5.0, z: -2.5},
    {kind: "fusto-tossico-sversato", x: 110.0, y: 25.4, size: 3.2, z: -1.2},
    {kind: "fumo-petrolchimico-nube", x: 130.0, y: 35.0, size: 16.0, z: -15.0},
    {kind: "rifiuti-plastica-costa", x: 175.0, y: 27.0, size: 4.8, z: -2.0},
    {kind: "ciminiera-fumo-animata", x: 210.0, y: 26.0, size: 22.0, z: -18.0}'''

code = code.replace(
    '    {kind: "cartello-bonifica", x: 216.0, y: 27.6, size: 2.8, z: -1.2}',
    l5_decor_patch,
    1
)

# 6. Level 6: Update sky, fog & decor
code = code.replace('sky: "#24191a",\n  fog: "#382326",', 'sky: "#24181a",\n  fog: "#392226",')
l6_decor_patch = '''    {kind: "stemma-federico", x: 220.0, y: 19.8, size: 3.0, z: -1.5},
    {kind: "scarico-fogna-liquami", x: 35.0, y: 16.6, size: 5.0, z: -2.5},
    {kind: "discarica-abusiva", x: 80.0, y: 15.4, size: 6.0, z: -3.0},
    {kind: "fusto-tossico-sversato", x: 120.0, y: 17.0, size: 3.0, z: -1.2},
    {kind: "fumo-petrolchimico-nube", x: 150.0, y: 28.0, size: 15.0, z: -15.0},
    {kind: "torcia-petrolchimico-fiamma", x: 190.0, y: 17.0, size: 22.0, z: -18.0}'''

code = code.replace(
    '    {kind: "stemma-federico", x: 220.0, y: 19.8, size: 3.0, z: -1.5}',
    l6_decor_patch,
    1
)

# 7. Level 7: Update decor
l7_decor_patch = '''    {kind: "campana-nebbia", x: 218.0, y: 20.8, size: 2.6, z: -1.2},
    {kind: "rifiuti-plastica-costa", x: 24.0, y: 16.6, size: 4.8, z: -2.0},
    {kind: "fusto-tossico-sversato", x: 60.0, y: 16.4, size: 3.2, z: -1.2},
    {kind: "rifiuti-plastica-costa", x: 110.0, y: 17.0, size: 5.0, z: -2.0},
    {kind: "discarica-abusiva", x: 150.0, y: 20.0, size: 6.5, z: -3.2},
    {kind: "fumo-petrolchimico-nube", x: 140.0, y: 30.0, size: 16.0, z: -16.0},
    {kind: "torcia-petrolchimico-fiamma", x: 195.0, y: 18.0, size: 22.0, z: -18.0}'''

code = code.replace(
    '    {kind: "campana-nebbia", x: 218.0, y: 20.8, size: 2.6, z: -1.2}',
    l7_decor_patch,
    1
)

# 8. Level 8: Update decor
l8_decor_patch = '''    {kind: "salt-windmill", x: 218.0, y: 16.8, size: 6.5, z: -3.5},
    {kind: "liquame-tossico-pozza", x: 65.0, y: 13.4, size: 4.0, z: -1.5},
    {kind: "scarico-fogna-liquami", x: 112.0, y: 15.0, size: 5.0, z: -2.5},
    {kind: "discarica-abusiva", x: 155.0, y: 17.0, size: 6.0, z: -3.0},
    {kind: "fumo-petrolchimico-nube", x: 170.0, y: 28.0, size: 16.0, z: -15.0},
    {kind: "ciminiera-fumo-animata", x: 215.0, y: 15.0, size: 22.0, z: -18.0}'''

code = code.replace(
    '    {kind: "salt-windmill", x: 218.0, y: 16.8, size: 6.5, z: -3.5}',
    l8_decor_patch,
    1
)

# 9. Level 9: Update sky, fog & decor
code = code.replace('sky: "#151e28",\n  fog: "#243242",', 'sky: "#161f2a",\n  fog: "#263546",')
l9_decor_patch = '''    {kind: "cannone-borbonico", x: 220.0, y: 20.8, size: 3.5, z: -1.6},
    {kind: "ciminiera-fumo-animata", x: 30.0, y: 16.6, size: 22.0, z: -16.0},
    {kind: "fumo-petrolchimico-nube", x: 70.0, y: 30.0, size: 17.0, z: -14.0},
    {kind: "torcia-petrolchimico-fiamma", x: 115.0, y: 17.0, size: 24.0, z: -18.0},
    {kind: "discarica-abusiva", x: 145.0, y: 20.0, size: 6.0, z: -3.0},
    {kind: "liquame-tossico-pozza", x: 175.0, y: 19.0, size: 4.2, z: -1.4},
    {kind: "fusto-tossico-sversato", x: 205.0, y: 19.8, size: 3.2, z: -1.2}'''

code = code.replace(
    '    {kind: "cannone-borbonico", x: 220.0, y: 20.8, size: 3.5, z: -1.6}',
    l9_decor_patch,
    1
)

# 10. Level 10: Update sky, fog & decor
code = code.replace('sky: "#19283e",\n  fog: "#2b4060",', 'sky: "#1a6faa",\n  fog: "#449cd6",')
l10_decor_patch = '''    {kind: "vaso-caltagirone", x: 230.0, y: 21.8, size: 3.2, z: -1.2},
    {kind: "discarica-abusiva", x: 24.0, y: 17.6, size: 5.0, z: -3.0},
    {kind: "rifiuti-plastica-costa", x: 60.0, y: 17.4, size: 4.2, z: -2.2},
    {kind: "ficus-centenario", x: 130.0, y: 20.0, size: 14.0, z: -4.5},
    {kind: "fountain-augusta", x: 180.0, y: 20.0, size: 4.5, z: -2.5},
    {kind: "ficus-centenario", x: 225.0, y: 20.8, size: 15.0, z: -5.0}'''

code = code.replace(
    '    {kind: "vaso-caltagirone", x: 230.0, y: 21.8, size: 3.2, z: -1.2}',
    l10_decor_patch,
    1
)

with open("tools/gta_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(code)

print("[✓] Successfully updated tools/gta_all_10_levels.py with environmental hazards and skies!")
