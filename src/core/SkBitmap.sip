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
    void setIsVolatile(bool);
    void reset();
    // FIXME: static size_t ComputeRowBytes(Config c, int width);
    static int ComputeBytesPerPixel(Config c);
    static int ComputeShiftPerPixel(Config c);
    static Sk64 ComputeSize64(Config, int width, int height);
    // FIXME: static size_t ComputeSize(Config, int width, int height);
    static bool ComputeIsOpaque(const SkBitmap&);
    void computeAndSetOpaquePredicate();
    void getBounds(SkRect* bounds) const;
    void getBounds(SkIRect* bounds) const;
    // FIXME: void setConfig(Config, int width, int height, size_t rowBytes = 0);
    void setPixels(void* p, SkColorTable* ctable = NULL);
    // FIXME: bool copyPixelsTo(void* const dst, size_t dstSize, size_t dstRowBytes = 0,
    //                 bool preserveDstPad = false) const;
    bool allocPixels(SkColorTable* ctable = NULL);
    // Skipped: bool allocPixels(Allocator* allocator, SkColorTable* ctable);
};
