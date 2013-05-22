# -*- coding: utf-8 -*-

from skia.core import SkIPoint, SkPoint
import unittest


class SkIPointTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkIPoint(), SkIPoint)


class SkPointTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkPoint(), SkPoint)
