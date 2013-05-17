# -*- coding: utf-8 -*-

from skia.core import SkColorTable
import unittest


class SkColorTableTests(unittest.TestCase):

    @unittest.skip("FIXME")
    def test_instance(self):
        self.assertIsInstance(SkColorTable(16), SkColorTable)
        self.assertIsInstance(SkColorTable(SkColorTable(16)), SkColorTable)

    def test_flags_enum(self):
        self.assertTrue(hasattr(SkColorTable, "kColorsAreOpaque_Flag"))

    @unittest.skip("FIXME")
    def test_get_flags(self):
        self.assertIsInstance(SkColorTable(16).getFlags(), int)

    @unittest.skip("FIXME")
    def test_is_opaque(self):
        self.assertIsInstance(SkColorTable(16).isOpaque(), bool)

    @unittest.skip("FIXME")
    def test_count(self):
        self.assertIsInstance(SkColorTable(16).count(), bool)

    @unittest.skip("FIXME")
    def test_lock_colors(self):
        self.assertIsInstance(SkColorTable(16).lockColors(), int)

    @unittest.skip("FIXME")
    def test_lock_16_bit_cache(self):
        self.assertIsInstance(SkColorTable(16).lock16BitCache(), int)

    @unittest.skip("FIXME")
    def test_unlock_colors(self):
        try:
            SkColorTable(16).unlockColors()
            SkColorTable(16).unlockColors(False)
        except Exception as e:
            self.fail(e)

    @unittest.skip("FIXME")
    def test_unlock_16_bit_cache(self):
        try:
            SkColorTable(16).unlock16BitCache()
        except Exception as e:
            self.fail(e)

    @unittest.skip("FIXME")
    def test_set_flags(self):
        t = SkColorTable(16)
        t.setFlags(SkColorTable.kColorsAreOpaque_Flag)

        self.assertEqual(t.getFlags(), SkColorTable.kColorsAreOpaque_Flag)
