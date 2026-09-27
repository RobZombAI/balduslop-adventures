# tools/package_android_assets.py
import os
import shutil

print("=== PACKAGING OFFLINE ASSETS FOR ANDROID APP ===")

app_assets = "android-app/app/src/main/assets"
www_dir = os.path.join(app_assets, "www")

os.makedirs(www_dir, exist_ok=True)
os.makedirs(os.path.join(www_dir, "bundle"), exist_ok=True)
os.makedirs(os.path.join(www_dir, "assets"), exist_ok=True)

# Remove any old duplicate assets folder in root of app assets
dst_root = os.path.join(app_assets, "assets")
if os.path.exists(dst_root):
    print("Removing legacy duplicate assets folder in Android assets root...")
    shutil.rmtree(dst_root, ignore_errors=True)

# 1. Copy bundle files (excluding unused alternative index bundles)
print("Copying bundle files...")
unused_bundles = {"index-augusta.js", "index-augusta-v2.js", "index-B9TPSTBI.js", "index-CzjHjcy4.js"}
for old_bundle in unused_bundles:
    old_path = os.path.join(www_dir, "bundle", old_bundle)
    if os.path.exists(old_path):
        os.remove(old_path)
for item in os.listdir("bundle"):
    if item in unused_bundles:
        continue
    src = os.path.join("bundle", item)
    dst = os.path.join(www_dir, "bundle", item)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

# 2. Copy 3D assets to www/assets
print("Copying 3D assets to www/assets...")
for item in os.listdir("assets"):
    src = os.path.join("assets", item)
    dst = os.path.join(www_dir, "assets", item)
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif os.path.isfile(src):
        shutil.copy2(src, dst)

# 3. Copy GTA root files (icons, logo, manifest, sw)
print("Copying root web assets...")
for item in ["logo-gta.webp", "icon-32.png", "icon-180.png", "icon-192.png", "icon-512.png", "cover-art.webp", "manifest.webmanifest", "sw.js"]:
    src = os.path.join("gta", item)
    dst = os.path.join(www_dir, item)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

# 4. Prepare index.html with local relative paths
print("Adapting index.html for Android assets...")
with open("gta/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace ../bundle/ with ./bundle/
html = html.replace("../bundle/", "./bundle/")
# Replace ../assets/ with ./assets/
html = html.replace("../assets/", "./assets/")
# Adapt switch link for local acqua directory in Android
html = html.replace('href="../acqua/index.html"', 'href="./acqua/index.html"')
# Strip crossorigin attributes
html = html.replace(' crossorigin', '')
# Remove other external web links in standalone app
html = html.replace('<a href="../augusta/index.html"', '<a href="#" style="display:none;"')
html = html.replace('<a href="../index.html"', '<a href="#" style="display:none;"')

with open(os.path.join(www_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

# 5. Adapt bundle JS for local relative paths
js_file = os.path.join(www_dir, "bundle", "index-gta-v1.js")
if os.path.exists(js_file):
    print("Adapting bundle JS for standalone Android WebView...")
    with open(js_file, "r", encoding="utf-8") as f:
        js = f.read()
    js = js.replace('"../assets/completion/', '"./assets/completion/')
    js = js.replace('"../assets/third-party-licenses.txt"', '"./assets/third-party-licenses.txt"')
    js = js.replace('"../assets/"', '"./assets/"')
    js = js.replace("'../assets/'", "'./assets/'")
    with open(js_file, "w", encoding="utf-8") as f:
        f.write(js)

# 6. Copy and adapt Acqua game into Android assets
print("Copying Acqua puzzle game into Android assets...")
os.makedirs(os.path.join(www_dir, "acqua"), exist_ok=True)
with open("acqua/index.html", "r", encoding="utf-8") as f:
    acqua_html = f.read()

# In standalone Android app: root index.html is GTA
acqua_html = acqua_html.replace('href="../gta/"', 'href="../index.html"')
acqua_html = acqua_html.replace('href="../gta/index.html"', 'href="../index.html"')
acqua_html = acqua_html.replace('href="../index.html"', 'href="../index.html"')
acqua_html = acqua_html.replace('href="../augusta/"', 'href="../index.html"')
acqua_html = acqua_html.replace('href="../gta/icon-32.png"', 'href="../icon-32.png"')
acqua_html = acqua_html.replace('href="../gta/icon-180.png"', 'href="../icon-180.png"')

with open(os.path.join(www_dir, "acqua", "index.html"), "w", encoding="utf-8") as f:
    f.write(acqua_html)

print("[✓] Successfully packaged all standalone assets (including Acqua) in android-app/app/src/main/assets/www!")
