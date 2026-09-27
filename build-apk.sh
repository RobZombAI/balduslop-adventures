#!/bin/bash
set -e

echo "=== BUILDING GTA: GIUSEPPE TAGLIA ALBERI (ANDROID APK) ==="

# 1. Detect Java 17
if [ -d "/opt/homebrew/opt/openjdk@17" ]; then
    export JAVA_HOME="/opt/homebrew/opt/openjdk@17"
    export PATH="$JAVA_HOME/bin:$PATH"
fi

# 2. Package offline web assets
echo "1. Packaging offline web and 3D assets..."
python3 tools/package_android_assets.py

# 3. Assemble Android APK
echo "2. Compiling Android APK with Gradle..."
cd android-app
./gradlew assembleDebug --no-daemon

# 4. Copy to accessible paths
cd ..
cp android-app/app/build/outputs/apk/debug/app-debug.apk gta/GTA-Giuseppe-Taglia-Alberi.apk
cp android-app/app/build/outputs/apk/debug/app-debug.apk GTA-Giuseppe-Taglia-Alberi-Augusta.apk

echo ""
echo "=========================================================="
echo " [✓] APK BUILD SUCCESSFUL!"
echo " File: gta/GTA-Giuseppe-Taglia-Alberi.apk"
echo " Size: $(ls -lh gta/GTA-Giuseppe-Taglia-Alberi.apk | awk '{print $5}')"
echo " To install on connected Android device via ADB:"
echo "   adb install -r gta/GTA-Giuseppe-Taglia-Alberi.apk"
echo "=========================================================="
