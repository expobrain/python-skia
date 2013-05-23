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
%Include(name=SkTypes.sip)
%Include(name=SkPostConfig.sip)


struct Sk64 {

    %TypeHeaderCode
    #include <Sk64.h>
    %End

    enum DivOptions {
        kTrunc_DivOption,
        kRound_DivOption
    };

    int32_t fHi;
    uint32_t fLo;
    SkBool is32();
    SkBool is64();
    SkBool isFixed();
    int32_t get32();
    SkFixed getFixed();
    SkFract getFract();
    int32_t getSqrt();
    int getClzAbs();
    SkBool isZero();
    SkBool nonZero();
    SkBool isNeg();
    SkBool isPos();
    int getSign();
    void negate();
    void abs();
    int shiftToMake32();
    void setZero();
    void set(int32_t hi, uint32_t lo);
    void set(int32_t a);
    void setMul(int32_t a, int32_t b);
    void shiftLeft(unsigned bits);
    void shiftRight(unsigned bits);
    void roundRight(unsigned bits);
    void add(int32_t lo);
    void add(int32_t hi, uint32_t lo);
    void add(Sk64& other);
    void sub(Sk64& num);
    // not exported: void rsub(const Sk64& num);
    // MISSING IN SKIA: void mul(int32_t);
    void div(int32_t, DivOptions);
    SkFixed addGetFixed(Sk64& other);
    SkFixed addGetFixed(int32_t hi, uint32_t lo);
    SkFixed getFixedDiv(Sk64& denom);
    SkLONGLONG getLongLong();
};
