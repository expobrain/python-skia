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

class SkGpuRenderTarget /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkDevice.h>
    %End
};


class SkDevice /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkDevice.h>
    %End

public:
    enum Capabilities {
        kGL_Capability     = 0x1,  //!< mask indicating GL support
        kVector_Capability = 0x2,  //!< mask indicating a vector representation
        kAll_Capabilities  = 0x3
    };

    SkDevice(const SkBitmap& bitmap);
    SkDevice(const SkBitmap& bitmap,
             const SkDeviceProperties& deviceProperties);
    SkDevice(SkBitmap::Config config, int width, int height,
             bool isOpaque = false);
    SkDevice(SkBitmap::Config config, int width, int height,
             bool isOpaque, const SkDeviceProperties& deviceProperties);

    virtual ~SkDevice();

    SkDevice* createCompatibleDevice(SkBitmap::Config config,
                                     int width, int height,
                                     bool isOpaque);
    virtual uint32_t getDeviceCapabilities();
    virtual int width() const;
    virtual int height() const;
    virtual const SkDeviceProperties& getDeviceProperties() const;
    void getGlobalBounds(SkIRect* bounds) const;
    bool isOpaque() const;
    SkBitmap::Config config() const;
    const SkBitmap& accessBitmap(bool changePixels);
    virtual void writePixels(
        const SkBitmap& bitmap, int x, int y,
        SkCanvas::Config8888 config8888 = SkCanvas::kNative_Premul_Config8888
    ) /Deprecated/ ;
    virtual SkGpuRenderTarget* accessRenderTarget();
    const SkIPoint& getOrigin() const;
    virtual void onAttachToCanvas(SkCanvas*);
    virtual void onDetachFromCanvas();
};
