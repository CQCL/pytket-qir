; ModuleID = 'ptest_pytket_qir_14'
source_filename = "ptest_pytket_qir_14"

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
  %29 = and i64 9223372036854775806, %0
  br label %entry_11

sb_1_11:                                          ; preds = %entry_10
  %30 = or i64 1, %0
  br label %entry_11

entry_11:                                         ; preds = %sb_0_11, %sb_1_11
  %31 = phi i64 [ %29, %sb_0_11 ], [ %30, %sb_1_11 ]
  br i1 true, label %sb_1_12, label %sb_0_12

sb_0_12:                                          ; preds = %entry_11
  %32 = and i64 9223372036854775805, %31
  br label %entry_12

sb_1_12:                                          ; preds = %entry_11
  %33 = or i64 2, %31
  br label %entry_12

entry_12:                                         ; preds = %sb_0_12, %sb_1_12
  %34 = phi i64 [ %32, %sb_0_12 ], [ %33, %sb_1_12 ]
  br i1 false, label %sb_1_13, label %sb_0_13

sb_0_13:                                          ; preds = %entry_12
  %35 = and i64 9223372036854775803, %34
  br label %entry_13

sb_1_13:                                          ; preds = %entry_12
  %36 = or i64 4, %34
  br label %entry_13

entry_13:                                         ; preds = %sb_0_13, %sb_1_13
  %37 = phi i64 [ %35, %sb_0_13 ], [ %36, %sb_1_13 ]
  br i1 false, label %sb_1_14, label %sb_0_14

sb_0_14:                                          ; preds = %entry_13
  %38 = and i64 9223372036854775799, %37
  br label %entry_14

sb_1_14:                                          ; preds = %entry_13
  %39 = or i64 8, %37
  br label %entry_14

entry_14:                                         ; preds = %sb_0_14, %sb_1_14
  %40 = phi i64 [ %38, %sb_0_14 ], [ %39, %sb_1_14 ]
  br i1 false, label %sb_1_15, label %sb_0_15

sb_0_15:                                          ; preds = %entry_14
  %41 = and i64 9223372036854775791, %40
  br label %entry_15

sb_1_15:                                          ; preds = %entry_14
  %42 = or i64 16, %40
  br label %entry_15

entry_15:                                         ; preds = %sb_0_15, %sb_1_15
  %43 = phi i64 [ %41, %sb_0_15 ], [ %42, %sb_1_15 ]
  br i1 false, label %sb_1_16, label %sb_0_16

sb_0_16:                                          ; preds = %entry_15
  %44 = and i64 9223372036854775775, %43
  br label %entry_16

sb_1_16:                                          ; preds = %entry_15
  %45 = or i64 32, %43
  br label %entry_16

entry_16:                                         ; preds = %sb_0_16, %sb_1_16
  %46 = phi i64 [ %44, %sb_0_16 ], [ %45, %sb_1_16 ]
  br i1 false, label %sb_1_17, label %sb_0_17

sb_0_17:                                          ; preds = %entry_16
  %47 = and i64 9223372036854775743, %46
  br label %entry_17

sb_1_17:                                          ; preds = %entry_16
  %48 = or i64 64, %46
  br label %entry_17

entry_17:                                         ; preds = %sb_0_17, %sb_1_17
  %49 = phi i64 [ %47, %sb_0_17 ], [ %48, %sb_1_17 ]
  br i1 false, label %sb_1_18, label %sb_0_18

sb_0_18:                                          ; preds = %entry_17
  %50 = and i64 9223372036854775679, %49
  br label %entry_18

sb_1_18:                                          ; preds = %entry_17
  %51 = or i64 128, %49
  br label %entry_18

entry_18:                                         ; preds = %sb_0_18, %sb_1_18
  %52 = phi i64 [ %50, %sb_0_18 ], [ %51, %sb_1_18 ]
  br i1 true, label %sb_1_19, label %sb_0_19

