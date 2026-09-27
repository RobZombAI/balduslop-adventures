# tools/apply_perfect_tree_offsets.py
import re

print("=== APPLYING PERFECT TREE OFFSETS ACROSS ALL 10 LEVELS ===")

with open("tools/generate_all_10_levels.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace decor blocks for each level with strictly verified positions:

l1_decor = '''  decor: [
    {kind: "ficus-centenario", x: -4.0, y: 13.0, size: 14.0, z: -1.2},
    {kind: "palma-augusta", x: 1.0, y: 13.0, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 8.5, y: 13.6, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 18.0, y: 14.4, size: 6.5, z: -1.2},
    {kind: "palma-augusta", x: 38.5, y: 15.2, size: 8.5, z: -1.0},
    {kind: "ficus-centenario", x: 52.0, y: 15.2, size: 14.0, z: -1.5},
    {kind: "tree-sapling", x: 66.5, y: 14.2, size: 3.8, z: -0.6},
    {kind: "olivo-secolare", x: 94.5, y: 13.8, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 106.0, y: 11.2, size: 5.8, z: -0.8},
    {kind: "palma-augusta", x: 151.0, y: 16.0, size: 9.0, z: -1.0},
    {kind: "tree-sapling", x: 156.0, y: 16.0, size: 4.0, z: -0.6},
    {kind: "ficus-centenario", x: 168.0, y: 16.0, size: 13.5, z: -1.5},
    {kind: "arancio-siciliano", x: 190.5, y: 15.0, size: 6.0, z: -0.8},
    {kind: "palma-augusta", x: 208.0, y: 16.0, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 217.0, y: 16.5, size: 7.2, z: -1.2},
    {kind: "ficus-rinascita", x: 238.0, y: 18.8, size: 6.5, z: -0.8},
    {kind: "tree-sapling", x: 244.0, y: 18.8, size: 4.2, z: -0.6},
    {kind: "cartello-salviamo-verde", x: -1.0, y: 13.0, size: 4.0, z: -1.8},
    {kind: "panchina-villa", x: 2.0, y: 13.0, size: 3.0, z: -1.5},
    {kind: "vaso-terracotta-agave", x: 17.0, y: 14.4, size: 2.2, z: -1.2},
    {kind: "cato-carrucola-acqua", x: 65.0, y: 14.2, size: 7.0, z: -1.5},
    {kind: "ficus-chioma-attraversabile", x: 76.0, y: 14.4, size: 13.5, z: -2.6},
    {kind: "balustrata-xifonio", x: 106.0, y: 11.2, size: 4.5, z: -2.5},
    {kind: "gozzo-xifonio", x: 118.0, y: 7.5, size: 5.5, z: -10.0},
    {kind: "fountain-augusta", x: 190.0, y: 15.0, size: 4.0, z: -2.5},
    {kind: "barocco-duomo", x: 235.0, y: 18.8, size: 18.0, z: -4.5},
    {kind: "fumo-petrolchimico-nube", x: 120.0, y: 26.0, size: 14.0, z: -15.0}
  ]'''

l2_decor = '''  decor: [
    {kind: "palma-augusta", x: -4.0, y: 9.0, size: 8.5, z: -1.0},
    {kind: "palma-augusta", x: 1.0, y: 9.0, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 7.8, y: 9.6, size: 6.2, z: -1.2},
    {kind: "arancio-siciliano", x: 16.0, y: 10.4, size: 5.5, z: -0.8},
    {kind: "palma-augusta", x: 31.0, y: 11.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 45.0, y: 12.0, size: 3.8, z: -0.6},
    {kind: "olivo-secolare", x: 80.0, y: 12.0, size: 6.8, z: -1.2},
    {kind: "palma-augusta", x: 90.0, y: 12.2, size: 9.0, z: -1.0},
    {kind: "arancio-siciliano", x: 136.0, y: 13.5, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 145.0, y: 13.5, size: 4.0, z: -0.6},
    {kind: "palma-augusta", x: 153.0, y: 13.5, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 175.5, y: 12.8, size: 6.5, z: -1.2},
    {kind: "tree-sapling", x: 193.0, y: 13.2, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 13.5, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 14.8, size: 6.0, z: -0.8},
    {kind: "arancio-siciliano", x: 239.0, y: 14.8, size: 5.5, z: -0.8},
    {kind: "fiume-fognatura-reflui", x: 55.0, y: 6.0, size: 14.0, z: -2.0},
    {kind: "scarico-fogna-liquami", x: 38.0, y: 11.5, size: 4.5, z: -2.0},
    {kind: "sewer-manhole", x: 3.0, y: 9.6, size: 2.2, z: -1.2},
    {kind: "pompa-idrovora", x: 42.0, y: 12.0, size: 2.8, z: -1.5},
    {kind: "valvola-spurgo", x: 44.5, y: 12.0, size: 2.2, z: -1.0},
    {kind: "gru-portuale-rossini", x: 88.0, y: 12.2, size: 16.0, z: -4.5},
    {kind: "chiatta-megara", x: 152.0, y: 11.0, size: 13.0, z: -5.0},
    {kind: "salvagente-rossini", x: 175.0, y: 12.8, size: 1.8, z: -1.2},
    {kind: "rifiuti-plastica-costa", x: 16.0, y: 10.4, size: 4.0, z: -1.8},
    {kind: "fumo-petrolchimico-nube", x: 100.0, y: 25.0, size: 16.0, z: -15.0}
  ]'''

l3_decor = '''  decor: [
    {kind: "olivo-secolare", x: -4.0, y: 11.0, size: 7.0, z: -1.2},
    {kind: "tree-sapling", x: 2.0, y: 11.0, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 8.5, y: 12.2, size: 6.5, z: -1.2},
    {kind: "arancio-siciliano", x: 17.0, y: 13.8, size: 5.5, z: -0.8},
    {kind: "tree-sapling", x: 33.0, y: 16.5, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 48.5, y: 17.0, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 82.0, y: 17.5, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 92.0, y: 18.0, size: 5.8, z: -0.8},
    {kind: "palma-augusta", x: 136.0, y: 22.0, size: 9.0, z: -1.0},
    {kind: "tree-sapling", x: 145.0, y: 22.0, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 153.0, y: 22.0, size: 6.8, z: -1.2},
    {kind: "arancio-siciliano", x: 175.5, y: 21.0, size: 6.0, z: -0.8},
    {kind: "palma-augusta", x: 193.0, y: 21.5, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 208.0, y: 22.5, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 233.0, y: 23.8, size: 4.2, z: -0.6},
    {kind: "olivo-secolare", x: 239.0, y: 23.8, size: 7.0, z: -1.2},
    {kind: "fiume-petrolio-greggio", x: 60.0, y: 4.5, size: 14.0, z: -2.0},
    {kind: "fusto-tossico-sversato", x: 33.0, y: 16.5, size: 3.0, z: -1.2},
    {kind: "traliccio-tubi", x: 17.0, y: 13.8, size: 8.0, z: -3.0},
    {kind: "oil-tank", x: 82.0, y: 17.5, size: 14.0, z: -6.0},
    {kind: "ciminiera-fumo-animata", x: 105.0, y: 20.0, size: 22.0, z: -16.0},
    {kind: "torcia-petrolchimico-fiamma", x: 165.0, y: 21.0, size: 24.0, z: -18.0}
  ]'''

l4_decor = '''  decor: [
    {kind: "olivo-secolare", x: -4.0, y: 12.0, size: 7.2, z: -1.2},
    {kind: "palma-augusta", x: 2.0, y: 12.0, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 8.5, y: 13.0, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 17.0, y: 14.4, size: 6.8, z: -1.2},
    {kind: "tree-sapling", x: 33.0, y: 16.8, size: 4.0, z: -0.6},
    {kind: "palma-augusta", x: 48.5, y: 17.4, size: 9.0, z: -1.0},
    {kind: "olivo-secolare", x: 82.0, y: 18.5, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 92.0, y: 19.5, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 136.0, y: 26.5, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 145.0, y: 26.5, size: 9.0, z: -1.0},
    {kind: "olivo-secolare", x: 153.0, y: 26.5, size: 7.0, z: -1.2},
    {kind: "tree-sapling", x: 175.5, y: 24.5, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 193.0, y: 24.8, size: 6.0, z: -0.8},
    {kind: "palma-augusta", x: 208.0, y: 26.0, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 27.8, size: 6.2, z: -0.8},
    {kind: "tree-sapling", x: 239.0, y: 27.8, size: 4.0, z: -0.6},
    {kind: "colata-cemento-fresco", x: 60.0, y: 6.0, size: 14.0, z: -2.0},
    {kind: "hangar-arch", x: 10.0, y: 12.0, size: 28.0, z: -5.0},
    {kind: "hangar-arch", x: 100.0, y: 18.0, size: 30.0, z: -5.0},
    {kind: "dirigibile-relique", x: 50.0, y: 20.0, size: 16.0, z: -4.0},
    {kind: "cartello-bonifica", x: 17.0, y: 14.4, size: 3.0, z: -1.2},
    {kind: "pannello-amianto", x: 33.0, y: 16.8, size: 3.0, z: -1.4},
    {kind: "bidone-decontaminazione", x: 92.0, y: 19.5, size: 2.5, z: -1.2},
    {kind: "faro-cantiere", x: 153.0, y: 26.5, size: 3.5, z: -1.5}
  ]'''

l5_decor = '''  decor: [
    {kind: "ficus-centenario", x: -4.0, y: 11.0, size: 13.0, z: -1.5},
    {kind: "palma-augusta", x: 2.0, y: 11.0, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 8.5, y: 12.0, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 17.0, y: 13.0, size: 6.8, z: -1.2},
    {kind: "palma-augusta", x: 33.0, y: 14.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 48.5, y: 14.8, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 82.0, y: 15.0, size: 7.0, z: -1.2},
    {kind: "palma-augusta", x: 92.0, y: 15.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 136.0, y: 19.5, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 145.0, y: 19.5, size: 6.0, z: -0.8},
    {kind: "olivo-secolare", x: 153.0, y: 19.5, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 175.5, y: 18.8, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 193.0, y: 19.8, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 20.8, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 21.8, size: 6.5, z: -0.8},
    {kind: "olivo-secolare", x: 239.0, y: 21.8, size: 7.2, z: -1.2},
    {kind: "fiume-fognatura-reflui", x: 60.0, y: 3.0, size: 14.0, z: -2.0},
    {kind: "torre-castello-svevo", x: 88.0, y: 15.5, size: 18.0, z: -4.5},
    {kind: "armi-medievali-rastrelliera", x: 33.0, y: 14.5, size: 3.2, z: -1.2},
    {kind: "argano-ponte-levatoio", x: 44.0, y: 14.8, size: 3.5, z: -1.5},
    {kind: "portone-ferro-svevo", x: 142.0, y: 19.5, size: 4.5, z: -2.0},
    {kind: "stemma-federico-aquila", x: 208.0, y: 20.8, size: 3.5, z: -1.5}
  ]'''

l6_decor = '''  decor: [
    {kind: "ficus-centenario", x: -4.0, y: 12.0, size: 13.5, z: -1.5},
    {kind: "palma-augusta", x: 2.0, y: 12.0, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 8.5, y: 10.5, size: 3.8, z: -0.6},
    {kind: "olivo-secolare", x: 17.0, y: 8.8, size: 6.8, z: -1.2},
    {kind: "palma-augusta", x: 33.0, y: 11.8, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 48.5, y: 12.8, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 82.0, y: 14.5, size: 7.0, z: -1.2},
    {kind: "palma-augusta", x: 92.0, y: 15.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 136.0, y: 21.5, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 145.0, y: 21.5, size: 6.0, z: -0.8},
    {kind: "olivo-secolare", x: 153.0, y: 21.5, size: 7.0, z: -1.2},
    {kind: "olivo-secolare", x: 175.5, y: 21.2, size: 6.8, z: -1.2},
    {kind: "tree-sapling", x: 193.0, y: 22.2, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 23.2, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 24.5, size: 6.5, z: -0.8},
    {kind: "tree-sapling", x: 239.0, y: 24.5, size: 4.0, z: -0.6},
    {kind: "rogo-tossico-pneumatici", x: 60.0, y: 3.5, size: 14.0, z: -2.0},
    {kind: "idrante-civico-acqua", x: 44.0, y: 12.8, size: 2.8, z: -1.2},
    {kind: "catasta-pneumatici", x: 33.0, y: 11.8, size: 3.5, z: -1.2},
    {kind: "faro-capo-croce-torre", x: 153.0, y: 21.5, size: 16.0, z: -4.5},
    {kind: "scogliera-calcarea", x: 88.0, y: 15.5, size: 10.0, z: -3.0}
  ]'''

l7_decor = '''  decor: [
    {kind: "palma-augusta", x: -4.0, y: 10.0, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 2.0, y: 10.0, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 8.5, y: 10.5, size: 6.2, z: -1.2},
    {kind: "tree-sapling", x: 17.0, y: 11.0, size: 3.8, z: -0.6},
    {kind: "palma-augusta", x: 33.0, y: 11.5, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 48.5, y: 12.0, size: 5.8, z: -0.8},
    {kind: "olivo-secolare", x: 82.0, y: 12.2, size: 7.0, z: -1.2},
    {kind: "palma-augusta", x: 92.0, y: 12.6, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 136.0, y: 14.8, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 145.0, y: 14.8, size: 6.0, z: -0.8},
    {kind: "olivo-secolare", x: 153.0, y: 14.8, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 175.5, y: 14.2, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 193.0, y: 14.8, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 15.0, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 15.5, size: 6.5, z: -0.8},
    {kind: "tree-sapling", x: 239.0, y: 15.5, size: 4.0, z: -0.6},
    {kind: "fiume-fognatura-reflui", x: 60.0, y: 3.0, size: 14.0, z: -2.0},
    {kind: "paratoia-idraulica-metallo", x: 44.0, y: 12.0, size: 3.2, z: -1.2},
    {kind: "piramide-sale-bianco", x: 82.0, y: 12.2, size: 4.5, z: -1.8},
    {kind: "mulino-salina-pale", x: 88.0, y: 12.6, size: 14.0, z: -4.5},
    {kind: "fenicottero-saline", x: 193.0, y: 14.8, size: 3.0, z: -1.5}
  ]'''

l8_decor = '''  decor: [
    {kind: "palma-augusta", x: -4.0, y: 9.0, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 2.0, y: 9.0, size: 6.5, z: -1.2},
    {kind: "tree-sapling", x: 8.5, y: 9.8, size: 3.8, z: -0.6},
    {kind: "olivo-secolare", x: 17.0, y: 10.6, size: 6.8, z: -1.2},
    {kind: "palma-augusta", x: 33.0, y: 11.8, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 48.5, y: 12.2, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 82.0, y: 12.5, size: 7.0, z: -1.2},
    {kind: "palma-augusta", x: 92.0, y: 13.0, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 136.0, y: 16.5, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 145.0, y: 16.5, size: 6.0, z: -0.8},
    {kind: "olivo-secolare", x: 153.0, y: 16.5, size: 7.0, z: -1.2},
    {kind: "olivo-secolare", x: 175.5, y: 16.2, size: 6.8, z: -1.2},
    {kind: "tree-sapling", x: 193.0, y: 16.8, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 17.2, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 17.5, size: 6.5, z: -0.8},
    {kind: "olivo-secolare", x: 239.0, y: 17.5, size: 7.2, z: -1.2},
    {kind: "fiume-petrolio-greggio", x: 60.0, y: 3.0, size: 14.0, z: -2.0},
    {kind: "barriera-panne-anti-petrolio", x: 60.0, y: 12.2, size: 14.0, z: -1.5},
    {kind: "argano-cavo-barriera", x: 44.0, y: 12.2, size: 3.2, z: -1.2},
    {kind: "cannone-spagnolo-bronzo", x: 17.0, y: 10.6, size: 3.5, z: -1.2},
    {kind: "torre-forte-vittoria", x: 153.0, y: 16.5, size: 18.0, z: -4.5}
  ]'''

l9_decor = '''  decor: [
    {kind: "ficus-centenario", x: -4.0, y: 11.5, size: 13.5, z: -1.5},
    {kind: "palma-augusta", x: 2.0, y: 11.5, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 8.5, y: 12.8, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 17.0, y: 14.0, size: 6.8, z: -1.2},
    {kind: "tree-sapling", x: 33.0, y: 15.6, size: 4.0, z: -0.6},
    {kind: "palma-augusta", x: 48.5, y: 16.2, size: 8.5, z: -1.0},
    {kind: "olivo-secolare", x: 82.0, y: 16.8, size: 7.0, z: -1.2},
    {kind: "arancio-siciliano", x: 92.0, y: 17.2, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 136.0, y: 20.2, size: 4.0, z: -0.6},
    {kind: "olivo-secolare", x: 145.0, y: 20.2, size: 7.0, z: -1.2},
    {kind: "palma-augusta", x: 153.0, y: 20.2, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 175.5, y: 20.0, size: 6.0, z: -0.8},
    {kind: "tree-sapling", x: 193.0, y: 20.6, size: 4.2, z: -0.6},
    {kind: "palma-augusta", x: 208.0, y: 20.8, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 233.0, y: 21.0, size: 6.5, z: -0.8},
    {kind: "olivo-secolare", x: 239.0, y: 21.0, size: 7.2, z: -1.2},
    {kind: "rogo-tossico-pneumatici", x: 60.0, y: 5.0, size: 14.0, z: -2.0},
    {kind: "idrante-civico-acqua", x: 44.0, y: 16.2, size: 2.8, z: -1.2},
    {kind: "muretto-secco-siciliano", x: 33.0, y: 15.6, size: 3.5, z: -1.2},
    {kind: "veduta-golfo-augusta", x: 153.0, y: 20.2, size: 16.0, z: -5.0}
  ]'''

l10_decor = '''  decor: [
    {kind: "ficus-centenario", x: -4.0, y: 12.0, size: 14.0, z: -1.5},
    {kind: "palma-augusta", x: 2.0, y: 12.0, size: 8.5, z: -1.0},
    {kind: "arancio-siciliano", x: 8.5, y: 13.0, size: 5.5, z: -0.8},
    {kind: "olivo-secolare", x: 17.0, y: 14.0, size: 6.8, z: -1.2},
    {kind: "palma-augusta", x: 33.0, y: 15.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 48.5, y: 16.0, size: 4.0, z: -0.6},
    {kind: "ficus-centenario", x: 82.0, y: 17.0, size: 13.5, z: -1.5},
    {kind: "palma-augusta", x: 92.0, y: 17.5, size: 8.5, z: -1.0},
    {kind: "tree-sapling", x: 136.0, y: 21.0, size: 4.0, z: -0.6},
    {kind: "arancio-siciliano", x: 145.0, y: 21.0, size: 6.0, z: -0.8},
    {kind: "ficus-centenario", x: 153.0, y: 21.0, size: 13.5, z: -1.5},
    {kind: "arancio-siciliano", x: 175.5, y: 20.8, size: 6.0, z: -0.8},
    {kind: "palma-augusta", x: 193.0, y: 21.5, size: 8.5, z: -1.0},
    {kind: "ficus-rinascita", x: 208.0, y: 22.2, size: 6.5, z: -0.8},
    {kind: "tree-sapling", x: 233.0, y: 22.5, size: 4.5, z: -0.6},
    {kind: "ficus-centenario", x: 239.0, y: 22.5, size: 15.0, z: -1.5},
    {kind: "fiume-petrolio-greggio", x: 60.0, y: 5.0, size: 12.0, z: -2.0},
    {kind: "ficus-chioma-attraversabile", x: 60.0, y: 16.2, size: 15.0, z: -2.8},
    {kind: "porta-spagnola", x: 88.0, y: 17.5, size: 12.0, z: -3.5},
    {kind: "arco-trionfale-verde", x: 132.0, y: 21.0, size: 10.0, z: -2.5},
    {kind: "barocco-duomo", x: 231.0, y: 22.5, size: 20.0, z: -5.0},
    {kind: "vaso-caltagirone", x: 17.0, y: 14.0, size: 3.0, z: -1.2},
    {kind: "palina-raccolta-differenziata", x: 33.0, y: 15.5, size: 2.2, z: -1.0},
    {kind: "fountain-augusta", x: 175.5, y: 20.8, size: 4.5, z: -2.5}
  ]'''

decors = [l1_decor, l2_decor, l3_decor, l4_decor, l5_decor, l6_decor, l7_decor, l8_decor, l9_decor, l10_decor]

# For each level function, replace its decor: [...] block
for lvl in range(1, 11):
    fn_header = f"def get_level_{lvl}():"
    p_fn = content.find(fn_header)
    if p_fn == -1:
        print(f"Error: {fn_header} not found!")
        continue
    next_p = content.find(f"def get_level_{lvl+1}():", p_fn) if lvl < 10 else content.find("def get_all_levels():", p_fn)
    block = content[p_fn:next_p]
    
    # Replace decor: [...]
    pattern = r'decor:\s*\[[\s\S]*?\n  \]'
    m = re.search(pattern, block)
    if not m:
        print(f"Error: decor not found in level {lvl}!")
        continue
    new_block = block[:m.start()] + decors[lvl-1] + block[m.end():]
    content = content[:p_fn] + new_block + content[next_p:]

with open("tools/generate_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(content)

print("[✓] Successfully updated tools/generate_all_10_levels.py!")
