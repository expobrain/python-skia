class SkBitmap {

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
};
