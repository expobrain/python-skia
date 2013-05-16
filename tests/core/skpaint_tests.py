# -*- coding: utf-8 -*-

from skia.core import SkPaint
import unittest


class SkPaintTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkPaint(), SkPaint)
