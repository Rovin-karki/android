from pythonforandroid.toolchain import Recipe, current_directory, shprint
from os.path import join
import sh

class Panda3DRecipe(Recipe):
    version = "1.10.15"  # Specify the desired version
    url = f"https://github.com/panda3d/panda3d/archive/v{version}.tar.gz"
    depends = ["python3", "freetype", "libpng", "zlib"]  # Add core dependencies
    conflicts = []  # Specify conflicts if any

    def get_recipe_env(self, arch):
        env = super(Panda3DRecipe, self).get_recipe_env(arch)
        # Add environment variables for cross-compilation
        env["USE_EGL"] = "1"  # Enable OpenGL ES (Android)
        env["ANDROID"] = "1"  # Indicate the Android target
        env["CC"] = self.ctx.ndk_dir + "/toolchains/llvm/prebuilt/linux-x86_64/bin/clang"
        env["CXX"] = self.ctx.ndk_dir + "/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++"
        env["AR"] = self.ctx.ndk_dir + "/toolchains/llvm/prebuilt/linux-x86_64/bin/ar"
        env["LD"] = self.ctx.ndk_dir + "/toolchains/llvm/prebuilt/linux-x86_64/bin/ld"
        return env

    def build_arch(self, arch):
        super(Panda3DRecipe, self).build_arch(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            env = self.get_recipe_env(arch)

            # Run the Panda3D build process
            # Step 1: Generate the build scripts using 'makepanda.py'
            shprint(sh.python3, "makepanda/makepanda.py", "--everything", "--outputdir", "./built", "--target", "android", _env=env)

            # Step 2: Install the built files
            shprint(sh.cp, "-r", "built", self.ctx.get_python_install_dir())

recipe = Panda3DRecipe()
