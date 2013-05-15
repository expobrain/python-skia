# -*- coding: utf-8 -*-

from skia.core import SkRect, SkIRect
import unittest


class SkRectTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkRect(), SkRect)


class SkIRectTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkIRect(), SkIRect)
