; ModuleID = 'test_pytket_qir_conditional_11'
source_filename = "test_pytket_qir_conditional_11"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [17 x i8] c"tk_SCRATCH_BIT_0\00"
@2 = internal constant [17 x i8] c"tk_SCRATCH_BIT_1\00"
@3 = internal constant [17 x i8] c"tk_SCRATCH_BIT_2\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i32 4)
  %1 = call i1* @create_creg(i32 32)
  %2 = call i1* @create_creg(i32 32)
  %3 = call i1* @create_creg(i32 2)
  %4 = call i32 @get_int_from_creg(i1* %0)
  %5 = icmp eq i32 1, %4
  call void @set_creg_bit(i1* %1, i32 0, i1 %5)
  %6 = call i32 @get_int_from_creg(i1* %0)
  %7 = icmp eq i32 2, %6
  call void @set_creg_bit(i1* %1, i32 1, i1 %7)
  %8 = call i32 @get_int_from_creg(i1* %0)
  %9 = icmp eq i32 2, %8
  call void @set_creg_bit(i1* %1, i32 2, i1 %9)
  %10 = call i32 @get_int_from_creg(i1* %0)
  %11 = icmp eq i32 3, %10
  call void @set_creg_bit(i1* %1, i32 3, i1 %11)
  %12 = call i32 @get_int_from_creg(i1* %0)
  %13 = icmp eq i32 4, %12
  call void @set_creg_bit(i1* %1, i32 4, i1 %13)
  %14 = call i32 @get_int_from_creg(i1* %0)
  %15 = icmp eq i32 4, %14
  call void @set_creg_bit(i1* %1, i32 5, i1 %15)
  %16 = call i32 @get_int_from_creg(i1* %0)
  %17 = icmp eq i32 1, %16
  call void @set_creg_bit(i1* %1, i32 6, i1 %17)
  %18 = call i32 @get_int_from_creg(i1* %0)
  %19 = icmp eq i32 2, %18
  call void @set_creg_bit(i1* %1, i32 7, i1 %19)
  %20 = call i32 @get_int_from_creg(i1* %0)
  %21 = icmp eq i32 2, %20
  call void @set_creg_bit(i1* %1, i32 8, i1 %21)
  %22 = call i32 @get_int_from_creg(i1* %0)
  %23 = icmp eq i32 3, %22
  call void @set_creg_bit(i1* %1, i32 9, i1 %23)
  %24 = call i32 @get_int_from_creg(i1* %0)
  %25 = icmp eq i32 4, %24
  call void @set_creg_bit(i1* %1, i32 10, i1 %25)
  %26 = call i32 @get_int_from_creg(i1* %0)
  %27 = icmp eq i32 4, %26
  call void @set_creg_bit(i1* %1, i32 11, i1 %27)
  %28 = call i32 @get_int_from_creg(i1* %0)
  %29 = icmp eq i32 1, %28
  call void @set_creg_bit(i1* %1, i32 12, i1 %29)
  %30 = call i32 @get_int_from_creg(i1* %0)
  %31 = icmp eq i32 2, %30
  call void @set_creg_bit(i1* %1, i32 13, i1 %31)
  %32 = call i32 @get_int_from_creg(i1* %0)
  %33 = icmp eq i32 2, %32
  call void @set_creg_bit(i1* %1, i32 14, i1 %33)
  %34 = call i32 @get_int_from_creg(i1* %0)
  %35 = icmp eq i32 3, %34
  call void @set_creg_bit(i1* %1, i32 15, i1 %35)
  %36 = call i32 @get_int_from_creg(i1* %0)
  %37 = icmp eq i32 4, %36
  call void @set_creg_bit(i1* %1, i32 16, i1 %37)
  %38 = call i32 @get_int_from_creg(i1* %0)
  %39 = icmp eq i32 4, %38
  call void @set_creg_bit(i1* %1, i32 17, i1 %39)
  %40 = call i32 @get_int_from_creg(i1* %0)
  %41 = icmp eq i32 1, %40
  call void @set_creg_bit(i1* %1, i32 18, i1 %41)
  %42 = call i32 @get_int_from_creg(i1* %0)
  %43 = icmp eq i32 2, %42
  call void @set_creg_bit(i1* %1, i32 19, i1 %43)
  %44 = call i32 @get_int_from_creg(i1* %0)
  %45 = icmp eq i32 2, %44
  call void @set_creg_bit(i1* %1, i32 20, i1 %45)
  %46 = call i32 @get_int_from_creg(i1* %0)
  %47 = icmp eq i32 3, %46
  call void @set_creg_bit(i1* %1, i32 21, i1 %47)
  %48 = call i32 @get_int_from_creg(i1* %0)
  %49 = icmp eq i32 4, %48
  call void @set_creg_bit(i1* %1, i32 22, i1 %49)
  %50 = call i32 @get_int_from_creg(i1* %0)
  %51 = icmp eq i32 4, %50
  call void @set_creg_bit(i1* %1, i32 23, i1 %51)
  %52 = call i32 @get_int_from_creg(i1* %0)
  %53 = icmp eq i32 1, %52
  call void @set_creg_bit(i1* %1, i32 24, i1 %53)
  %54 = call i32 @get_int_from_creg(i1* %0)
  %55 = icmp eq i32 2, %54
  call void @set_creg_bit(i1* %1, i32 25, i1 %55)
  %56 = call i32 @get_int_from_creg(i1* %0)
  %57 = icmp eq i32 2, %56
  call void @set_creg_bit(i1* %1, i32 26, i1 %57)
  %58 = call i32 @get_int_from_creg(i1* %0)
  %59 = icmp eq i32 3, %58
  call void @set_creg_bit(i1* %1, i32 27, i1 %59)
  %60 = call i32 @get_int_from_creg(i1* %0)
  %61 = icmp eq i32 4, %60
  call void @set_creg_bit(i1* %1, i32 28, i1 %61)
  %62 = call i32 @get_int_from_creg(i1* %0)
  %63 = icmp eq i32 4, %62
  call void @set_creg_bit(i1* %1, i32 29, i1 %63)
  %64 = call i32 @get_int_from_creg(i1* %0)
  %65 = icmp eq i32 1, %64
  call void @set_creg_bit(i1* %1, i32 30, i1 %65)
  %66 = call i32 @get_int_from_creg(i1* %0)
  %67 = icmp eq i32 2, %66
  call void @set_creg_bit(i1* %1, i32 31, i1 %67)
  %68 = call i32 @get_int_from_creg(i1* %0)
  %69 = icmp eq i32 2, %68
  call void @set_creg_bit(i1* %2, i32 0, i1 %69)
  %70 = call i32 @get_int_from_creg(i1* %0)
  %71 = icmp eq i32 3, %70
  call void @set_creg_bit(i1* %2, i32 1, i1 %71)
  %72 = call i32 @get_int_from_creg(i1* %0)
  %73 = icmp eq i32 4, %72
  call void @set_creg_bit(i1* %2, i32 2, i1 %73)
  %74 = call i32 @get_int_from_creg(i1* %0)
  %75 = icmp eq i32 4, %74
  call void @set_creg_bit(i1* %2, i32 3, i1 %75)
  %76 = call i32 @get_int_from_creg(i1* %0)
  %77 = icmp eq i32 1, %76
  call void @set_creg_bit(i1* %2, i32 4, i1 %77)
  %78 = call i32 @get_int_from_creg(i1* %0)
  %79 = icmp eq i32 2, %78
  call void @set_creg_bit(i1* %2, i32 5, i1 %79)
  %80 = call i32 @get_int_from_creg(i1* %0)
  %81 = icmp eq i32 2, %80
  call void @set_creg_bit(i1* %2, i32 6, i1 %81)
  %82 = call i32 @get_int_from_creg(i1* %0)
  %83 = icmp eq i32 3, %82
  call void @set_creg_bit(i1* %2, i32 7, i1 %83)
  %84 = call i32 @get_int_from_creg(i1* %0)
  %85 = icmp eq i32 4, %84
  call void @set_creg_bit(i1* %2, i32 8, i1 %85)
  %86 = call i32 @get_int_from_creg(i1* %0)
  %87 = icmp eq i32 4, %86
  call void @set_creg_bit(i1* %2, i32 9, i1 %87)
  %88 = call i32 @get_int_from_creg(i1* %0)
  %89 = icmp eq i32 1, %88
  call void @set_creg_bit(i1* %2, i32 10, i1 %89)
  %90 = call i32 @get_int_from_creg(i1* %0)
  %91 = icmp eq i32 2, %90
  call void @set_creg_bit(i1* %2, i32 11, i1 %91)
  %92 = call i32 @get_int_from_creg(i1* %0)
  %93 = icmp eq i32 2, %92
  call void @set_creg_bit(i1* %2, i32 12, i1 %93)
  %94 = call i32 @get_int_from_creg(i1* %0)
  %95 = icmp eq i32 3, %94
  call void @set_creg_bit(i1* %2, i32 13, i1 %95)
  %96 = call i32 @get_int_from_creg(i1* %0)
  %97 = icmp eq i32 4, %96
  call void @set_creg_bit(i1* %2, i32 14, i1 %97)
  %98 = call i32 @get_int_from_creg(i1* %0)
  %99 = icmp eq i32 4, %98
  call void @set_creg_bit(i1* %2, i32 15, i1 %99)
  %100 = call i32 @get_int_from_creg(i1* %0)
  %101 = icmp eq i32 1, %100
  call void @set_creg_bit(i1* %2, i32 16, i1 %101)
  %102 = call i32 @get_int_from_creg(i1* %0)
  %103 = icmp eq i32 2, %102
  call void @set_creg_bit(i1* %2, i32 17, i1 %103)
  %104 = call i32 @get_int_from_creg(i1* %0)
  %105 = icmp eq i32 2, %104
  call void @set_creg_bit(i1* %2, i32 18, i1 %105)
  %106 = call i32 @get_int_from_creg(i1* %0)
  %107 = icmp eq i32 3, %106
  call void @set_creg_bit(i1* %2, i32 19, i1 %107)
  %108 = call i32 @get_int_from_creg(i1* %0)
  %109 = icmp eq i32 4, %108
  call void @set_creg_bit(i1* %2, i32 20, i1 %109)
  %110 = call i32 @get_int_from_creg(i1* %0)
  %111 = icmp eq i32 4, %110
  call void @set_creg_bit(i1* %2, i32 21, i1 %111)
  %112 = call i32 @get_int_from_creg(i1* %0)
  %113 = icmp eq i32 1, %112
  call void @set_creg_bit(i1* %2, i32 22, i1 %113)
  %114 = call i32 @get_int_from_creg(i1* %0)
  %115 = icmp eq i32 2, %114
  call void @set_creg_bit(i1* %2, i32 23, i1 %115)
  %116 = call i32 @get_int_from_creg(i1* %0)
  %117 = icmp eq i32 2, %116
  call void @set_creg_bit(i1* %2, i32 24, i1 %117)
  %118 = call i32 @get_int_from_creg(i1* %0)
  %119 = icmp eq i32 3, %118
  call void @set_creg_bit(i1* %2, i32 25, i1 %119)
  %120 = call i32 @get_int_from_creg(i1* %0)
  %121 = icmp eq i32 4, %120
  call void @set_creg_bit(i1* %2, i32 26, i1 %121)
  %122 = call i32 @get_int_from_creg(i1* %0)
  %123 = icmp eq i32 4, %122
  call void @set_creg_bit(i1* %2, i32 27, i1 %123)
  %124 = call i32 @get_int_from_creg(i1* %0)
  %125 = icmp eq i32 1, %124
  call void @set_creg_bit(i1* %2, i32 28, i1 %125)
  %126 = call i32 @get_int_from_creg(i1* %0)
  %127 = icmp eq i32 2, %126
  call void @set_creg_bit(i1* %2, i32 29, i1 %127)
  %128 = call i32 @get_int_from_creg(i1* %0)
  %129 = icmp eq i32 2, %128
  call void @set_creg_bit(i1* %2, i32 30, i1 %129)
  %130 = call i32 @get_int_from_creg(i1* %0)
  %131 = icmp eq i32 3, %130
  call void @set_creg_bit(i1* %2, i32 31, i1 %131)
  %132 = call i32 @get_int_from_creg(i1* %0)
  %133 = icmp eq i32 4, %132
  call void @set_creg_bit(i1* %3, i32 0, i1 %133)
  %134 = call i32 @get_int_from_creg(i1* %0)
  %135 = icmp eq i32 4, %134
  call void @set_creg_bit(i1* %3, i32 1, i1 %135)
  %136 = call i1 @get_creg_bit(i1* %1, i32 0)
  br i1 %136, label %then, label %else

