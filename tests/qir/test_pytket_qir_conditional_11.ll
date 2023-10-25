; ModuleID = 'test_pytket_qir_conditional_11'
source_filename = "test_pytket_qir_conditional_11"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [17 x i8] c"tk_SCRATCH_BIT_0\00"
@2 = internal constant [17 x i8] c"tk_SCRATCH_BIT_1\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 4)
  %1 = call i1* @create_creg(i64 64)
  %2 = call i1* @create_creg(i64 2)
  %3 = call i64 @get_int_from_creg(i1* %0)
  %4 = icmp eq i64 1, %3
  call void @set_creg_bit(i1* %1, i64 0, i1 %4)
  %5 = call i64 @get_int_from_creg(i1* %0)
  %6 = icmp eq i64 2, %5
  call void @set_creg_bit(i1* %1, i64 1, i1 %6)
  %7 = call i64 @get_int_from_creg(i1* %0)
  %8 = icmp eq i64 2, %7
  call void @set_creg_bit(i1* %1, i64 2, i1 %8)
  %9 = call i64 @get_int_from_creg(i1* %0)
  %10 = icmp eq i64 3, %9
  call void @set_creg_bit(i1* %1, i64 3, i1 %10)
  %11 = call i64 @get_int_from_creg(i1* %0)
  %12 = icmp eq i64 4, %11
  call void @set_creg_bit(i1* %1, i64 4, i1 %12)
  %13 = call i64 @get_int_from_creg(i1* %0)
  %14 = icmp eq i64 4, %13
  call void @set_creg_bit(i1* %1, i64 5, i1 %14)
  %15 = call i64 @get_int_from_creg(i1* %0)
  %16 = icmp eq i64 1, %15
  call void @set_creg_bit(i1* %1, i64 6, i1 %16)
  %17 = call i64 @get_int_from_creg(i1* %0)
  %18 = icmp eq i64 2, %17
  call void @set_creg_bit(i1* %1, i64 7, i1 %18)
  %19 = call i64 @get_int_from_creg(i1* %0)
  %20 = icmp eq i64 2, %19
  call void @set_creg_bit(i1* %1, i64 8, i1 %20)
  %21 = call i64 @get_int_from_creg(i1* %0)
  %22 = icmp eq i64 3, %21
  call void @set_creg_bit(i1* %1, i64 9, i1 %22)
  %23 = call i64 @get_int_from_creg(i1* %0)
  %24 = icmp eq i64 4, %23
  call void @set_creg_bit(i1* %1, i64 10, i1 %24)
  %25 = call i64 @get_int_from_creg(i1* %0)
  %26 = icmp eq i64 4, %25
  call void @set_creg_bit(i1* %1, i64 11, i1 %26)
  %27 = call i64 @get_int_from_creg(i1* %0)
  %28 = icmp eq i64 1, %27
  call void @set_creg_bit(i1* %1, i64 12, i1 %28)
  %29 = call i64 @get_int_from_creg(i1* %0)
  %30 = icmp eq i64 2, %29
  call void @set_creg_bit(i1* %1, i64 13, i1 %30)
  %31 = call i64 @get_int_from_creg(i1* %0)
  %32 = icmp eq i64 2, %31
  call void @set_creg_bit(i1* %1, i64 14, i1 %32)
  %33 = call i64 @get_int_from_creg(i1* %0)
  %34 = icmp eq i64 3, %33
  call void @set_creg_bit(i1* %1, i64 15, i1 %34)
  %35 = call i64 @get_int_from_creg(i1* %0)
  %36 = icmp eq i64 4, %35
  call void @set_creg_bit(i1* %1, i64 16, i1 %36)
  %37 = call i64 @get_int_from_creg(i1* %0)
  %38 = icmp eq i64 4, %37
  call void @set_creg_bit(i1* %1, i64 17, i1 %38)
  %39 = call i64 @get_int_from_creg(i1* %0)
  %40 = icmp eq i64 1, %39
  call void @set_creg_bit(i1* %1, i64 18, i1 %40)
  %41 = call i64 @get_int_from_creg(i1* %0)
  %42 = icmp eq i64 2, %41
  call void @set_creg_bit(i1* %1, i64 19, i1 %42)
  %43 = call i64 @get_int_from_creg(i1* %0)
  %44 = icmp eq i64 2, %43
  call void @set_creg_bit(i1* %1, i64 20, i1 %44)
  %45 = call i64 @get_int_from_creg(i1* %0)
  %46 = icmp eq i64 3, %45
  call void @set_creg_bit(i1* %1, i64 21, i1 %46)
  %47 = call i64 @get_int_from_creg(i1* %0)
  %48 = icmp eq i64 4, %47
  call void @set_creg_bit(i1* %1, i64 22, i1 %48)
  %49 = call i64 @get_int_from_creg(i1* %0)
  %50 = icmp eq i64 4, %49
  call void @set_creg_bit(i1* %1, i64 23, i1 %50)
  %51 = call i64 @get_int_from_creg(i1* %0)
  %52 = icmp eq i64 1, %51
  call void @set_creg_bit(i1* %1, i64 24, i1 %52)
  %53 = call i64 @get_int_from_creg(i1* %0)
  %54 = icmp eq i64 2, %53
  call void @set_creg_bit(i1* %1, i64 25, i1 %54)
  %55 = call i64 @get_int_from_creg(i1* %0)
  %56 = icmp eq i64 2, %55
  call void @set_creg_bit(i1* %1, i64 26, i1 %56)
  %57 = call i64 @get_int_from_creg(i1* %0)
  %58 = icmp eq i64 3, %57
  call void @set_creg_bit(i1* %1, i64 27, i1 %58)
  %59 = call i64 @get_int_from_creg(i1* %0)
  %60 = icmp eq i64 4, %59
  call void @set_creg_bit(i1* %1, i64 28, i1 %60)
  %61 = call i64 @get_int_from_creg(i1* %0)
  %62 = icmp eq i64 4, %61
  call void @set_creg_bit(i1* %1, i64 29, i1 %62)
  %63 = call i64 @get_int_from_creg(i1* %0)
  %64 = icmp eq i64 1, %63
  call void @set_creg_bit(i1* %1, i64 30, i1 %64)
  %65 = call i64 @get_int_from_creg(i1* %0)
  %66 = icmp eq i64 2, %65
  call void @set_creg_bit(i1* %1, i64 31, i1 %66)
  %67 = call i64 @get_int_from_creg(i1* %0)
  %68 = icmp eq i64 2, %67
  call void @set_creg_bit(i1* %1, i64 32, i1 %68)
  %69 = call i64 @get_int_from_creg(i1* %0)
  %70 = icmp eq i64 3, %69
  call void @set_creg_bit(i1* %1, i64 33, i1 %70)
  %71 = call i64 @get_int_from_creg(i1* %0)
  %72 = icmp eq i64 4, %71
  call void @set_creg_bit(i1* %1, i64 34, i1 %72)
  %73 = call i64 @get_int_from_creg(i1* %0)
  %74 = icmp eq i64 4, %73
  call void @set_creg_bit(i1* %1, i64 35, i1 %74)
  %75 = call i64 @get_int_from_creg(i1* %0)
  %76 = icmp eq i64 1, %75
  call void @set_creg_bit(i1* %1, i64 36, i1 %76)
  %77 = call i64 @get_int_from_creg(i1* %0)
  %78 = icmp eq i64 2, %77
  call void @set_creg_bit(i1* %1, i64 37, i1 %78)
  %79 = call i64 @get_int_from_creg(i1* %0)
  %80 = icmp eq i64 2, %79
  call void @set_creg_bit(i1* %1, i64 38, i1 %80)
  %81 = call i64 @get_int_from_creg(i1* %0)
  %82 = icmp eq i64 3, %81
  call void @set_creg_bit(i1* %1, i64 39, i1 %82)
  %83 = call i64 @get_int_from_creg(i1* %0)
  %84 = icmp eq i64 4, %83
  call void @set_creg_bit(i1* %1, i64 40, i1 %84)
  %85 = call i64 @get_int_from_creg(i1* %0)
  %86 = icmp eq i64 4, %85
  call void @set_creg_bit(i1* %1, i64 41, i1 %86)
  %87 = call i64 @get_int_from_creg(i1* %0)
  %88 = icmp eq i64 1, %87
  call void @set_creg_bit(i1* %1, i64 42, i1 %88)
  %89 = call i64 @get_int_from_creg(i1* %0)
  %90 = icmp eq i64 2, %89
  call void @set_creg_bit(i1* %1, i64 43, i1 %90)
  %91 = call i64 @get_int_from_creg(i1* %0)
  %92 = icmp eq i64 2, %91
  call void @set_creg_bit(i1* %1, i64 44, i1 %92)
  %93 = call i64 @get_int_from_creg(i1* %0)
  %94 = icmp eq i64 3, %93
  call void @set_creg_bit(i1* %1, i64 45, i1 %94)
  %95 = call i64 @get_int_from_creg(i1* %0)
  %96 = icmp eq i64 4, %95
  call void @set_creg_bit(i1* %1, i64 46, i1 %96)
  %97 = call i64 @get_int_from_creg(i1* %0)
  %98 = icmp eq i64 4, %97
  call void @set_creg_bit(i1* %1, i64 47, i1 %98)
  %99 = call i64 @get_int_from_creg(i1* %0)
  %100 = icmp eq i64 1, %99
  call void @set_creg_bit(i1* %1, i64 48, i1 %100)
  %101 = call i64 @get_int_from_creg(i1* %0)
  %102 = icmp eq i64 2, %101
  call void @set_creg_bit(i1* %1, i64 49, i1 %102)
  %103 = call i64 @get_int_from_creg(i1* %0)
  %104 = icmp eq i64 2, %103
  call void @set_creg_bit(i1* %1, i64 50, i1 %104)
  %105 = call i64 @get_int_from_creg(i1* %0)
  %106 = icmp eq i64 3, %105
  call void @set_creg_bit(i1* %1, i64 51, i1 %106)
  %107 = call i64 @get_int_from_creg(i1* %0)
  %108 = icmp eq i64 4, %107
  call void @set_creg_bit(i1* %1, i64 52, i1 %108)
  %109 = call i64 @get_int_from_creg(i1* %0)
  %110 = icmp eq i64 4, %109
  call void @set_creg_bit(i1* %1, i64 53, i1 %110)
  %111 = call i64 @get_int_from_creg(i1* %0)
  %112 = icmp eq i64 1, %111
  call void @set_creg_bit(i1* %1, i64 54, i1 %112)
  %113 = call i64 @get_int_from_creg(i1* %0)
  %114 = icmp eq i64 2, %113
  call void @set_creg_bit(i1* %1, i64 55, i1 %114)
  %115 = call i64 @get_int_from_creg(i1* %0)
  %116 = icmp eq i64 2, %115
  call void @set_creg_bit(i1* %1, i64 56, i1 %116)
  %117 = call i64 @get_int_from_creg(i1* %0)
  %118 = icmp eq i64 3, %117
  call void @set_creg_bit(i1* %1, i64 57, i1 %118)
  %119 = call i64 @get_int_from_creg(i1* %0)
  %120 = icmp eq i64 4, %119
  call void @set_creg_bit(i1* %1, i64 58, i1 %120)
  %121 = call i64 @get_int_from_creg(i1* %0)
  %122 = icmp eq i64 4, %121
  call void @set_creg_bit(i1* %1, i64 59, i1 %122)
  %123 = call i64 @get_int_from_creg(i1* %0)
  %124 = icmp eq i64 1, %123
  call void @set_creg_bit(i1* %1, i64 60, i1 %124)
  %125 = call i64 @get_int_from_creg(i1* %0)
  %126 = icmp eq i64 2, %125
  call void @set_creg_bit(i1* %1, i64 61, i1 %126)
  %127 = call i64 @get_int_from_creg(i1* %0)
  %128 = icmp eq i64 2, %127
  call void @set_creg_bit(i1* %1, i64 62, i1 %128)
  %129 = call i64 @get_int_from_creg(i1* %0)
  %130 = icmp eq i64 3, %129
  call void @set_creg_bit(i1* %1, i64 63, i1 %130)
  %131 = call i64 @get_int_from_creg(i1* %0)
  %132 = icmp eq i64 4, %131
  call void @set_creg_bit(i1* %2, i64 0, i1 %132)
  %133 = call i64 @get_int_from_creg(i1* %0)
  %134 = icmp eq i64 4, %133
  call void @set_creg_bit(i1* %2, i64 1, i1 %134)
  %135 = call i1 @get_creg_bit(i1* %1, i64 0)
  br i1 %135, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %136 = call i1 @get_creg_bit(i1* %1, i64 1)
  br i1 %136, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %137 = call i1 @get_creg_bit(i1* %1, i64 2)
  br i1 %137, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %138 = call i1 @get_creg_bit(i1* %1, i64 3)
  br i1 %138, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %139 = call i1 @get_creg_bit(i1* %1, i64 4)
  br i1 %139, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %140 = call i1 @get_creg_bit(i1* %1, i64 5)
  br i1 %140, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  %141 = call i1 @get_creg_bit(i1* %1, i64 6)
  br i1 %141, label %then16, label %else17

