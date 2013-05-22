%Include(name=SkPoint.sip)


struct SkIRect /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkRect.h>
    %End

    int32_t fLeft;
    int32_t fTop;
    int32_t fRight;
    int32_t fBottom;

    static SkIRect MakeEmpty();
    static SkIRect MakeWH(int32_t w, int32_t h);
    static SkIRect MakeSize(const SkISize& size);
    static SkIRect MakeLTRB(int32_t l, int32_t t, int32_t r, int32_t b);
    static SkIRect MakeXYWH(int32_t x, int32_t y, int32_t w, int32_t h);

    static bool Intersects(const SkIRect& a, const SkIRect& b);
    static bool IntersectsNoEmptyCheck(const SkIRect& a, const SkIRect& b);
    static const SkIRect& EmptyIRect();

    int left() const;
    int top() const;
    int right() const;
    int bottom() const;
    int x() const;
    int y() const;
    int width() const;
    int height() const;
    int centerX() const;
    int centerY() const;
    bool isEmpty() const;
    bool is16Bit() const;
    void setEmpty();
    void set(int32_t left, int32_t top, int32_t right, int32_t bottom);
    void setLTRB(int32_t left, int32_t top, int32_t right, int32_t bottom);
    void setXYWH(int32_t x, int32_t y, int32_t width, int32_t height);
    void setLargest();
    void setLargestInverted();
    void offset(int32_t dx, int32_t dy);
    void offset(const SkIPoint& delta);
    void offsetTo(int32_t newX, int32_t newY);
    void inset(int32_t dx, int32_t dy);
    void outset(int32_t dx, int32_t dy);
    bool quickReject(int l, int t, int r, int b) const;
    bool contains(int32_t x, int32_t y) const;
    bool contains(int32_t left, int32_t top,
                  int32_t right, int32_t bottom) const;
    bool contains(const SkIRect& r) const;
    bool containsNoEmptyCheck(int32_t left, int32_t top,
                              int32_t right, int32_t bottom) const;
    bool containsNoEmptyCheck(const SkIRect& r) const;
    bool intersect(const SkIRect& r);
    bool intersect(const SkIRect& a, const SkIRect& b);
    bool intersect(int32_t left, int32_t top, int32_t right, int32_t bottom);
    bool intersectNoEmptyCheck(const SkIRect& a, const SkIRect& b);
    void join(int32_t left, int32_t top, int32_t right, int32_t bottom);
    void join(const SkIRect& r);
    void sort();
};

struct SkRect /NoDefaultCtors/ {

    %TypeHeaderCode
    #include <SkRect.h>
    %End

    static SkRect MakeEmpty();
    static SkRect MakeWH(SkScalar w, SkScalar h);
    static SkRect MakeSize(const SkSize& size);
    static SkRect MakeLTRB(SkScalar l, SkScalar t, SkScalar r, SkScalar b);
    static SkRect MakeXYWH(SkScalar x, SkScalar y, SkScalar w, SkScalar h);
    static SkRect MakeFromIRect(const SkIRect& irect) /Deprecated/ ;
    static SkRect Make(const SkIRect& irect);

    static bool Intersects(const SkRect& a, const SkRect& b);

    bool isEmpty() const;
    bool isFinite() const;
    SkScalar x() const;
    SkScalar y() const;
    SkScalar left() const;
    SkScalar top() const;
    SkScalar right() const;
    SkScalar bottom() const;
    SkScalar width() const;
    SkScalar height() const;
    SkScalar centerX() const;
    SkScalar centerY() const;
    //void toQuad(SkPoint quad[4]) const;
    void setEmpty();
    void set(const SkIRect& src);
    void set(SkScalar left, SkScalar top, SkScalar right, SkScalar bottom);
    //void set(const SkPoint pts[], int count);
    void set(const SkPoint& p0, const SkPoint& p1);
    void setLTRB(SkScalar left, SkScalar top, SkScalar right, SkScalar bottom);
    void iset(int left, int top, int right, int bottom);
    void isetWH(int width, int height);
    //void setBounds(const SkPoint pts[], int count);
    //bool setBoundsCheck(const SkPoint pts[], int count);
    void setXYWH(SkScalar x, SkScalar y, SkScalar width, SkScalar height);
    void setWH(SkScalar width, SkScalar height);
    void setLargest();
    void setLargestInverted();
    void offset(SkScalar dx, SkScalar dy);
    void offset(const SkPoint& delta);
    void offsetTo(SkScalar newX, SkScalar newY);
    void inset(SkScalar dx, SkScalar dy);
    void outset(SkScalar dx, SkScalar dy);
    bool intersect(const SkRect& r);
    bool intersect(SkScalar left, SkScalar top,
                   SkScalar right, SkScalar bottom);
    bool intersect(const SkRect& a, const SkRect& b);
    bool intersects(SkScalar left, SkScalar top,
                    SkScalar right, SkScalar bottom) const;
    void join(SkScalar left, SkScalar top, SkScalar right, SkScalar bottom);
    void join(const SkRect& r);
    void growToInclude(const SkRect& r);
    void growToInclude(SkScalar x, SkScalar y);
    bool contains(const SkPoint& p) const;
    bool contains(SkScalar x, SkScalar y) const;
    bool contains(const SkRect& r) const;
    void round(SkIRect* dst) const;
    void roundOut();
    void roundOut(SkIRect* dst) const;
    void roundIn(SkIRect* dst) const;
    void sort();
    // FIXME: const SkScalar* asScalars() const;
};