then:                                             ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue

else:                                             ; preds = %entry
  br label %continue

continue:                                         ; preds = %else, %then
  %137 = call i1 @get_creg_bit(i1* %1, i32 1)
  br i1 %137, label %then1, label %else2

then1:                                            ; preds = %continue
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue3

else2:                                            ; preds = %continue
  br label %continue3

continue3:                                        ; preds = %else2, %then1
  %138 = call i1 @get_creg_bit(i1* %1, i32 2)
  br i1 %138, label %then4, label %else5

then4:                                            ; preds = %continue3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue6

else5:                                            ; preds = %continue3
  br label %continue6

continue6:                                        ; preds = %else5, %then4
  %139 = call i1 @get_creg_bit(i1* %1, i32 3)
  br i1 %139, label %then7, label %else8

then7:                                            ; preds = %continue6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue9

else8:                                            ; preds = %continue6
  br label %continue9

continue9:                                        ; preds = %else8, %then7
  %140 = call i1 @get_creg_bit(i1* %1, i32 4)
  br i1 %140, label %then10, label %else11

then10:                                           ; preds = %continue9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue12

else11:                                           ; preds = %continue9
  br label %continue12

continue12:                                       ; preds = %else11, %then10
  %141 = call i1 @get_creg_bit(i1* %1, i32 5)
  br i1 %141, label %then13, label %else14

