; ModuleID = 'ptest_pytket_qir_14_b'
source_filename = "ptest_pytket_qir_14_b"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"d\00"
@3 = internal constant [15 x i8] c"tk_SCRATCH_BIT\00"
@4 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_0\00"
@5 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_1\00"
@6 = internal constant [20 x i8] c"tk_SCRATCH_BITREG_2\00"

define void @main() #0 {
entry:
  br i1 true, label %sb_1_0, label %sb_0_0

sb_0_0:                                           ; preds = %entry
  br label %entry_0

sb_1_0:                                           ; preds = %entry
  br label %entry_0

entry_0:                                          ; preds = %sb_0_0, %sb_1_0
  %0 = phi i64 [ 0, %sb_0_0 ], [ 1, %sb_1_0 ]
  br i1 true, label %sb_1_1, label %sb_0_1

sb_0_1:                                           ; preds = %entry_0
  br label %entry_1

sb_1_1:                                           ; preds = %entry_0
  br label %entry_1

entry_1:                                          ; preds = %sb_0_1, %sb_1_1
  %1 = phi i64 [ 0, %sb_0_1 ], [ 1, %sb_1_1 ]
  br i1 true, label %sb_1_2, label %sb_0_2

sb_0_2:                                           ; preds = %entry_1
  %2 = and i64 9223372036854775805, %1
  br label %entry_2

sb_1_2:                                           ; preds = %entry_1
  %3 = or i64 2, %1
  br label %entry_2

entry_2:                                          ; preds = %sb_0_2, %sb_1_2
  %4 = phi i64 [ %2, %sb_0_2 ], [ %3, %sb_1_2 ]
  br i1 false, label %sb_1_3, label %sb_0_3

sb_0_3:                                           ; preds = %entry_2
  %5 = and i64 9223372036854775803, %4
  br label %entry_3

sb_1_3:                                           ; preds = %entry_2
  %6 = or i64 4, %4
  br label %entry_3

entry_3:                                          ; preds = %sb_0_3, %sb_1_3
  %7 = phi i64 [ %5, %sb_0_3 ], [ %6, %sb_1_3 ]
  br i1 false, label %sb_1_4, label %sb_0_4

sb_0_4:                                           ; preds = %entry_3
  %8 = and i64 9223372036854775799, %7
  br label %entry_4

sb_1_4:                                           ; preds = %entry_3
  %9 = or i64 8, %7
  br label %entry_4

entry_4:                                          ; preds = %sb_0_4, %sb_1_4
  %10 = phi i64 [ %8, %sb_0_4 ], [ %9, %sb_1_4 ]
  br i1 false, label %sb_1_5, label %sb_0_5

sb_0_5:                                           ; preds = %entry_4
  %11 = and i64 9223372036854775791, %10
  br label %entry_5

sb_1_5:                                           ; preds = %entry_4
  %12 = or i64 16, %10
  br label %entry_5

entry_5:                                          ; preds = %sb_0_5, %sb_1_5
  %13 = phi i64 [ %11, %sb_0_5 ], [ %12, %sb_1_5 ]
  br i1 false, label %sb_1_6, label %sb_0_6

sb_0_6:                                           ; preds = %entry_5
  %14 = and i64 9223372036854775775, %13
  br label %entry_6

sb_1_6:                                           ; preds = %entry_5
  %15 = or i64 32, %13
  br label %entry_6

entry_6:                                          ; preds = %sb_0_6, %sb_1_6
  %16 = phi i64 [ %14, %sb_0_6 ], [ %15, %sb_1_6 ]
  br i1 false, label %sb_1_7, label %sb_0_7

sb_0_7:                                           ; preds = %entry_6
  %17 = and i64 9223372036854775743, %16
  br label %entry_7

sb_1_7:                                           ; preds = %entry_6
  %18 = or i64 64, %16
  br label %entry_7

entry_7:                                          ; preds = %sb_0_7, %sb_1_7
  %19 = phi i64 [ %17, %sb_0_7 ], [ %18, %sb_1_7 ]
  br i1 false, label %sb_1_8, label %sb_0_8

sb_0_8:                                           ; preds = %entry_7
  %20 = and i64 9223372036854775679, %19
  br label %entry_8

sb_1_8:                                           ; preds = %entry_7
  %21 = or i64 128, %19
  br label %entry_8

entry_8:                                          ; preds = %sb_0_8, %sb_1_8
  %22 = phi i64 [ %20, %sb_0_8 ], [ %21, %sb_1_8 ]
  br i1 false, label %sb_1_9, label %sb_0_9

sb_0_9:                                           ; preds = %entry_8
  %23 = and i64 9223372036854775551, %22
  br label %entry_9

sb_1_9:                                           ; preds = %entry_8
  %24 = or i64 256, %22
  br label %entry_9

entry_9:                                          ; preds = %sb_0_9, %sb_1_9
  %25 = phi i64 [ %23, %sb_0_9 ], [ %24, %sb_1_9 ]
  br i1 false, label %sb_1_10, label %sb_0_10

sb_0_10:                                          ; preds = %entry_9
  %26 = and i64 9223372036854775295, %25
  br label %entry_10

sb_1_10:                                          ; preds = %entry_9
  %27 = or i64 512, %25
  br label %entry_10

entry_10:                                         ; preds = %sb_0_10, %sb_1_10
  %28 = phi i64 [ %26, %sb_0_10 ], [ %27, %sb_1_10 ]
  br i1 false, label %sb_1_11, label %sb_0_11

sb_0_11:                                          ; preds = %entry_10
  %29 = and i64 9223372036854774783, %28
  br label %entry_11

sb_1_11:                                          ; preds = %entry_10
  %30 = or i64 1024, %28
  br label %entry_11

entry_11:                                         ; preds = %sb_0_11, %sb_1_11
  %31 = phi i64 [ %29, %sb_0_11 ], [ %30, %sb_1_11 ]
  br i1 false, label %sb_1_12, label %sb_0_12

sb_0_12:                                          ; preds = %entry_11
  %32 = and i64 9223372036854773759, %31
  br label %entry_12

sb_1_12:                                          ; preds = %entry_11
  %33 = or i64 2048, %31
  br label %entry_12

entry_12:                                         ; preds = %sb_0_12, %sb_1_12
  %34 = phi i64 [ %32, %sb_0_12 ], [ %33, %sb_1_12 ]
  br i1 false, label %sb_1_13, label %sb_0_13

sb_0_13:                                          ; preds = %entry_12
  %35 = and i64 9223372036854771711, %34
  br label %entry_13

sb_1_13:                                          ; preds = %entry_12
  %36 = or i64 4096, %34
  br label %entry_13

entry_13:                                         ; preds = %sb_0_13, %sb_1_13
  %37 = phi i64 [ %35, %sb_0_13 ], [ %36, %sb_1_13 ]
  br i1 false, label %sb_1_14, label %sb_0_14

sb_0_14:                                          ; preds = %entry_13
  %38 = and i64 9223372036854767615, %37
  br label %entry_14

sb_1_14:                                          ; preds = %entry_13
  %39 = or i64 8192, %37
  br label %entry_14

entry_14:                                         ; preds = %sb_0_14, %sb_1_14
  %40 = phi i64 [ %38, %sb_0_14 ], [ %39, %sb_1_14 ]
  br i1 false, label %sb_1_15, label %sb_0_15

sb_0_15:                                          ; preds = %entry_14
  %41 = and i64 9223372036854759423, %40
  br label %entry_15

sb_1_15:                                          ; preds = %entry_14
  %42 = or i64 16384, %40
  br label %entry_15

entry_15:                                         ; preds = %sb_0_15, %sb_1_15
  %43 = phi i64 [ %41, %sb_0_15 ], [ %42, %sb_1_15 ]
  br i1 false, label %sb_1_16, label %sb_0_16

sb_0_16:                                          ; preds = %entry_15
  %44 = and i64 9223372036854743039, %43
  br label %entry_16

sb_1_16:                                          ; preds = %entry_15
  %45 = or i64 32768, %43
  br label %entry_16

entry_16:                                         ; preds = %sb_0_16, %sb_1_16
  %46 = phi i64 [ %44, %sb_0_16 ], [ %45, %sb_1_16 ]
  br i1 false, label %sb_1_17, label %sb_0_17

sb_0_17:                                          ; preds = %entry_16
  %47 = and i64 9223372036854710271, %46
  br label %entry_17

sb_1_17:                                          ; preds = %entry_16
  %48 = or i64 65536, %46
  br label %entry_17

entry_17:                                         ; preds = %sb_0_17, %sb_1_17
  %49 = phi i64 [ %47, %sb_0_17 ], [ %48, %sb_1_17 ]
  br i1 false, label %sb_1_18, label %sb_0_18

sb_0_18:                                          ; preds = %entry_17
  %50 = and i64 9223372036854644735, %49
  br label %entry_18

