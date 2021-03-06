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

%Include(name=../config/sk_stdint.sip)

class SkBitmap /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkBitmap.h>
    %End

public:
    enum Config {
        kNo_Config,
        kA1_Config,
        kA8_Config,
        kIndex8_Config,
        kRGB_565_Config,
        kARGB_4444_Config,
        kARGB_8888_Config,
        kRLE_Index8_Config,
        kConfigCount
    };

    SkBitmap();
    SkBitmap(const SkBitmap& src);

    ~SkBitmap();

    // Method not exported in Java nor Python: void swap(SkBitmap& other);
    bool empty();
    bool isNull();
    Config config();
    int width();
    int height();
    // FIXME: size_t rowBytes();
    int shiftPerPixel();
    int bytesPerPixel();
    int rowBytesAsPixels();
    void* getPixels();
    // FIXME: size_t getSize();
    // FIXME: size_t getSafeSize();
    Sk64 getSize64();
    Sk64 getSafeSize64();
    bool isImmutable();
    void setImmutable();
    bool isOpaque();
    void setIsOpaque(bool);
    bool isVolatile();
    void setIsVolatile(bool);
    void reset();
    // FIXME: static size_t ComputeRowBytes(Config c, int width);
    static int ComputeBytesPerPixel(Config c);
    static int ComputeShiftPerPixel(Config c);
    static Sk64 ComputeSize64(Config, int width, int height);
    // FIXME: static size_t ComputeSize(Config, int width, int height);
    static bool ComputeIsOpaque(SkBitmap&);
    void computeAndSetOpaquePredicate();
    void getBounds(SkRect* bounds);
    void getBounds(SkIRect* bounds);
    void setConfig(Config, int width, int height, size_t rowBytes = 0);
    void setPixels(void* p, SkColorTable* ctable = NULL);
    // FIXME: bool copyPixelsTo(void* dst, size_t dstSize, size_t dstRowBytes = 0,
    //                 bool preserveDstPad = false);
    bool allocPixels(SkColorTable* ctable = NULL);
    // Skipped: bool allocPixels(Allocator* allocator, SkColorTable* ctable);
    SkPixelRef* pixelRef();
    // FIXME: size_t pixelRefOffset();
    // FIXME: SkPixelRef* setPixelRef(SkPixelRef* pr, size_t offset = 0);
    void lockPixels();
    void unlockPixels();
    bool lockPixelsAreWritable();
    bool readyToDraw();
    SkGpuTexture* getTexture();
    SkColorTable* getColorTable();
    uint32_t getGenerationID();
    void notifyPixelsChanged();
    void eraseARGB(U8CPU a, U8CPU r, U8CPU g, U8CPU b);
    void eraseRGB(U8CPU r, U8CPU g, U8CPU b);
    void eraseColor(SkColor c);
    bool scrollRect(SkIRect* subset, int dx, int dy, SkRegion* inval = NULL);
    SkColor getColor(int x, int y);
    SkPMColor getIndex8Color(int x, int y);
    // FIXME: bool extractSubset(SkBitmap* dst, const SkIRect& subset) const;
    // FIXME: bool copyTo(SkBitmap* dst, Config c, Allocator* allocator = NULL) const;
    // FIXME: bool deepCopyTo(SkBitmap* dst, Config c) const;
    bool canCopyTo(Config newConfig);
    bool hasMipMap();
    void buildMipMap(bool forceRebuild = false);
    void freeMipMap();
    int extractMipLevel(SkBitmap* dst, SkFixed sx, SkFixed sy);
    bool extractAlpha(SkBitmap* dst);
    bool extractAlpha(SkBitmap* dst, SkPaint* paint, SkIPoint* offset);
    // Not exported: bool extractAlpha(SkBitmap* dst, SkPaint* paint,
    //                                 Allocator* allocator, SkIPoint* offset);
    // Not exported: void flatten(SkFlattenableWriteBuffer&);
    // Not exported: void unflatten(SkFlattenableReadBuffer&);
};


class SkAutoLockPixels /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkBitmap.h>
    %End

public:
    SkAutoLockPixels(SkBitmap& bm, bool doLock = true);
};


class SkAutoLockColors /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkBitmap.h>
    %End

public:
    SkAutoLockColors();
    SkAutoLockColors(SkBitmap& bm);
    // FIXME: SkAutoLockColors(SkColorTable* ctable);
    // FIXME: SkPMColor* colors();
    // FIXME: SkPMColor* lockColors(SkColorTable* ctable);
    // FIXME: SkPMColor* lockColors(const SkBitmap& bm);
};