then13:                                           ; preds = %continue12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue15

else14:                                           ; preds = %continue12
  br label %continue15

continue15:                                       ; preds = %else14, %then13
  %142 = call i1 @get_creg_bit(i1* %1, i32 6)
  br i1 %142, label %then16, label %else17

then16:                                           ; preds = %continue15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue18

else17:                                           ; preds = %continue15
  br label %continue18

continue18:                                       ; preds = %else17, %then16
  %143 = call i1 @get_creg_bit(i1* %1, i32 7)
  br i1 %143, label %then19, label %else20

then19:                                           ; preds = %continue18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue21

else20:                                           ; preds = %continue18
  br label %continue21

continue21:                                       ; preds = %else20, %then19
  %144 = call i1 @get_creg_bit(i1* %1, i32 8)
  br i1 %144, label %then22, label %else23

then22:                                           ; preds = %continue21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue24

else23:                                           ; preds = %continue21
  br label %continue24

continue24:                                       ; preds = %else23, %then22
  %145 = call i1 @get_creg_bit(i1* %1, i32 9)
  br i1 %145, label %then25, label %else26

then25:                                           ; preds = %continue24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue27

else26:                                           ; preds = %continue24
  br label %continue27

continue27:                                       ; preds = %else26, %then25
  %146 = call i1 @get_creg_bit(i1* %1, i32 10)
  br i1 %146, label %then28, label %else29

