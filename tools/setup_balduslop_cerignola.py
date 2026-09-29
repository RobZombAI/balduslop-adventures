# tools/setup_balduslop_cerignola.py
import re
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from cerignola_decor_and_level import get_cerignola_decor_models, get_cerignola_level_code

print("=== RECONFIGURING CERIGNOLA AS EXCLUSIVE LEVEL OF BALDUSLOP ===")

# ==============================================================================
# PART 1: RESTORE GTA TO 100% PURE AUGUSTA (REMOVE CERIGNOLA FROM GTA)
# ==============================================================================
print("\n--- 1. Restoring GTA Augusta (bundle/index-gta-v1.js) ---")
with open("bundle/index-gta-v1.js", "r", encoding="utf-8") as f:
    gta_bundle = f.read()

# Remove Cerignola decor models from GTA
gta_bundle = re.sub(r',\s*"duomo-tonti-cerignola"[\s\S]*?,\s*"olivo-bella-di-cerignola"\(t,e,n\)\{[\s\S]*?\}', '', gta_bundle)

# Remove cerignola level definition from GTA
gta_bundle = re.sub(r'\n*// --- CERIGNOLA:[\s\S]*?const cerignolaL1 = yr\(\{[\s\S]*?\}\);\n*', '\n\n', gta_bundle)

# Restore Sc to 10 Augusta levels
sc_11 = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10,cerignolaL1]"
sc_10 = "const Sc=[augustaL1,augustaL2,augustaL3,augustaL4,augustaL5,augustaL6,augustaL7,augustaL8,augustaL9,augustaL10]"
if sc_11 in gta_bundle:
    gta_bundle = gta_bundle.replace(sc_11, sc_10)
    print("[✓] Restored Sc to 10 Augusta levels in GTA bundle!")

with open("bundle/index-gta-v1.js", "w", encoding="utf-8") as f:
    f.write(gta_bundle)
print(f"[✓] Successfully cleaned bundle/index-gta-v1.js (size: {len(gta_bundle):,} bytes)")

# Remove Cerignola link from gta/index.html
with open("gta/index.html", "r", encoding="utf-8") as f:
    gta_html = f.read()

gta_html = re.sub(r'\s*<a href="\.\./cerignola/"[\s\S]*?🌾 Cerignola</span>\s*</a>', '', gta_html)
with open("gta/index.html", "w", encoding="utf-8") as f:
    f.write(gta_html)
print("[✓] Removed Cerignola link from gta/index.html!")


# ==============================================================================
# PART 2: INJECT CERIGNOLA LEVEL & DECOR INTO BALDUSLOP (bundle/index-B9TPSTBI.js)
# ==============================================================================
print("\n--- 2. Setting up Cerignola in BalduSlop (bundle/index-B9TPSTBI.js) ---")
with open("bundle/index-B9TPSTBI.js", "r", encoding="utf-8") as f:
    baldu_bundle = f.read()

# 2a. Inject Cerignola Decor Models into _D
decor_code = get_cerignola_decor_models()

# Clean existing if present
baldu_bundle = re.sub(r',\s*"duomo-tonti-cerignola"[\s\S]*?,\s*"olivo-bella-di-cerignola"\(t,e,n\)\{[\s\S]*?\}', '', baldu_bundle)

pos_d = baldu_bundle.find("}};function kre(t,e){t.backdropLayers??=new Map;")
if pos_d != -1:
    # insert before the closing };
    baldu_bundle = baldu_bundle[:pos_d+1] + decor_code + baldu_bundle[pos_d+1:]
    print("[✓] Injected Cerignola 3D procedural decor models into BalduSlop _D dictionary!")
