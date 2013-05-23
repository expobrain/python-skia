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

from skia.core import (SkDevice, SkBitmap, SkDeviceProperties, SkIRect,
    SkGpuRenderTarget, SkIPoint, SkCanvas)
from tests import assert_not_fail
import unittest


class Sk64Tests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkDevice(SkBitmap()), SkDevice)
        self.assertIsInstance(
            SkDevice(SkBitmap(), SkDeviceProperties.MakeDefault()), SkDevice)
        self.assertIsInstance(SkDevice(SkBitmap.kA8_Config, 1, 1), SkDevice)
        self.assertIsInstance(
            SkDevice(SkBitmap.kA8_Config, 1, 1, isOpaque=True), SkDevice)
        self.assertIsInstance(
            SkDevice(
                SkBitmap.kA8_Config,
                1, 1,
                True,
                SkDeviceProperties.MakeDefault()
            ),
            SkDevice
        )

    @unittest.skip("FIXME")
    def test_create_compatible_device(self):
        self.assertIsInstance(
            SkDevice().createCompatibleDevice(SkBitmap.kA8_Config, 1, 1, True),
            SkDevice
        )

    def test_capabilities_enum(self):
        attrs = ("kGL_Capability", "kVector_Capability", "kAll_Capabilities")

        for attr in attrs:
            self.assertTrue(hasattr(SkDevice, attr))

    def test_get_device_capabilities(self):
        self.assertIsInstance(SkDevice(SkBitmap()).getDeviceCapabilities(), int)

    def test_get_device_properties(self):
        self.assertIsInstance(
            SkDevice(SkBitmap()).getDeviceProperties(), SkDeviceProperties)

    def test_config(self):
        self.assertIsInstance(SkDevice(SkBitmap()).config(), SkBitmap.Config)

    @assert_not_fail
    def test_access_bitmap(self):
        SkDevice(SkBitmap()).accessBitmap(False)

    @assert_not_fail
    def test_on_attach_to_canvas(self):
        SkDevice(SkBitmap()).onAttachToCanvas(SkCanvas())

    @assert_not_fail
    def test_on_detach_from_canvas(self):
        SkDevice(SkBitmap()).onDetachFromCanvas()

    @unittest.skip("FIXME")
    def test_write_pixels(self):
        with self.assertRaises(DeprecationWarning):
            SkDevice(SkBitmap()).writePixels(SkBitmap(), 1, 1)

    @unittest.skip("FIXME")
    def test_get_global_bounds(self):
        self.assertIsInstance(SkDevice(SkBitmap()).getGlobalBounds(), SkIRect)

    @unittest.skip("FIXME")
    def test_access_rendered_target(self):
        self.assertIsInstance(
            SkDevice(SkBitmap()).accessRenderTarget(), SkGpuRenderTarget)

    def test_is_opaque(self):
        self.assertIsInstance(SkDevice(SkBitmap()).isOpaque(), bool)

    def test_get_origin(self):
        self.assertIsInstance(SkDevice(SkBitmap()).getOrigin(), SkIPoint)

    def test_width(self):
        self.assertIsInstance(SkDevice(SkBitmap()).width(), int)

    def test_height(self):
        self.assertIsInstance(SkDevice(SkBitmap()).height(), int)