then28:                                           ; preds = %continue27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue30

else29:                                           ; preds = %continue27
  br label %continue30

continue30:                                       ; preds = %else29, %then28
  %147 = call i1 @get_creg_bit(i1* %1, i32 11)
  br i1 %147, label %then31, label %else32

then31:                                           ; preds = %continue30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue33

else32:                                           ; preds = %continue30
  br label %continue33

continue33:                                       ; preds = %else32, %then31
  %148 = call i1 @get_creg_bit(i1* %1, i32 12)
  br i1 %148, label %then34, label %else35

then34:                                           ; preds = %continue33
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue36

else35:                                           ; preds = %continue33
  br label %continue36

continue36:                                       ; preds = %else35, %then34
  %149 = call i1 @get_creg_bit(i1* %1, i32 13)
  br i1 %149, label %then37, label %else38

then37:                                           ; preds = %continue36
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue39

else38:                                           ; preds = %continue36
  br label %continue39

continue39:                                       ; preds = %else38, %then37
  %150 = call i1 @get_creg_bit(i1* %1, i32 14)
  br i1 %150, label %then40, label %else41

then40:                                           ; preds = %continue39
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue42

else41:                                           ; preds = %continue39
  br label %continue42

continue42:                                       ; preds = %else41, %then40
  %151 = call i1 @get_creg_bit(i1* %1, i32 15)
  br i1 %151, label %then43, label %else44

