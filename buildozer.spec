[app]

# (str) Title of your application
title = My Ursina App

# (str) Package name
package.name = ursina_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add 'panda3d' and 'ursina' to the list of requirements
requirements = python3,kivy,panda3d

# (str) Custom source folders for requirements
# This ensures that Buildozer knows where to find the local recipes for Panda3D and Ursina
p4a.local_recipes = ./recipes

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
# Match the version required by python-for-android
android.ndk = 23b

# (list) The Android architectures to build for, choose the relevant ones
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
# Enable when using modern dependencies or gradle configurations
android.enable_androidx = True

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions for the app
# Add permissions required by Panda3D and Ursina if needed
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (bool) Indicate whether the screen should stay on
android.wakelock = True

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