then16:                                           ; preds = %continue15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue18

else17:                                           ; preds = %continue15
  br label %continue18

continue18:                                       ; preds = %else17, %then16
  %142 = call i1 @get_creg_bit(i1* %1, i64 7)
  br i1 %142, label %then19, label %else20

then19:                                           ; preds = %continue18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue21

else20:                                           ; preds = %continue18
  br label %continue21

continue21:                                       ; preds = %else20, %then19
  %143 = call i1 @get_creg_bit(i1* %1, i64 8)
  br i1 %143, label %then22, label %else23

then22:                                           ; preds = %continue21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue24

else23:                                           ; preds = %continue21
  br label %continue24

continue24:                                       ; preds = %else23, %then22
  %144 = call i1 @get_creg_bit(i1* %1, i64 9)
  br i1 %144, label %then25, label %else26

then25:                                           ; preds = %continue24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue27

else26:                                           ; preds = %continue24
  br label %continue27

continue27:                                       ; preds = %else26, %then25
  %145 = call i1 @get_creg_bit(i1* %1, i64 10)
  br i1 %145, label %then28, label %else29

then28:                                           ; preds = %continue27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue30

else29:                                           ; preds = %continue27
  br label %continue30

continue30:                                       ; preds = %else29, %then28
  %146 = call i1 @get_creg_bit(i1* %1, i64 11)
  br i1 %146, label %then31, label %else32

