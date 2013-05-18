struct SkISize /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkSize.h>
    %End
};


struct SkSize : public SkISize /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkSize.h>
    %End

    static SkSize Make(SkScalar w, SkScalar h);
    SkISize toRound() const;
    SkISize toCeil() const;
    SkISize toFloor() const;
};
