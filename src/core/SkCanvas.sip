/*
 * Copyright (c) 2013, Daniele Esposti <expo@expobrain.net>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * The name of the contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

class SkCanvas /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkCanvas.h>
    %End

public:
    enum Config8888 {
        kNative_Premul_Config8888,
        kNative_Unpremul_Config8888,
        kBGRA_Premul_Config8888,
        kBGRA_Unpremul_Config8888,
        kRGBA_Premul_Config8888,
        kRGBA_Unpremul_Config8888
    };
    enum SaveFlags {
        kMatrix_SaveFlag            = 0x01,
        kClip_SaveFlag              = 0x02,
        kHasAlphaLayer_SaveFlag     = 0x04,
        kFullColorLayer_SaveFlag    = 0x08,
        kClipToLayer_SaveFlag       = 0x10,
        kMatrixClip_SaveFlag        = 0x03,
        kARGB_NoClipLayer_SaveFlag  = 0x0F,
        kARGB_ClipLayer_SaveFlag    = 0x1F
    };
    enum PointMode {
        kPoints_PointMode,
        kLines_PointMode,
        kPolygon_PointMode
    };
    enum VertexMode {
        kTriangles_VertexMode,
        kTriangleStrip_VertexMode,
        kTriangleFan_VertexMode
    };
    enum ClipType {
        kEmpty_ClipType = 0,
        kRect_ClipType,
        kComplex_ClipType
    };

    class ClipVisitor /Abstract/ {
    public:
        virtual ~ClipVisitor();
        virtual void clipRect(const SkRect&, SkRegion::Op, bool antialias) = 0;
        virtual void clipPath(const SkPath&, SkRegion::Op, bool antialias) = 0;
    };

    SkCanvas();
    explicit SkCanvas(SkDevice* device);
    explicit SkCanvas(const SkBitmap& bitmap);

    virtual ~SkCanvas();

    // not exported: SkMetaData& getMetaData();
    void flush();
    SkISize getDeviceSize() const;
    SkDevice* getDevice() const;
    SkDevice* getTopDevice(bool updateMatrixClip = false) const;
    SkDevice* createCompatibleDevice(SkBitmap::Config config,
                                     int width, int height,
                                     bool isOpaque);
    bool readPixels(SkBitmap* bitmap,
                    int x, int y,
                    Config8888 config8888 = kNative_Premul_Config8888);
    bool readPixels(const SkIRect& srcRect, SkBitmap* bitmap) /Deprecated/;
    void writePixels(const SkBitmap& bitmap,
                     int x, int y,
                     Config8888 config8888 = kNative_Premul_Config8888);

    virtual int save(SaveFlags flags = kMatrixClip_SaveFlag);
    virtual int saveLayer(const SkRect* bounds, const SkPaint* paint,
                          SaveFlags flags = kARGB_ClipLayer_SaveFlag);
    int saveLayerAlpha(const SkRect* bounds, U8CPU alpha,
                       SaveFlags flags = kARGB_ClipLayer_SaveFlag);
    virtual void restore();
    int getSaveCount() const;
    virtual bool isDrawingToLayer() const;
    virtual bool translate(SkScalar dx, SkScalar dy);
    virtual bool scale(SkScalar sx, SkScalar sy);
    virtual bool rotate(SkScalar degrees);
    virtual bool skew(SkScalar sx, SkScalar sy);
    virtual bool concat(const SkMatrix& matrix);
    virtual void setMatrix(const SkMatrix& matrix);
    void resetMatrix();
    virtual bool clipRect(const SkRect& rect,
                          SkRegion::Op op = SkRegion::kIntersect_Op,
                          bool doAntiAlias = false);
    virtual bool clipRRect(const SkRRect& rrect,
                           SkRegion::Op op = SkRegion::kIntersect_Op,
                           bool doAntiAlias = false);
    virtual bool clipPath(const SkPath& path,
                          SkRegion::Op op = SkRegion::kIntersect_Op,
                          bool doAntiAlias = false);
    // EXPERIMENTAL: void setAllowSoftClip(bool allow);
    // EXPERIMENTAL: void setAllowSimplifyClip(bool allow);
    virtual bool clipRegion(const SkRegion& deviceRgn,
                            SkRegion::Op op = SkRegion::kIntersect_Op);
    bool quickReject(const SkRect& rect) const;
    bool quickReject(const SkPath& path) const;
    bool quickRejectY(SkScalar top, SkScalar bottom) const;
    bool getClipBounds(SkRect* bounds) const;
    bool getClipDeviceBounds(SkIRect* bounds) const;
    void drawARGB(U8CPU a, U8CPU r, U8CPU g, U8CPU b,
                  SkXfermode::Mode mode = SkXfermode::kSrcOver_Mode);
    void drawColor(SkColor color,
                   SkXfermode::Mode mode = SkXfermode::kSrcOver_Mode);
    virtual void clear(SkColor);
    virtual void drawPaint(const SkPaint& paint);
    // FIXME: virtual void drawPoints(PointMode mode, size_t count, const SkPoint pts[],
    //                         const SkPaint& paint);
    void drawPoint(SkScalar x, SkScalar y, const SkPaint& paint);
    void drawPoint(SkScalar x, SkScalar y, SkColor color);
    void drawLine(SkScalar x0, SkScalar y0, SkScalar x1, SkScalar y1,
                  const SkPaint& paint);
    virtual void drawRect(const SkRect& rect, const SkPaint& paint);
    void drawIRect(const SkIRect& rect, const SkPaint& paint);
    void drawRectCoords(SkScalar left, SkScalar top, SkScalar right,
                        SkScalar bottom, const SkPaint& paint);
    virtual void drawOval(const SkRect& oval, const SkPaint&);
    virtual void drawRRect(const SkRRect& rrect, const SkPaint& paint);
    void drawCircle(SkScalar cx, SkScalar cy, SkScalar radius,
                    const SkPaint& paint);
    void drawArc(const SkRect& oval, SkScalar startAngle, SkScalar sweepAngle,
                 bool useCenter, const SkPaint& paint);
    void drawRoundRect(const SkRect& rect, SkScalar rx, SkScalar ry,
                       const SkPaint& paint);
    virtual void drawPath(const SkPath& path, const SkPaint& paint);
    virtual void drawBitmap(const SkBitmap& bitmap, SkScalar left, SkScalar top,
                            const SkPaint* paint = NULL);
    virtual void drawBitmapRectToRect(const SkBitmap& bitmap, const SkRect* src,
                                      const SkRect& dst,
                                      const SkPaint* paint);
    void drawBitmapRect(const SkBitmap& bitmap, const SkIRect* isrc,
                        const SkRect& dst, const SkPaint* paint = NULL);
    virtual void drawBitmapMatrix(const SkBitmap& bitmap, const SkMatrix& m,
                                  const SkPaint* paint = NULL);
    virtual void drawBitmapNine(const SkBitmap& bitmap, const SkIRect& center,
                                const SkRect& dst, const SkPaint* paint = NULL);
    virtual void drawSprite(const SkBitmap& bitmap, int left, int top,
                            const SkPaint* paint = NULL);
    virtual void drawText(const void* text, size_t byteLength, SkScalar x,
                          SkScalar y, const SkPaint& paint);
    // FIXME: virtual void drawPosText(const void* text, size_t byteLength,
    //                          const SkPoint pos[], const SkPaint& paint);
    // FIXME: virtual void drawPosTextH(const void* text, size_t byteLength,
    //                           const SkScalar xpos[], SkScalar constY,
    //                           const SkPaint& paint);
    void drawTextOnPathHV(const void* text, size_t byteLength,
                          const SkPath& path, SkScalar hOffset,
                          SkScalar vOffset, const SkPaint& paint);
    // ANDROID ONLY: void drawPosTextOnPath(const void* text, size_t byteLength,
    //                      const SkPoint pos[], const SkPaint& paint,
    //                      const SkPath& path, const SkMatrix* matrix);
    virtual void drawPicture(SkPicture& picture);
    // FIXME: virtual void drawVertices(VertexMode vmode, int vertexCount,
    //                          const SkPoint vertices[], const SkPoint texs[],
    //                          const SkColor colors[], SkXfermode* xmode,
    //                          const uint16_t indices[], int indexCount,
    //                          const SkPaint& paint);
    virtual void drawData(const void* data, size_t length);
    SkBounder*  getBounder() const;
    virtual SkBounder* setBounder(SkBounder* bounder);
    SkDrawFilter* getDrawFilter() const;
    virtual SkDrawFilter* setDrawFilter(SkDrawFilter* filter);
    const SkMatrix& getTotalMatrix() const;
    ClipType getClipType() const;
    const SkRegion& getTotalClip() const /Deprecated/ ;
    const SkClipStack* getClipStack() const;
    void replayClips(ClipVisitor*) const;
};
