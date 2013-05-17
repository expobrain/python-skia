%Include(name=../config/sk_stdint.sip)


class SkColorTable {

    %TypeHeaderCode
    #include <SkColorTable.h>
    %End

public:
    enum Flags {
        kColorsAreOpaque_Flag = 0x01
    };

    SkColorTable(SkColorTable& src);
    SkColorTable(int count);
    // FIXME: SkColorTable(SkPMColor colors[], int count);
    unsigned getFlags();
    void setFlags(unsigned flags);
    bool isOpaque();
    int count();
    // FIXME: SkPMColor operator[](int index);
    // FIXME: SkPMColor* lockColors();
    void unlockColors(bool changed);
    // FIXME: uint16_t* lock16BitCache();
};