then43:                                           ; preds = %continue42
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue45

else44:                                           ; preds = %continue42
  br label %continue45

continue45:                                       ; preds = %else44, %then43
  %152 = call i1 @get_creg_bit(i1* %1, i32 16)
  br i1 %152, label %then46, label %else47

then46:                                           ; preds = %continue45
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue48

else47:                                           ; preds = %continue45
  br label %continue48

continue48:                                       ; preds = %else47, %then46
  %153 = call i1 @get_creg_bit(i1* %1, i32 17)
  br i1 %153, label %then49, label %else50

then49:                                           ; preds = %continue48
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue51

else50:                                           ; preds = %continue48
  br label %continue51

continue51:                                       ; preds = %else50, %then49
  %154 = call i1 @get_creg_bit(i1* %1, i32 18)
  br i1 %154, label %then52, label %else53

then52:                                           ; preds = %continue51
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue54

else53:                                           ; preds = %continue51
  br label %continue54

continue54:                                       ; preds = %else53, %then52
  %155 = call i1 @get_creg_bit(i1* %1, i32 19)
  br i1 %155, label %then55, label %else56

then55:                                           ; preds = %continue54
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue57

else56:                                           ; preds = %continue54
  br label %continue57

continue57:                                       ; preds = %else56, %then55
  %156 = call i1 @get_creg_bit(i1* %1, i32 20)
  br i1 %156, label %then58, label %else59

then58:                                           ; preds = %continue57
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue60

else59:                                           ; preds = %continue57
  br label %continue60

continue60:                                       ; preds = %else59, %then58
  %157 = call i1 @get_creg_bit(i1* %1, i32 21)
  br i1 %157, label %then61, label %else62

then61:                                           ; preds = %continue60
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue63

else62:                                           ; preds = %continue60
  br label %continue63

continue63:                                       ; preds = %else62, %then61
  %158 = call i1 @get_creg_bit(i1* %1, i32 22)
  br i1 %158, label %then64, label %else65

then64:                                           ; preds = %continue63
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue66

else65:                                           ; preds = %continue63
  br label %continue66

continue66:                                       ; preds = %else65, %then64
  %159 = call i1 @get_creg_bit(i1* %1, i32 23)
  br i1 %159, label %then67, label %else68

then67:                                           ; preds = %continue66
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue69

else68:                                           ; preds = %continue66
  br label %continue69

continue69:                                       ; preds = %else68, %then67
  %160 = call i1 @get_creg_bit(i1* %1, i32 24)
  br i1 %160, label %then70, label %else71

then70:                                           ; preds = %continue69
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue72

else71:                                           ; preds = %continue69
  br label %continue72

continue72:                                       ; preds = %else71, %then70
  %161 = call i1 @get_creg_bit(i1* %1, i32 25)
  br i1 %161, label %then73, label %else74

then73:                                           ; preds = %continue72
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue75

else74:                                           ; preds = %continue72
  br label %continue75