sb_1_18:                                          ; preds = %entry_17
  %51 = or i64 131072, %49
  br label %entry_18

entry_18:                                         ; preds = %sb_0_18, %sb_1_18
  %52 = phi i64 [ %50, %sb_0_18 ], [ %51, %sb_1_18 ]
  br i1 false, label %sb_1_19, label %sb_0_19

sb_0_19:                                          ; preds = %entry_18
  %53 = and i64 9223372036854513663, %52
  br label %entry_19

sb_1_19:                                          ; preds = %entry_18
  %54 = or i64 262144, %52
  br label %entry_19

entry_19:                                         ; preds = %sb_0_19, %sb_1_19
  %55 = phi i64 [ %53, %sb_0_19 ], [ %54, %sb_1_19 ]
  br i1 false, label %sb_1_20, label %sb_0_20

sb_0_20:                                          ; preds = %entry_19
  %56 = and i64 9223372036854251519, %55
  br label %entry_20

sb_1_20:                                          ; preds = %entry_19
  %57 = or i64 524288, %55
  br label %entry_20

entry_20:                                         ; preds = %sb_0_20, %sb_1_20
  %58 = phi i64 [ %56, %sb_0_20 ], [ %57, %sb_1_20 ]
  br i1 false, label %sb_1_21, label %sb_0_21

sb_0_21:                                          ; preds = %entry_20
  %59 = and i64 9223372036853727231, %58
  br label %entry_21

sb_1_21:                                          ; preds = %entry_20
  %60 = or i64 1048576, %58
  br label %entry_21

entry_21:                                         ; preds = %sb_0_21, %sb_1_21
  %61 = phi i64 [ %59, %sb_0_21 ], [ %60, %sb_1_21 ]
  br i1 false, label %sb_1_22, label %sb_0_22

sb_0_22:                                          ; preds = %entry_21
  %62 = and i64 9223372036852678655, %61
  br label %entry_22

sb_1_22:                                          ; preds = %entry_21
  %63 = or i64 2097152, %61
  br label %entry_22

entry_22:                                         ; preds = %sb_0_22, %sb_1_22
  %64 = phi i64 [ %62, %sb_0_22 ], [ %63, %sb_1_22 ]
  br i1 false, label %sb_1_23, label %sb_0_23

sb_0_23:                                          ; preds = %entry_22
  %65 = and i64 9223372036850581503, %64
  br label %entry_23

sb_1_23:                                          ; preds = %entry_22
  %66 = or i64 4194304, %64
  br label %entry_23

entry_23:                                         ; preds = %sb_0_23, %sb_1_23
  %67 = phi i64 [ %65, %sb_0_23 ], [ %66, %sb_1_23 ]
  br i1 false, label %sb_1_24, label %sb_0_24

sb_0_24:                                          ; preds = %entry_23
  %68 = and i64 9223372036846387199, %67
  br label %entry_24

sb_1_24:                                          ; preds = %entry_23
  %69 = or i64 8388608, %67
  br label %entry_24

entry_24:                                         ; preds = %sb_0_24, %sb_1_24
  %70 = phi i64 [ %68, %sb_0_24 ], [ %69, %sb_1_24 ]
  br i1 false, label %sb_1_25, label %sb_0_25

sb_0_25:                                          ; preds = %entry_24
  %71 = and i64 9223372036837998591, %70
  br label %entry_25

sb_1_25:                                          ; preds = %entry_24
  %72 = or i64 16777216, %70
  br label %entry_25

entry_25:                                         ; preds = %sb_0_25, %sb_1_25
  %73 = phi i64 [ %71, %sb_0_25 ], [ %72, %sb_1_25 ]
  br i1 false, label %sb_1_26, label %sb_0_26

sb_0_26:                                          ; preds = %entry_25
  %74 = and i64 9223372036821221375, %73
  br label %entry_26

sb_1_26:                                          ; preds = %entry_25
  %75 = or i64 33554432, %73
  br label %entry_26

entry_26:                                         ; preds = %sb_0_26, %sb_1_26
  %76 = phi i64 [ %74, %sb_0_26 ], [ %75, %sb_1_26 ]
  br i1 false, label %sb_1_27, label %sb_0_27

sb_0_27:                                          ; preds = %entry_26
  %77 = and i64 9223372036787666943, %76
  br label %entry_27

sb_1_27:                                          ; preds = %entry_26
  %78 = or i64 67108864, %76
  br label %entry_27

entry_27:                                         ; preds = %sb_0_27, %sb_1_27
  %79 = phi i64 [ %77, %sb_0_27 ], [ %78, %sb_1_27 ]
  br i1 false, label %sb_1_28, label %sb_0_28

sb_0_28:                                          ; preds = %entry_27
  %80 = and i64 9223372036720558079, %79
  br label %entry_28

sb_1_28:                                          ; preds = %entry_27
  %81 = or i64 134217728, %79
  br label %entry_28

entry_28:                                         ; preds = %sb_0_28, %sb_1_28
  %82 = phi i64 [ %80, %sb_0_28 ], [ %81, %sb_1_28 ]
  br i1 false, label %sb_1_29, label %sb_0_29

sb_0_29:                                          ; preds = %entry_28
  %83 = and i64 9223372036586340351, %82
  br label %entry_29

sb_1_29:                                          ; preds = %entry_28
  %84 = or i64 268435456, %82
  br label %entry_29

entry_29:                                         ; preds = %sb_0_29, %sb_1_29
  %85 = phi i64 [ %83, %sb_0_29 ], [ %84, %sb_1_29 ]
  br i1 false, label %sb_1_30, label %sb_0_30

sb_0_30:                                          ; preds = %entry_29
  %86 = and i64 9223372036317904895, %85
  br label %entry_30

sb_1_30:                                          ; preds = %entry_29
  %87 = or i64 536870912, %85
  br label %entry_30

entry_30:                                         ; preds = %sb_0_30, %sb_1_30
  %88 = phi i64 [ %86, %sb_0_30 ], [ %87, %sb_1_30 ]
  br i1 false, label %sb_1_31, label %sb_0_31

sb_0_31:                                          ; preds = %entry_30
  %89 = and i64 9223372035781033983, %88
  br label %entry_31

sb_1_31:                                          ; preds = %entry_30
  %90 = or i64 1073741824, %88
  br label %entry_31

entry_31:                                         ; preds = %sb_0_31, %sb_1_31
  %91 = phi i64 [ %89, %sb_0_31 ], [ %90, %sb_1_31 ]
  br i1 false, label %sb_1_32, label %sb_0_32

sb_0_32:                                          ; preds = %entry_31
  %92 = and i64 9223372034707292159, %91
  br label %entry_32

sb_1_32:                                          ; preds = %entry_31
  %93 = or i64 2147483648, %91
  br label %entry_32

entry_32:                                         ; preds = %sb_0_32, %sb_1_32
  %94 = phi i64 [ %92, %sb_0_32 ], [ %93, %sb_1_32 ]
  br i1 false, label %sb_1_33, label %sb_0_33

sb_0_33:                                          ; preds = %entry_32
  %95 = and i64 9223372036854775806, %0
  br label %entry_33

sb_1_33:                                          ; preds = %entry_32
  %96 = or i64 1, %0
  br label %entry_33

entry_33:                                         ; preds = %sb_0_33, %sb_1_33
  %97 = phi i64 [ %95, %sb_0_33 ], [ %96, %sb_1_33 ]
  br i1 true, label %sb_1_34, label %sb_0_34

sb_0_34:                                          ; preds = %entry_33
  %98 = and i64 9223372036854775805, %97
  br label %entry_34

sb_1_34:                                          ; preds = %entry_33
  %99 = or i64 2, %97
  br label %entry_34

entry_34:                                         ; preds = %sb_0_34, %sb_1_34
  %100 = phi i64 [ %98, %sb_0_34 ], [ %99, %sb_1_34 ]
  br i1 false, label %sb_1_35, label %sb_0_35

sb_0_35:                                          ; preds = %entry_34
  %101 = and i64 9223372036854775803, %100
  br label %entry_35

sb_1_35:                                          ; preds = %entry_34
  %102 = or i64 4, %100
  br label %entry_35

entry_35:                                         ; preds = %sb_0_35, %sb_1_35
  %103 = phi i64 [ %101, %sb_0_35 ], [ %102, %sb_1_35 ]
  br i1 false, label %sb_1_36, label %sb_0_36

sb_0_36:                                          ; preds = %entry_35
  %104 = and i64 9223372036854775799, %103
  br label %entry_36

sb_1_36:                                          ; preds = %entry_35
  %105 = or i64 8, %103
  br label %entry_36

entry_36:                                         ; preds = %sb_0_36, %sb_1_36
  %106 = phi i64 [ %104, %sb_0_36 ], [ %105, %sb_1_36 ]
  br i1 false, label %sb_1_37, label %sb_0_37

