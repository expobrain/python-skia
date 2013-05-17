# -*- coding: utf-8 -*-

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
