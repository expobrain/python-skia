# -*- coding: utf-8 -*-

from skia.core import SkRect, SkIRect, SkSize, SkIPoint, SkPoint
from tests import assert_not_fail
import unittest


class SkRectTests(unittest.TestCase):

    @property
    def rect(self):
        return SkRect.MakeEmpty()

    def test_no_default_ctors(self):
        self.assertRaises(TypeError, SkRect)

    @unittest.skip("FIXME")
    def test_deprecated_instance(self):
        self.assertRaises(
            DeprecationWarning, SkRect.MakeFromIRect, SkIRect.MakeEmpty())

    def test_instance(self):
        self.assertIsInstance(SkRect.MakeEmpty(), SkRect)
        self.assertIsInstance(SkRect.MakeWH(1, 1), SkRect)
        self.assertIsInstance(SkRect.MakeSize(SkSize.Make(1, 1)), SkRect)
        self.assertIsInstance(SkRect.MakeLTRB(1, 1, 1, 1), SkRect)
        self.assertIsInstance(SkRect.MakeXYWH(1, 1, 1, 1), SkRect)
        self.assertIsInstance(SkRect.Make(SkIRect.MakeEmpty()), SkRect)

    def test_intersects(self):
        self.assertIsInstance(self.rect.intersects(1, 1, 1, 1), bool)
        self.assertIsInstance(
            SkRect.Intersects(SkRect.MakeEmpty(), SkRect.MakeEmpty()), bool)

    def test_intersect(self):
        self.assertIsInstance(self.rect.intersect(SkRect.MakeEmpty()), bool)
        self.assertIsInstance(self.rect.intersect(1, 1, 1, 1), bool)
        self.assertIsInstance(
            self.rect.intersect(SkRect.MakeEmpty(), SkRect.MakeEmpty()), bool)

    @assert_not_fail
    def test_inset(self):
        self.rect.inset(1, 1)

    @assert_not_fail
    def test_offset(self):
        self.rect.offset(1.0, 1.0)
        self.rect.offset(SkPoint())

    @assert_not_fail
    def test_offset_to(self):
        self.rect.offsetTo(1, 1)

    @assert_not_fail
    def test_outset(self):
        self.rect.outset(1, 1)

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_to_quad(self):
        self.rect.toQuad([SkPoint(), SkPoint(), SkPoint(), SkPoint()])

    @assert_not_fail
    def test_set_empty(self):
        self.rect.setEmpty()

    @assert_not_fail
    def test_iset(self):
        self.rect.iset(1, 1, 1, 1)

    @assert_not_fail
    def test_iset_wh(self):
        self.rect.isetWH(1, 1)

    @assert_not_fail
    def test_join(self):
        self.rect.join(1, 1, 1, 1)
        self.rect.join(SkRect.MakeEmpty())

    @assert_not_fail
    def test_grow_to_include(self):
        self.rect.growToInclude(SkRect.MakeEmpty())
        self.rect.growToInclude(1.0, 1.0)

    @assert_not_fail
    def test_set(self):
        self.rect.set(SkIRect.MakeEmpty())
        self.rect.set(1.0, 1.0, 1.0, 1.0)
