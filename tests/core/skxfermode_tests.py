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

from skia.core import SkXfermode
import unittest


class SkXfermodeTests(unittest.TestCase):

    def test_mode_enum(self):
        attrs = (
            "kClear_Mode", "kSrc_Mode", "kDst_Mode", "kSrcOver_Mode",
            "kDstOver_Mode", "kSrcIn_Mode", "kDstIn_Mode", "kSrcOut_Mode",
            "kDstOut_Mode", "kSrcATop_Mode", "kDstATop_Mode", "kXor_Mode",
            "kPlus_Mode", "kModulate_Mode",

            "kScreen_Mode", "kLastCoeffMode",

            "kOverlay_Mode", "kDarken_Mode", "kLighten_Mode",
            "kColorDodge_Mode", "kColorBurn_Mode", "kHardLight_Mode",
            "kSoftLight_Mode", "kDifference_Mode", "kExclusion_Mode",
            "kMultiply_Mode", "kLastSeparableMode",

            "kHue_Mode", "kSaturation_Mode", "kColor_Mode", "kLuminosity_Mode",
            "kLastMode"
        )

        for attr in attrs:
            self.assertTrue(hasattr(SkXfermode, attr))