else:
    pos_d2 = baldu_bundle.find("};function kre(t,e){")
    if pos_d2 != -1:
        baldu_bundle = baldu_bundle[:pos_d2] + decor_code + baldu_bundle[pos_d2:]
        print("[✓] Injected Cerignola decor models into BalduSlop _D dictionary (alt marker)!")
    else:
        print("[!] ERROR: Could not find _D marker in bundle/index-B9TPSTBI.js!")
        sys.exit(1)

# 2b. Inject Cerignola Level code into bundle/index-B9TPSTBI.js
level_code = get_cerignola_level_code()
baldu_bundle = re.sub(r'\n*// --- CERIGNOLA:[\s\S]*?const cerignolaL1 = yr\(\{[\s\S]*?\}\);\n*', '\n\n', baldu_bundle)

# In Balduslop, Sc was [BQ,DQ,TT,IQ,QC].
# Let's make Cerignola Chapter 1 (Lead level) of Balduslop:
# const Sc=[cerignolaL1,BQ,DQ,TT,IQ,QC]
sc_orig = "const Sc=[BQ,DQ,TT,IQ,QC]"
sc_new = "const Sc=[cerignolaL1,BQ,DQ,TT,IQ,QC]"

if sc_orig in baldu_bundle:
    p_sc = baldu_bundle.find(sc_orig)
    baldu_bundle = baldu_bundle[:p_sc] + "\n\n// --- CERIGNOLA: LA CITTÀ DI BALDU (LIVELLO PRINCIPALE DI BALDUSLOP) ---\n" + level_code + "\n\n" + sc_new + baldu_bundle[p_sc + len(sc_orig):]
    print("[✓] Successfully injected Cerignola as Chapter 01 of BalduSlop!")
elif sc_new in baldu_bundle:
    p_sc = baldu_bundle.find(sc_new)
    baldu_bundle = baldu_bundle[:p_sc] + "\n\n// --- CERIGNOLA: LA CITTÀ DI BALDU (LIVELLO PRINCIPALE DI BALDUSLOP) ---\n" + level_code + "\n\n" + sc_new + baldu_bundle[p_sc + len(sc_new):]
    print("[✓] Updated Cerignola as Chapter 01 of BalduSlop!")
else:
    print("[!] ERROR: Could not find Sc marker in bundle/index-B9TPSTBI.js!")
    sys.exit(1)

# 2c. Unlock all chapters & hook testing window variables
baldu_bundle = baldu_bundle.replace('Wt=new m0e(me("world")', 'window.__WORLD__=Wt=new m0e(me("world")')
baldu_bundle = baldu_bundle.replace('kne(t,e){const n=t.scene', 'kne(t,e){window.__WORLD_SCENE__=t.scene;const n=t.scene')

old_ade_block = 'ce=new $9(gde);window.ce=ce;const Ade=2,sh=t=>!!te.labUnlocked||t<Ade&&!kn[t]?.hidden,bde=t=>!!(te.best?.[t]||te.customBest?.[t]),_u=t=>!!te.labUnlocked||t<=1||!!kn[t]?.bench||bde(t-1)'
old_ade_block2 = 'ce=new $9(gde);window.ce=ce;const Ade=2,sh=t=>!!te.labUnlocked||t<Ade&&!kn[t]?.hidden,bde=t=>!!(te.best?.[t]||te.customBest?.[t]),_u=t=>!!te.labUnlocked||t<=0||!!kn[t]?.bench||bde(t-1)'

new_ade_block = '''ce=new $9(gde);window.ce=ce;window.__GAME_CE__=ce;window.__GAME_TE__=te;window.__START_LEVEL__=nl;
const Ade=10,sh=t=>!0,bde=t=>!!(te.best?.[t]||te.customBest?.[t]),_u=t=>!0'''

if old_ade_block in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_ade_block, new_ade_block)
    print("[✓] Hooked window variables & unlocked all chapters in BalduSlop!")
elif old_ade_block2 in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_ade_block2, new_ade_block)
    print("[✓] Hooked window variables & unlocked all chapters in BalduSlop (variant 2)!")
