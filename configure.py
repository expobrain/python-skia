import os
import sipconfig
import glob


class SkiaConfiguration(sipconfig.Configuration):

    SIP_DIR = os.path.join(os.path.dirname(__file__), "sip")
    MODULES = ["core"]

    def __init__(self):
        super(SkiaConfiguration, self).__init__()

        self.qt_framework = False

    @property
    def installs(self):
        return [("skia_config.py", self.default_mod_dir)]

    def generate_code(self):
        for module in self.MODULES:
            # Calculate SIP module folder and scan for .sip files
            module_installs = []
            module_dir = os.path.join(self.SIP_DIR, module)
            sip_defs = (os.path.splitext(f)[0]
                        for f in glob.iglob(os.path.join(module_dir, "*.sip")))

            sipconfig.inform("Processing {}...".format(module_dir))

            # Execute 'sip' command and update installs
            for sip_def in sip_defs:
                sip_file = "{}.sip".format(sip_def)
                build_file = "{}.sbf".format(sip_def)

                sipconfig.inform("..generating code for {}".format(sip_def))

                os.system(
                    " ".join([
                        self.sip_bin, "-c", module_dir, "-b",
                        build_file,
                        sip_file
                    ])
                )

                # Update installs
                module_installs.append(
                    (sip_file, os.path.join(self.default_sip_dir, sip_def)))

            # Generate module Makefile
            sipconfig.inform("Generating Makefile for '{}'...".format(module))

            makefiles = sipconfig.SIPModuleMakefile(
                self,
                os.path.join(module_dir, "{}.sbf".format(module)),
                installs=module_installs,
                makefile=os.path.join(module_dir, "Makefile")
            )

            makefiles.extra_lib_dirs = [
                os.path.join("..", "skia", "out", "Release"),
            ]
            makefiles.extra_include_dirs = [
                os.path.join("..", "skia", "include", "core"),
                os.path.join("..", "skia", "include", "config"),
            ]
            makefiles.extra_libs = [
                "skia_core", "skia_gr", "skia_skgr", "skia_ports", "skia_sfnt",
                "skia_opts", "skia_opts_ssse3"
            ]
            makefiles.extra_lflags = ["-framework ApplicationServices"]

            makefiles.generate()

        # Generate parent Makefile
        sipconfig.inform("Generating main Makefile...")
        sipconfig.ParentMakefile(
            configuration=self,
            subdirs=[os.path.join(self.SIP_DIR, m) for m in self.MODULES],
            installs=self.installs
        ).generate()


if __name__ == "__main__":
    # Get the SIP configuration information.
    config = SkiaConfiguration()
    config.generate_code()

    # Now we create the configuration module.  This is done by merging a Python
    # dictionary (whose values are normally determined dynamically) with a
    # (static) template.
    content = {
        # Publish where the SIP specifications for this module will be
        # installed.
        "skia_sip_dir": config.default_sip_dir,

        # Publish the set of SIP flags needed by this module.  As these are the
        # same flags needed by the qt module we could leave it out, but this
        # allows us to change the flags at a later date without breaking
        # scripts that import the configuration module.
    #     "hello_sip_flags":  pyqt_sip_flags
    }

    # This creates the helloconfig.py module from the helloconfig.py.in
    # template and the dictionary.
    sipconfig.create_config_module("skia_config.py", "skia_config.py.in", content)
