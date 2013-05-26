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

from skia.core import (SkCanvas, SkDevice, SkBitmap, SkISize, SkRect, SkPaint,
    SkMatrix, SkRegion, SkRRect, SkPath, SkXfermode, SkPoint, SkIRect,
    SkPicture, SkBounder, SkDrawFilter, SkClipStack)
from tests import assert_not_fail
import unittest


class SkCanvasTests(unittest.TestCase):

    @property
    def canvas(self):
        return SkCanvas(SkDevice(SkBitmap()))

    def test_instance(self):
        self.assertIsInstance(SkCanvas(), SkCanvas)
        self.assertIsInstance(SkCanvas(SkDevice(SkBitmap())), SkCanvas)
        self.assertIsInstance(SkCanvas(SkBitmap()), SkCanvas)

    def test_read_pixels(self):
        bitmap = SkBitmap()
        bitmap.setConfig(SkBitmap.kA8_Config, 1, 1)

        self.assertIsInstance(self.canvas.readPixels(bitmap, 0, 0), bool)
        self.assertIsInstance(
            self.canvas.readPixels(
                bitmap, 1, 1, SkCanvas.kNative_Premul_Config8888
            ),
            bool
        )

        # Deprecated signature
#         with self.assertRaises(DeprecationWarning):
#             self.canvas.readPixels(SkRect.Make(), bitmap)

    @assert_not_fail
    def test_write_pixels(self):
        bitmap = SkBitmap()
        bitmap.setConfig(SkBitmap.kA8_Config, 1, 1)

        self.canvas.readPixels(bitmap, 0, 0)
        self.canvas.readPixels(bitmap, 1, 1, SkCanvas.kNative_Premul_Config8888)

    def test_config888_enum(self):
        attrs = ("kNative_Premul_Config8888", "kNative_Unpremul_Config8888",
                 "kBGRA_Premul_Config8888", "kBGRA_Unpremul_Config8888",
                 "kRGBA_Premul_Config8888", "kRGBA_Unpremul_Config8888")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))

    def test_point_mode_enum(self):
        attrs = ("kPoints_PointMode", "kLines_PointMode", "kPolygon_PointMode")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))

    def test_clip_type_enum(self):
        attrs = ("kEmpty_ClipType", "kRect_ClipType", "kComplex_ClipType")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))

    def test_vertex_mode_enum(self):
        attrs = ("kTriangles_VertexMode", "kTriangleStrip_VertexMode",
                 "kTriangleFan_VertexMode")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))

    def test_save_flags_enum(self):
        attrs = ("kMatrix_SaveFlag", "kClip_SaveFlag",
                 "kHasAlphaLayer_SaveFlag", "kFullColorLayer_SaveFlag",
                 "kClipToLayer_SaveFlag", "kMatrixClip_SaveFlag",
                 "kARGB_NoClipLayer_SaveFlag", "kARGB_ClipLayer_SaveFlag")

        for attr in attrs:
            self.assertTrue(hasattr(SkCanvas, attr))

    @unittest.skip("FIXME")
    def test_save(self):
        self.assertIsInstance(self.canvas.save(), int)
        self.assertIsInstance(
            self.canvas.save(SkCanvas.kMatrixClip_SaveFlag), int)

    @assert_not_fail
    def test_flush(self):
        self.canvas.flush()

    @assert_not_fail
    def test_restore(self):
        self.canvas.restore()

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_restore_to_count(self):
        canvas = self.canvas
        count = canvas.save()

        canvas.restoreToCount(count)

    def test_get_save_count(self):
        self.assertIsInstance(self.canvas.getSaveCount(), int)

    def test_is_drawing_to_layer(self):
        self.assertIsInstance(self.canvas.isDrawingToLayer(), bool)

    def test_translate(self):
        self.assertIsInstance(self.canvas.translate(1, 1), bool)

    def test_scale(self):
        self.assertIsInstance(self.canvas.scale(1, 1), bool)

    def test_skew(self):
        self.assertIsInstance(self.canvas.skew(1, 1), bool)

    def test_rotate(self):
        self.assertIsInstance(self.canvas.rotate(1), bool)

    @unittest.skip("FIXME")
    def test_clip_path(self):
        self.assertIsInstance(self.canvas.clipPath(SkPath()), bool)
        self.assertIsInstance(
            self.canvas.clipPath(SkPath(), SkRegion.kIntersect_Op), bool)
        self.assertIsInstance(
            self.canvas.clipPath(SkPath(), SkRegion.kIntersect_Op, False), bool)

    @unittest.skip("FIXME")
    def test_clip_set_region(self):
        self.assertIsInstance(self.canvas.setClipRegion(SkRegion()), bool)

    @unittest.skip("FIXME")
    def test_clip_region(self):
        self.assertIsInstance(self.canvas.clipRegion(SkRegion()), bool)
        self.assertIsInstance(
            self.canvas.clipRegion(SkRegion(), SkRegion.kIntersect_Op), bool)
        self.assertIsInstance(
            self.canvas.clipRegion(SkRegion(), SkRegion.kIntersect_Op, False),
            bool
        )

    @unittest.skip("FIXME")
    def test_clip_rect(self):
        self.assertIsInstance(self.canvas.clipRect(SkRect.MakeEmpty()), bool)
        self.assertIsInstance(
            self.canvas.clipRect(SkRect.MakeEmpty(), SkRegion.kIntersect_Op),
            bool
        )
        self.assertIsInstance(
            self.canvas.clipRect(
                SkRect.MakeEmpty(), SkRegion.kIntersect_Op, False
            ),
            bool
        )

    @unittest.skip("FIXME")
    def test_clip_rrect(self):
        self.assertIsInstance(self.canvas.clipRect(SkRRect()), bool)
        self.assertIsInstance(
            self.canvas.clipRect(SkRRect(), SkRegion.kIntersect_Op), bool)
        self.assertIsInstance(
            self.canvas.clipRect(SkRRect(), SkRegion.kIntersect_Op, False),
            bool
        )

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_set_matrix(self):
        self.canvas.setMatrix(SkMatrix())

    def test_set_bounder(self):
        self.assertIsInstance(self.canvas.setBounder(SkBounder()), SkBounder)

    @unittest.skip("FIXME")
    def test_set_draw_filter(self):
        self.assertIsInstance(
            self.canvas.setDrawFilter(SkDrawFilter()), SkDrawFilter)

    @assert_not_fail
    def test_reset_matrix(self):
        self.canvas.resetMatrix()

    @unittest.skip("FIXME")
    def test_concat(self):
        self.assertIsInstance(self.canvas.concat(SkMatrix()), bool)

    @unittest.skip("FIXME")
    def test_save_layer(self):
        self.assertIsInstance(
            self.canvas.saveLayer(SkRect.MakeEmpty(), SkPaint()), int)
        self.assertIsInstance(
            self.canvas.saveLayer(
                SkRect.MakeEmpty(), SkPaint(),
                SkCanvas.kARGB_ClipLayer_SaveFlag
            ),
            int
        )

    @unittest.skip("FIXME")
    def test_save_layer_alpha(self):
        self.assertIsInstance(
            self.canvas.saveLayerAlpha(SkRect.MakeEmpty(), 50), int)
        self.assertIsInstance(
            self.canvas.saveLayerAlpha(
                SkRect.MakeEmpty(), 50, SkCanvas.kARGB_ClipLayer_SaveFlag),
            int
        )

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_oval(self):
        self.canvas.drawOval(SkRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_path(self):
        self.canvas.drawPath(SkPath(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_paint(self):
        self.canvas.drawPaint(SkPaint())

    @assert_not_fail
    def test_clear(self):
        self.canvas.clear(1)

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_round_rect(self):
        self.canvas.drawRoundRect(SkRect.MakeEmpty(), 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_picture(self):
        self.canvas.drawPicture(SkPicture())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_text(self):
        self.canvas.drawText(str("text"), 4, 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_pos_text(self):
        self.canvas.drawPosText(
            str("text"), 4, [SkPoint(), SkPoint(), SkPoint(), SkPoint()],
            SkPaint()
        )

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_text_on_path_hv(self):
        self.canvas.drawTextOnPathHV(
            str("text"), 4, SkPath(), 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_pos_text_h(self):
        self.canvas.drawPosTextH(
            str("text"), 4, [SkPoint(), SkPoint(), SkPoint(), SkPoint()], 1.0,
            SkPaint()
        )

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_rect(self):
        self.canvas.drawRect(SkRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_sprite(self):
        self.canvas.drawSprite(SkBitmap(), 1, 1)
        self.canvas.drawSprite(SkBitmap(), 1, 1, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_rect_coords(self):
        self.canvas.drawRect(1.0, 1.0, 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_irect(self):
        self.canvas.drawIRect(SkIRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_rrect(self):
        self.canvas.drawRRect(SkRRect(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_line(self):
        self.canvas.drawLine(1.0, 1.0, 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_point(self):
        self.canvas.drawPoint(1.0, 1.0, SkPaint())
        self.canvas.drawPoint(1.0, 1.0, 1)

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_points(self):
        self.canvas.drawPoints(
            SkCanvas.kPoints_PointMode, 1, [SkPoint()], SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_bitmap_rect_to_rect(self):
        self.canvas.drawBitmapRectToRect(
            SkBitmap(), SkRect.MakeEmpty(), SkRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_bitmap_rect(self):
        self.canvas.drawBitmapRect(SkBitmap(), SkIRect(), SkRect.MakeEmpty())
        self.canvas.drawBitmapRect(
            SkBitmap(), SkIRect(), SkRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_bitmap_nine(self):
        self.canvas.drawBitmapNine(SkBitmap(), SkIRect(), SkRect.MakeEmpty())
        self.canvas.drawBitmapNine(
            SkBitmap(), SkIRect(), SkRect.MakeEmpty(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_bitmap_matrix(self):
        self.canvas.drawBitmapMatrix(SkBitmap(), SkMatrix())
        self.canvas.drawBitmapMatrix(SkBitmap(), SkMatrix(), SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_bitmap(self):
        self.canvas.drawBitmap(SkBitmap(), 1.0, 1.0)
        self.canvas.drawBitmap(SkBitmap(), 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_circle(self):
        self.canvas.drawCircle(1.0, 1.0, 1.0, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_color(self):
        self.canvas.drawColor(1)
        self.canvas.drawARGB(1, SkXfermode.kSrcOver_Mode)

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_draw_arc(self):
        self.canvas.drawArc(SkRect.MakeEmpty(), 1.0, 1.0, True, SkPaint())

    @unittest.skip("FIXME")
    @assert_not_fail
    def test_replay_clips(self):
        self.canvas.replayClips(SkCanvas.ClipVisitor())

    @assert_not_fail
    def test_draw_argb(self):
        self.canvas.drawARGB(0xff, 0xff, 0xff, 0xff)
        self.canvas.drawARGB(0xff, 0xff, 0xff, 0xff, SkXfermode.kSrcOver_Mode)

    def test_get_device_size(self):
        self.assertIsInstance(SkCanvas().getDeviceSize(), SkISize)

    @unittest.skip("FIXME")
    def test_get_clip_device_bounds(self):
        self.assertIsInstance(
            self.canvas.getClipDeviceBounds(SkIRect.MakeEmpty()), bool)

    def test_get_clip_type(self):
        self.assertIsInstance(self.canvas.getClipType(), SkCanvas.ClipType)

    @unittest.skip("FIXME")
    def test_get_clip_bounds(self):
        self.assertIsInstance(
            self.canvas.getClipBounds(SkRect.MakeEmpty()), bool)

    def test_get_clip_stack(self):
        self.assertIsInstance(
            self.canvas.getClipStack(), SkClipStack)

    def test_quick_reject_y(self):
        self.assertIsInstance(self.canvas.quickRejectY(1.0, 1.0), bool)

    @unittest.skip("FIXME")
    def test_quick_reject(self):
        self.assertIsInstance(self.canvas.quickReject(SkRect.MakeEmpty()), bool)
        self.assertIsInstance(self.canvas.quickReject(SkPath()), bool)

    def test_get_total_matrix(self):
        self.assertIsInstance(self.canvas.getTotalMatrix(), SkMatrix)

    @unittest.skip("FIXME")
    def test_get_total_clip(self):
        self.assertRaises(DeprecationWarning, self.canvas.getTotalClip())

    @unittest.skip("FIXME")
    def test_get_bounder(self):
        canvas = self.canvas
        canvas.setBounder(SkBounder())

        self.assertIsInstance(canvas.getBounder(), SkBounder)

    @unittest.skip("FIXME")
    def test_get_draw_filter(self):
        canvas = self.canvas
        canvas = canvas.setDrawFilter(SkDrawFilter())

        self.assertIsInstance(canvas.getDrawFilter(), SkDrawFilter)

    def test_get_device(self):
        self.assertIsInstance(
            SkCanvas(SkDevice(SkBitmap())).getDevice(), SkDevice)

    def test_create_compatible_device(self):
        self.assertIsInstance(
            self.canvas.createCompatibleDevice(SkBitmap.kA8_Config, 1, 1, True),
            SkDevice
        )

    def test_get_top_device(self):
        self.assertIsInstance(
            SkCanvas(SkDevice(SkBitmap())).getTopDevice(), SkDevice)
        self.assertIsInstance(
            SkCanvas(SkDevice(SkBitmap())).getTopDevice(True), SkDevice)


class SkCanvasClipVisitorTests(unittest.TestCase):

    def test_abstract(self):
        self.assertRaises(TypeError, SkCanvas.ClipVisitor)
