; ModuleID = 'test_pytket_qir_conditional_17-block'
source_filename = "test_pytket_qir_conditional_17-block"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  %0 = call i1* @create_creg(i64 1)
  %1 = call i1* @create_creg(i64 10)
  %2 = call i1* @create_creg(i64 20)
  call void @mz_to_creg_bit(%Qubit* null, i1* %0, i64 0)
  %3 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %3, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 0)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %4 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %4, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 1)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %5 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %5, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 2)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %6 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %6, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 3)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %7 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %7, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 4)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %8 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %8, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 5)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %9 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %9, label %condb6, label %contb6

condb6:                                           ; preds = %contb5
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 6)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %10 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %10, label %condb7, label %contb7

condb7:                                           ; preds = %contb6
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 7)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %11 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %11, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 8)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %12 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %12, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @mz_to_creg_bit(%Qubit* null, i1* %1, i64 9)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %13 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %13, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @set_creg_bit(i1* %1, i64 0, i1 true)
  call void @set_creg_bit(i1* %1, i64 1, i1 true)
  call void @set_creg_bit(i1* %1, i64 2, i1 false)
  call void @set_creg_bit(i1* %1, i64 3, i1 false)
  call void @set_creg_bit(i1* %1, i64 4, i1 false)
  call void @set_creg_bit(i1* %1, i64 5, i1 false)
  call void @set_creg_bit(i1* %1, i64 6, i1 false)
  call void @set_creg_bit(i1* %1, i64 7, i1 false)
  call void @set_creg_bit(i1* %1, i64 8, i1 false)
  call void @set_creg_bit(i1* %1, i64 9, i1 false)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %14 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %14, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 0)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  %15 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %15, label %condb12, label %contb12

condb12:                                          ; preds = %contb11
  call void @set_creg_bit(i1* %1, i64 0, i1 true)
  call void @set_creg_bit(i1* %1, i64 1, i1 true)
  call void @set_creg_bit(i1* %1, i64 2, i1 false)
  call void @set_creg_bit(i1* %1, i64 3, i1 false)
  call void @set_creg_bit(i1* %1, i64 4, i1 false)
  call void @set_creg_bit(i1* %1, i64 5, i1 false)
  call void @set_creg_bit(i1* %1, i64 6, i1 false)
  call void @set_creg_bit(i1* %1, i64 7, i1 false)
  call void @set_creg_bit(i1* %1, i64 8, i1 false)
  call void @set_creg_bit(i1* %1, i64 9, i1 false)
  br label %contb12

contb12:                                          ; preds = %condb12, %contb11
  %16 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %16, label %condb13, label %contb13

condb13:                                          ; preds = %contb12
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 1)
  br label %contb13

contb13:                                          ; preds = %condb13, %contb12
  %17 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %17, label %condb14, label %contb14

condb14:                                          ; preds = %contb13
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 2)
  br label %contb14

contb14:                                          ; preds = %condb14, %contb13
  %18 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %18, label %condb15, label %contb15

condb15:                                          ; preds = %contb14
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 3)
  br label %contb15

contb15:                                          ; preds = %condb15, %contb14
  %19 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %19, label %condb16, label %contb16

condb16:                                          ; preds = %contb15
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 4)
  br label %contb16

contb16:                                          ; preds = %condb16, %contb15
  %20 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %20, label %condb17, label %contb17

condb17:                                          ; preds = %contb16
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 5)
  br label %contb17

contb17:                                          ; preds = %condb17, %contb16
  %21 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %21, label %condb18, label %contb18

condb18:                                          ; preds = %contb17
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 6)
  br label %contb18

contb18:                                          ; preds = %condb18, %contb17
  %22 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %22, label %condb19, label %contb19

condb19:                                          ; preds = %contb18
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 7)
  br label %contb19

contb19:                                          ; preds = %condb19, %contb18
  %23 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %23, label %condb20, label %contb20

condb20:                                          ; preds = %contb19
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 8)
  br label %contb20

contb20:                                          ; preds = %condb20, %contb19
  %24 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %24, label %condb21, label %contb21

condb21:                                          ; preds = %contb20
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 9)
  br label %contb21

contb21:                                          ; preds = %condb21, %contb20
  %25 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %25, label %condb22, label %contb22

condb22:                                          ; preds = %contb21
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 10)
  br label %contb22

contb22:                                          ; preds = %condb22, %contb21
  %26 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %26, label %condb23, label %contb23

condb23:                                          ; preds = %contb22
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 11)
  br label %contb23

contb23:                                          ; preds = %condb23, %contb22
  %27 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %27, label %condb24, label %contb24

condb24:                                          ; preds = %contb23
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 12)
  br label %contb24

contb24:                                          ; preds = %condb24, %contb23
  %28 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %28, label %condb25, label %contb25

condb25:                                          ; preds = %contb24
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 13)
  br label %contb25

contb25:                                          ; preds = %condb25, %contb24
  %29 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %29, label %condb26, label %contb26

condb26:                                          ; preds = %contb25
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 14)
  br label %contb26

contb26:                                          ; preds = %condb26, %contb25
  %30 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %30, label %condb27, label %contb27

condb27:                                          ; preds = %contb26
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 15)
  br label %contb27

contb27:                                          ; preds = %condb27, %contb26
  %31 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %31, label %condb28, label %contb28

condb28:                                          ; preds = %contb27
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 16)
  br label %contb28

contb28:                                          ; preds = %condb28, %contb27
  %32 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %32, label %condb29, label %contb29

condb29:                                          ; preds = %contb28
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 17)
  br label %contb29

contb29:                                          ; preds = %condb29, %contb28
  %33 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %33, label %condb30, label %contb30

condb30:                                          ; preds = %contb29
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 18)
  br label %contb30

contb30:                                          ; preds = %condb30, %contb29
  %34 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %34, label %condb31, label %contb31

condb31:                                          ; preds = %contb30
  call void @mz_to_creg_bit(%Qubit* null, i1* %2, i64 19)
  br label %contb31

contb31:                                          ; preds = %condb31, %contb30
  %35 = call i1 @get_creg_bit(i1* %0, i64 0)
  br i1 %35, label %condb32, label %contb32

condb32:                                          ; preds = %contb31
  %36 = call i64 @get_int_from_creg(i1* %0)
  %37 = call i64 @get_int_from_creg(i1* %1)
  %38 = add i64 %36, %37
  call void @set_creg_to_int(i1* %2, i64 %38)
  br label %contb32

contb32:                                          ; preds = %condb32, %contb31
  %39 = call i64 @get_int_from_creg(i1* %0)
  call void @__quantum__rt__int_record_output(i64 %39, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  %40 = call i64 @get_int_from_creg(i1* %1)
  call void @__quantum__rt__int_record_output(i64 %40, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  %41 = call i64 @get_int_from_creg(i1* %2)
  call void @__quantum__rt__int_record_output(i64 %41, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare i1 @get_creg_bit(i1*, i64)

declare void @set_creg_bit(i1*, i64, i1)

declare void @set_creg_to_int(i1*, i64)

declare i1* @create_creg(i64)

declare i64 @get_int_from_creg(i1*)

declare void @mz_to_creg_bit(%Qubit*, i1*, i64)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
