# -*- coding: utf-8 -*-

from skia.core import SkRRect
import unittest


class SkRRectTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkRRect(), SkRRect)
