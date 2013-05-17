%Include(name=../typedefs.sip)


class SkColorTable {

    %TypeHeaderCode
    #include <SkColorTable.h>
    %End

    SkColorTable(SkColorTable& src);
    SkColorTable(int count);
    // FIXME: SkColorTable(SkPMColor colors[], int count);
};