else:
    print("[!] Warning: old_ade_block not found in BalduSlop, checking partial match...")
    m_ce = baldu_bundle.find("window.ce=ce;const Ade=")
    if m_ce != -1:
        end_ade = baldu_bundle.find(",HI=()=>{let t=Cy();", m_ce)
        if end_ade != -1:
            baldu_bundle = baldu_bundle[:m_ce] + "window.ce=ce;window.__GAME_CE__=ce;window.__GAME_TE__=te;window.__START_LEVEL__=nl;const Ade=10,sh=t=>!0,bde=t=>!!(te.best?.[t]||te.customBest?.[t]),_u=t=>!0" + baldu_bundle[end_ade:]
            print("[✓] Replaced Ade block via range search!")

# 2d. Add ?level URL parameter support in BalduSlop
url_param_code = '''const _lvlParam = typeof window !== "undefined" ? new URLSearchParams(window.location.search).get("level") : null;
if (_lvlParam === "cerignola" || _lvlParam === "baldu" || _lvlParam === "1") {
  te.last = 0;
} else if (_lvlParam && !isNaN(Number(_lvlParam))) {
  te.last = Math.max(0, Math.min(Sc.length - 1, Number(_lvlParam) - 1));
} else {
  te.last = dl.includes(kn[Number(te.last)]) && sh(Number(te.last)) ? Number(te.last) : Math.max(0, Math.min(HI(), Math.floor(Number(te.last) || 0)));
}'''

old_te_last = 'te.last=dl.includes(kn[Number(te.last)])&&sh(Number(te.last))?Number(te.last):Math.max(0,Math.min(HI(),Math.floor(Number(te.last)||0)));'
if old_te_last in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_te_last, url_param_code)
    print("[✓] Added URL parameter ?level=cerignola support in BalduSlop!")

# 2e. Solid Platform Collision & Ceiling Limit in BalduSlop
old_l1 = 'function l1(t){return t.kind==="wall"?j3(t)?{x:t.x,w:t.w,top:t.y,bottom:t.y-X3(t)}:null:t.kind==="fold"&&c9(t)?mL(t):null}'
new_l1 = '''function l1(t){
  if(!t||t.active===!1||t.broken)return null;
  if(t.kind==="wall")return j3(t)?{x:t.x,w:t.w,top:t.y,bottom:t.y-X3(t)}:null;
  if(t.kind==="fold"&&c9(t))return mL(t);
  if(t.kind==="gate")return(t.open>0)?null:{x:t.x,w:t.w,top:t.y,bottom:t.y-(t.h||10)};
  if(t.kind==="switch"||t.kind==="hazard"||t.spiked)return null;
  const th=Number.isFinite(t.h)&&t.h>0?t.h:(Number.isFinite(t.thickness)&&t.thickness>0?t.thickness:0.65);
  return{x:t.x,w:t.w,top:t.y,bottom:t.y-th}
}'''
if old_l1 in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_l1, new_l1)
    print("[✓] Injected solid platform collision in BalduSlop l1(t)!")

old_ceil = 'for(const B of i.platforms){const T=l1(B);if(!T||!(o.x+ht.radius>T.x&&o.x-ht.radius<T.x+T.w))continue;const L=T.bottom;o.vy>0&&x+ht.height<=L+1e-7&&o.y+ht.height>=L&&(o.y=L-ht.height,o.vy=0,o.springing=!1)}'
new_ceil = '''for(const B of i.platforms){
  const T=l1(B);
  if(!T||!(o.x+ht.radius>T.x+0.04&&o.x-ht.radius<T.x+T.w-0.04))continue;
  const L=T.bottom;
  if(o.vy>0&&(x+ht.height<=L+0.18||(o.y+ht.height>=L&&o.y<T.top-0.2))){
    o.y=L-ht.height;
    o.vy=Math.min(0,-0.6);
    o.springing=!1;
  }
}'''
if old_ceil in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_ceil, new_ceil)
    print("[✓] Injected solid ceiling bump in BalduSlop!")

