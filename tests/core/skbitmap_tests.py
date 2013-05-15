# -*- coding: utf-8 -*-

from skia.core import SkBitmap, Sk64
import unittest


class SkBitmapTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkBitmap(), SkBitmap)

    def test_config_enum(self):
        attrs = ("kNo_Config", "kA1_Config", "kA8_Config", "kIndex8_Config",
                 "kRGB_565_Config", "kARGB_4444_Config", "kARGB_8888_Config",
                 "kRLE_Index8_Config", "kConfigCount")

        for attr in attrs:
            self.assertTrue(hasattr(SkBitmap, attr))

    def test_copy_constructor(self):
        self.assertIsInstance(SkBitmap(SkBitmap()), SkBitmap)

    def test_empty(self):
        self.assertTrue(SkBitmap().empty())

    def test_is_null(self):
        self.assertTrue(SkBitmap().isNull())

    def test_config(self):
        self.assertEqual(SkBitmap().config(), SkBitmap.kNo_Config)

    def test_width(self):
        self.assertEqual(SkBitmap().width(), 0)

    def test_height(self):
        self.assertEqual(SkBitmap().height(), 0)

    @unittest.skip("FIXME")
    def test_row_bytes(self):
        self.assertEqual(SkBitmap().rowBytes(), 0)

    def test_shift_per_pixel(self):
        self.assertEqual(SkBitmap().shiftPerPixel(), 0)

    def test_bytes_per_pixel(self):
        self.assertEqual(SkBitmap().bytesPerPixel(), 0)

    @unittest.skip("FIXME")
    def test_row_bytes_as_pixels(self):
        self.assertEqual(SkBitmap().rowBytesAsPixels(), 0)

    @unittest.skip("FIXME")
    def test_get_size(self):
        self.assertEqual(SkBitmap().getSize(), 0)

    def test_get_size_64(self):
        self.assertIsInstance(SkBitmap().getSize64(), Sk64)

    @unittest.skip("FIXME")
    def test_get_safe_size(self):
        self.assertEqual(SkBitmap().getSafeSize(), 0)

    def test_get_safe_size_64(self):
        self.assertIsInstance(SkBitmap().getSafeSize64(), Sk64)

    def test_is_immutable(self):
        self.assertIsInstance(SkBitmap().isImmutable(), bool)

    def test_is_volatile(self):
        self.assertIsInstance(SkBitmap().isVolatile(), bool)

    def test_is_opaque(self):
        self.assertIsInstance(SkBitmap().isOpaque(), bool)

    def test_reset(self):
        try:
            SkBitmap().reset()
        except Exception as e:
            self.fail(e)

    def test_compute_bytes_per_pixel(self):
        self.assertIsInstance(
            SkBitmap.ComputeBytesPerPixel(SkBitmap.kA8_Config), int)

    def test_compute_shift_per_pixel(self):
        self.assertIsInstance(
            SkBitmap.ComputeShiftPerPixel(SkBitmap.kA8_Config), int)

    def test_compute_size_64(self):
        self.assertIsInstance(
            SkBitmap.ComputeSize64(SkBitmap.kA8_Config, 1, 1), Sk64)

    def test_compute_is_opaque(self):
        self.assertIsInstance(SkBitmap.ComputeIsOpaque(SkBitmap()), int)

    def test_compute_and_set_opaque_predicate(self):
        try:
            SkBitmap().computeAndSetOpaquePredicate()
        except Exception as e:
            self.fail(e)

#     def test_get_bounds(self):
#         for rect in (Skrect(), SkIRect()):
#             try:
#                 SkBitmap().getBound(rect)
#             except Exception as e:
#                 self.fail(e)

    @unittest.skip("FIXME")
    def test_compute_size(self):
        self.assertIsInstance(
            SkBitmap.ComputeSize(SkBitmap.kA8_Config, 1, 1), int)

    @unittest.skip("FIXME")
    def test_compute_row_bytes(self):
        try:
            SkBitmap.ComputeRowBytes(SkBitmap.kA1_Config, 100)
        except Exception as e:
            self.fail(e)

    @unittest.skip("FIXME")
    def test_set_config(self):
        b = SkBitmap()
        b.setConfig(SkBitmap.kARGB_8888_Config, 100, 200)

        self.assertEqual(b.config(), SkBitmap.kARGB_8888_Config)
        self.assertEqual(b.width(), 100)
        self.assertEqual(b.height(), 200)

    def test_set_immutable(self):
        b = SkBitmap()
        self.assertFalse(b.isImmutable())

        b.setImmutable()
        self.assertTrue(b.isImmutable())

    def test_set_volatile(self):
        b = SkBitmap()
        self.assertFalse(b.isVolatile())

        b.setIsVolatile(True)
        self.assertTrue(b.isVolatile())

    @unittest.skip("FIXME")
    def test_set_is_opaque(self):
        b = SkBitmap()

        for v in (True, False):
            b.setIsOpaque(v)

            self.assertEqual(b.isOpaque(), v)

    @unittest.skip("FIXME")
    def test_get_pixels(self):
        self.assertIsInstance(SkBitmap().getPixels(), bytearray)