sb_0_19:                                          ; preds = %entry_18
  %53 = and i64 9223372036854775806, %52
  br label %entry_19

sb_1_19:                                          ; preds = %entry_18
  %54 = or i64 1, %52
  br label %entry_19

entry_19:                                         ; preds = %sb_0_19, %sb_1_19
  %55 = phi i64 [ %53, %sb_0_19 ], [ %54, %sb_1_19 ]
  br i1 true, label %sb_1_20, label %sb_0_20

sb_0_20:                                          ; preds = %entry_19
  %56 = and i64 9223372036854775805, %55
  br label %entry_20

sb_1_20:                                          ; preds = %entry_19
  %57 = or i64 2, %55
  br label %entry_20

entry_20:                                         ; preds = %sb_0_20, %sb_1_20
  %58 = phi i64 [ %56, %sb_0_20 ], [ %57, %sb_1_20 ]
  br i1 true, label %sb_1_21, label %sb_0_21

sb_0_21:                                          ; preds = %entry_20
  %59 = and i64 9223372036854775803, %58
  br label %entry_21

sb_1_21:                                          ; preds = %entry_20
  %60 = or i64 4, %58
  br label %entry_21

entry_21:                                         ; preds = %sb_0_21, %sb_1_21
  %61 = phi i64 [ %59, %sb_0_21 ], [ %60, %sb_1_21 ]
  br i1 false, label %sb_1_22, label %sb_0_22

sb_0_22:                                          ; preds = %entry_21
  %62 = and i64 9223372036854775799, %61
  br label %entry_22

sb_1_22:                                          ; preds = %entry_21
  %63 = or i64 8, %61
  br label %entry_22

entry_22:                                         ; preds = %sb_0_22, %sb_1_22
  %64 = phi i64 [ %62, %sb_0_22 ], [ %63, %sb_1_22 ]
  br i1 true, label %sb_1_23, label %sb_0_23

sb_0_23:                                          ; preds = %entry_22
  %65 = and i64 9223372036854775791, %64
  br label %entry_23

sb_1_23:                                          ; preds = %entry_22
  %66 = or i64 16, %64
  br label %entry_23

entry_23:                                         ; preds = %sb_0_23, %sb_1_23
  %67 = phi i64 [ %65, %sb_0_23 ], [ %66, %sb_1_23 ]
  br i1 false, label %sb_1_24, label %sb_0_24

sb_0_24:                                          ; preds = %entry_23
  %68 = and i64 9223372036854775775, %67
  br label %entry_24

sb_1_24:                                          ; preds = %entry_23
  %69 = or i64 32, %67
  br label %entry_24

entry_24:                                         ; preds = %sb_0_24, %sb_1_24
  %70 = phi i64 [ %68, %sb_0_24 ], [ %69, %sb_1_24 ]
  br i1 false, label %sb_1_25, label %sb_0_25

sb_0_25:                                          ; preds = %entry_24
  %71 = and i64 9223372036854775743, %70
  br label %entry_25

sb_1_25:                                          ; preds = %entry_24
  %72 = or i64 64, %70
  br label %entry_25

entry_25:                                         ; preds = %sb_0_25, %sb_1_25
  %73 = phi i64 [ %71, %sb_0_25 ], [ %72, %sb_1_25 ]
  br i1 false, label %sb_1_26, label %sb_0_26

sb_0_26:                                          ; preds = %entry_25
  %74 = and i64 9223372036854775679, %73
  br label %entry_26

sb_1_26:                                          ; preds = %entry_25
  %75 = or i64 128, %73
  br label %entry_26

entry_26:                                         ; preds = %sb_0_26, %sb_1_26
  %76 = phi i64 [ %74, %sb_0_26 ], [ %75, %sb_1_26 ]
  %77 = and i64 1, %76
  %78 = icmp eq i64 1, %77
  br i1 %78, label %sb_1_27, label %sb_0_27