continue75:                                       ; preds = %else74, %then73
  %162 = call i1 @get_creg_bit(i1* %1, i32 26)
  br i1 %162, label %then76, label %else77

then76:                                           ; preds = %continue75
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue78

else77:                                           ; preds = %continue75
  br label %continue78

continue78:                                       ; preds = %else77, %then76
  %163 = call i1 @get_creg_bit(i1* %1, i32 27)
  br i1 %163, label %then79, label %else80

then79:                                           ; preds = %continue78
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue81

else80:                                           ; preds = %continue78
  br label %continue81

continue81:                                       ; preds = %else80, %then79
  %164 = call i1 @get_creg_bit(i1* %1, i32 28)
  br i1 %164, label %then82, label %else83

then82:                                           ; preds = %continue81
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue84

else83:                                           ; preds = %continue81
  br label %continue84

continue84:                                       ; preds = %else83, %then82
  %165 = call i1 @get_creg_bit(i1* %1, i32 29)
  br i1 %165, label %then85, label %else86

then85:                                           ; preds = %continue84
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue87

else86:                                           ; preds = %continue84
  br label %continue87

continue87:                                       ; preds = %else86, %then85
  %166 = call i1 @get_creg_bit(i1* %1, i32 30)
  br i1 %166, label %then88, label %else89

then88:                                           ; preds = %continue87
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue90

else89:                                           ; preds = %continue87
  br label %continue90

continue90:                                       ; preds = %else89, %then88
  %167 = call i1 @get_creg_bit(i1* %1, i32 31)
  br i1 %167, label %then91, label %else92

then91:                                           ; preds = %continue90
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue93

else92:                                           ; preds = %continue90
  br label %continue93

continue93:                                       ; preds = %else92, %then91
  %168 = call i1 @get_creg_bit(i1* %2, i32 0)
  br i1 %168, label %then94, label %else95

then94:                                           ; preds = %continue93
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue96

else95:                                           ; preds = %continue93
  br label %continue96

continue96:                                       ; preds = %else95, %then94
  %169 = call i1 @get_creg_bit(i1* %2, i32 1)
  br i1 %169, label %then97, label %else98

then97:                                           ; preds = %continue96
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue99

else98:                                           ; preds = %continue96
  br label %continue99

continue99:                                       ; preds = %else98, %then97
  %170 = call i1 @get_creg_bit(i1* %2, i32 2)
  br i1 %170, label %then100, label %else101

then100:                                          ; preds = %continue99
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue102

else101:                                          ; preds = %continue99
  br label %continue102

continue102:                                      ; preds = %else101, %then100
  %171 = call i1 @get_creg_bit(i1* %2, i32 3)
  br i1 %171, label %then103, label %else104

then103:                                          ; preds = %continue102
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue105

else104:                                          ; preds = %continue102
  br label %continue105

continue105:                                      ; preds = %else104, %then103
  %172 = call i1 @get_creg_bit(i1* %2, i32 4)
  br i1 %172, label %then106, label %else107

then106:                                          ; preds = %continue105
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue108

else107:                                          ; preds = %continue105
  br label %continue108

continue108:                                      ; preds = %else107, %then106
  %173 = call i1 @get_creg_bit(i1* %2, i32 5)
  br i1 %173, label %then109, label %else110

then109:                                          ; preds = %continue108
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue111

else110:                                          ; preds = %continue108
  br label %continue111

continue111:                                      ; preds = %else110, %then109
  %174 = call i1 @get_creg_bit(i1* %2, i32 6)
  br i1 %174, label %then112, label %else113

then112:                                          ; preds = %continue111
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue114

else113:                                          ; preds = %continue111
  br label %continue114

continue114:                                      ; preds = %else113, %then112
  %175 = call i1 @get_creg_bit(i1* %2, i32 7)
  br i1 %175, label %then115, label %else116

then115:                                          ; preds = %continue114
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue117

else116:                                          ; preds = %continue114
  br label %continue117

continue117:                                      ; preds = %else116, %then115
  %176 = call i1 @get_creg_bit(i1* %2, i32 8)
  br i1 %176, label %then118, label %else119

