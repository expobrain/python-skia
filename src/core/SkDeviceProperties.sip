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