sb_0_37:                                          ; preds = %entry_36
  %107 = and i64 9223372036854775791, %106
  br label %entry_37

sb_1_37:                                          ; preds = %entry_36
  %108 = or i64 16, %106
  br label %entry_37

entry_37:                                         ; preds = %sb_0_37, %sb_1_37
  %109 = phi i64 [ %107, %sb_0_37 ], [ %108, %sb_1_37 ]
  br i1 false, label %sb_1_38, label %sb_0_38

sb_0_38:                                          ; preds = %entry_37
  %110 = and i64 9223372036854775775, %109
  br label %entry_38

sb_1_38:                                          ; preds = %entry_37
  %111 = or i64 32, %109
  br label %entry_38

entry_38:                                         ; preds = %sb_0_38, %sb_1_38
  %112 = phi i64 [ %110, %sb_0_38 ], [ %111, %sb_1_38 ]
  br i1 false, label %sb_1_39, label %sb_0_39

sb_0_39:                                          ; preds = %entry_38
  %113 = and i64 9223372036854775743, %112
  br label %entry_39

sb_1_39:                                          ; preds = %entry_38
  %114 = or i64 64, %112
  br label %entry_39

entry_39:                                         ; preds = %sb_0_39, %sb_1_39
  %115 = phi i64 [ %113, %sb_0_39 ], [ %114, %sb_1_39 ]
  br i1 false, label %sb_1_40, label %sb_0_40

sb_0_40:                                          ; preds = %entry_39
  %116 = and i64 9223372036854775679, %115
  br label %entry_40

sb_1_40:                                          ; preds = %entry_39
  %117 = or i64 128, %115
  br label %entry_40

entry_40:                                         ; preds = %sb_0_40, %sb_1_40
  %118 = phi i64 [ %116, %sb_0_40 ], [ %117, %sb_1_40 ]
  br i1 false, label %sb_1_41, label %sb_0_41

sb_0_41:                                          ; preds = %entry_40
  %119 = and i64 9223372036854775551, %118
  br label %entry_41

sb_1_41:                                          ; preds = %entry_40
  %120 = or i64 256, %118
  br label %entry_41

entry_41:                                         ; preds = %sb_0_41, %sb_1_41
  %121 = phi i64 [ %119, %sb_0_41 ], [ %120, %sb_1_41 ]
  br i1 false, label %sb_1_42, label %sb_0_42

sb_0_42:                                          ; preds = %entry_41
  %122 = and i64 9223372036854775295, %121
  br label %entry_42

sb_1_42:                                          ; preds = %entry_41
  %123 = or i64 512, %121
  br label %entry_42

entry_42:                                         ; preds = %sb_0_42, %sb_1_42
  %124 = phi i64 [ %122, %sb_0_42 ], [ %123, %sb_1_42 ]
  br i1 false, label %sb_1_43, label %sb_0_43

sb_0_43:                                          ; preds = %entry_42
  %125 = and i64 9223372036854774783, %124
  br label %entry_43

sb_1_43:                                          ; preds = %entry_42
  %126 = or i64 1024, %124
  br label %entry_43

entry_43:                                         ; preds = %sb_0_43, %sb_1_43
  %127 = phi i64 [ %125, %sb_0_43 ], [ %126, %sb_1_43 ]
  br i1 false, label %sb_1_44, label %sb_0_44

sb_0_44:                                          ; preds = %entry_43
  %128 = and i64 9223372036854773759, %127
  br label %entry_44

sb_1_44:                                          ; preds = %entry_43
  %129 = or i64 2048, %127
  br label %entry_44

entry_44:                                         ; preds = %sb_0_44, %sb_1_44
  %130 = phi i64 [ %128, %sb_0_44 ], [ %129, %sb_1_44 ]
  br i1 false, label %sb_1_45, label %sb_0_45

sb_0_45:                                          ; preds = %entry_44
  %131 = and i64 9223372036854771711, %130
  br label %entry_45

sb_1_45:                                          ; preds = %entry_44
  %132 = or i64 4096, %130
  br label %entry_45

entry_45:                                         ; preds = %sb_0_45, %sb_1_45
  %133 = phi i64 [ %131, %sb_0_45 ], [ %132, %sb_1_45 ]
  br i1 false, label %sb_1_46, label %sb_0_46

sb_0_46:                                          ; preds = %entry_45
  %134 = and i64 9223372036854767615, %133
  br label %entry_46

sb_1_46:                                          ; preds = %entry_45
  %135 = or i64 8192, %133
  br label %entry_46

entry_46:                                         ; preds = %sb_0_46, %sb_1_46
  %136 = phi i64 [ %134, %sb_0_46 ], [ %135, %sb_1_46 ]
  br i1 false, label %sb_1_47, label %sb_0_47

sb_0_47:                                          ; preds = %entry_46
  %137 = and i64 9223372036854759423, %136
  br label %entry_47

sb_1_47:                                          ; preds = %entry_46
  %138 = or i64 16384, %136
  br label %entry_47

entry_47:                                         ; preds = %sb_0_47, %sb_1_47
  %139 = phi i64 [ %137, %sb_0_47 ], [ %138, %sb_1_47 ]
  br i1 false, label %sb_1_48, label %sb_0_48

sb_0_48:                                          ; preds = %entry_47
  %140 = and i64 9223372036854743039, %139
  br label %entry_48

sb_1_48:                                          ; preds = %entry_47
  %141 = or i64 32768, %139
  br label %entry_48

entry_48:                                         ; preds = %sb_0_48, %sb_1_48
  %142 = phi i64 [ %140, %sb_0_48 ], [ %141, %sb_1_48 ]
  br i1 false, label %sb_1_49, label %sb_0_49

sb_0_49:                                          ; preds = %entry_48
  %143 = and i64 9223372036854710271, %142
  br label %entry_49

sb_1_49:                                          ; preds = %entry_48
  %144 = or i64 65536, %142
  br label %entry_49

entry_49:                                         ; preds = %sb_0_49, %sb_1_49
  %145 = phi i64 [ %143, %sb_0_49 ], [ %144, %sb_1_49 ]
  br i1 false, label %sb_1_50, label %sb_0_50

sb_0_50:                                          ; preds = %entry_49
  %146 = and i64 9223372036854644735, %145
  br label %entry_50

sb_1_50:                                          ; preds = %entry_49
  %147 = or i64 131072, %145
  br label %entry_50

entry_50:                                         ; preds = %sb_0_50, %sb_1_50
  %148 = phi i64 [ %146, %sb_0_50 ], [ %147, %sb_1_50 ]
  br i1 false, label %sb_1_51, label %sb_0_51

sb_0_51:                                          ; preds = %entry_50
  %149 = and i64 9223372036854513663, %148
  br label %entry_51

sb_1_51:                                          ; preds = %entry_50
  %150 = or i64 262144, %148
  br label %entry_51

entry_51:                                         ; preds = %sb_0_51, %sb_1_51
  %151 = phi i64 [ %149, %sb_0_51 ], [ %150, %sb_1_51 ]
  br i1 false, label %sb_1_52, label %sb_0_52

sb_0_52:                                          ; preds = %entry_51
  %152 = and i64 9223372036854251519, %151
  br label %entry_52

sb_1_52:                                          ; preds = %entry_51
  %153 = or i64 524288, %151
  br label %entry_52

entry_52:                                         ; preds = %sb_0_52, %sb_1_52
  %154 = phi i64 [ %152, %sb_0_52 ], [ %153, %sb_1_52 ]
  br i1 false, label %sb_1_53, label %sb_0_53

sb_0_53:                                          ; preds = %entry_52
  %155 = and i64 9223372036853727231, %154
  br label %entry_53

sb_1_53:                                          ; preds = %entry_52
  %156 = or i64 1048576, %154
  br label %entry_53

entry_53:                                         ; preds = %sb_0_53, %sb_1_53
  %157 = phi i64 [ %155, %sb_0_53 ], [ %156, %sb_1_53 ]
  br i1 false, label %sb_1_54, label %sb_0_54

sb_0_54:                                          ; preds = %entry_53
  %158 = and i64 9223372036852678655, %157
  br label %entry_54

sb_1_54:                                          ; preds = %entry_53
  %159 = or i64 2097152, %157
  br label %entry_54

entry_54:                                         ; preds = %sb_0_54, %sb_1_54
  %160 = phi i64 [ %158, %sb_0_54 ], [ %159, %sb_1_54 ]
  br i1 false, label %sb_1_55, label %sb_0_55

sb_0_55:                                          ; preds = %entry_54
  %161 = and i64 9223372036850581503, %160
  br label %entry_55

sb_1_55:                                          ; preds = %entry_54
  %162 = or i64 4194304, %160
  br label %entry_55

