# -*- coding: utf-8 -*-

from skia.core import SkSize, SkISize
import unittest


class SkSizeTests(unittest.TestCase):

    def test_no_default_ctors(self):
        self.assertRaises(TypeError, SkSize)

    def test_instance(self):
        self.assertIsInstance(SkSize.Make(1, 1), SkSize)

    def test_to_round(self):
        self.assertIsInstance(SkSize.Make(1, 1).toRound(), SkISize)

    def test_to_ceil(self):
        self.assertIsInstance(SkSize.Make(1, 1).toCeil(), SkISize)

    def test_to_floor(self):
        self.assertIsInstance(SkSize.Make(1, 1).toFloor(), SkISize)
