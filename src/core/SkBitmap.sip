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

    // Method not exported in Java nor Python
    // void swap(SkBitmap& other);

    bool empty() const;
    bool isNull() const;
    Config config() const;
    int width() const;
    int height() const;
    // FIXME: size_t rowBytes() const;
    int shiftPerPixel() const;
    int bytesPerPixel() const;
    int rowBytesAsPixels() const;
    void* getPixels();
    // FIXME: size_t getSize() const;
    // FIXME: size_t getSafeSize() const;
    Sk64 getSize64() const;
    Sk64 getSafeSize64();
    bool isImmutable();
    void setImmutable();
    bool isOpaque() const;
    void setIsOpaque(bool);
    bool isVolatile() const;


    // FIXME: void setConfig(Config, int width, int height, size_t rowBytes = 0);
};
