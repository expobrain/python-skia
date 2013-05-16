# -*- coding: utf-8 -*-

from skia.core import SkIPoint
import unittest


class SkIPointTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkIPoint(), SkIPoint)