old_wall = 'for(const B of i.platforms){const T=l1(B);if(!T)continue;const L=T.bottom,R=T.x-ht.radius,F=T.x+T.w+ht.radius;x<T.top-1e-7&&x+ht.height>L+1e-7&&(w<=R&&o.x>R?(o.x=R,o.vx=Math.min(0,o.vx)):w>=F&&o.x<F?(o.x=F,o.vx=Math.max(0,o.vx)):o.x>R&&o.x<F&&(o.x=w<(R+F)/2?R:F,o.vx=0))}'
new_wall = '''for(const B of i.platforms){
  const T=l1(B);
  if(!T)continue;
  const L=T.bottom,R=T.x-ht.radius,F=T.x+T.w+ht.radius;
  if(x<T.top-0.12&&x+ht.height>L+0.05){
    if(w<=R&&o.x>R){o.x=R;o.vx=Math.min(0,o.vx);}
    else if(w>=F&&o.x<F){o.x=F;o.vx=Math.max(0,o.vx);}
    else if(o.x>R&&o.x<F){o.x=w<(R+F)/2?R:F;o.vx=0;}
  }
}'''
if old_wall in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_wall, new_wall)
    print("[✓] Injected solid horizontal wall collision in BalduSlop!")

# 2f. Add Civic Moral Card to BalduSlop completion modal
old_comp = """      <dl class="completion-stats" aria-label="Your chapter results">
        ${d("bead",`${t.coins}<span class="completion-denominator"> / ${e.coins.length}</span>`,"Clay beads")}
        ${u(t.stamps,e.stamps.length)}
        ${d("timer",IB(t.time),"Your time",h)}
      </dl>
      <nav class="completion-actions" aria-label="Continue your adventure">"""

new_comp = """      <dl class="completion-stats" aria-label="I tuoi risultati">
        ${d("bead",`${t.coins}<span class="completion-denominator"> / ${e.coins.length}</span>`,"Monete / Bustine")}
        ${u(t.stamps,e.stamps.length)}
        ${d("timer",IB(t.time),"Tempo impiegato",h)}
      </dl>
      ${(e.moralTitle&&e.moralStory)?`<div class="augusta-moral-box">
        <div class="augusta-moral-header">
          <span class="moral-icon">🌾</span>
          <span class="moral-tag">LA STORIA DI CERIGNOLA &bull; RISCATTO E LEGALITÀ</span>
        </div>
        <h3 class="augusta-moral-title">${e.moralTitle}</h3>
        <p class="augusta-moral-text">${e.moralStory}</p>
      </div>`:""}
      <nav class="completion-actions" aria-label="Continue your adventure">"""

if old_comp in baldu_bundle:
    baldu_bundle = baldu_bundle.replace(old_comp, new_comp)
    print("[✓] Added Civic Moral Card to BalduSlop completion modal!")

# 2g. Decor error logging in BalduSlop
baldu_bundle = baldu_bundle.replace(
    'try{_D[e.kind]?.(t,o,Kr(e))}catch(i){}',
    'try{_D[e.kind]?.(t,o,Kr(e))}catch(i){o.userData.decorError=i.message;console.error("Decor error on "+e.kind+":", i)}'
)

# 2h. Toast for Cerignola mechanics in BalduSlop
baldu_bundle = baldu_bundle.replace(
    'toast.style.transform="scale(1)",$n=setTimeout(()=>{toast.style.opacity="0",toast.style.transform="scale(.95)"},2400)',
    '''
    try {
      const msgs = {
        "portavalori-open": "💰 BLINDATO SBLOCCATO! Superato il commando dei portavalori: il varco sulle lamiere è aperto!",
        "cancello-duomo": "🚨 POSTO DI BLOCCO SUPERATO! Sfuggito ai pusher e alle pattuglie: la via per il Duomo Tonti è libera!"
      };
      if (msgs[e]) {
        toast.innerHTML = '<span style="font-size:22px;margin-right:8px;vertical-align:middle;">✨</span>' + msgs[e];
      }
    } catch(err){}
    toast.style.transform="scale(1)",$n=setTimeout(()=>{toast.style.opacity="0",toast.style.transform="scale(.95)"},2400)
    '''
)

