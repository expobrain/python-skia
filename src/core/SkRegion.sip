struct SkRegion {

    %TypeHeaderCode
    #include <SkRegion.h>
    %End

    enum Op {
            kDifference_Op,
            kIntersect_Op,
            kUnion_Op,
            kXOR_Op,
            kReverseDifference_Op,
            kReplace_Op
        };
};
