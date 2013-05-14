# -*- coding: utf-8 -*-

from skia.core import SkCanvas
import unittest


class SkCanvasTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkCanvas(), SkCanvas)