with open("bundle/index-B9TPSTBI.js", "w", encoding="utf-8") as f:
    f.write(baldu_bundle)
print(f"[✓] Successfully wrote updated bundle/index-B9TPSTBI.js (size: {len(baldu_bundle):,} bytes)")


# ==============================================================================
# PART 3: UPDATE index.html (BALDUSLOP) STYLES & HEADER
# ==============================================================================
print("\n--- 3. Updating BalduSlop index.html ---")
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Add styling for moral box in index.html if not already present
if ".augusta-moral-box" not in index_html:
    moral_css = """
    /* Cerignola Moral Box in BalduSlop */
    .augusta-moral-box {
      grid-column: 1 / 2;
      margin: 8px 0 0 0;
      max-width: 520px;
      width: 100%;
      background: linear-gradient(135deg, rgba(30, 20, 10, 0.96), rgba(20, 12, 6, 0.98));
      border: 2px solid #eab308;
      border-radius: 14px;
      padding: 10px 14px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.55), 0 0 16px rgba(234, 179, 8, 0.28);
      text-align: left;
      animation: moralFadeIn 0.45s ease-out;
      box-sizing: border-box;
      max-height: 210px;
      overflow-y: auto;
    }
    @keyframes moralFadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .augusta-moral-header {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 4px;
    }
    .augusta-moral-header .moral-icon {
      font-size: 16px;
      line-height: 1;
    }
    .augusta-moral-header .moral-tag {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.8px;
      color: #facc15;
      background: rgba(234, 179, 8, 0.2);
      padding: 2px 7px;
      border-radius: 5px;
      text-transform: uppercase;
    }
    .augusta-moral-title {
      margin: 3px 0 5px 0;
      font-size: 14px;
      font-weight: 800;
      color: #fef08a;
      line-height: 1.3;
      font-family: inherit;
    }
    .augusta-moral-text {
      margin: 0;
      font-size: 12.5px;
      line-height: 1.45;
      color: #f8fafc;
      font-weight: 500;
      letter-spacing: -0.01em;
      opacity: 0.96;
      font-family: inherit;
    }
  </style>"""
    index_html = index_html.replace("</style>", moral_css)
    print("[✓] Added Cerignola moral box CSS to index.html!")

# Update description in index.html
index_html = index_html.replace(
    '<p id="title-tagline">Demo</p>',
    '<p id="title-tagline">La Città di Baldu: Cerignola, Portavalori & Fosse Granarie</p>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("[✓] Updated index.html!")

# Redirect cerignola/index.html to BalduSlop
cerignola_redirect = """<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <title>BalduSlop Adventures — Cerignola</title>
  <meta http-equiv="refresh" content="0; url=../?level=cerignola">
  <script>window.location.replace('../?level=cerignola');</script>
</head>
<body style="background:#111;color:#fff;font-family:sans-serif;text-align:center;padding:50px;">
  <h1>Caricamento livello Cerignola in BalduSlop...</h1>
  <p><a href="../?level=cerignola" style="color:#eab308">Clicca qui se non vieni reindirizzato automaticamente</a></p>
</body>
</html>"""

with open("cerignola/index.html", "w", encoding="utf-8") as f:
    f.write(cerignola_redirect)
print("[✓] Configured cerignola/index.html to open BalduSlop's Cerignola level!")

print("\n=== COMPLETE! Cerignola is now officially and exclusively part of BalduSlop! ===")