sb_0_27:                                          ; preds = %entry_26
  %79 = and i64 9223372036854775806, %28
  br label %entry_27

sb_1_27:                                          ; preds = %entry_26
  %80 = or i64 1, %28
  br label %entry_27

entry_27:                                         ; preds = %sb_0_27, %sb_1_27
  %81 = phi i64 [ %79, %sb_0_27 ], [ %80, %sb_1_27 ]
  %82 = and i64 2, %76
  %83 = icmp eq i64 2, %82
  br i1 %83, label %sb_1_28, label %sb_0_28

sb_0_28:                                          ; preds = %entry_27
  %84 = and i64 9223372036854775805, %81
  br label %entry_28

sb_1_28:                                          ; preds = %entry_27
  %85 = or i64 2, %81
  br label %entry_28

entry_28:                                         ; preds = %sb_0_28, %sb_1_28
  %86 = phi i64 [ %84, %sb_0_28 ], [ %85, %sb_1_28 ]
  %87 = and i64 4, %76
  %88 = icmp eq i64 4, %87
  br i1 %88, label %sb_1_29, label %sb_0_29

sb_0_29:                                          ; preds = %entry_28
  %89 = and i64 9223372036854775803, %86
  br label %entry_29

sb_1_29:                                          ; preds = %entry_28
  %90 = or i64 4, %86
  br label %entry_29

entry_29:                                         ; preds = %sb_0_29, %sb_1_29
  %91 = phi i64 [ %89, %sb_0_29 ], [ %90, %sb_1_29 ]
  %92 = and i64 8, %76
  %93 = icmp eq i64 8, %92
  br i1 %93, label %sb_1_30, label %sb_0_30

sb_0_30:                                          ; preds = %entry_29
  %94 = and i64 9223372036854775799, %91
  br label %entry_30

sb_1_30:                                          ; preds = %entry_29
  %95 = or i64 8, %91
  br label %entry_30

entry_30:                                         ; preds = %sb_0_30, %sb_1_30
  %96 = phi i64 [ %94, %sb_0_30 ], [ %95, %sb_1_30 ]
  %97 = and i64 16, %76
  %98 = icmp eq i64 16, %97
  br i1 %98, label %sb_1_31, label %sb_0_31

sb_0_31:                                          ; preds = %entry_30
  %99 = and i64 9223372036854775791, %96
  br label %entry_31

sb_1_31:                                          ; preds = %entry_30
  %100 = or i64 16, %96
  br label %entry_31

entry_31:                                         ; preds = %sb_0_31, %sb_1_31
  %101 = phi i64 [ %99, %sb_0_31 ], [ %100, %sb_1_31 ]
  %102 = and i64 32, %76
  %103 = icmp eq i64 32, %102
  br i1 %103, label %sb_1_32, label %sb_0_32

sb_0_32:                                          ; preds = %entry_31
  %104 = and i64 9223372036854775775, %101
  br label %entry_32

sb_1_32:                                          ; preds = %entry_31
  %105 = or i64 32, %101
  br label %entry_32

entry_32:                                         ; preds = %sb_0_32, %sb_1_32
  %106 = phi i64 [ %104, %sb_0_32 ], [ %105, %sb_1_32 ]
  %107 = and i64 64, %76
  %108 = icmp eq i64 64, %107
  br i1 %108, label %sb_1_33, label %sb_0_33

sb_0_33:                                          ; preds = %entry_32
  %109 = and i64 9223372036854775743, %106
  br label %entry_33

sb_1_33:                                          ; preds = %entry_32
  %110 = or i64 64, %106
  br label %entry_33

entry_33:                                         ; preds = %sb_0_33, %sb_1_33
  %111 = phi i64 [ %109, %sb_0_33 ], [ %110, %sb_1_33 ]
  %112 = and i64 128, %76
  %113 = icmp eq i64 128, %112
  br i1 %113, label %sb_1_34, label %sb_0_34