#         self.rect.set([SkPoint(), SkPoint()], 2)
        self.rect.set(SkPoint(), SkPoint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_set_bounds(self):
        self.rect.setBounds([SkPoint(), SkPoint()], 2)

    @unittest.skip("FIXME")
    def test_set_bounds_check(self):
        self.assertIsInstance(
            self.rect.setBoundsCheck([SkPoint(), SkPoint()], 2), bool)

    @assert_not_fail
    def test_set_largest(self):
        self.rect.setLargest()

    @assert_not_fail
    def test_set_largest_inverted(self):
        self.rect.setLargestInverted()

    @assert_not_fail
    def test_set_wh(self):
        self.rect.setWH(1, 1)

    @assert_not_fail
    def test_round(self):
        self.rect.round(SkIRect.MakeEmpty())

    @assert_not_fail
    def test_round_in(self):
        self.rect.roundIn(SkIRect.MakeEmpty())

    @assert_not_fail
    def test_round_out(self):
        self.rect.roundOut()
        self.rect.roundOut(SkIRect.MakeEmpty())

    @assert_not_fail
    def test_set_xywh(self):
        self.rect.setXYWH(1, 1, 1, 1)

    @assert_not_fail
    def test_sort(self):
        self.rect.sort()

    @assert_not_fail
    def test_set_ltrb(self):
        self.rect.setLTRB(1.0, 1.0, 1.0, 1.0)

    @unittest.skip("FIXME")
    def test_as_scalars(self):
        scalars = self.rect.asScalars()

        self.assertIsInstance(scalars, tuple)
        self.assertEqual(len(scalars), 4)
        self.assertTrue(all(isinstance(s, int) for s in scalars))

    def test_is_empty(self):
        self.assertIsInstance(self.rect.isEmpty(), bool)

    def test_is_finite(self):
        self.assertIsInstance(self.rect.isFinite(), bool)

    def test_center_x(self):
        self.assertIsInstance(self.rect.centerX(), float)

    def test_center_y(self):
        self.assertIsInstance(self.rect.centerY(), float)

    def test_contains(self):
        self.assertIsInstance(self.rect.contains(SkPoint()), bool)
        self.assertIsInstance(self.rect.contains(1, 1), bool)
        self.assertIsInstance(self.rect.contains(SkRect.MakeEmpty()), bool)

    def test_left(self):
        self.assertIsInstance(self.rect.left(), float)

    def test_top(self):
        self.assertIsInstance(self.rect.top(), float)

    def test_right(self):
        self.assertIsInstance(self.rect.right(), float)

    def test_bottom(self):
        self.assertIsInstance(self.rect.bottom(), float)

    def test_x(self):
        self.assertIsInstance(self.rect.x(), float)

    def test_y(self):
        self.assertIsInstance(self.rect.y(), float)

    def test_width(self):
        self.assertIsInstance(self.rect.width(), float)

    def test_height(self):
        self.assertIsInstance(self.rect.height(), float)


class SkIRectTests(unittest.TestCase):

    @property
    def rect(self):
        return SkIRect.MakeEmpty()

    def test_no_default_ctors(self):
        self.assertRaises(TypeError, SkIRect)

    def test_instance(self):
        self.assertIsInstance(SkIRect.EmptyIRect(), SkIRect)
        self.assertIsInstance(SkIRect.MakeEmpty(), SkIRect)
        self.assertIsInstance(SkIRect.MakeWH(1, 1), SkIRect)
        self.assertIsInstance(SkIRect.MakeSize(SkSize.Make(1, 1)), SkIRect)
        self.assertIsInstance(SkIRect.MakeLTRB(1, 1, 1, 1), SkIRect)
        self.assertIsInstance(SkIRect.MakeXYWH(1, 1, 1, 1), SkIRect)

    def test_public_attributes(self):
        rect = self.rect
        attrs = ("fLeft", "fTop", "fRight", "fBottom")

        for attr in attrs:
            self.assertIsInstance(getattr(rect, attr), int)

    @assert_not_fail
    def test_set_empty(self):
        self.rect.setEmpty()

    @assert_not_fail
    def test_set(self):
        self.rect.set(1, 1, 1, 1)

    @assert_not_fail
    def test_set_ltrb(self):
        self.rect.setLTRB(1, 1, 1, 1)

    @assert_not_fail
    def test_set_xywh(self):
        self.rect.setXYWH(1, 1, 1, 1)

    @assert_not_fail
    def test_set_largest(self):
        self.rect.setLargest()

    @assert_not_fail
    def test_set_largest_inverted(self):
        self.rect.setLargestInverted()

    @assert_not_fail
    def test_inset(self):
        self.rect.inset(1, 1)

    @assert_not_fail
    def test_outset(self):
        self.rect.outset(1, 1)

    @assert_not_fail
    def test_offset_to(self):
        self.rect.offsetTo(1, 1)

    @assert_not_fail
    def test_offset(self):
        self.rect.offset(1, 1)
        self.rect.offset(SkIPoint())

    def test_quick_reject(self):
        self.assertIsInstance(self.rect.quickReject(1, 1, 1, 1), bool)

    @assert_not_fail
    def test_sort(self):
        self.rect.sort()

    @assert_not_fail
    def test_join(self):
        self.rect.join(1, 1, 1, 1)
        self.rect.join(SkIRect.MakeEmpty())

    def test_contains_no_empty_check(self):
        self.assertIsInstance(self.rect.containsNoEmptyCheck(1, 1, 1, 1), bool)
        self.assertIsInstance(
            self.rect.containsNoEmptyCheck(SkIRect.MakeEmpty()), bool)

    def test_intersect_no_empty_check(self):
        self.assertIsInstance(
            self.rect.intersectNoEmptyCheck(
                SkIRect.MakeEmpty(), SkIRect.MakeEmpty()
            ), bool
        )

    def test_intersects_no_empty_check(self):
        self.assertIsInstance(
            SkIRect.IntersectsNoEmptyCheck(
                SkIRect.MakeEmpty(), SkIRect.MakeEmpty()
            ),
            bool
        )

    def test_intersects(self):
        self.assertIsInstance(
            SkIRect.Intersects(SkIRect.MakeEmpty(), SkIRect.MakeEmpty()), bool)

    def test_intersect(self):
        self.assertIsInstance(self.rect.intersect(1, 1, 1, 1), bool)
        self.assertIsInstance(self.rect.intersect(SkIRect.MakeEmpty()), bool)
        self.assertIsInstance(
            self.rect.intersect(SkIRect.MakeEmpty(), SkIRect.MakeEmpty()), bool)

    def test_contains(self):
        self.assertIsInstance(self.rect.contains(SkIRect.MakeEmpty()), bool)
        self.assertIsInstance(self.rect.contains(1, 1), bool)
        self.assertIsInstance(self.rect.contains(1, 1, 1, 1), bool)

    def test_is_16_bit(self):
        self.assertIsInstance(self.rect.is16Bit(), bool)

    def test_is_empty(self):
        self.assertIsInstance(self.rect.isEmpty(), bool)

    def test_center_x(self):
        self.assertIsInstance(self.rect.centerX(), int)

    def test_center_y(self):
        self.assertIsInstance(self.rect.centerY(), int)

    def test_left(self):
        self.assertIsInstance(self.rect.left(), int)

    def test_top(self):
        self.assertIsInstance(self.rect.top(), int)

    def test_right(self):
        self.assertIsInstance(self.rect.right(), int)

    def test_bottom(self):
        self.assertIsInstance(self.rect.bottom(), int)

    def test_x(self):
        self.assertIsInstance(self.rect.x(), int)

    def test_y(self):
        self.assertIsInstance(self.rect.y(), int)

    def test_width(self):
        self.assertIsInstance(self.rect.width(), int)

    def test_height(self):
        self.assertIsInstance(self.rect.height(), int)