then31:                                           ; preds = %continue30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue33

else32:                                           ; preds = %continue30
  br label %continue33

continue33:                                       ; preds = %else32, %then31
  %147 = call i1 @get_creg_bit(i1* %1, i64 12)
  br i1 %147, label %then34, label %else35

then34:                                           ; preds = %continue33
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue36

else35:                                           ; preds = %continue33
  br label %continue36

continue36:                                       ; preds = %else35, %then34
  %148 = call i1 @get_creg_bit(i1* %1, i64 13)
  br i1 %148, label %then37, label %else38

then37:                                           ; preds = %continue36
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue39

else38:                                           ; preds = %continue36
  br label %continue39

continue39:                                       ; preds = %else38, %then37
  %149 = call i1 @get_creg_bit(i1* %1, i64 14)
  br i1 %149, label %then40, label %else41

then40:                                           ; preds = %continue39
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue42

else41:                                           ; preds = %continue39
  br label %continue42

continue42:                                       ; preds = %else41, %then40
  %150 = call i1 @get_creg_bit(i1* %1, i64 15)
  br i1 %150, label %then43, label %else44

then43:                                           ; preds = %continue42
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue45

else44:                                           ; preds = %continue42
  br label %continue45

continue45:                                       ; preds = %else44, %then43
  %151 = call i1 @get_creg_bit(i1* %1, i64 16)
  br i1 %151, label %then46, label %else47

