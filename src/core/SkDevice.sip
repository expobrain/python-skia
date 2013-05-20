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
