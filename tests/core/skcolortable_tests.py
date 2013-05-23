# -*- coding: utf-8 -*-

"""
Copyright (c) 2013, Daniele Esposti <expo@expobrain.net>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * The name of the contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
