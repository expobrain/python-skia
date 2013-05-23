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

from skia.core import SkDeviceProperties
import unittest


class SkDevicePropertiesTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(
            SkDeviceProperties.MakeDefault(), SkDeviceProperties)
        self.assertIsInstance(
            SkDeviceProperties.Make(SkDeviceProperties.Geometry(), 1),
            SkDeviceProperties
        )
        self.assertRaises(TypeError, SkDeviceProperties)

    def test_fGeometry(self):
        self.assertIsInstance(
            SkDeviceProperties.MakeDefault().fGeometry,
            SkDeviceProperties.Geometry
        )

    def test_fGamma(self):
        self.assertIsInstance(SkDeviceProperties.MakeDefault().fGamma, float)


class SkDevicePropertiesGeometryTests(unittest.TestCase):

    @unittest.skip("FIXME")
    def test_instance(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry.MakeDefault(),
            SkDeviceProperties.Geometry
        )

    def test_fGeometry(self):
        self.assertIsInstance(SkDeviceProperties.Geometry().fGeometry, int)

    def test_orientation_enum(self):
        attrs = ("kUnknown_Orientation", "kKnown_Orientation",
                 "kHorizontal_Orientation", "kVertical_Orientation",
                 "kOrientationMask")

        for attr in attrs:
            self.assertTrue(hasattr(SkDeviceProperties.Geometry, attr))

    def test_layout_enum(self):
        attrs = ("kUnknown_Layout", "kKnown_Layout", "kRGB_Layout",
                 "kBGR_Layout", "kLayoutMask")

        for attr in attrs:
            self.assertTrue(hasattr(SkDeviceProperties.Geometry, attr))

    def test_orientation(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().getOrientation(),
            SkDeviceProperties.Geometry.Orientation
        )

    def test_is_orientation_known(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().isOrientationKnown(), bool)

    def test_is_layout_known(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().isLayoutKnown(), bool)

    def test_layout(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().getLayout(),
            SkDeviceProperties.Geometry.Layout
        )