then46:                                           ; preds = %continue45
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue48

else47:                                           ; preds = %continue45
  br label %continue48

continue48:                                       ; preds = %else47, %then46
  %152 = call i1 @get_creg_bit(i1* %1, i64 17)
  br i1 %152, label %then49, label %else50

then49:                                           ; preds = %continue48
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue51

else50:                                           ; preds = %continue48
  br label %continue51

continue51:                                       ; preds = %else50, %then49
  %153 = call i1 @get_creg_bit(i1* %1, i64 18)
  br i1 %153, label %then52, label %else53

then52:                                           ; preds = %continue51
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue54

else53:                                           ; preds = %continue51
  br label %continue54

continue54:                                       ; preds = %else53, %then52
  %154 = call i1 @get_creg_bit(i1* %1, i64 19)
  br i1 %154, label %then55, label %else56

then55:                                           ; preds = %continue54
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue57

else56:                                           ; preds = %continue54
  br label %continue57

continue57:                                       ; preds = %else56, %then55
  %155 = call i1 @get_creg_bit(i1* %1, i64 20)
  br i1 %155, label %then58, label %else59

then58:                                           ; preds = %continue57
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue60

else59:                                           ; preds = %continue57
  br label %continue60

continue60:                                       ; preds = %else59, %then58
  %156 = call i1 @get_creg_bit(i1* %1, i64 21)
  br i1 %156, label %then61, label %else62

