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
  br i1 %135, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %136 = call i1 @get_creg_bit(i1* %1, i64 1)
  br i1 %136, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %137 = call i1 @get_creg_bit(i1* %1, i64 2)
  br i1 %137, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %138 = call i1 @get_creg_bit(i1* %1, i64 3)
  br i1 %138, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %139 = call i1 @get_creg_bit(i1* %1, i64 4)
  br i1 %139, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %140 = call i1 @get_creg_bit(i1* %1, i64 5)
  br i1 %140, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %141 = call i1 @get_creg_bit(i1* %1, i64 6)
  br i1 %141, label %condb6, label %contb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %142 = call i1 @get_creg_bit(i1* %1, i64 7)
  br i1 %142, label %condb7, label %contb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %143 = call i1 @get_creg_bit(i1* %1, i64 8)
  br i1 %143, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %144 = call i1 @get_creg_bit(i1* %1, i64 9)
  br i1 %144, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %145 = call i1 @get_creg_bit(i1* %1, i64 10)
  br i1 %145, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %146 = call i1 @get_creg_bit(i1* %1, i64 11)
  br i1 %146, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  %147 = call i1 @get_creg_bit(i1* %1, i64 12)
  br i1 %147, label %condb12, label %contb12

condb12:                                          ; preds = %contb11
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb12

contb12:                                          ; preds = %condb12, %contb11
  %148 = call i1 @get_creg_bit(i1* %1, i64 13)
  br i1 %148, label %condb13, label %contb13

condb13:                                          ; preds = %contb12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb13

contb13:                                          ; preds = %condb13, %contb12
  %149 = call i1 @get_creg_bit(i1* %1, i64 14)
  br i1 %149, label %condb14, label %contb14

condb14:                                          ; preds = %contb13
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb14

contb14:                                          ; preds = %condb14, %contb13
  %150 = call i1 @get_creg_bit(i1* %1, i64 15)
  br i1 %150, label %condb15, label %contb15

condb15:                                          ; preds = %contb14
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb15

contb15:                                          ; preds = %condb15, %contb14
  %151 = call i1 @get_creg_bit(i1* %1, i64 16)
  br i1 %151, label %condb16, label %contb16

condb16:                                          ; preds = %contb15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb16

contb16:                                          ; preds = %condb16, %contb15
  %152 = call i1 @get_creg_bit(i1* %1, i64 17)
  br i1 %152, label %condb17, label %contb17

condb17:                                          ; preds = %contb16
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb17

contb17:                                          ; preds = %condb17, %contb16
  %153 = call i1 @get_creg_bit(i1* %1, i64 18)
  br i1 %153, label %condb18, label %contb18

condb18:                                          ; preds = %contb17
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb18

contb18:                                          ; preds = %condb18, %contb17
  %154 = call i1 @get_creg_bit(i1* %1, i64 19)
  br i1 %154, label %condb19, label %contb19

condb19:                                          ; preds = %contb18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb19

contb19:                                          ; preds = %condb19, %contb18
  %155 = call i1 @get_creg_bit(i1* %1, i64 20)
  br i1 %155, label %condb20, label %contb20

condb20:                                          ; preds = %contb19
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb20

contb20:                                          ; preds = %condb20, %contb19
  %156 = call i1 @get_creg_bit(i1* %1, i64 21)
  br i1 %156, label %condb21, label %contb21

condb21:                                          ; preds = %contb20
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb21

contb21:                                          ; preds = %condb21, %contb20
  %157 = call i1 @get_creg_bit(i1* %1, i64 22)
  br i1 %157, label %condb22, label %contb22

condb22:                                          ; preds = %contb21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb22

contb22:                                          ; preds = %condb22, %contb21
  %158 = call i1 @get_creg_bit(i1* %1, i64 23)
  br i1 %158, label %condb23, label %contb23

condb23:                                          ; preds = %contb22
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb23

contb23:                                          ; preds = %condb23, %contb22
  %159 = call i1 @get_creg_bit(i1* %1, i64 24)
  br i1 %159, label %condb24, label %contb24

condb24:                                          ; preds = %contb23
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb24

contb24:                                          ; preds = %condb24, %contb23
  %160 = call i1 @get_creg_bit(i1* %1, i64 25)
  br i1 %160, label %condb25, label %contb25

condb25:                                          ; preds = %contb24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb25

contb25:                                          ; preds = %condb25, %contb24
  %161 = call i1 @get_creg_bit(i1* %1, i64 26)
  br i1 %161, label %condb26, label %contb26

condb26:                                          ; preds = %contb25
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb26