then118:                                          ; preds = %continue117
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue120

else119:                                          ; preds = %continue117
  br label %continue120

continue120:                                      ; preds = %else119, %then118
  %177 = call i1 @get_creg_bit(i1* %2, i32 9)
  br i1 %177, label %then121, label %else122

then121:                                          ; preds = %continue120
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue123

else122:                                          ; preds = %continue120
  br label %continue123

continue123:                                      ; preds = %else122, %then121
  %178 = call i1 @get_creg_bit(i1* %2, i32 10)
  br i1 %178, label %then124, label %else125

then124:                                          ; preds = %continue123
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue126

else125:                                          ; preds = %continue123
  br label %continue126

continue126:                                      ; preds = %else125, %then124
  %179 = call i1 @get_creg_bit(i1* %2, i32 11)
  br i1 %179, label %then127, label %else128

then127:                                          ; preds = %continue126
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue129

else128:                                          ; preds = %continue126
  br label %continue129

continue129:                                      ; preds = %else128, %then127
  %180 = call i1 @get_creg_bit(i1* %2, i32 12)
  br i1 %180, label %then130, label %else131

then130:                                          ; preds = %continue129
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue132

else131:                                          ; preds = %continue129
  br label %continue132

continue132:                                      ; preds = %else131, %then130
  %181 = call i1 @get_creg_bit(i1* %2, i32 13)
  br i1 %181, label %then133, label %else134

then133:                                          ; preds = %continue132
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue135

else134:                                          ; preds = %continue132
  br label %continue135

continue135:                                      ; preds = %else134, %then133
  %182 = call i1 @get_creg_bit(i1* %2, i32 14)
  br i1 %182, label %then136, label %else137

then136:                                          ; preds = %continue135
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue138

else137:                                          ; preds = %continue135
  br label %continue138

continue138:                                      ; preds = %else137, %then136
  %183 = call i1 @get_creg_bit(i1* %2, i32 15)
  br i1 %183, label %then139, label %else140

then139:                                          ; preds = %continue138
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue141

else140:                                          ; preds = %continue138
  br label %continue141

continue141:                                      ; preds = %else140, %then139
  %184 = call i1 @get_creg_bit(i1* %2, i32 16)
  br i1 %184, label %then142, label %else143

then142:                                          ; preds = %continue141
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue144

else143:                                          ; preds = %continue141
  br label %continue144

continue144:                                      ; preds = %else143, %then142
  %185 = call i1 @get_creg_bit(i1* %2, i32 17)
  br i1 %185, label %then145, label %else146

then145:                                          ; preds = %continue144
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue147

else146:                                          ; preds = %continue144
  br label %continue147

continue147:                                      ; preds = %else146, %then145
  %186 = call i1 @get_creg_bit(i1* %2, i32 18)
  br i1 %186, label %then148, label %else149

then148:                                          ; preds = %continue147
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue150

else149:                                          ; preds = %continue147
  br label %continue150

continue150:                                      ; preds = %else149, %then148
  %187 = call i1 @get_creg_bit(i1* %2, i32 19)
  br i1 %187, label %then151, label %else152

then151:                                          ; preds = %continue150
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue153

else152:                                          ; preds = %continue150
  br label %continue153

continue153:                                      ; preds = %else152, %then151
  %188 = call i1 @get_creg_bit(i1* %2, i32 20)
  br i1 %188, label %then154, label %else155

then154:                                          ; preds = %continue153
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue156

else155:                                          ; preds = %continue153
  br label %continue156

continue156:                                      ; preds = %else155, %then154
  %189 = call i1 @get_creg_bit(i1* %2, i32 21)
  br i1 %189, label %then157, label %else158

then157:                                          ; preds = %continue156
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue159

else158:                                          ; preds = %continue156
  br label %continue159

continue159:                                      ; preds = %else158, %then157
  %190 = call i1 @get_creg_bit(i1* %2, i32 22)
  br i1 %190, label %then160, label %else161