then61:                                           ; preds = %continue60
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue63

else62:                                           ; preds = %continue60
  br label %continue63

continue63:                                       ; preds = %else62, %then61
  %157 = call i1 @get_creg_bit(i1* %1, i64 22)
  br i1 %157, label %then64, label %else65

then64:                                           ; preds = %continue63
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue66

else65:                                           ; preds = %continue63
  br label %continue66

continue66:                                       ; preds = %else65, %then64
  %158 = call i1 @get_creg_bit(i1* %1, i64 23)
  br i1 %158, label %then67, label %else68

then67:                                           ; preds = %continue66
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue69

else68:                                           ; preds = %continue66
  br label %continue69

continue69:                                       ; preds = %else68, %then67
  %159 = call i1 @get_creg_bit(i1* %1, i64 24)
  br i1 %159, label %then70, label %else71

then70:                                           ; preds = %continue69
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue72

else71:                                           ; preds = %continue69
  br label %continue72

continue72:                                       ; preds = %else71, %then70
  %160 = call i1 @get_creg_bit(i1* %1, i64 25)
  br i1 %160, label %then73, label %else74

then73:                                           ; preds = %continue72
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue75

else74:                                           ; preds = %continue72
  br label %continue75

continue75:                                       ; preds = %else74, %then73
  %161 = call i1 @get_creg_bit(i1* %1, i64 26)
  br i1 %161, label %then76, label %else77

then76:                                           ; preds = %continue75
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue78

else77:                                           ; preds = %continue75
  br label %continue78

continue78:                                       ; preds = %else77, %then76
  %162 = call i1 @get_creg_bit(i1* %1, i64 27)
  br i1 %162, label %then79, label %else80

then79:                                           ; preds = %continue78
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue81

else80:                                           ; preds = %continue78
  br label %continue81

continue81:                                       ; preds = %else80, %then79
  %163 = call i1 @get_creg_bit(i1* %1, i64 28)
  br i1 %163, label %then82, label %else83

then82:                                           ; preds = %continue81
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue84

else83:                                           ; preds = %continue81
  br label %continue84

continue84:                                       ; preds = %else83, %then82
  %164 = call i1 @get_creg_bit(i1* %1, i64 29)
  br i1 %164, label %then85, label %else86

then85:                                           ; preds = %continue84
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue87

else86:                                           ; preds = %continue84
  br label %continue87

continue87:                                       ; preds = %else86, %then85
  %165 = call i1 @get_creg_bit(i1* %1, i64 30)
  br i1 %165, label %then88, label %else89

then88:                                           ; preds = %continue87
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue90

else89:                                           ; preds = %continue87
  br label %continue90

continue90:                                       ; preds = %else89, %then88
  %166 = call i1 @get_creg_bit(i1* %1, i64 31)
  br i1 %166, label %then91, label %else92

then91:                                           ; preds = %continue90
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue93

else92:                                           ; preds = %continue90
  br label %continue93

continue93:                                       ; preds = %else92, %then91
  %167 = call i1 @get_creg_bit(i1* %1, i64 32)
  br i1 %167, label %then94, label %else95

then94:                                           ; preds = %continue93
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue96

else95:                                           ; preds = %continue93
  br label %continue96

continue96:                                       ; preds = %else95, %then94
  %168 = call i1 @get_creg_bit(i1* %1, i64 33)
  br i1 %168, label %then97, label %else98

then97:                                           ; preds = %continue96
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue99

else98:                                           ; preds = %continue96
  br label %continue99

continue99:                                       ; preds = %else98, %then97
  %169 = call i1 @get_creg_bit(i1* %1, i64 34)
  br i1 %169, label %then100, label %else101

then100:                                          ; preds = %continue99
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue102

else101:                                          ; preds = %continue99
  br label %continue102

continue102:                                      ; preds = %else101, %then100
  %170 = call i1 @get_creg_bit(i1* %1, i64 35)
  br i1 %170, label %then103, label %else104

then103:                                          ; preds = %continue102
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue105

else104:                                          ; preds = %continue102
  br label %continue105

continue105:                                      ; preds = %else104, %then103
  %171 = call i1 @get_creg_bit(i1* %1, i64 36)
  br i1 %171, label %then106, label %else107

