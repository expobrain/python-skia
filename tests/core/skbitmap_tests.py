# -*- coding: utf-8 -*-

from skia.core import (SkBitmap, Sk64, SkRect, SkIRect, SkPixelRef, SkGpuTexture,
    SkColorTable, SkPaint, SkIPoint, SkAutoLockPixels, SkAutoLockColors)
from tests import assert_not_fail
import unittest


class SkBitmapTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkBitmap(), SkBitmap)

    def test_config_enum(self):
        attrs = ("kNo_Config", "kA1_Config", "kA8_Config", "kIndex8_Config",
                 "kRGB_565_Config", "kARGB_4444_Config", "kARGB_8888_Config",
                 "kRLE_Index8_Config", "kConfigCount")

        for attr in attrs:
            self.assertTrue(hasattr(SkBitmap, attr))

    def test_copy_constructor(self):
        self.assertIsInstance(SkBitmap(SkBitmap()), SkBitmap)

    def test_empty(self):
        self.assertTrue(SkBitmap().empty())

    def test_is_null(self):
        self.assertTrue(SkBitmap().isNull())

    def test_config(self):
        self.assertEqual(SkBitmap().config(), SkBitmap.kNo_Config)

    def test_width(self):
        self.assertEqual(SkBitmap().width(), 0)

    def test_height(self):
        self.assertEqual(SkBitmap().height(), 0)

    @unittest.skip("FIXME")
    def test_row_bytes(self):
        self.assertEqual(SkBitmap().rowBytes(), 0)

    def test_shift_per_pixel(self):
        self.assertEqual(SkBitmap().shiftPerPixel(), 0)

    def test_bytes_per_pixel(self):
        self.assertEqual(SkBitmap().bytesPerPixel(), 0)

    @unittest.skip("FIXME")
    def test_row_bytes_as_pixels(self):
        self.assertEqual(SkBitmap().rowBytesAsPixels(), 0)

    @unittest.skip("FIXME")
    def test_get_size(self):
        self.assertEqual(SkBitmap().getSize(), 0)

    def test_get_size_64(self):
        self.assertIsInstance(SkBitmap().getSize64(), Sk64)

    @unittest.skip("FIXME")
    def test_get_safe_size(self):
        self.assertEqual(SkBitmap().getSafeSize(), 0)

    def test_get_safe_size_64(self):
        self.assertIsInstance(SkBitmap().getSafeSize64(), Sk64)

    def test_is_immutable(self):
        self.assertIsInstance(SkBitmap().isImmutable(), bool)

    def test_is_volatile(self):
        self.assertIsInstance(SkBitmap().isVolatile(), bool)

    def test_is_opaque(self):
        self.assertIsInstance(SkBitmap().isOpaque(), bool)

    def test_reset(self):
        try:
            SkBitmap().reset()
        except Exception as e:
            self.fail(e)

    def test_compute_bytes_per_pixel(self):
        self.assertIsInstance(
            SkBitmap.ComputeBytesPerPixel(SkBitmap.kA8_Config), int)

    def test_compute_shift_per_pixel(self):
        self.assertIsInstance(
            SkBitmap.ComputeShiftPerPixel(SkBitmap.kA8_Config), int)

    def test_compute_size_64(self):
        self.assertIsInstance(
            SkBitmap.ComputeSize64(SkBitmap.kA8_Config, 1, 1), Sk64)

    def test_compute_is_opaque(self):
        self.assertIsInstance(SkBitmap.ComputeIsOpaque(SkBitmap()), int)

    def test_ready_to_draw(self):
        self.assertIsInstance(SkBitmap().readyToDraw(), bool)

    def test_compute_and_set_opaque_predicate(self):
        try:
            SkBitmap().computeAndSetOpaquePredicate()
        except Exception as e:
            self.fail(e)

    @unittest.skip("FIX ME")
    def test_get_texture(self):
        b = SkBitmap()
        b.setConfig(SkBitmap.kA8_Config, 1, 1)

        self.assertIsInstance(b.getTexture(), SkGpuTexture)

    @unittest.skip("FIX ME")
    def test_get_index_8_color(self):
        self.assertIsInstance(SkBitmap().getIndex8Color(0, 0), int)

    def test_get_color(self):
        self.assertIsInstance(SkBitmap().getColor(0, 0), int)

    def test_can_copy_to(self):
        self.assertIsInstance(SkBitmap().canCopyTo(SkBitmap.kA8_Config), bool)

    def test_has_mip_map(self):
        self.assertIsInstance(SkBitmap().hasMipMap(), bool)

    def test_extract_alpha(self):
        self.assertIsInstance(SkBitmap().extractAlpha(SkBitmap()), bool)
        self.assertIsInstance(
            SkBitmap().extractAlpha(SkBitmap(), SkPaint(), SkIPoint()), bool)

    def test_extract_mip_level(self):
        self.assertIsInstance(
            SkBitmap().extractMipLevel(SkBitmap(), 0, 0), int)

    def test_free_mip_map(self):
        try:
            SkBitmap().freeMipMap()
        except Exception as e:
            self.fail(e)

    def test_build_mip_map(self):
        try:
            SkBitmap().buildMipMap()
            SkBitmap().buildMipMap(True)
        except Exception as e:
            self.fail(e)

    def test_scroll_rect(self):
        self.assertIsInstance(SkBitmap().scrollRect(SkIRect(), 0, 0), bool)

    def test_erase_RGB(self):
        try:
            SkBitmap().eraseRGB(0xff, 0xff, 0xff)
        except Exception as e:
            self.fail(e)

    def test_erase_color(self):
        try:
            SkBitmap().eraseColor(0x00)
        except Exception as e:
            self.fail(e)

    def test_erase_ARGB(self):
        try:
            SkBitmap().eraseARGB(0xff, 0xff, 0xff, 0xff)
        except Exception as e:
            self.fail(e)

    @unittest.skip("FIX ME")
    def test_get_color_table(self):
        self.assertIsInstance(SkBitmap().getColorTable(), SkColorTable)

    def test_get_color_table_default(self):
        self.assertIsNone(SkBitmap().getColorTable())

    def test_get_generation_id(self):
        self.assertIsInstance(SkBitmap().getGenerationID(), int)

    def test_notify_pixels_changed(self):
        try:
            SkBitmap().notifyPixelsChanged()
        except Exception as e:
            self.fail(e)

    def test_get_texture_null(self):
        self.assertIsNone(SkBitmap().getTexture())

    def test_loc_pixels_are_writable(self):
        self.assertIsInstance(SkBitmap().lockPixelsAreWritable(), bool)

    def test_lock_pixels(self):
        try:
            SkBitmap().lockPixels()
        except Exception as e:
            self.fail(e)

    def test_unlock_pixels(self):
        try:
            SkBitmap().unlockPixels()
        except Exception as e:
            self.fail(e)

    def test_get_bounds(self):
        for rect in (SkRect(), SkIRect()):
            try:
                SkBitmap().getBounds(rect)
            except Exception as e:
                self.fail(e)

    @unittest.skip("FIXME")
    def test_set_pixels(self):
        pass

    def test_alloc_pixels(self):
        self.assertIsInstance(SkBitmap().allocPixels(), bool)

    def test_pixel_ref(self):
        self.assertIsNone(SkBitmap().pixelRef())  # Default value

    @unittest.skip("FIXME")
    def test_pixel_ref_offset(self):
        pass

    @unittest.skip("FIXME")
    def test_set_pixel_ref(self):
        b = SkBitmap()
        b.setPixelRef(SkPixelRef())

        self.assertIsInstance(SkBitmap().pixelRef(), SkPixelRef)

    @unittest.skip("FIXME")
    def test_copy_pixels(self):
        pass

    @unittest.skip("FIXME")
    def test_compute_size(self):
        self.assertIsInstance(
            SkBitmap.ComputeSize(SkBitmap.kA8_Config, 1, 1), int)

    @unittest.skip("FIXME")
    def test_compute_row_bytes(self):
        try:
            SkBitmap.ComputeRowBytes(SkBitmap.kA1_Config, 100)
        except Exception as e:
            self.fail(e)

    @assert_not_fail
    def test_set_config(self):
        b = SkBitmap()

        b.setConfig(SkBitmap.kARGB_8888_Config, 1, 1)
        b.setConfig(SkBitmap.kARGB_8888_Config, 1, 1, 1)

    def test_set_immutable(self):
        b = SkBitmap()
        self.assertFalse(b.isImmutable())

        b.setImmutable()
        self.assertTrue(b.isImmutable())

    def test_set_volatile(self):
        b = SkBitmap()
        self.assertFalse(b.isVolatile())

        b.setIsVolatile(True)
        self.assertTrue(b.isVolatile())

    @unittest.skip("FIXME")
    def test_set_is_opaque(self):
        b = SkBitmap()

        for v in (True, False):
            b.setIsOpaque(v)

            self.assertEqual(b.isOpaque(), v)

    @unittest.skip("FIXME")
    def test_get_pixels(self):
        self.assertIsInstance(SkBitmap().getPixels(), bytearray)


class SkAutoLockPixelsTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkAutoLockPixels(SkBitmap()), SkAutoLockPixels)
        self.assertIsInstance(
            SkAutoLockPixels(SkBitmap(), False), SkAutoLockPixels)


class SkAutoLockColorsTests(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(SkAutoLockColors(), SkAutoLockColors)
        self.assertIsInstance(SkAutoLockColors(SkBitmap()), SkAutoLockColors)
#         self.assertIsInstance(
#             SkAutoLockColors(SkColorTable(16)), SkAutoLockColors)

    @unittest.skip("FIXME")
    def test_colors(self):
        self.assertIsNone(SkAutoLockColors().colors())
        self.assertIsNone(SkAutoLockColors(SkBitmap()).colors())