entry_55:                                         ; preds = %sb_0_55, %sb_1_55
  %163 = phi i64 [ %161, %sb_0_55 ], [ %162, %sb_1_55 ]
  br i1 false, label %sb_1_56, label %sb_0_56

sb_0_56:                                          ; preds = %entry_55
  %164 = and i64 9223372036846387199, %163
  br label %entry_56

sb_1_56:                                          ; preds = %entry_55
  %165 = or i64 8388608, %163
  br label %entry_56

entry_56:                                         ; preds = %sb_0_56, %sb_1_56
  %166 = phi i64 [ %164, %sb_0_56 ], [ %165, %sb_1_56 ]
  br i1 false, label %sb_1_57, label %sb_0_57

sb_0_57:                                          ; preds = %entry_56
  %167 = and i64 9223372036837998591, %166
  br label %entry_57

sb_1_57:                                          ; preds = %entry_56
  %168 = or i64 16777216, %166
  br label %entry_57

entry_57:                                         ; preds = %sb_0_57, %sb_1_57
  %169 = phi i64 [ %167, %sb_0_57 ], [ %168, %sb_1_57 ]
  br i1 false, label %sb_1_58, label %sb_0_58

sb_0_58:                                          ; preds = %entry_57
  %170 = and i64 9223372036821221375, %169
  br label %entry_58

sb_1_58:                                          ; preds = %entry_57
  %171 = or i64 33554432, %169
  br label %entry_58

entry_58:                                         ; preds = %sb_0_58, %sb_1_58
  %172 = phi i64 [ %170, %sb_0_58 ], [ %171, %sb_1_58 ]
  br i1 false, label %sb_1_59, label %sb_0_59

sb_0_59:                                          ; preds = %entry_58
  %173 = and i64 9223372036787666943, %172
  br label %entry_59

sb_1_59:                                          ; preds = %entry_58
  %174 = or i64 67108864, %172
  br label %entry_59

entry_59:                                         ; preds = %sb_0_59, %sb_1_59
  %175 = phi i64 [ %173, %sb_0_59 ], [ %174, %sb_1_59 ]
  br i1 false, label %sb_1_60, label %sb_0_60

sb_0_60:                                          ; preds = %entry_59
  %176 = and i64 9223372036720558079, %175
  br label %entry_60

sb_1_60:                                          ; preds = %entry_59
  %177 = or i64 134217728, %175
  br label %entry_60

entry_60:                                         ; preds = %sb_0_60, %sb_1_60
  %178 = phi i64 [ %176, %sb_0_60 ], [ %177, %sb_1_60 ]
  br i1 false, label %sb_1_61, label %sb_0_61

sb_0_61:                                          ; preds = %entry_60
  %179 = and i64 9223372036586340351, %178
  br label %entry_61

sb_1_61:                                          ; preds = %entry_60
  %180 = or i64 268435456, %178
  br label %entry_61

entry_61:                                         ; preds = %sb_0_61, %sb_1_61
  %181 = phi i64 [ %179, %sb_0_61 ], [ %180, %sb_1_61 ]
  br i1 false, label %sb_1_62, label %sb_0_62

sb_0_62:                                          ; preds = %entry_61
  %182 = and i64 9223372036317904895, %181
  br label %entry_62

sb_1_62:                                          ; preds = %entry_61
  %183 = or i64 536870912, %181
  br label %entry_62

entry_62:                                         ; preds = %sb_0_62, %sb_1_62
  %184 = phi i64 [ %182, %sb_0_62 ], [ %183, %sb_1_62 ]
  br i1 false, label %sb_1_63, label %sb_0_63

sb_0_63:                                          ; preds = %entry_62
  %185 = and i64 9223372035781033983, %184
  br label %entry_63

sb_1_63:                                          ; preds = %entry_62
  %186 = or i64 1073741824, %184
  br label %entry_63

entry_63:                                         ; preds = %sb_0_63, %sb_1_63
  %187 = phi i64 [ %185, %sb_0_63 ], [ %186, %sb_1_63 ]
  br i1 false, label %sb_1_64, label %sb_0_64

sb_0_64:                                          ; preds = %entry_63
  %188 = and i64 9223372034707292159, %187
  br label %entry_64

sb_1_64:                                          ; preds = %entry_63
  %189 = or i64 2147483648, %187
  br label %entry_64

entry_64:                                         ; preds = %sb_0_64, %sb_1_64
  %190 = phi i64 [ %188, %sb_0_64 ], [ %189, %sb_1_64 ]
  br i1 true, label %sb_1_65, label %sb_0_65

sb_0_65:                                          ; preds = %entry_64
  %191 = and i64 9223372036854775806, %190
  br label %entry_65

sb_1_65:                                          ; preds = %entry_64
  %192 = or i64 1, %190
  br label %entry_65

entry_65:                                         ; preds = %sb_0_65, %sb_1_65
  %193 = phi i64 [ %191, %sb_0_65 ], [ %192, %sb_1_65 ]
  br i1 true, label %sb_1_66, label %sb_0_66

sb_0_66:                                          ; preds = %entry_65
  %194 = and i64 9223372036854775805, %193
  br label %entry_66

sb_1_66:                                          ; preds = %entry_65
  %195 = or i64 2, %193
  br label %entry_66

entry_66:                                         ; preds = %sb_0_66, %sb_1_66
  %196 = phi i64 [ %194, %sb_0_66 ], [ %195, %sb_1_66 ]
  br i1 true, label %sb_1_67, label %sb_0_67

sb_0_67:                                          ; preds = %entry_66
  %197 = and i64 9223372036854775803, %196
  br label %entry_67

sb_1_67:                                          ; preds = %entry_66
  %198 = or i64 4, %196
  br label %entry_67

entry_67:                                         ; preds = %sb_0_67, %sb_1_67
  %199 = phi i64 [ %197, %sb_0_67 ], [ %198, %sb_1_67 ]
  br i1 false, label %sb_1_68, label %sb_0_68

sb_0_68:                                          ; preds = %entry_67
  %200 = and i64 9223372036854775799, %199
  br label %entry_68

sb_1_68:                                          ; preds = %entry_67
  %201 = or i64 8, %199
  br label %entry_68

entry_68:                                         ; preds = %sb_0_68, %sb_1_68
  %202 = phi i64 [ %200, %sb_0_68 ], [ %201, %sb_1_68 ]
  br i1 true, label %sb_1_69, label %sb_0_69

sb_0_69:                                          ; preds = %entry_68
  %203 = and i64 9223372036854775791, %202
  br label %entry_69

sb_1_69:                                          ; preds = %entry_68
  %204 = or i64 16, %202
  br label %entry_69

entry_69:                                         ; preds = %sb_0_69, %sb_1_69
  %205 = phi i64 [ %203, %sb_0_69 ], [ %204, %sb_1_69 ]
  br i1 false, label %sb_1_70, label %sb_0_70

sb_0_70:                                          ; preds = %entry_69
  %206 = and i64 9223372036854775775, %205
  br label %entry_70

sb_1_70:                                          ; preds = %entry_69
  %207 = or i64 32, %205
  br label %entry_70

entry_70:                                         ; preds = %sb_0_70, %sb_1_70
  %208 = phi i64 [ %206, %sb_0_70 ], [ %207, %sb_1_70 ]
  br i1 false, label %sb_1_71, label %sb_0_71

sb_0_71:                                          ; preds = %entry_70
  %209 = and i64 9223372036854775743, %208
  br label %entry_71

sb_1_71:                                          ; preds = %entry_70
  %210 = or i64 64, %208
  br label %entry_71

entry_71:                                         ; preds = %sb_0_71, %sb_1_71
  %211 = phi i64 [ %209, %sb_0_71 ], [ %210, %sb_1_71 ]
  br i1 false, label %sb_1_72, label %sb_0_72

sb_0_72:                                          ; preds = %entry_71
  %212 = and i64 9223372036854775679, %211
  br label %entry_72

sb_1_72:                                          ; preds = %entry_71
  %213 = or i64 128, %211
  br label %entry_72

entry_72:                                         ; preds = %sb_0_72, %sb_1_72
  %214 = phi i64 [ %212, %sb_0_72 ], [ %213, %sb_1_72 ]
  br i1 false, label %sb_1_73, label %sb_0_73

sb_0_73:                                          ; preds = %entry_72
  %215 = and i64 9223372036854775551, %214
  br label %entry_73

sb_1_73:                                          ; preds = %entry_72
  %216 = or i64 256, %214
  br label %entry_73

entry_73:                                         ; preds = %sb_0_73, %sb_1_73
  %217 = phi i64 [ %215, %sb_0_73 ], [ %216, %sb_1_73 ]
  br i1 false, label %sb_1_74, label %sb_0_74

sb_0_74:                                          ; preds = %entry_73
  %218 = and i64 9223372036854775295, %217
  br label %entry_74

sb_1_74:                                          ; preds = %entry_73
  %219 = or i64 512, %217
  br label %entry_74

