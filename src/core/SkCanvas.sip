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

    SkCanvas();
    explicit SkCanvas(SkDevice* device);
    explicit SkCanvas(const SkBitmap& bitmap);
    virtual ~SkCanvas();
};
