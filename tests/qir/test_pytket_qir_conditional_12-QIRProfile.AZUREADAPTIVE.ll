; ModuleID = 'test_pytket_qir_conditional_12'
source_filename = "test_pytket_qir_conditional_12"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [4 x i8] c"syn\00"
@1 = internal constant [17 x i8] c"tk_SCRATCH_BIT_0\00"
@2 = internal constant [17 x i8] c"tk_SCRATCH_BIT_1\00"

define void @main() #0 {
entry:
  br i1 false, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  br i1 false, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  br i1 false, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  br i1 false, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  br i1 false, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  br i1 false, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  br i1 false, label %condb6, label %contb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  br i1 false, label %condb7, label %contb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  br i1 false, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  br i1 false, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  br i1 false, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  br i1 false, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  br i1 false, label %condb12, label %contb12

condb12:                                          ; preds = %contb11
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb12

contb12:                                          ; preds = %condb12, %contb11
  br i1 false, label %condb13, label %contb13

condb13:                                          ; preds = %contb12
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb13

contb13:                                          ; preds = %condb13, %contb12
  br i1 false, label %condb14, label %contb14

condb14:                                          ; preds = %contb13
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb14

contb14:                                          ; preds = %condb14, %contb13
  br i1 false, label %condb15, label %contb15

condb15:                                          ; preds = %contb14
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb15

contb15:                                          ; preds = %condb15, %contb14
  br i1 false, label %condb16, label %contb16

condb16:                                          ; preds = %contb15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb16

contb16:                                          ; preds = %condb16, %contb15
  br i1 false, label %condb17, label %contb17

condb17:                                          ; preds = %contb16
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb17

contb17:                                          ; preds = %condb17, %contb16
  br i1 false, label %condb18, label %contb18

condb18:                                          ; preds = %contb17
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb18

contb18:                                          ; preds = %condb18, %contb17
  br i1 false, label %condb19, label %contb19

condb19:                                          ; preds = %contb18
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb19

contb19:                                          ; preds = %condb19, %contb18
  br i1 false, label %condb20, label %contb20

condb20:                                          ; preds = %contb19
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb20

contb20:                                          ; preds = %condb20, %contb19
  br i1 false, label %condb21, label %contb21

condb21:                                          ; preds = %contb20
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb21

contb21:                                          ; preds = %condb21, %contb20
  br i1 false, label %condb22, label %contb22

condb22:                                          ; preds = %contb21
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb22

contb22:                                          ; preds = %condb22, %contb21
  br i1 false, label %condb23, label %contb23

condb23:                                          ; preds = %contb22
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb23

contb23:                                          ; preds = %condb23, %contb22
  br i1 false, label %condb24, label %contb24

condb24:                                          ; preds = %contb23
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb24

contb24:                                          ; preds = %condb24, %contb23
  br i1 false, label %condb25, label %contb25

condb25:                                          ; preds = %contb24
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb25

contb25:                                          ; preds = %condb25, %contb24
  br i1 false, label %condb26, label %contb26

condb26:                                          ; preds = %contb25
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb26

contb26:                                          ; preds = %condb26, %contb25
  br i1 false, label %condb27, label %contb27

condb27:                                          ; preds = %contb26
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb27

contb27:                                          ; preds = %condb27, %contb26
  br i1 false, label %condb28, label %contb28

condb28:                                          ; preds = %contb27
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb28

contb28:                                          ; preds = %condb28, %contb27
  br i1 false, label %condb29, label %contb29

condb29:                                          ; preds = %contb28
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb29

contb29:                                          ; preds = %condb29, %contb28
  br i1 false, label %condb30, label %contb30

condb30:                                          ; preds = %contb29
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb30

contb30:                                          ; preds = %condb30, %contb29
  br i1 false, label %condb31, label %contb31

condb31:                                          ; preds = %contb30
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb31

contb31:                                          ; preds = %condb31, %contb30
  br i1 false, label %condb32, label %contb32

condb32:                                          ; preds = %contb31
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb32

contb32:                                          ; preds = %condb32, %contb31
  br i1 false, label %condb33, label %contb33

condb33:                                          ; preds = %contb32
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb33

contb33:                                          ; preds = %condb33, %contb32
  br i1 false, label %condb34, label %contb34

condb34:                                          ; preds = %contb33
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb34

contb34:                                          ; preds = %condb34, %contb33
  br i1 false, label %condb35, label %contb35

condb35:                                          ; preds = %contb34
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb35

contb35:                                          ; preds = %condb35, %contb34
  br i1 false, label %condb36, label %contb36

condb36:                                          ; preds = %contb35
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb36

contb36:                                          ; preds = %condb36, %contb35
  br i1 false, label %condb37, label %contb37

condb37:                                          ; preds = %contb36
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb37

contb37:                                          ; preds = %condb37, %contb36
  br i1 false, label %condb38, label %contb38

condb38:                                          ; preds = %contb37
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb38

contb38:                                          ; preds = %condb38, %contb37
  br i1 false, label %condb39, label %contb39

