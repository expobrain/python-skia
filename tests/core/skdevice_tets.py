# -*- coding: utf-8 -*-

from skia.core import SkDevice, SkBitmap
import unittest


class Sk64Tests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkDevice(SkBitmap()), SkDevice)
