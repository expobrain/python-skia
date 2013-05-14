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
