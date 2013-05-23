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


struct SkDeviceProperties {

    %TypeHeaderCode
    #include <SkScalar.h>
    #include <SkDeviceProperties.h>
    %End

    struct Geometry {
        %TypeHeaderCode
        #include <SkDeviceProperties.h>
        %End

        enum Orientation {
            kUnknown_Orientation      = 0x0,
            kKnown_Orientation        = 0x2,

            kHorizontal_Orientation   = 0x2,  //!< this is the default
            kVertical_Orientation     = 0x3,

            kOrientationMask          = 0x3,
        };

        enum Layout {
            kUnknown_Layout   = 0x0,
            kKnown_Layout     = 0x8,

            kRGB_Layout       = 0x8,  //!< this is the default
            kBGR_Layout       = 0xC,

            kLayoutMask       = 0xC,
        };

        Orientation getOrientation();
        Layout getLayout();
        bool isOrientationKnown();
        bool isLayoutKnown();

    public:
        // FIXME: static Geometry MakeDefault();
        // FIXME: static Geometry Make(Orientation orientation, Layout layout);

        uint8_t fGeometry;
    };

    static SkDeviceProperties MakeDefault();
    static SkDeviceProperties Make(Geometry geometry, SkScalar gamma);

    Geometry fGeometry;
    SkScalar fGamma;
};