entry_74:                                         ; preds = %sb_0_74, %sb_1_74
  %220 = phi i64 [ %218, %sb_0_74 ], [ %219, %sb_1_74 ]
  br i1 false, label %sb_1_75, label %sb_0_75

sb_0_75:                                          ; preds = %entry_74
  %221 = and i64 9223372036854774783, %220
  br label %entry_75

sb_1_75:                                          ; preds = %entry_74
  %222 = or i64 1024, %220
  br label %entry_75

entry_75:                                         ; preds = %sb_0_75, %sb_1_75
  %223 = phi i64 [ %221, %sb_0_75 ], [ %222, %sb_1_75 ]
  br i1 false, label %sb_1_76, label %sb_0_76

sb_0_76:                                          ; preds = %entry_75
  %224 = and i64 9223372036854773759, %223
  br label %entry_76

sb_1_76:                                          ; preds = %entry_75
  %225 = or i64 2048, %223
  br label %entry_76

entry_76:                                         ; preds = %sb_0_76, %sb_1_76
  %226 = phi i64 [ %224, %sb_0_76 ], [ %225, %sb_1_76 ]
  br i1 false, label %sb_1_77, label %sb_0_77

sb_0_77:                                          ; preds = %entry_76
  %227 = and i64 9223372036854771711, %226
  br label %entry_77

sb_1_77:                                          ; preds = %entry_76
  %228 = or i64 4096, %226
  br label %entry_77

entry_77:                                         ; preds = %sb_0_77, %sb_1_77
  %229 = phi i64 [ %227, %sb_0_77 ], [ %228, %sb_1_77 ]
  br i1 false, label %sb_1_78, label %sb_0_78

sb_0_78:                                          ; preds = %entry_77
  %230 = and i64 9223372036854767615, %229
  br label %entry_78

sb_1_78:                                          ; preds = %entry_77
  %231 = or i64 8192, %229
  br label %entry_78

entry_78:                                         ; preds = %sb_0_78, %sb_1_78
  %232 = phi i64 [ %230, %sb_0_78 ], [ %231, %sb_1_78 ]
  br i1 false, label %sb_1_79, label %sb_0_79

sb_0_79:                                          ; preds = %entry_78
  %233 = and i64 9223372036854759423, %232
  br label %entry_79

sb_1_79:                                          ; preds = %entry_78
  %234 = or i64 16384, %232
  br label %entry_79

entry_79:                                         ; preds = %sb_0_79, %sb_1_79
  %235 = phi i64 [ %233, %sb_0_79 ], [ %234, %sb_1_79 ]
  br i1 false, label %sb_1_80, label %sb_0_80

sb_0_80:                                          ; preds = %entry_79
  %236 = and i64 9223372036854743039, %235
  br label %entry_80

sb_1_80:                                          ; preds = %entry_79
  %237 = or i64 32768, %235
  br label %entry_80

entry_80:                                         ; preds = %sb_0_80, %sb_1_80
  %238 = phi i64 [ %236, %sb_0_80 ], [ %237, %sb_1_80 ]
  br i1 false, label %sb_1_81, label %sb_0_81

sb_0_81:                                          ; preds = %entry_80
  %239 = and i64 9223372036854710271, %238
  br label %entry_81

sb_1_81:                                          ; preds = %entry_80
  %240 = or i64 65536, %238
  br label %entry_81

entry_81:                                         ; preds = %sb_0_81, %sb_1_81
  %241 = phi i64 [ %239, %sb_0_81 ], [ %240, %sb_1_81 ]
  br i1 false, label %sb_1_82, label %sb_0_82

sb_0_82:                                          ; preds = %entry_81
  %242 = and i64 9223372036854644735, %241
  br label %entry_82

sb_1_82:                                          ; preds = %entry_81
  %243 = or i64 131072, %241
  br label %entry_82

entry_82:                                         ; preds = %sb_0_82, %sb_1_82
  %244 = phi i64 [ %242, %sb_0_82 ], [ %243, %sb_1_82 ]
  br i1 false, label %sb_1_83, label %sb_0_83

sb_0_83:                                          ; preds = %entry_82
  %245 = and i64 9223372036854513663, %244
  br label %entry_83

sb_1_83:                                          ; preds = %entry_82
  %246 = or i64 262144, %244
  br label %entry_83

entry_83:                                         ; preds = %sb_0_83, %sb_1_83
  %247 = phi i64 [ %245, %sb_0_83 ], [ %246, %sb_1_83 ]
  br i1 false, label %sb_1_84, label %sb_0_84

sb_0_84:                                          ; preds = %entry_83
  %248 = and i64 9223372036854251519, %247
  br label %entry_84

sb_1_84:                                          ; preds = %entry_83
  %249 = or i64 524288, %247
  br label %entry_84

entry_84:                                         ; preds = %sb_0_84, %sb_1_84
  %250 = phi i64 [ %248, %sb_0_84 ], [ %249, %sb_1_84 ]
  br i1 false, label %sb_1_85, label %sb_0_85

sb_0_85:                                          ; preds = %entry_84
  %251 = and i64 9223372036853727231, %250
  br label %entry_85

sb_1_85:                                          ; preds = %entry_84
  %252 = or i64 1048576, %250
  br label %entry_85

entry_85:                                         ; preds = %sb_0_85, %sb_1_85
  %253 = phi i64 [ %251, %sb_0_85 ], [ %252, %sb_1_85 ]
  br i1 false, label %sb_1_86, label %sb_0_86

sb_0_86:                                          ; preds = %entry_85
  %254 = and i64 9223372036852678655, %253
  br label %entry_86

sb_1_86:                                          ; preds = %entry_85
  %255 = or i64 2097152, %253
  br label %entry_86

entry_86:                                         ; preds = %sb_0_86, %sb_1_86
  %256 = phi i64 [ %254, %sb_0_86 ], [ %255, %sb_1_86 ]
  br i1 false, label %sb_1_87, label %sb_0_87

sb_0_87:                                          ; preds = %entry_86
  %257 = and i64 9223372036850581503, %256
  br label %entry_87

sb_1_87:                                          ; preds = %entry_86
  %258 = or i64 4194304, %256
  br label %entry_87

entry_87:                                         ; preds = %sb_0_87, %sb_1_87
  %259 = phi i64 [ %257, %sb_0_87 ], [ %258, %sb_1_87 ]
  br i1 false, label %sb_1_88, label %sb_0_88

sb_0_88:                                          ; preds = %entry_87
  %260 = and i64 9223372036846387199, %259
  br label %entry_88

sb_1_88:                                          ; preds = %entry_87
  %261 = or i64 8388608, %259
  br label %entry_88

entry_88:                                         ; preds = %sb_0_88, %sb_1_88
  %262 = phi i64 [ %260, %sb_0_88 ], [ %261, %sb_1_88 ]
  br i1 false, label %sb_1_89, label %sb_0_89

sb_0_89:                                          ; preds = %entry_88
  %263 = and i64 9223372036837998591, %262
  br label %entry_89

sb_1_89:                                          ; preds = %entry_88
  %264 = or i64 16777216, %262
  br label %entry_89

entry_89:                                         ; preds = %sb_0_89, %sb_1_89
  %265 = phi i64 [ %263, %sb_0_89 ], [ %264, %sb_1_89 ]
  br i1 false, label %sb_1_90, label %sb_0_90

sb_0_90:                                          ; preds = %entry_89
  %266 = and i64 9223372036821221375, %265
  br label %entry_90

sb_1_90:                                          ; preds = %entry_89
  %267 = or i64 33554432, %265
  br label %entry_90

entry_90:                                         ; preds = %sb_0_90, %sb_1_90
  %268 = phi i64 [ %266, %sb_0_90 ], [ %267, %sb_1_90 ]
  br i1 false, label %sb_1_91, label %sb_0_91

sb_0_91:                                          ; preds = %entry_90
  %269 = and i64 9223372036787666943, %268
  br label %entry_91

sb_1_91:                                          ; preds = %entry_90
  %270 = or i64 67108864, %268
  br label %entry_91

entry_91:                                         ; preds = %sb_0_91, %sb_1_91
  %271 = phi i64 [ %269, %sb_0_91 ], [ %270, %sb_1_91 ]
  br i1 false, label %sb_1_92, label %sb_0_92

sb_0_92:                                          ; preds = %entry_91
  %272 = and i64 9223372036720558079, %271
  br label %entry_92

sb_1_92:                                          ; preds = %entry_91
  %273 = or i64 134217728, %271
  br label %entry_92

entry_92:                                         ; preds = %sb_0_92, %sb_1_92
  %274 = phi i64 [ %272, %sb_0_92 ], [ %273, %sb_1_92 ]
  br i1 false, label %sb_1_93, label %sb_0_93

sb_0_93:                                          ; preds = %entry_92
  %275 = and i64 9223372036586340351, %274
  br label %entry_93

