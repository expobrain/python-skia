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
