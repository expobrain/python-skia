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

from skia.core import SkAdvancedTypefaceMetrics, SkString, SkIRect
from tests import SkiaTestMixin
import unittest


class SkAdvancedTypefaceMetricsVerticalMetricTests(SkiaTestMixin,
                                                   unittest.TestCase):
    @property
    def metric(self):
        return SkAdvancedTypefaceMetrics.VerticalMetric()

    def test_attributes(self):
        metric = self.metric

        self.assertIsInstance(metric.fVerticalAdvance, int)
        self.assertIsInstance(metric.fOriginXDisp, int)
        self.assertIsInstance(metric.fOriginYDisp, int)

    def test_instance(self):
        self.assertIsInstance(
            SkAdvancedTypefaceMetrics.VerticalMetric(),
            SkAdvancedTypefaceMetrics.VerticalMetric
        )


class SkAdvancedTypefaceMetricsTests(SkiaTestMixin, unittest.TestCase):

    @property
    def atmetrics(self):
        return SkAdvancedTypefaceMetrics()

    def test_attributes(self):
        metrics = self.atmetrics

        self.assertIsInstance(metrics.fFontName, SkString)
        self.assertIsInstance(metrics.fMultiMaster, bool)
        self.assertIsInstance(metrics.fLastGlyphID, int)
        self.assertIsInstance(metrics.fStyle, int)
        self.assertIsInstance(metrics.fItalicAngle, int)
        self.assertIsInstance(metrics.fAscent, int)
        self.assertIsInstance(metrics.fDescent, int)
        self.assertIsInstance(metrics.fStemV, int)
        self.assertIsInstance(metrics.fCapHeight, int)
        self.assertIsInstance(metrics.fEmSize, int)
        self.assertIsInstance(metrics.fBBox, SkIRect)
        self.assertIsInstance(metrics.fType, SkAdvancedTypefaceMetrics.FontType)

    def test_font_type_enum(self):
        self.assertHasEnum(
            SkAdvancedTypefaceMetrics,
            "FontType",
            ("kType1_Font", "kType1CID_Font", "kCFF_Font", "kTrueType_Font",
             "kOther_Font", "kNotEmbeddable_Font")
        )

    def test_style_flags_enum(self):
        self.assertHasEnum(
            SkAdvancedTypefaceMetrics,
            "StyleFlags",
            ("kFixedPitch_Style", "kSerif_Style", "kScript_Style",
             "kItalic_Style", "kAllCaps_Style", "kSmallCaps_Style",
             "kForceBold_Style")
        )

    def test_per_glyph_info_enum(self):
        self.assertHasEnum(
            SkAdvancedTypefaceMetrics,
            "PerGlyphInfo",
            ("kNo_PerGlyphInfo", "kHAdvance_PerGlyphInfo",
             "kVAdvance_PerGlyphInfo", "kGlyphNames_PerGlyphInfo",
             "kToUnicode_PerGlyphInfo")
        )
