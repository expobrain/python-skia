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

struct SkRect {

    %TypeHeaderCode
    #include <SkRect.h>
    %End
};