then106:                                          ; preds = %continue105
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue108

else107:                                          ; preds = %continue105
  br label %continue108

continue108:                                      ; preds = %else107, %then106
  %172 = call i1 @get_creg_bit(i1* %1, i64 37)
  br i1 %172, label %then109, label %else110

then109:                                          ; preds = %continue108
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue111

else110:                                          ; preds = %continue108
  br label %continue111

continue111:                                      ; preds = %else110, %then109
  %173 = call i1 @get_creg_bit(i1* %1, i64 38)
  br i1 %173, label %then112, label %else113

then112:                                          ; preds = %continue111
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue114

else113:                                          ; preds = %continue111
  br label %continue114

continue114:                                      ; preds = %else113, %then112
  %174 = call i1 @get_creg_bit(i1* %1, i64 39)
  br i1 %174, label %then115, label %else116

then115:                                          ; preds = %continue114
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue117

else116:                                          ; preds = %continue114
  br label %continue117

continue117:                                      ; preds = %else116, %then115
  %175 = call i1 @get_creg_bit(i1* %1, i64 40)
  br i1 %175, label %then118, label %else119

then118:                                          ; preds = %continue117
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue120

else119:                                          ; preds = %continue117
  br label %continue120

continue120:                                      ; preds = %else119, %then118
  %176 = call i1 @get_creg_bit(i1* %1, i64 41)
  br i1 %176, label %then121, label %else122

then121:                                          ; preds = %continue120
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue123

else122:                                          ; preds = %continue120
  br label %continue123

continue123:                                      ; preds = %else122, %then121
  %177 = call i1 @get_creg_bit(i1* %1, i64 42)
  br i1 %177, label %then124, label %else125

then124:                                          ; preds = %continue123
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue126

else125:                                          ; preds = %continue123
  br label %continue126

continue126:                                      ; preds = %else125, %then124
  %178 = call i1 @get_creg_bit(i1* %1, i64 43)
  br i1 %178, label %then127, label %else128

then127:                                          ; preds = %continue126
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue129

else128:                                          ; preds = %continue126
  br label %continue129

continue129:                                      ; preds = %else128, %then127
  %179 = call i1 @get_creg_bit(i1* %1, i64 44)
  br i1 %179, label %then130, label %else131

then130:                                          ; preds = %continue129
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue132

else131:                                          ; preds = %continue129
  br label %continue132

continue132:                                      ; preds = %else131, %then130
  %180 = call i1 @get_creg_bit(i1* %1, i64 45)
  br i1 %180, label %then133, label %else134

then133:                                          ; preds = %continue132
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue135

else134:                                          ; preds = %continue132
  br label %continue135

continue135:                                      ; preds = %else134, %then133
  %181 = call i1 @get_creg_bit(i1* %1, i64 46)
  br i1 %181, label %then136, label %else137

then136:                                          ; preds = %continue135
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue138

else137:                                          ; preds = %continue135
  br label %continue138

continue138:                                      ; preds = %else137, %then136
  %182 = call i1 @get_creg_bit(i1* %1, i64 47)
  br i1 %182, label %then139, label %else140

then139:                                          ; preds = %continue138
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue141

else140:                                          ; preds = %continue138
  br label %continue141

continue141:                                      ; preds = %else140, %then139
  %183 = call i1 @get_creg_bit(i1* %1, i64 48)
  br i1 %183, label %then142, label %else143

then142:                                          ; preds = %continue141
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue144

else143:                                          ; preds = %continue141
  br label %continue144

continue144:                                      ; preds = %else143, %then142
  %184 = call i1 @get_creg_bit(i1* %1, i64 49)
  br i1 %184, label %then145, label %else146

then145:                                          ; preds = %continue144
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue147

else146:                                          ; preds = %continue144
  br label %continue147

continue147:                                      ; preds = %else146, %then145
  %185 = call i1 @get_creg_bit(i1* %1, i64 50)
  br i1 %185, label %then148, label %else149

then148:                                          ; preds = %continue147
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue150

else149:                                          ; preds = %continue147
  br label %continue150

continue150:                                      ; preds = %else149, %then148
  %186 = call i1 @get_creg_bit(i1* %1, i64 51)
  br i1 %186, label %then151, label %else152

then151:                                          ; preds = %continue150
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue153

