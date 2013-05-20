# -*- coding: utf-8 -*-

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