sb_1_93:                                          ; preds = %entry_92
  %276 = or i64 268435456, %274
  br label %entry_93

entry_93:                                         ; preds = %sb_0_93, %sb_1_93
  %277 = phi i64 [ %275, %sb_0_93 ], [ %276, %sb_1_93 ]
  br i1 false, label %sb_1_94, label %sb_0_94

sb_0_94:                                          ; preds = %entry_93
  %278 = and i64 9223372036317904895, %277
  br label %entry_94

sb_1_94:                                          ; preds = %entry_93
  %279 = or i64 536870912, %277
  br label %entry_94

entry_94:                                         ; preds = %sb_0_94, %sb_1_94
  %280 = phi i64 [ %278, %sb_0_94 ], [ %279, %sb_1_94 ]
  br i1 false, label %sb_1_95, label %sb_0_95

sb_0_95:                                          ; preds = %entry_94
  %281 = and i64 9223372035781033983, %280
  br label %entry_95

sb_1_95:                                          ; preds = %entry_94
  %282 = or i64 1073741824, %280
  br label %entry_95

entry_95:                                         ; preds = %sb_0_95, %sb_1_95
  %283 = phi i64 [ %281, %sb_0_95 ], [ %282, %sb_1_95 ]
  br i1 false, label %sb_1_96, label %sb_0_96

sb_0_96:                                          ; preds = %entry_95
  %284 = and i64 9223372034707292159, %283
  br label %entry_96

sb_1_96:                                          ; preds = %entry_95
  %285 = or i64 2147483648, %283
  br label %entry_96

entry_96:                                         ; preds = %sb_0_96, %sb_1_96
  %286 = phi i64 [ %284, %sb_0_96 ], [ %285, %sb_1_96 ]
  %287 = and i64 1, %286
  %288 = icmp eq i64 1, %287
  br i1 %288, label %sb_1_97, label %sb_0_97

sb_0_97:                                          ; preds = %entry_96
  %289 = and i64 9223372036854775806, %94
  br label %entry_97

sb_1_97:                                          ; preds = %entry_96
  %290 = or i64 1, %94
  br label %entry_97

entry_97:                                         ; preds = %sb_0_97, %sb_1_97
  %291 = phi i64 [ %289, %sb_0_97 ], [ %290, %sb_1_97 ]
  %292 = and i64 2, %286
  %293 = icmp eq i64 2, %292
  br i1 %293, label %sb_1_98, label %sb_0_98

sb_0_98:                                          ; preds = %entry_97
  %294 = and i64 9223372036854775805, %291
  br label %entry_98

sb_1_98:                                          ; preds = %entry_97
  %295 = or i64 2, %291
  br label %entry_98

entry_98:                                         ; preds = %sb_0_98, %sb_1_98
  %296 = phi i64 [ %294, %sb_0_98 ], [ %295, %sb_1_98 ]
  %297 = and i64 4, %286
  %298 = icmp eq i64 4, %297
  br i1 %298, label %sb_1_99, label %sb_0_99

sb_0_99:                                          ; preds = %entry_98
  %299 = and i64 9223372036854775803, %296
  br label %entry_99

sb_1_99:                                          ; preds = %entry_98
  %300 = or i64 4, %296
  br label %entry_99

entry_99:                                         ; preds = %sb_0_99, %sb_1_99
  %301 = phi i64 [ %299, %sb_0_99 ], [ %300, %sb_1_99 ]
  %302 = and i64 8, %286
  %303 = icmp eq i64 8, %302
  br i1 %303, label %sb_1_100, label %sb_0_100

sb_0_100:                                         ; preds = %entry_99
  %304 = and i64 9223372036854775799, %301
  br label %entry_100

sb_1_100:                                         ; preds = %entry_99
  %305 = or i64 8, %301
  br label %entry_100

entry_100:                                        ; preds = %sb_0_100, %sb_1_100
  %306 = phi i64 [ %304, %sb_0_100 ], [ %305, %sb_1_100 ]
  %307 = and i64 16, %286
  %308 = icmp eq i64 16, %307
  br i1 %308, label %sb_1_101, label %sb_0_101

sb_0_101:                                         ; preds = %entry_100
  %309 = and i64 9223372036854775791, %306
  br label %entry_101

sb_1_101:                                         ; preds = %entry_100
  %310 = or i64 16, %306
  br label %entry_101

entry_101:                                        ; preds = %sb_0_101, %sb_1_101
  %311 = phi i64 [ %309, %sb_0_101 ], [ %310, %sb_1_101 ]
  %312 = and i64 32, %286
  %313 = icmp eq i64 32, %312
  br i1 %313, label %sb_1_102, label %sb_0_102

sb_0_102:                                         ; preds = %entry_101
  %314 = and i64 9223372036854775775, %311
  br label %entry_102

sb_1_102:                                         ; preds = %entry_101
  %315 = or i64 32, %311
  br label %entry_102

entry_102:                                        ; preds = %sb_0_102, %sb_1_102
  %316 = phi i64 [ %314, %sb_0_102 ], [ %315, %sb_1_102 ]
  %317 = and i64 64, %286
  %318 = icmp eq i64 64, %317
  br i1 %318, label %sb_1_103, label %sb_0_103

sb_0_103:                                         ; preds = %entry_102
  %319 = and i64 9223372036854775743, %316
  br label %entry_103

sb_1_103:                                         ; preds = %entry_102
  %320 = or i64 64, %316
  br label %entry_103

entry_103:                                        ; preds = %sb_0_103, %sb_1_103
  %321 = phi i64 [ %319, %sb_0_103 ], [ %320, %sb_1_103 ]
  %322 = and i64 128, %286
  %323 = icmp eq i64 128, %322
  br i1 %323, label %sb_1_104, label %sb_0_104

sb_0_104:                                         ; preds = %entry_103
  %324 = and i64 9223372036854775679, %321
  br label %entry_104

sb_1_104:                                         ; preds = %entry_103
  %325 = or i64 128, %321
  br label %entry_104

entry_104:                                        ; preds = %sb_0_104, %sb_1_104
  %326 = phi i64 [ %324, %sb_0_104 ], [ %325, %sb_1_104 ]
  %327 = and i64 256, %286
  %328 = icmp eq i64 256, %327
  br i1 %328, label %sb_1_105, label %sb_0_105

sb_0_105:                                         ; preds = %entry_104
  %329 = and i64 9223372036854775551, %326
  br label %entry_105

sb_1_105:                                         ; preds = %entry_104
  %330 = or i64 256, %326
  br label %entry_105

entry_105:                                        ; preds = %sb_0_105, %sb_1_105
  %331 = phi i64 [ %329, %sb_0_105 ], [ %330, %sb_1_105 ]
  %332 = and i64 512, %286
  %333 = icmp eq i64 512, %332
  br i1 %333, label %sb_1_106, label %sb_0_106

sb_0_106:                                         ; preds = %entry_105
  %334 = and i64 9223372036854775295, %331
  br label %entry_106

sb_1_106:                                         ; preds = %entry_105
  %335 = or i64 512, %331
  br label %entry_106

entry_106:                                        ; preds = %sb_0_106, %sb_1_106
  %336 = phi i64 [ %334, %sb_0_106 ], [ %335, %sb_1_106 ]
  %337 = and i64 1024, %286
  %338 = icmp eq i64 1024, %337
  br i1 %338, label %sb_1_107, label %sb_0_107

sb_0_107:                                         ; preds = %entry_106
  %339 = and i64 9223372036854774783, %336
  br label %entry_107

sb_1_107:                                         ; preds = %entry_106
  %340 = or i64 1024, %336
  br label %entry_107

entry_107:                                        ; preds = %sb_0_107, %sb_1_107
  %341 = phi i64 [ %339, %sb_0_107 ], [ %340, %sb_1_107 ]
  %342 = and i64 2048, %286
  %343 = icmp eq i64 2048, %342
  br i1 %343, label %sb_1_108, label %sb_0_108

sb_0_108:                                         ; preds = %entry_107
  %344 = and i64 9223372036854773759, %341
  br label %entry_108

sb_1_108:                                         ; preds = %entry_107
  %345 = or i64 2048, %341
  br label %entry_108

entry_108:                                        ; preds = %sb_0_108, %sb_1_108
  %346 = phi i64 [ %344, %sb_0_108 ], [ %345, %sb_1_108 ]
  %347 = and i64 4096, %286
  %348 = icmp eq i64 4096, %347
  br i1 %348, label %sb_1_109, label %sb_0_109

sb_0_109:                                         ; preds = %entry_108
  %349 = and i64 9223372036854771711, %346
  br label %entry_109

sb_1_109:                                         ; preds = %entry_108
  %350 = or i64 4096, %346
  br label %entry_109

