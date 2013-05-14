# -*- coding: utf-8 -*-

from skia.core import SkBitmap
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

#     def test_get_size_64(self):
#         self.assertIsInstance(SkBitmap().getSize64(), Sk64)

    @unittest.skip("FIXME")
    def test_get_safe_size(self):
        self.assertEqual(SkBitmap().getSafeSize(), 0)

    @unittest.skip("FIXME")
    def test_get_pixels(self):
        self.assertIsInstance(SkBitmap().getPixels(), bytearray)
