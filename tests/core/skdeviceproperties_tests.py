# -*- coding: utf-8 -*-

from skia.core import SkDeviceProperties
import unittest


class SkDevicePropertiesTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(
            SkDeviceProperties.MakeDefault(), SkDeviceProperties)
        self.assertIsInstance(
            SkDeviceProperties.Make(SkDeviceProperties.Geometry(), 1),
            SkDeviceProperties
        )
        self.assertRaises(TypeError, SkDeviceProperties)

    def test_fGeometry(self):
        self.assertIsInstance(
            SkDeviceProperties.MakeDefault().fGeometry,
            SkDeviceProperties.Geometry
        )

    def test_fGamma(self):
        self.assertIsInstance(SkDeviceProperties.MakeDefault().fGamma, float)


class SkDevicePropertiesGeometryTests(unittest.TestCase):

    @unittest.skip("FIXME")
    def test_instance(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry.MakeDefault(),
            SkDeviceProperties.Geometry
        )

    def test_fGeometry(self):
        self.assertIsInstance(SkDeviceProperties.Geometry().fGeometry, int)

    def test_orientation_enum(self):
        attrs = ("kUnknown_Orientation", "kKnown_Orientation",
                 "kHorizontal_Orientation", "kVertical_Orientation",
                 "kOrientationMask")

        for attr in attrs:
            self.assertTrue(hasattr(SkDeviceProperties.Geometry, attr))

    def test_layout_enum(self):
        attrs = ("kUnknown_Layout", "kKnown_Layout", "kRGB_Layout",
                 "kBGR_Layout", "kLayoutMask")

        for attr in attrs:
            self.assertTrue(hasattr(SkDeviceProperties.Geometry, attr))

    def test_orientation(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().getOrientation(),
            SkDeviceProperties.Geometry.Orientation
        )

    def test_is_orientation_known(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().isOrientationKnown(), bool)

    def test_is_layout_known(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().isLayoutKnown(), bool)

    def test_layout(self):
        self.assertIsInstance(
            SkDeviceProperties.Geometry().getLayout(),
            SkDeviceProperties.Geometry.Layout
        )
