# -*- coding: utf-8 -*-

from skia.core import SkCanvas, SkDevice, SkBitmap
import unittest


class SkCanvasTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkCanvas(), SkCanvas)
        self.assertIsInstance(SkCanvas(SkDevice(SkBitmap())), SkCanvas)
        self.assertIsInstance(SkCanvas(SkBitmap()), SkCanvas)

    def test_config888_enum(self):
        attrs = ("kNative_Premul_Config8888", "kNative_Unpremul_Config8888",
                 "kBGRA_Premul_Config8888", "kBGRA_Unpremul_Config8888",
                 "kRGBA_Premul_Config8888", "kRGBA_Unpremul_Config8888")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))
