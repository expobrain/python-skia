# -*- coding: utf-8 -*-

from skia.core import SkColorTable
import unittest


class SkColorTableTests(unittest.TestCase):

    @unittest.skip("FIXME")
    def testInstance(self):
        self.assertIsInstance(SkColorTable(16), SkColorTable)
        self.assertIsInstance(SkColorTable(SkColorTable(16)), SkColorTable)
