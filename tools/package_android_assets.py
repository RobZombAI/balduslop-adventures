# tools/package_android_assets.py
import os
import shutil

print("=== PACKAGING OFFLINE ASSETS FOR ANDROID APP ===")

app_assets = "android-app/app/src/main/assets"
www_dir = os.path.join(app_assets, "www")

os.makedirs(www_dir, exist_ok=True)
os.makedirs(os.path.join(www_dir, "bundle"), exist_ok=True)
os.makedirs(os.path.join(www_dir, "assets"), exist_ok=True)

# 1. Copy bundle files
print("Copying bundle files...")
for item in os.listdir("bundle"):
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

# Also duplicate to app_assets/assets as safety fallback for "../assets/" requests
print("Creating root assets fallback in Android assets...")
dst_root = os.path.join(app_assets, "assets")
os.makedirs(dst_root, exist_ok=True)
for item in os.listdir("assets"):
    src = os.path.join("assets", item)
    dst = os.path.join(dst_root, item)
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
# Remove game switch nav (not needed in standalone GTA app)
html = html.replace('<div class="game-switch-nav">', '<div class="game-switch-nav" style="display:none;">')

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
    with open(js_file, "w", encoding="utf-8") as f:
        f.write(js)

print("[✓] Successfully packaged all standalone assets in android-app/app/src/main/assets/www!")