condb39:                                          ; preds = %contb38
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb39

contb39:                                          ; preds = %condb39, %contb38
  br i1 false, label %condb40, label %contb40

condb40:                                          ; preds = %contb39
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb40

contb40:                                          ; preds = %condb40, %contb39
  br i1 false, label %condb41, label %contb41

condb41:                                          ; preds = %contb40
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb41

contb41:                                          ; preds = %condb41, %contb40
  br i1 false, label %condb42, label %contb42

condb42:                                          ; preds = %contb41
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb42

contb42:                                          ; preds = %condb42, %contb41
  br i1 false, label %condb43, label %contb43

condb43:                                          ; preds = %contb42
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb43

contb43:                                          ; preds = %condb43, %contb42
  br i1 false, label %condb44, label %contb44

condb44:                                          ; preds = %contb43
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb44

contb44:                                          ; preds = %condb44, %contb43
  br i1 false, label %condb45, label %contb45

condb45:                                          ; preds = %contb44
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb45

contb45:                                          ; preds = %condb45, %contb44
  br i1 false, label %condb46, label %contb46

condb46:                                          ; preds = %contb45
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb46

contb46:                                          ; preds = %condb46, %contb45
  br i1 false, label %condb47, label %contb47

condb47:                                          ; preds = %contb46
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb47

contb47:                                          ; preds = %condb47, %contb46
  br i1 false, label %condb48, label %contb48

condb48:                                          ; preds = %contb47
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb48

contb48:                                          ; preds = %condb48, %contb47
  br i1 false, label %condb49, label %contb49

condb49:                                          ; preds = %contb48
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb49

contb49:                                          ; preds = %condb49, %contb48
  br i1 false, label %condb50, label %contb50

condb50:                                          ; preds = %contb49
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb50

contb50:                                          ; preds = %condb50, %contb49
  br i1 false, label %condb51, label %contb51

condb51:                                          ; preds = %contb50
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb51

contb51:                                          ; preds = %condb51, %contb50
  br i1 false, label %condb52, label %contb52

condb52:                                          ; preds = %contb51
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb52

contb52:                                          ; preds = %condb52, %contb51
  br i1 false, label %condb53, label %contb53

condb53:                                          ; preds = %contb52
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb53

contb53:                                          ; preds = %condb53, %contb52
  br i1 false, label %condb54, label %contb54

condb54:                                          ; preds = %contb53
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb54

contb54:                                          ; preds = %condb54, %contb53
  br i1 false, label %condb55, label %contb55

condb55:                                          ; preds = %contb54
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb55

contb55:                                          ; preds = %condb55, %contb54
  br i1 false, label %condb56, label %contb56

condb56:                                          ; preds = %contb55
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb56

contb56:                                          ; preds = %condb56, %contb55
  br i1 false, label %condb57, label %contb57

condb57:                                          ; preds = %contb56
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb57

contb57:                                          ; preds = %condb57, %contb56
  br i1 false, label %condb58, label %contb58

condb58:                                          ; preds = %contb57
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb58

contb58:                                          ; preds = %condb58, %contb57
  br i1 false, label %condb59, label %contb59

condb59:                                          ; preds = %contb58
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb59

contb59:                                          ; preds = %condb59, %contb58
  br i1 false, label %condb60, label %contb60

condb60:                                          ; preds = %contb59
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb60

contb60:                                          ; preds = %condb60, %contb59
  br i1 false, label %condb61, label %contb61

condb61:                                          ; preds = %contb60
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb61

contb61:                                          ; preds = %condb61, %contb60
  br i1 false, label %condb62, label %contb62

condb62:                                          ; preds = %contb61
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb62

contb62:                                          ; preds = %condb62, %contb61
  br i1 false, label %condb63, label %contb63

condb63:                                          ; preds = %contb62
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb63

contb63:                                          ; preds = %condb63, %contb62
  br i1 false, label %condb64, label %contb64

condb64:                                          ; preds = %contb63
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb64

contb64:                                          ; preds = %condb64, %contb63
  br i1 false, label %condb65, label %contb65

condb65:                                          ; preds = %contb64
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb65

contb65:                                          ; preds = %condb65, %contb64
  call void @__quantum__rt__array_record_output(i64 3, i8* null)
  call void @__quantum__rt__int_record_output(i64 0, i8* null)
  call void @__quantum__rt__int_record_output(i64 0, i8* null)
  call void @__quantum__rt__int_record_output(i64 0, i8* null)
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__array_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="7" "required_num_results"="7" }

!llvm.module.flags = !{!0, !1, !2, !3, !4, !5, !6, !7, !8, !9, !10}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
!4 = !{i32 1, !"classical_ints", i1 true}
!5 = !{i32 1, !"qubit_resetting", i1 true}
!6 = !{i32 1, !"classical_floats", i1 false}
!7 = !{i32 1, !"backwards_branching", i1 false}
!8 = !{i32 1, !"classical_fixed_points", i1 false}
!9 = !{i32 1, !"user_functions", i1 false}
!10 = !{i32 1, !"multiple_target_branching", i1 false}
