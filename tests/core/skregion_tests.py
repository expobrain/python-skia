# -*- coding: utf-8 -*-

from skia.core import SkRegion
import unittest


class SkRegionTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkRegion(), SkRegion)

    def test_config_enum(self):
        attrs = ("kDifference_Op", "kIntersect_Op", "kUnion_Op", "kXOR_Op",
                 "kReverseDifference_Op", "kReplace_Op")

        for attr in attrs:
            self.assertTrue(hasattr(SkRegion, attr))
