# -*- coding: utf-8 -*-

"""
Copyright (c) 2013, Daniele Esposti <expo@expobrain.net>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * The name of the contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from optparse import OptionParser
import glob
import os
import sipconfig
import subprocess
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
        self.skia_mod_dir = os.path.join(self.default_mod_dir, "skia")

        # Build skia include dirs list
        for d in os.listdir(skia_includes_dir):
            d = os.path.join(skia_includes_dir, d)

            if os.path.isdir(d) and not d.startswith("."):
                self.skia_includes.append(d)

        # Build skia libs list
        for lib in glob.iglob(os.path.join(skia_libs_dir, "lib*.a")):
            # Remove path, extension and 'lib' prefix and add it to libs list
            lib = os.path.split(lib)[1]
            lib = os.path.splitext(lib)[0]
            lib = lib[3:]

            self.skia_libs.append(lib)


class SkiaPreprocessor(object):

    SIP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
    BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "build"))
    MODULES = ("core", "effects", "gpu")

    def generate_code(self, config):
        sip_install_dir = os.path.join(config.default_sip_dir, "skia")
        module_install_dir = os.path.join(config.default_mod_dir, "skia")

        for module in self.MODULES:
            # Calculate SIP module folder and scan for .sip files
            module_dir = os.path.join(self.SIP_DIR, module)

            sipconfig.inform("Processing {}...".format(module_dir))

            # Calculate module paths
            sip_file = os.path.join(module_dir, "{}.sip".format(module))
            build_dir = os.path.join(self.BUILD_DIR, module)
            build_file = os.path.join(build_dir, "{}.sbf".format(module))

            # Creating paths
            if not os.path.exists(build_dir):
                os.makedirs(build_dir)

            # Execute 'sip' command
            cmd = [
                config.sip_bin,
                "-c", build_dir,
                "-b", build_file,
                sip_file
            ]

            if subprocess.call(cmd):
                sipconfig.error(sip_file)
                sys.exit(1)

            # Generate module Makefile
            sipconfig.inform("Generating Makefile for '{}'...".format(module))

            makefile = sipconfig.SIPModuleMakefile(
                config,
                build_file,
                dir=build_dir,
                install_dir=module_install_dir,
                installs=[(sip_file, os.path.join(sip_install_dir, module))],
                makefile=os.path.join(build_dir, "Makefile")
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
            subdirs=[os.path.join(self.BUILD_DIR, m) for m in self.MODULES],
            installs=[(f, config.skia_mod_dir) for f in self.package_installs],
        ).generate()

    @property
    def package_installs(self):
        return [os.path.join(self.SIP_DIR, "__init__.py")]


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