contb26:                                          ; preds = %condb26, %contb25
  %162 = call i1 @get_creg_bit(i1* %1, i64 27)
  br i1 %162, label %condb27, label %contb27

condb27:                                          ; preds = %contb26
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb27

contb27:                                          ; preds = %condb27, %contb26
  %163 = call i1 @get_creg_bit(i1* %1, i64 28)
  br i1 %163, label %condb28, label %contb28

condb28:                                          ; preds = %contb27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb28

contb28:                                          ; preds = %condb28, %contb27
  %164 = call i1 @get_creg_bit(i1* %1, i64 29)
  br i1 %164, label %condb29, label %contb29

condb29:                                          ; preds = %contb28
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb29

contb29:                                          ; preds = %condb29, %contb28
  %165 = call i1 @get_creg_bit(i1* %1, i64 30)
  br i1 %165, label %condb30, label %contb30

condb30:                                          ; preds = %contb29
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb30

contb30:                                          ; preds = %condb30, %contb29
  %166 = call i1 @get_creg_bit(i1* %1, i64 31)
  br i1 %166, label %condb31, label %contb31

condb31:                                          ; preds = %contb30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb31

contb31:                                          ; preds = %condb31, %contb30
  %167 = call i1 @get_creg_bit(i1* %1, i64 32)
  br i1 %167, label %condb32, label %contb32

condb32:                                          ; preds = %contb31
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb32

contb32:                                          ; preds = %condb32, %contb31
  %168 = call i1 @get_creg_bit(i1* %1, i64 33)
  br i1 %168, label %condb33, label %contb33

condb33:                                          ; preds = %contb32
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb33

contb33:                                          ; preds = %condb33, %contb32
  %169 = call i1 @get_creg_bit(i1* %1, i64 34)
  br i1 %169, label %condb34, label %contb34

condb34:                                          ; preds = %contb33
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb34

contb34:                                          ; preds = %condb34, %contb33
  %170 = call i1 @get_creg_bit(i1* %1, i64 35)
  br i1 %170, label %condb35, label %contb35

condb35:                                          ; preds = %contb34
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb35

contb35:                                          ; preds = %condb35, %contb34
  %171 = call i1 @get_creg_bit(i1* %1, i64 36)
  br i1 %171, label %condb36, label %contb36

condb36:                                          ; preds = %contb35
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb36

contb36:                                          ; preds = %condb36, %contb35
  %172 = call i1 @get_creg_bit(i1* %1, i64 37)
  br i1 %172, label %condb37, label %contb37

condb37:                                          ; preds = %contb36
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb37

contb37:                                          ; preds = %condb37, %contb36
  %173 = call i1 @get_creg_bit(i1* %1, i64 38)
  br i1 %173, label %condb38, label %contb38

condb38:                                          ; preds = %contb37
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb38

contb38:                                          ; preds = %condb38, %contb37
  %174 = call i1 @get_creg_bit(i1* %1, i64 39)
  br i1 %174, label %condb39, label %contb39

condb39:                                          ; preds = %contb38
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb39

contb39:                                          ; preds = %condb39, %contb38
  %175 = call i1 @get_creg_bit(i1* %1, i64 40)
  br i1 %175, label %condb40, label %contb40

condb40:                                          ; preds = %contb39
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb40

contb40:                                          ; preds = %condb40, %contb39
  %176 = call i1 @get_creg_bit(i1* %1, i64 41)
  br i1 %176, label %condb41, label %contb41

condb41:                                          ; preds = %contb40
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb41

contb41:                                          ; preds = %condb41, %contb40
  %177 = call i1 @get_creg_bit(i1* %1, i64 42)
  br i1 %177, label %condb42, label %contb42

condb42:                                          ; preds = %contb41
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb42

contb42:                                          ; preds = %condb42, %contb41
  %178 = call i1 @get_creg_bit(i1* %1, i64 43)
  br i1 %178, label %condb43, label %contb43

condb43:                                          ; preds = %contb42
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb43

contb43:                                          ; preds = %condb43, %contb42
  %179 = call i1 @get_creg_bit(i1* %1, i64 44)
  br i1 %179, label %condb44, label %contb44

condb44:                                          ; preds = %contb43
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb44

contb44:                                          ; preds = %condb44, %contb43
  %180 = call i1 @get_creg_bit(i1* %1, i64 45)
  br i1 %180, label %condb45, label %contb45

condb45:                                          ; preds = %contb44
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb45

contb45:                                          ; preds = %condb45, %contb44
  %181 = call i1 @get_creg_bit(i1* %1, i64 46)
  br i1 %181, label %condb46, label %contb46