then160:                                          ; preds = %continue159
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue162

else161:                                          ; preds = %continue159
  br label %continue162

continue162:                                      ; preds = %else161, %then160
  %191 = call i1 @get_creg_bit(i1* %2, i32 23)
  br i1 %191, label %then163, label %else164

then163:                                          ; preds = %continue162
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue165

else164:                                          ; preds = %continue162
  br label %continue165

continue165:                                      ; preds = %else164, %then163
  %192 = call i1 @get_creg_bit(i1* %2, i32 24)
  br i1 %192, label %then166, label %else167

then166:                                          ; preds = %continue165
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue168

else167:                                          ; preds = %continue165
  br label %continue168

continue168:                                      ; preds = %else167, %then166
  %193 = call i1 @get_creg_bit(i1* %2, i32 25)
  br i1 %193, label %then169, label %else170

then169:                                          ; preds = %continue168
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue171

else170:                                          ; preds = %continue168
  br label %continue171

continue171:                                      ; preds = %else170, %then169
  %194 = call i1 @get_creg_bit(i1* %2, i32 26)
  br i1 %194, label %then172, label %else173

then172:                                          ; preds = %continue171
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue174

else173:                                          ; preds = %continue171
  br label %continue174

continue174:                                      ; preds = %else173, %then172
  %195 = call i1 @get_creg_bit(i1* %2, i32 27)
  br i1 %195, label %then175, label %else176

then175:                                          ; preds = %continue174
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue177

else176:                                          ; preds = %continue174
  br label %continue177

continue177:                                      ; preds = %else176, %then175
  %196 = call i1 @get_creg_bit(i1* %2, i32 28)
  br i1 %196, label %then178, label %else179

then178:                                          ; preds = %continue177
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue180

else179:                                          ; preds = %continue177
  br label %continue180

continue180:                                      ; preds = %else179, %then178
  %197 = call i1 @get_creg_bit(i1* %2, i32 29)
  br i1 %197, label %then181, label %else182

then181:                                          ; preds = %continue180
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue183

else182:                                          ; preds = %continue180
  br label %continue183

continue183:                                      ; preds = %else182, %then181
  %198 = call i1 @get_creg_bit(i1* %2, i32 30)
  br i1 %198, label %then184, label %else185

then184:                                          ; preds = %continue183
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue186

else185:                                          ; preds = %continue183
  br label %continue186

continue186:                                      ; preds = %else185, %then184
  %199 = call i1 @get_creg_bit(i1* %2, i32 31)
  br i1 %199, label %then187, label %else188

then187:                                          ; preds = %continue186
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue189

else188:                                          ; preds = %continue186
  br label %continue189

continue189:                                      ; preds = %else188, %then187
  %200 = call i1 @get_creg_bit(i1* %3, i32 0)
  br i1 %200, label %then190, label %else191

then190:                                          ; preds = %continue189
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue192

else191:                                          ; preds = %continue189
  br label %continue192

continue192:                                      ; preds = %else191, %then190
  %201 = call i1 @get_creg_bit(i1* %3, i32 1)
  br i1 %201, label %then193, label %else194

then193:                                          ; preds = %continue192
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue195

else194:                                          ; preds = %continue192
  br label %continue195

continue195:                                      ; preds = %else194, %then193
  call void @__quantum__rt__tuple_start_record_output()
  %202 = call i32 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i32 %202, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @0, i32 0, i32 0))
  %203 = call i32 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i32 %203, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @1, i32 0, i32 0))
  %204 = call i32 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i32 %204, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @2, i32 0, i32 0))
  %205 = call i32 @get_int_from_creg(i1* %3)
  call void @__quantum__rt__int_record_output(i32 %205, i8* getelementptr inbounds ([17 x i8], [17 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare i1 @get_creg_bit(i1*, i32)

declare void @set_creg_bit(i1*, i32, i1)

declare void @set_creg_to_int(i1*, i32)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i1* @create_creg(i32)

declare i32 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i32)

declare void @__quantum__rt__int_record_output(i32, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
