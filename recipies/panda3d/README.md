# Panda3D Recipe
This recipe builds and packages Panda3D for Android using python-for-android.

## Dependencies
- Python 3
- Freetype
- Zlib
- Libpng

## Build Instructions
Place this recipe in the `recipes` directory of p4a and build the APK with the following command:
```bash
p4a apk --private <your_code_dir> --requirements=panda3d