sb_0_34:                                          ; preds = %entry_33
  %114 = and i64 9223372036854775679, %111
  br label %entry_34

sb_1_34:                                          ; preds = %entry_33
  %115 = or i64 128, %111
  br label %entry_34

entry_34:                                         ; preds = %sb_0_34, %sb_1_34
  %116 = phi i64 [ %114, %sb_0_34 ], [ %115, %sb_1_34 ]
  %117 = add i64 %76, %116
  %118 = trunc i64 %117 to i10
  %119 = zext i10 %118 to i64
  %120 = sub i64 %76, %116
  %121 = trunc i64 %120 to i10
  %122 = zext i10 %121 to i64
  %123 = shl i64 %76, 1
  %124 = trunc i64 %123 to i8
  %125 = zext i8 %124 to i64
  %126 = lshr i64 %125, 1
  %127 = trunc i64 %126 to i10
  %128 = zext i10 %127 to i64
  %129 = icmp eq i64 1, %125
  br i1 %129, label %sb_1_35, label %sb_0_35

sb_0_35:                                          ; preds = %entry_34
  br label %entry_35

sb_1_35:                                          ; preds = %entry_34
  br label %entry_35

entry_35:                                         ; preds = %sb_0_35, %sb_1_35
  %130 = phi i64 [ 0, %sb_0_35 ], [ 16, %sb_1_35 ]
  %131 = icmp sgt i64 2, %125
  %132 = icmp sgt i64 %125, -1
  %133 = and i1 %131, %132
  br i1 %133, label %sb_1_36, label %sb_0_36

sb_0_36:                                          ; preds = %entry_35
  %134 = and i64 9223372036854775775, %130
  br label %entry_36

sb_1_36:                                          ; preds = %entry_35
  %135 = or i64 32, %130
  br label %entry_36

entry_36:                                         ; preds = %sb_0_36, %sb_1_36
  %136 = phi i64 [ %134, %sb_0_36 ], [ %135, %sb_1_36 ]
  %137 = icmp eq i64 0, %125
  br i1 %137, label %sb_1_37, label %sb_0_37

sb_0_37:                                          ; preds = %entry_36
  %138 = and i64 9223372036854775743, %136
  br label %entry_37

sb_1_37:                                          ; preds = %entry_36
  %139 = or i64 64, %136
  br label %entry_37

entry_37:                                         ; preds = %sb_0_37, %sb_1_37
  %140 = phi i64 [ %138, %sb_0_37 ], [ %139, %sb_1_37 ]
  %141 = icmp sgt i64 1, %125
  %142 = icmp sgt i64 %125, -1
  %143 = and i1 %141, %142
  br i1 %143, label %sb_1_38, label %sb_0_38

sb_0_38:                                          ; preds = %entry_37
  %144 = and i64 9223372036854775679, %140
  br label %entry_38

sb_1_38:                                          ; preds = %entry_37
  %145 = or i64 128, %140
  br label %entry_38

entry_38:                                         ; preds = %sb_0_38, %sb_1_38
  %146 = phi i64 [ %144, %sb_0_38 ], [ %145, %sb_1_38 ]
  %147 = icmp sgt i64 0, %125
  %148 = icmp sgt i64 %125, 1
  %149 = and i1 %147, %148
  br i1 %149, label %sb_1_39, label %sb_0_39

sb_0_39:                                          ; preds = %entry_38
  %150 = and i64 9223372036854775551, %146
  br label %entry_39

sb_1_39:                                          ; preds = %entry_38
  %151 = or i64 256, %146
  br label %entry_39

entry_39:                                         ; preds = %sb_0_39, %sb_1_39
  %152 = phi i64 [ %150, %sb_0_39 ], [ %151, %sb_1_39 ]
  %153 = and i64 1, %125
  %154 = icmp eq i64 1, %153
  br i1 %154, label %condb0, label %contb0

