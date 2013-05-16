# -*- coding: utf-8 -*-

from skia.core import SkRegion
import unittest


class SkRegionTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkRegion(), SkRegion)
