# tools/apply_cerignola_level.py
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from cerignola_decor_and_level import get_cerignola_decor_models, get_cerignola_level_code

BUNDLE_PATH = "bundle/index-gta-v1.js"

print("=== APPLYING CERIGNOLA LEVEL & DECOR TO BUNDLE ===")

with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Inject 3D Decor Models into _D dictionary
decor_marker = "};\nfunction kre(t,e){t.backdropLayers??=new Map;con"
alt_decor_marker = "}\n};\nfunction kre(t,e){t.backdropLayers??=new Map;con"
alt_decor_marker2 = "}\n};function kre(t,e){t.backdropLayers??=new Map;con"

decor_code = get_cerignola_decor_models()

if '"duomo-tonti-cerignola"' in bundle:
    print("[!] Cerignola decor models already present in bundle, replacing them...")
    import re
    # Remove existing cerignola decor if present
    bundle = re.sub(r',\s*"duomo-tonti-cerignola"[\s\S]*?,\s*"olivo-bella-di-cerignola"\(t,e,n\)\{[\s\S]*?\}', '', bundle)

pos_d_end = bundle.find("};function kre(t,e){")
if pos_d_end == -1:
    pos_d_end = bundle.find("};\nfunction kre(t,e){")
if pos_d_end == -1:
    pos_d_end = bundle.find("};function kre")

if pos_d_end != -1:
    bundle = bundle[:pos_d_end] + decor_code + bundle[pos_d_end:]
    print("[✓] Successfully injected Cerignola 3D procedural decor models into _D!")
else:
    print("[!] ERROR: Could not find end of _D dictionary!")
    sys.exit(1)

# 2. Inject Cerignola Level code and update Sc
level_code = get_cerignola_level_code()

# Check if cerignolaL1 already exists in bundle
if "const cerignolaL1" in bundle:
    print("[!] Removing old cerignolaL1 code...")
    import re
    bundle = re.sub(r'// --- CERIGNOLA:[\s\S]*?const cerignolaL1 = yr\(\{[\s\S]*?\}\);\n*', '', bundle)

sc_target_10 = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10]"
sc_target_11 = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10,cerignolaL1]"

if sc_target_10 in bundle:
    pos_sc = bundle.find(sc_target_10)
    bundle = bundle[:pos_sc] + "\n\n// --- CERIGNOLA: LA CITTÀ DI BALDU (LIVELLO SPECIALE) ---\n" + level_code + "\n\n" + sc_target_11 + bundle[pos_sc + len(sc_target_10):]
    print("[✓] Successfully injected Cerignola level and updated Sc array with 11 levels!")
elif sc_target_11 in bundle:
    pos_sc = bundle.find(sc_target_11)
    # Search backwards for the cerignola comment or insert right before
    bundle = bundle[:pos_sc] + "\n\n// --- CERIGNOLA: LA CITTÀ DI BALDU (LIVELLO SPECIALE) ---\n" + level_code + "\n\n" + sc_target_11 + bundle[pos_sc + len(sc_target_11):]
    print("[✓] Updated Cerignola level in bundle!")
else:
    print("[!] ERROR: Could not find Sc marker in bundle!")
    sys.exit(1)

# 3. Add URL search parameter support for ?level=cerignola or ?level=11
url_param_code = '''const _lvlParam = typeof window !== "undefined" ? new URLSearchParams(window.location.search).get("level") : null;
if (_lvlParam === "cerignola" || _lvlParam === "11" || _lvlParam === "baldu") {
  te.last = 10;
} else if (_lvlParam && !isNaN(Number(_lvlParam))) {
  te.last = Math.max(0, Math.min(Sc.length - 1, Number(_lvlParam) - 1));
} else {
  te.last = dl.includes(kn[Number(te.last)]) && sh(Number(te.last)) ? Number(te.last) : Math.max(0, Math.min(HI(), Math.floor(Number(te.last) || 0)));
}'''

old_te_last = 'te.last=dl.includes(kn[Number(te.last)])&&sh(Number(te.last))?Number(te.last):Math.max(0,Math.min(HI(),Math.floor(Number(te.last)||0)));'
if old_te_last in bundle:
    bundle = bundle.replace(old_te_last, url_param_code)
    print("[✓] Added URL parameter ?level=cerignola & ?level=11 support!")

# 4. Enhance Moral Card for Cerignola
old_moral_header = '<span class="moral-tag">LA MORALE DI AUGUSTA &bull; SENSIBILIZZAZIONE CIVICA</span>'
new_moral_header = '<span class="moral-tag">${e.short==="Cerignola"?"LA STORIA DI CERIGNOLA &bull; RISCATTO E LEGALITÀ":"LA MORALE DI AUGUSTA &bull; SENSIBILIZZAZIONE CIVICA"}</span>'
if old_moral_header in bundle:
    bundle = bundle.replace(old_moral_header, new_moral_header)
    print("[✓] Enhanced civic moral header to reflect Cerignola!")

old_moral_icon = '<span class="moral-icon">🌿</span>'
new_moral_icon = '<span class="moral-icon">${e.short==="Cerignola"?"🌾":"🌿"}</span>'
if old_moral_icon in bundle:
    bundle = bundle.replace(old_moral_icon, new_moral_icon)
    print("[✓] Enhanced civic moral icon for Cerignola (durum wheat / olive)!")

# 5. Write back to bundle/index-gta-v1.js
with open(BUNDLE_PATH, "w", encoding="utf-8") as f:
    f.write(bundle)

print(f"[✓] Successfully wrote updated {BUNDLE_PATH} (size: {len(bundle):,} bytes)")