entry_109:                                        ; preds = %sb_0_109, %sb_1_109
  %351 = phi i64 [ %349, %sb_0_109 ], [ %350, %sb_1_109 ]
  %352 = and i64 8192, %286
  %353 = icmp eq i64 8192, %352
  br i1 %353, label %sb_1_110, label %sb_0_110

sb_0_110:                                         ; preds = %entry_109
  %354 = and i64 9223372036854767615, %351
  br label %entry_110

sb_1_110:                                         ; preds = %entry_109
  %355 = or i64 8192, %351
  br label %entry_110

entry_110:                                        ; preds = %sb_0_110, %sb_1_110
  %356 = phi i64 [ %354, %sb_0_110 ], [ %355, %sb_1_110 ]
  %357 = and i64 16384, %286
  %358 = icmp eq i64 16384, %357
  br i1 %358, label %sb_1_111, label %sb_0_111

sb_0_111:                                         ; preds = %entry_110
  %359 = and i64 9223372036854759423, %356
  br label %entry_111

sb_1_111:                                         ; preds = %entry_110
  %360 = or i64 16384, %356
  br label %entry_111

entry_111:                                        ; preds = %sb_0_111, %sb_1_111
  %361 = phi i64 [ %359, %sb_0_111 ], [ %360, %sb_1_111 ]
  %362 = and i64 32768, %286
  %363 = icmp eq i64 32768, %362
  br i1 %363, label %sb_1_112, label %sb_0_112

sb_0_112:                                         ; preds = %entry_111
  %364 = and i64 9223372036854743039, %361
  br label %entry_112

sb_1_112:                                         ; preds = %entry_111
  %365 = or i64 32768, %361
  br label %entry_112

entry_112:                                        ; preds = %sb_0_112, %sb_1_112
  %366 = phi i64 [ %364, %sb_0_112 ], [ %365, %sb_1_112 ]
  %367 = and i64 65536, %286
  %368 = icmp eq i64 65536, %367
  br i1 %368, label %sb_1_113, label %sb_0_113

sb_0_113:                                         ; preds = %entry_112
  %369 = and i64 9223372036854710271, %366
  br label %entry_113

sb_1_113:                                         ; preds = %entry_112
  %370 = or i64 65536, %366
  br label %entry_113

entry_113:                                        ; preds = %sb_0_113, %sb_1_113
  %371 = phi i64 [ %369, %sb_0_113 ], [ %370, %sb_1_113 ]
  %372 = and i64 131072, %286
  %373 = icmp eq i64 131072, %372
  br i1 %373, label %sb_1_114, label %sb_0_114

sb_0_114:                                         ; preds = %entry_113
  %374 = and i64 9223372036854644735, %371
  br label %entry_114

sb_1_114:                                         ; preds = %entry_113
  %375 = or i64 131072, %371
  br label %entry_114

entry_114:                                        ; preds = %sb_0_114, %sb_1_114
  %376 = phi i64 [ %374, %sb_0_114 ], [ %375, %sb_1_114 ]
  %377 = and i64 262144, %286
  %378 = icmp eq i64 262144, %377
  br i1 %378, label %sb_1_115, label %sb_0_115

sb_0_115:                                         ; preds = %entry_114
  %379 = and i64 9223372036854513663, %376
  br label %entry_115

sb_1_115:                                         ; preds = %entry_114
  %380 = or i64 262144, %376
  br label %entry_115

entry_115:                                        ; preds = %sb_0_115, %sb_1_115
  %381 = phi i64 [ %379, %sb_0_115 ], [ %380, %sb_1_115 ]
  %382 = and i64 524288, %286
  %383 = icmp eq i64 524288, %382
  br i1 %383, label %sb_1_116, label %sb_0_116

sb_0_116:                                         ; preds = %entry_115
  %384 = and i64 9223372036854251519, %381
  br label %entry_116

sb_1_116:                                         ; preds = %entry_115
  %385 = or i64 524288, %381
  br label %entry_116

entry_116:                                        ; preds = %sb_0_116, %sb_1_116
  %386 = phi i64 [ %384, %sb_0_116 ], [ %385, %sb_1_116 ]
  %387 = and i64 1048576, %286
  %388 = icmp eq i64 1048576, %387
  br i1 %388, label %sb_1_117, label %sb_0_117

sb_0_117:                                         ; preds = %entry_116
  %389 = and i64 9223372036853727231, %386
  br label %entry_117

sb_1_117:                                         ; preds = %entry_116
  %390 = or i64 1048576, %386
  br label %entry_117

entry_117:                                        ; preds = %sb_0_117, %sb_1_117
  %391 = phi i64 [ %389, %sb_0_117 ], [ %390, %sb_1_117 ]
  %392 = and i64 2097152, %286
  %393 = icmp eq i64 2097152, %392
  br i1 %393, label %sb_1_118, label %sb_0_118

sb_0_118:                                         ; preds = %entry_117
  %394 = and i64 9223372036852678655, %391
  br label %entry_118

sb_1_118:                                         ; preds = %entry_117
  %395 = or i64 2097152, %391
  br label %entry_118

entry_118:                                        ; preds = %sb_0_118, %sb_1_118
  %396 = phi i64 [ %394, %sb_0_118 ], [ %395, %sb_1_118 ]
  %397 = and i64 4194304, %286
  %398 = icmp eq i64 4194304, %397
  br i1 %398, label %sb_1_119, label %sb_0_119

sb_0_119:                                         ; preds = %entry_118
  %399 = and i64 9223372036850581503, %396
  br label %entry_119

sb_1_119:                                         ; preds = %entry_118
  %400 = or i64 4194304, %396
  br label %entry_119

entry_119:                                        ; preds = %sb_0_119, %sb_1_119
  %401 = phi i64 [ %399, %sb_0_119 ], [ %400, %sb_1_119 ]
  %402 = and i64 8388608, %286
  %403 = icmp eq i64 8388608, %402
  br i1 %403, label %sb_1_120, label %sb_0_120

sb_0_120:                                         ; preds = %entry_119
  %404 = and i64 9223372036846387199, %401
  br label %entry_120

sb_1_120:                                         ; preds = %entry_119
  %405 = or i64 8388608, %401
  br label %entry_120

entry_120:                                        ; preds = %sb_0_120, %sb_1_120
  %406 = phi i64 [ %404, %sb_0_120 ], [ %405, %sb_1_120 ]
  %407 = and i64 16777216, %286
  %408 = icmp eq i64 16777216, %407
  br i1 %408, label %sb_1_121, label %sb_0_121

sb_0_121:                                         ; preds = %entry_120
  %409 = and i64 9223372036837998591, %406
  br label %entry_121

sb_1_121:                                         ; preds = %entry_120
  %410 = or i64 16777216, %406
  br label %entry_121

entry_121:                                        ; preds = %sb_0_121, %sb_1_121
  %411 = phi i64 [ %409, %sb_0_121 ], [ %410, %sb_1_121 ]
  %412 = and i64 33554432, %286
  %413 = icmp eq i64 33554432, %412
  br i1 %413, label %sb_1_122, label %sb_0_122

sb_0_122:                                         ; preds = %entry_121
  %414 = and i64 9223372036821221375, %411
  br label %entry_122

sb_1_122:                                         ; preds = %entry_121
  %415 = or i64 33554432, %411
  br label %entry_122

entry_122:                                        ; preds = %sb_0_122, %sb_1_122
  %416 = phi i64 [ %414, %sb_0_122 ], [ %415, %sb_1_122 ]
  %417 = and i64 67108864, %286
  %418 = icmp eq i64 67108864, %417
  br i1 %418, label %sb_1_123, label %sb_0_123

sb_0_123:                                         ; preds = %entry_122
  %419 = and i64 9223372036787666943, %416
  br label %entry_123

sb_1_123:                                         ; preds = %entry_122
  %420 = or i64 67108864, %416
  br label %entry_123

entry_123:                                        ; preds = %sb_0_123, %sb_1_123
  %421 = phi i64 [ %419, %sb_0_123 ], [ %420, %sb_1_123 ]
  %422 = and i64 134217728, %286
  %423 = icmp eq i64 134217728, %422
  br i1 %423, label %sb_1_124, label %sb_0_124

sb_0_124:                                         ; preds = %entry_123
  %424 = and i64 9223372036720558079, %421
  br label %entry_124

sb_1_124:                                         ; preds = %entry_123
  %425 = or i64 134217728, %421
  br label %entry_124

entry_124:                                        ; preds = %sb_0_124, %sb_1_124
  %426 = phi i64 [ %424, %sb_0_124 ], [ %425, %sb_1_124 ]
  %427 = and i64 268435456, %286
  %428 = icmp eq i64 268435456, %427
  br i1 %428, label %sb_1_125, label %sb_0_125

sb_0_125:                                         ; preds = %entry_124
  %429 = and i64 9223372036586340351, %426
  br label %entry_125

