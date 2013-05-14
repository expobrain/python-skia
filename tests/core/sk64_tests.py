# -*- coding: utf-8 -*-

from skia.core import Sk64
import unittest


class Sk64Tests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(Sk64(), Sk64)
