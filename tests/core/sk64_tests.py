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

from skia.core import Sk64
import unittest


class Sk64Tests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(Sk64(), Sk64)

    def test_hi_lo(self):
        self.assertIsInstance(Sk64().fHi, int)
        self.assertIsInstance(Sk64().fLo, int)

    def test_is_32(self):
        self.assertIsInstance(Sk64().is32(), bool)

    def test_get_32(self):
        self.assertIsInstance(Sk64().get32(), int)

    def test_get_sign(self):
        self.assertIsInstance(Sk64().getSign(), int)

    def test_is_64(self):
        self.assertIsInstance(Sk64().is64(), bool)

    def test_is_zero(self):
        self.assertIsInstance(Sk64().isZero(), bool)

    def test_is_pos(self):
        self.assertIsInstance(Sk64().isPos(), bool)

    def test_non_zero(self):
        self.assertIsInstance(Sk64().nonZero(), bool)

    def test_is_fixed(self):
        self.assertIsInstance(Sk64().isFixed(), bool)

    def test_is_neg(self):
        self.assertIsInstance(Sk64().isNeg(), bool)

    def test_get_fixed(self):
        self.assertIsInstance(Sk64().getFixed(), int)

    def test_get_fract(self):
        self.assertIsInstance(Sk64().getFract(), int)

    def test_get_sqtr(self):
        self.assertIsInstance(Sk64().getSqrt(), int)

    def test_get_clx_abs(self):
        self.assertIsInstance(Sk64().getClzAbs(), int)

    def test_shift_to_make_32(self):
        self.assertIsInstance(Sk64().shiftToMake32(), int)

    def test_div_optins_enum(self):
        for attr in ("kTrunc_DivOption", "kRound_DivOption"):
            self.assertTrue(hasattr(Sk64, attr))

    def test_div(self):
        try:
            Sk64().div(1, Sk64.kTrunc_DivOption)
        except Exception as e:
            self.fail(e)

    def test_add_get_fixed(self):
        self.assertIsInstance(Sk64().addGetFixed(Sk64()), int)
        self.assertIsInstance(Sk64().addGetFixed(1, 1), int)

    def test_get_fixed_div(self):
        self.assertIsInstance(Sk64().getFixedDiv(Sk64()), int)

    def test_get_logn_long(self):
        self.assertIsInstance(Sk64().getLongLong(), long)

    @unittest.skip("MISSING IN skia")
    def test_mul(self):
        try:
            Sk64().mul(1)
        except Exception as e:
            self.fail(e)

    def test_sub(self):
        try:
            Sk64().sub(Sk64())
        except Exception as e:
            self.fail(e)

    def test_add(self):
        try:
            Sk64().add(1)
            Sk64().add(1, 1)
            Sk64().add(Sk64())
        except Exception as e:
            self.fail(e)

    def test_round_right(self):
        try:
            Sk64().roundRight(1)
        except Exception as e:
            self.fail(e)

    def test_shift_right(self):
        try:
            Sk64().shiftRight(1)
        except Exception as e:
            self.fail(e)

    def test_shift_left(self):
        try:
            Sk64().shiftLeft(1)
        except Exception as e:
            self.fail(e)

    def test_set_mul(self):
        try:
            Sk64().setMul(1, 1)
        except Exception as e:
            self.fail(e)

    def test_set(self):
        try:
            Sk64().set(1)
            Sk64().set(1, 1)
        except Exception as e:
            self.fail(e)

    def test_set_zero(self):
        try:
            Sk64().setZero()
        except Exception as e:
            self.fail(e)

    def test_negate(self):
        try:
            Sk64().negate()
        except Exception as e:
            self.fail(e)

    def test_abs(self):
        try:
            Sk64().abs()
        except Exception as e:
            self.fail(e)