condb0:                                           ; preds = %entry_39
  br label %contb0

contb0:                                           ; preds = %condb0, %entry_39
  %155 = and i64 1, %125
  %156 = icmp eq i64 1, %155
  %157 = and i64 1, %128
  %158 = icmp eq i64 1, %157
  %159 = xor i1 %156, %158
  br i1 %159, label %sb_1_40, label %sb_0_40

sb_0_40:                                          ; preds = %contb0
  %160 = and i64 9223372036854775805, %152
  br label %contb0_40

sb_1_40:                                          ; preds = %contb0
  %161 = or i64 2, %152
  br label %contb0_40

contb0_40:                                        ; preds = %sb_0_40, %sb_1_40
  %162 = phi i64 [ %160, %sb_0_40 ], [ %161, %sb_1_40 ]
  %163 = xor i64 %125, %128
  %164 = and i64 %125, %128
  %165 = or i64 %125, %128
  %166 = icmp eq i64 1, %163
  br i1 %166, label %sb_1_41, label %sb_0_41

sb_0_41:                                          ; preds = %contb0_40
  %167 = and i64 9223372036854775806, %162
  br label %contb0_41

sb_1_41:                                          ; preds = %contb0_40
  %168 = or i64 1, %162
  br label %contb0_41

contb0_41:                                        ; preds = %sb_0_41, %sb_1_41
  %169 = phi i64 [ %167, %sb_0_41 ], [ %168, %sb_1_41 ]
  %170 = icmp eq i64 1, %164
  br i1 %170, label %sb_1_42, label %sb_0_42

sb_0_42:                                          ; preds = %contb0_41
  %171 = and i64 9223372036854775803, %169
  br label %contb0_42

sb_1_42:                                          ; preds = %contb0_41
  %172 = or i64 4, %169
  br label %contb0_42

contb0_42:                                        ; preds = %sb_0_42, %sb_1_42
  %173 = phi i64 [ %171, %sb_0_42 ], [ %172, %sb_1_42 ]
  %174 = icmp eq i64 1, %165
  br i1 %174, label %sb_1_43, label %sb_0_43

sb_0_43:                                          ; preds = %contb0_42
  %175 = and i64 9223372036854775799, %173
  br label %contb0_43

sb_1_43:                                          ; preds = %contb0_42
  %176 = or i64 8, %173
  br label %contb0_43

contb0_43:                                        ; preds = %sb_0_43, %sb_1_43
  %177 = phi i64 [ %175, %sb_0_43 ], [ %176, %sb_1_43 ]
  %178 = and i64 1, %177
  %179 = icmp eq i64 1, %178
  br i1 %179, label %condb1, label %contb1

condb1:                                           ; preds = %contb0_43
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0_43
  %180 = and i64 2, %177
  %181 = icmp eq i64 2, %180
  br i1 %181, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %182 = and i64 4, %177
  %183 = icmp eq i64 4, %182
  br i1 %183, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %184 = and i64 8, %177
  %185 = icmp eq i64 8, %184
  br i1 %185, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %186 = and i64 1, %125
  %187 = icmp eq i64 1, %186
  br i1 %187, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %188 = and i64 16, %177
  %189 = icmp eq i64 16, %188
  br i1 %189, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %190 = and i64 1, %125
  %191 = icmp eq i64 1, %190
  br i1 %191, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %192 = and i64 32, %177
  %193 = icmp eq i64 32, %192
  br i1 %193, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %194 = and i64 64, %177
  %195 = icmp eq i64 64, %194
  br i1 %195, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %196 = and i64 128, %177
  %197 = icmp eq i64 128, %196
  br i1 %197, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %198 = and i64 256, %177
  %199 = icmp eq i64 256, %198
  br i1 %199, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  call void @__quantum__rt__int_record_output(i64 %125, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %128, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %122, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %177, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %163, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %164, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %165, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
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