sb_1_125:                                         ; preds = %entry_124
  %430 = or i64 268435456, %426
  br label %entry_125

entry_125:                                        ; preds = %sb_0_125, %sb_1_125
  %431 = phi i64 [ %429, %sb_0_125 ], [ %430, %sb_1_125 ]
  %432 = and i64 536870912, %286
  %433 = icmp eq i64 536870912, %432
  br i1 %433, label %sb_1_126, label %sb_0_126

sb_0_126:                                         ; preds = %entry_125
  %434 = and i64 9223372036317904895, %431
  br label %entry_126

sb_1_126:                                         ; preds = %entry_125
  %435 = or i64 536870912, %431
  br label %entry_126

entry_126:                                        ; preds = %sb_0_126, %sb_1_126
  %436 = phi i64 [ %434, %sb_0_126 ], [ %435, %sb_1_126 ]
  %437 = and i64 1073741824, %286
  %438 = icmp eq i64 1073741824, %437
  br i1 %438, label %sb_1_127, label %sb_0_127

sb_0_127:                                         ; preds = %entry_126
  %439 = and i64 9223372035781033983, %436
  br label %entry_127

sb_1_127:                                         ; preds = %entry_126
  %440 = or i64 1073741824, %436
  br label %entry_127

entry_127:                                        ; preds = %sb_0_127, %sb_1_127
  %441 = phi i64 [ %439, %sb_0_127 ], [ %440, %sb_1_127 ]
  %442 = and i64 2147483648, %286
  %443 = icmp eq i64 2147483648, %442
  br i1 %443, label %sb_1_128, label %sb_0_128

sb_0_128:                                         ; preds = %entry_127
  %444 = and i64 9223372034707292159, %441
  br label %entry_128

sb_1_128:                                         ; preds = %entry_127
  %445 = or i64 2147483648, %441
  br label %entry_128

entry_128:                                        ; preds = %sb_0_128, %sb_1_128
  %446 = phi i64 [ %444, %sb_0_128 ], [ %445, %sb_1_128 ]
  %447 = add i64 %286, %446
  %448 = sub i64 %286, %446
  %449 = shl i64 %286, 1
  %450 = lshr i64 %449, 1
  %451 = icmp eq i64 1, %449
  br i1 %451, label %sb_1_129, label %sb_0_129

sb_0_129:                                         ; preds = %entry_128
  br label %entry_129

sb_1_129:                                         ; preds = %entry_128
  br label %entry_129

entry_129:                                        ; preds = %sb_0_129, %sb_1_129
  %452 = phi i64 [ 0, %sb_0_129 ], [ 16, %sb_1_129 ]
  %453 = icmp sgt i64 2, %449
  %454 = icmp sgt i64 %449, -1
  %455 = and i1 %453, %454
  br i1 %455, label %sb_1_130, label %sb_0_130

sb_0_130:                                         ; preds = %entry_129
  %456 = and i64 9223372036854775775, %452
  br label %entry_130

sb_1_130:                                         ; preds = %entry_129
  %457 = or i64 32, %452
  br label %entry_130

entry_130:                                        ; preds = %sb_0_130, %sb_1_130
  %458 = phi i64 [ %456, %sb_0_130 ], [ %457, %sb_1_130 ]
  %459 = icmp eq i64 0, %449
  br i1 %459, label %sb_1_131, label %sb_0_131

sb_0_131:                                         ; preds = %entry_130
  %460 = and i64 9223372036854775743, %458
  br label %entry_131

sb_1_131:                                         ; preds = %entry_130
  %461 = or i64 64, %458
  br label %entry_131

entry_131:                                        ; preds = %sb_0_131, %sb_1_131
  %462 = phi i64 [ %460, %sb_0_131 ], [ %461, %sb_1_131 ]
  %463 = icmp sgt i64 1, %449
  %464 = icmp sgt i64 %449, -1
  %465 = and i1 %463, %464
  br i1 %465, label %sb_1_132, label %sb_0_132

sb_0_132:                                         ; preds = %entry_131
  %466 = and i64 9223372036854775679, %462
  br label %entry_132

sb_1_132:                                         ; preds = %entry_131
  %467 = or i64 128, %462
  br label %entry_132

entry_132:                                        ; preds = %sb_0_132, %sb_1_132
  %468 = phi i64 [ %466, %sb_0_132 ], [ %467, %sb_1_132 ]
  %469 = icmp sgt i64 0, %449
  %470 = icmp sgt i64 %449, 1
  %471 = and i1 %469, %470
  br i1 %471, label %sb_1_133, label %sb_0_133

sb_0_133:                                         ; preds = %entry_132
  %472 = and i64 9223372036854775551, %468
  br label %entry_133

sb_1_133:                                         ; preds = %entry_132
  %473 = or i64 256, %468
  br label %entry_133

entry_133:                                        ; preds = %sb_0_133, %sb_1_133
  %474 = phi i64 [ %472, %sb_0_133 ], [ %473, %sb_1_133 ]
  %475 = and i64 1, %449
  %476 = icmp eq i64 1, %475
  br i1 %476, label %condb0, label %contb0

condb0:                                           ; preds = %entry_133
  br label %contb0

contb0:                                           ; preds = %condb0, %entry_133
  %477 = and i64 1, %449
  %478 = icmp eq i64 1, %477
  %479 = and i64 1, %450
  %480 = icmp eq i64 1, %479
  %481 = xor i1 %478, %480
  br i1 %481, label %sb_1_134, label %sb_0_134

sb_0_134:                                         ; preds = %contb0
  %482 = and i64 9223372036854775805, %474
  br label %contb0_134

sb_1_134:                                         ; preds = %contb0
  %483 = or i64 2, %474
  br label %contb0_134

contb0_134:                                       ; preds = %sb_0_134, %sb_1_134
  %484 = phi i64 [ %482, %sb_0_134 ], [ %483, %sb_1_134 ]
  %485 = xor i64 %449, %450
  %486 = and i64 %449, %450
  %487 = or i64 %449, %450
  %488 = icmp eq i64 1, %485
  br i1 %488, label %sb_1_135, label %sb_0_135

sb_0_135:                                         ; preds = %contb0_134
  %489 = and i64 9223372036854775806, %484
  br label %contb0_135

sb_1_135:                                         ; preds = %contb0_134
  %490 = or i64 1, %484
  br label %contb0_135

contb0_135:                                       ; preds = %sb_0_135, %sb_1_135
  %491 = phi i64 [ %489, %sb_0_135 ], [ %490, %sb_1_135 ]
  %492 = icmp eq i64 1, %486
  br i1 %492, label %sb_1_136, label %sb_0_136

sb_0_136:                                         ; preds = %contb0_135
  %493 = and i64 9223372036854775803, %491
  br label %contb0_136

sb_1_136:                                         ; preds = %contb0_135
  %494 = or i64 4, %491
  br label %contb0_136

contb0_136:                                       ; preds = %sb_0_136, %sb_1_136
  %495 = phi i64 [ %493, %sb_0_136 ], [ %494, %sb_1_136 ]
  %496 = icmp eq i64 1, %487
  br i1 %496, label %sb_1_137, label %sb_0_137

sb_0_137:                                         ; preds = %contb0_136
  %497 = and i64 9223372036854775799, %495
  br label %contb0_137

sb_1_137:                                         ; preds = %contb0_136
  %498 = or i64 8, %495
  br label %contb0_137

contb0_137:                                       ; preds = %sb_0_137, %sb_1_137
  %499 = phi i64 [ %497, %sb_0_137 ], [ %498, %sb_1_137 ]
  %500 = and i64 1, %499
  %501 = icmp eq i64 1, %500
  br i1 %501, label %condb1, label %contb1

condb1:                                           ; preds = %contb0_137
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0_137
  %502 = and i64 2, %499
  %503 = icmp eq i64 2, %502
  br i1 %503, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %504 = and i64 4, %499
  %505 = icmp eq i64 4, %504
  br i1 %505, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %506 = and i64 8, %499
  %507 = icmp eq i64 8, %506
  br i1 %507, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %508 = and i64 1, %449
  %509 = icmp eq i64 1, %508
  br i1 %509, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %510 = and i64 16, %499
  %511 = icmp eq i64 16, %510
  br i1 %511, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %512 = and i64 1, %449
  %513 = icmp eq i64 1, %512
  br i1 %513, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %514 = and i64 32, %499
  %515 = icmp eq i64 32, %514
  br i1 %515, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %516 = and i64 64, %499
  %517 = icmp eq i64 64, %516
  br i1 %517, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %518 = and i64 128, %499
  %519 = icmp eq i64 128, %518
  br i1 %519, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %520 = and i64 256, %499
  %521 = icmp eq i64 256, %520
  br i1 %521, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  call void @__quantum__rt__int_record_output(i64 %449, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %450, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %448, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %499, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %485, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %486, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %487, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
