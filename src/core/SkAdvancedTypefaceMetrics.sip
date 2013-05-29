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


class SkAdvancedTypefaceMetrics /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkAdvancedTypefaceMetrics.h>
    %End

public:
    SkAdvancedTypefaceMetrics();

    enum FontType {
        kType1_Font,
        kType1CID_Font,
        kCFF_Font,
        kTrueType_Font,
        kOther_Font,
        kNotEmbeddable_Font
    };
    enum StyleFlags {
        kFixedPitch_Style,
        kSerif_Style,
        kScript_Style,
        kItalic_Style,
        kAllCaps_Style,
        kSmallCaps_Style,
        kForceBold_Style,
    };
    enum PerGlyphInfo {
      kNo_PerGlyphInfo,
      kHAdvance_PerGlyphInfo,
      kVAdvance_PerGlyphInfo,
      kGlyphNames_PerGlyphInfo,
      kToUnicode_PerGlyphInfo,
    };

    /*
     * FIXME:
     * template <typename Data>
     * struct AdvanceMetric {
     *     enum MetricType {
     *         kDefault,  // Default advance: fAdvance.count = 1
     *         kRange,    // Advances for a range: fAdvance.count = fEndID-fStartID
     *         kRun       // fStartID-fEndID have same advance: fAdvance.count = 1
     *     };
     *     MetricType fType;
     *     uint16_t fStartId;
     *     uint16_t fEndId;
     *     SkTDArray<Data> fAdvance;
     *     SkTScopedPtr<AdvanceMetric<Data> > fNext;
     *  };
     */

    struct VerticalMetric {
        int16_t fVerticalAdvance;
        int16_t fOriginXDisp;
        int16_t fOriginYDisp;
    };

    SkString fFontName;
    FontType fType;
    bool fMultiMaster;
    uint16_t fLastGlyphID;
    uint16_t fEmSize;
    uint16_t fStyle;
    int16_t fItalicAngle;
    int16_t fAscent;
    int16_t fDescent;
    int16_t fStemV;
    int16_t fCapHeight;
    SkIRect fBBox;
    // FIXME: typedef AdvanceMetric<int16_t> WidthRange;
    // FIXME: typedef AdvanceMetric<VerticalMetric> VerticalAdvanceRange;
    // FIXME: SkTScopedPtr<WidthRange> fGlyphWidths;
    // FIXME: SkTScopedPtr<VerticalAdvanceRange> fVerticalMetrics;
    // FIXME: SkTScopedPtr<SkAutoTArray<SkString> > fGlyphNames;
    // FIXME: SkTDArray<SkUnichar> fGlyphToUnicode;
};