condb46:                                          ; preds = %contb45
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb46

contb46:                                          ; preds = %condb46, %contb45
  %182 = call i1 @get_creg_bit(i1* %1, i64 47)
  br i1 %182, label %condb47, label %contb47

condb47:                                          ; preds = %contb46
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb47

contb47:                                          ; preds = %condb47, %contb46
  %183 = call i1 @get_creg_bit(i1* %1, i64 48)
  br i1 %183, label %condb48, label %contb48

condb48:                                          ; preds = %contb47
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb48

contb48:                                          ; preds = %condb48, %contb47
  %184 = call i1 @get_creg_bit(i1* %1, i64 49)
  br i1 %184, label %condb49, label %contb49

condb49:                                          ; preds = %contb48
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb49

contb49:                                          ; preds = %condb49, %contb48
  %185 = call i1 @get_creg_bit(i1* %1, i64 50)
  br i1 %185, label %condb50, label %contb50

condb50:                                          ; preds = %contb49
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb50

contb50:                                          ; preds = %condb50, %contb49
  %186 = call i1 @get_creg_bit(i1* %1, i64 51)
  br i1 %186, label %condb51, label %contb51

condb51:                                          ; preds = %contb50
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb51

contb51:                                          ; preds = %condb51, %contb50
  %187 = call i1 @get_creg_bit(i1* %1, i64 52)
  br i1 %187, label %condb52, label %contb52

condb52:                                          ; preds = %contb51
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb52

contb52:                                          ; preds = %condb52, %contb51
  %188 = call i1 @get_creg_bit(i1* %1, i64 53)
  br i1 %188, label %condb53, label %contb53

condb53:                                          ; preds = %contb52
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb53

contb53:                                          ; preds = %condb53, %contb52
  %189 = call i1 @get_creg_bit(i1* %1, i64 54)
  br i1 %189, label %condb54, label %contb54

condb54:                                          ; preds = %contb53
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb54

contb54:                                          ; preds = %condb54, %contb53
  %190 = call i1 @get_creg_bit(i1* %1, i64 55)
  br i1 %190, label %condb55, label %contb55

condb55:                                          ; preds = %contb54
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb55

contb55:                                          ; preds = %condb55, %contb54
  %191 = call i1 @get_creg_bit(i1* %1, i64 56)
  br i1 %191, label %condb56, label %contb56

condb56:                                          ; preds = %contb55
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb56

contb56:                                          ; preds = %condb56, %contb55
  %192 = call i1 @get_creg_bit(i1* %1, i64 57)
  br i1 %192, label %condb57, label %contb57

condb57:                                          ; preds = %contb56
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb57

contb57:                                          ; preds = %condb57, %contb56
  %193 = call i1 @get_creg_bit(i1* %1, i64 58)
  br i1 %193, label %condb58, label %contb58

condb58:                                          ; preds = %contb57
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb58

contb58:                                          ; preds = %condb58, %contb57
  %194 = call i1 @get_creg_bit(i1* %1, i64 59)
  br i1 %194, label %condb59, label %contb59

condb59:                                          ; preds = %contb58
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb59

contb59:                                          ; preds = %condb59, %contb58
  %195 = call i1 @get_creg_bit(i1* %1, i64 60)
  br i1 %195, label %condb60, label %contb60

condb60:                                          ; preds = %contb59
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb60

contb60:                                          ; preds = %condb60, %contb59
  %196 = call i1 @get_creg_bit(i1* %1, i64 61)
  br i1 %196, label %condb61, label %contb61

condb61:                                          ; preds = %contb60
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb61

contb61:                                          ; preds = %condb61, %contb60
  %197 = call i1 @get_creg_bit(i1* %1, i64 62)
  br i1 %197, label %condb62, label %contb62

condb62:                                          ; preds = %contb61
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb62

contb62:                                          ; preds = %condb62, %contb61
  %198 = call i1 @get_creg_bit(i1* %1, i64 63)
  br i1 %198, label %condb63, label %contb63

condb63:                                          ; preds = %contb62
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb63

contb63:                                          ; preds = %condb63, %contb62
  %199 = call i1 @get_creg_bit(i1* %2, i64 0)
  br i1 %199, label %condb64, label %contb64

condb64:                                          ; preds = %contb63
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb64

contb64:                                          ; preds = %condb64, %contb63
  %200 = call i1 @get_creg_bit(i1* %2, i64 1)
  br i1 %200, label %condb65, label %contb65

condb65:                                          ; preds = %contb64
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb65

contb65:                                          ; preds = %condb65, %contb64
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

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
