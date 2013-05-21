# -*- coding: utf-8 -*-

from skia.core import SkMatrix
import unittest


class SkMatrixTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkMatrix(), SkMatrix)
