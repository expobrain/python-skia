# -*- coding: utf-8 -*-

from optparse import OptionParser
import glob
import os
import sipconfig
import sys


class SkiaConfiguration(sipconfig.Configuration):

    def __init__(self, skia_includes_dir, skia_libs_dir):
        # Call superclass
        super(SkiaConfiguration, self).__init__()

        # Absolute paths
        skia_includes_dir = os.path.abspath(skia_includes_dir)
        skia_libs_dir = os.path.abspath(skia_libs_dir)

        # Check
        for d in (skia_includes_dir, skia_libs_dir):
            if not os.path.exists(d):
                raise IOError("{} is missing".format(d))

        self.qt_framework = False  # We are not using Qt framework
        self.skia_includes = []
        self.skia_libs_dir = skia_libs_dir
        self.skia_libs = []

        # Build skia include dirs list
        for d in os.listdir(skia_includes_dir):
            d = os.path.join(skia_includes_dir, d)

            if os.path.isdir(d) and not d.startswith("."):
                self.skia_includes.append(d)

        # Build skia libs list
        for lib in glob.iglob(os.path.join(skia_libs_dir, "lib*.a")):
            # Remove path, extention and 'lib' prefix and add it to libs list
            lib = os.path.split(lib)[1]
            lib = os.path.splitext(lib)[0]
            lib = lib[3:]

            self.skia_libs.append(lib)


class SkiaPreprocessor(object):

    SIP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "sip"))
    MODULES = ("core", "effects")

    def generate_code(self, config):
        sip_install_dir = os.path.join(config.default_sip_dir, "skia")
        module_install_dir = os.path.join(config.default_mod_dir, "skia")

        for module in self.MODULES:
            # Calculate SIP module folder and scan for .sip files
            module_dir = os.path.join(self.SIP_DIR, module)

            sipconfig.inform("Processing {}...".format(module_dir))

            # Execute 'sip' command
            sip_file = os.path.join(module_dir, "{}.sip".format(module))
            build_file = os.path.join(module_dir, "{}.sbf".format(module))

            os.system(
                " ".join([
                    config.sip_bin,
                    "-c", module_dir,
                    "-b",
                    build_file,
                    sip_file
                ])
            )

            # Generate module Makefile
            sipconfig.inform("Generating Makefile for '{}'...".format(module))

            makefile = sipconfig.SIPModuleMakefile(
                config,
                os.path.join(module_dir, "{}.sbf".format(module)),
                install_dir=module_install_dir,
                installs=[(sip_file, os.path.join(sip_install_dir, module))],
                makefile=os.path.join(module_dir, "Makefile")
            )

            makefile.extra_lib_dirs = [config.skia_libs_dir]
            makefile.extra_include_dirs = config.skia_includes
            makefile.extra_libs = config.skia_libs
            makefile.extra_lflags = ["-framework ApplicationServices"]

            makefile.generate()

        # Generate parent Makefile
        sipconfig.inform("Generating main Makefile...")
        sipconfig.ParentMakefile(
            configuration=config,
            subdirs=[os.path.join(self.SIP_DIR, m) for m in self.MODULES],
            installs=[("skia_config.py", config.default_mod_dir)]
        ).generate()


if __name__ == "__main__":
    # Get command line options
    parser = OptionParser()
    parser.add_option(
        "-L", "--skia-libraries", dest="skia_libs_dir",
        help="Skia libraries directory"
    )
    parser.add_option(
        "-I", "--skia-includes", dest="skia_include_dir",
        help="Skia headers directory"
    )

    options, args = parser.parse_args()

    if not options.skia_include_dir:
        parser.error("Missing Skia include directory")
        sys.exit(1)

    if not options.skia_libs_dir:
        parser.error("Missing Skia libraries directory")
        sys.exit(1)

    # Get the SIP configuration and pre-process code
    config = SkiaConfiguration(options.skia_include_dir, options.skia_libs_dir)
    preprocessor = SkiaPreprocessor()
    preprocessor.generate_code(config)

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
    sipconfig.create_config_module(
        "skia_config.py", "skia_config.py.in", content)