else152:                                          ; preds = %continue150
  br label %continue153

continue153:                                      ; preds = %else152, %then151
  %187 = call i1 @get_creg_bit(i1* %1, i64 52)
  br i1 %187, label %then154, label %else155

then154:                                          ; preds = %continue153
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue156

else155:                                          ; preds = %continue153
  br label %continue156

continue156:                                      ; preds = %else155, %then154
  %188 = call i1 @get_creg_bit(i1* %1, i64 53)
  br i1 %188, label %then157, label %else158

then157:                                          ; preds = %continue156
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue159

else158:                                          ; preds = %continue156
  br label %continue159

continue159:                                      ; preds = %else158, %then157
  %189 = call i1 @get_creg_bit(i1* %1, i64 54)
  br i1 %189, label %then160, label %else161

then160:                                          ; preds = %continue159
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue162

else161:                                          ; preds = %continue159
  br label %continue162

continue162:                                      ; preds = %else161, %then160
  %190 = call i1 @get_creg_bit(i1* %1, i64 55)
  br i1 %190, label %then163, label %else164

then163:                                          ; preds = %continue162
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue165

else164:                                          ; preds = %continue162
  br label %continue165

continue165:                                      ; preds = %else164, %then163
  %191 = call i1 @get_creg_bit(i1* %1, i64 56)
  br i1 %191, label %then166, label %else167

then166:                                          ; preds = %continue165
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue168

else167:                                          ; preds = %continue165
  br label %continue168

continue168:                                      ; preds = %else167, %then166
  %192 = call i1 @get_creg_bit(i1* %1, i64 57)
  br i1 %192, label %then169, label %else170

then169:                                          ; preds = %continue168
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue171

else170:                                          ; preds = %continue168
  br label %continue171

continue171:                                      ; preds = %else170, %then169
  %193 = call i1 @get_creg_bit(i1* %1, i64 58)
  br i1 %193, label %then172, label %else173

then172:                                          ; preds = %continue171
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue174

else173:                                          ; preds = %continue171
  br label %continue174

continue174:                                      ; preds = %else173, %then172
  %194 = call i1 @get_creg_bit(i1* %1, i64 59)
  br i1 %194, label %then175, label %else176

then175:                                          ; preds = %continue174
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue177

else176:                                          ; preds = %continue174
  br label %continue177

continue177:                                      ; preds = %else176, %then175
  %195 = call i1 @get_creg_bit(i1* %1, i64 60)
  br i1 %195, label %then178, label %else179

then178:                                          ; preds = %continue177
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue180

else179:                                          ; preds = %continue177
  br label %continue180

continue180:                                      ; preds = %else179, %then178
  %196 = call i1 @get_creg_bit(i1* %1, i64 61)
  br i1 %196, label %then181, label %else182

then181:                                          ; preds = %continue180
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue183

else182:                                          ; preds = %continue180
  br label %continue183

continue183:                                      ; preds = %else182, %then181
  %197 = call i1 @get_creg_bit(i1* %1, i64 62)
  br i1 %197, label %then184, label %else185

then184:                                          ; preds = %continue183
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue186

else185:                                          ; preds = %continue183
  br label %continue186

continue186:                                      ; preds = %else185, %then184
  %198 = call i1 @get_creg_bit(i1* %1, i64 63)
  br i1 %198, label %then187, label %else188

then187:                                          ; preds = %continue186
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue189

else188:                                          ; preds = %continue186
  br label %continue189

continue189:                                      ; preds = %else188, %then187
  %199 = call i1 @get_creg_bit(i1* %2, i64 0)
  br i1 %199, label %then190, label %else191

then190:                                          ; preds = %continue189
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue192

else191:                                          ; preds = %continue189
  br label %continue192

continue192:                                      ; preds = %else191, %then190
  %200 = call i1 @get_creg_bit(i1* %2, i64 1)
  br i1 %200, label %then193, label %else194

then193:                                          ; preds = %continue192
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue195

else194:                                          ; preds = %continue192
  br label %continue195

continue195:                                      ; preds = %else194, %then193
  call void @__quantum__rt__tuple_start_record_output()
  %201 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %201, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  %202 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %202, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @1, i32 0, i32 0))
  %203 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %203, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg(%Qubit*, i1*, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "num_required_qubits"="7" "num_required_results"="7" "output_labeling_schema" "qir_profiles"="custom" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
