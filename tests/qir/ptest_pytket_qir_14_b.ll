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
  %0 = call i64 @create_int(i64 32)
  %1 = call i64 @create_int(i64 32)
  %2 = call i64 @create_int(i64 32)
  %3 = call i64 @create_int(i64 9)
  %4 = call i64 @create_int(i64 64)
  %5 = call i64 @create_int(i64 64)
  %6 = call i64 @create_int(i64 64)
  %7 = call i64 @set_bit_in_int(i64 %0, i64 0, i1 true)
  %8 = call i64 @set_bit_in_int(i64 %1, i64 0, i1 true)
  %9 = call i64 @set_bit_in_int(i64 %8, i64 1, i1 true)
  %10 = call i64 @set_bit_in_int(i64 %9, i64 2, i1 false)
  %11 = call i64 @set_bit_in_int(i64 %10, i64 3, i1 false)
  %12 = call i64 @set_bit_in_int(i64 %11, i64 4, i1 false)
  %13 = call i64 @set_bit_in_int(i64 %12, i64 5, i1 false)
  %14 = call i64 @set_bit_in_int(i64 %13, i64 6, i1 false)
  %15 = call i64 @set_bit_in_int(i64 %14, i64 7, i1 false)
  %16 = call i64 @set_bit_in_int(i64 %15, i64 8, i1 false)
  %17 = call i64 @set_bit_in_int(i64 %16, i64 9, i1 false)
  %18 = call i64 @set_bit_in_int(i64 %17, i64 10, i1 false)
  %19 = call i64 @set_bit_in_int(i64 %18, i64 11, i1 false)
  %20 = call i64 @set_bit_in_int(i64 %19, i64 12, i1 false)
  %21 = call i64 @set_bit_in_int(i64 %20, i64 13, i1 false)
  %22 = call i64 @set_bit_in_int(i64 %21, i64 14, i1 false)
  %23 = call i64 @set_bit_in_int(i64 %22, i64 15, i1 false)
  %24 = call i64 @set_bit_in_int(i64 %23, i64 16, i1 false)
  %25 = call i64 @set_bit_in_int(i64 %24, i64 17, i1 false)
  %26 = call i64 @set_bit_in_int(i64 %25, i64 18, i1 false)
  %27 = call i64 @set_bit_in_int(i64 %26, i64 19, i1 false)
  %28 = call i64 @set_bit_in_int(i64 %27, i64 20, i1 false)
  %29 = call i64 @set_bit_in_int(i64 %28, i64 21, i1 false)
  %30 = call i64 @set_bit_in_int(i64 %29, i64 22, i1 false)
  %31 = call i64 @set_bit_in_int(i64 %30, i64 23, i1 false)
  %32 = call i64 @set_bit_in_int(i64 %31, i64 24, i1 false)
  %33 = call i64 @set_bit_in_int(i64 %32, i64 25, i1 false)
  %34 = call i64 @set_bit_in_int(i64 %33, i64 26, i1 false)
  %35 = call i64 @set_bit_in_int(i64 %34, i64 27, i1 false)
  %36 = call i64 @set_bit_in_int(i64 %35, i64 28, i1 false)
  %37 = call i64 @set_bit_in_int(i64 %36, i64 29, i1 false)
  %38 = call i64 @set_bit_in_int(i64 %37, i64 30, i1 false)
  %39 = call i64 @set_bit_in_int(i64 %38, i64 31, i1 false)
  %40 = call i64 @set_bit_in_int(i64 %7, i64 0, i1 false)
  %41 = call i64 @set_bit_in_int(i64 %40, i64 1, i1 true)
  %42 = call i64 @set_bit_in_int(i64 %41, i64 2, i1 false)
  %43 = call i64 @set_bit_in_int(i64 %42, i64 3, i1 false)
  %44 = call i64 @set_bit_in_int(i64 %43, i64 4, i1 false)
  %45 = call i64 @set_bit_in_int(i64 %44, i64 5, i1 false)
  %46 = call i64 @set_bit_in_int(i64 %45, i64 6, i1 false)
  %47 = call i64 @set_bit_in_int(i64 %46, i64 7, i1 false)
  %48 = call i64 @set_bit_in_int(i64 %47, i64 8, i1 false)
  %49 = call i64 @set_bit_in_int(i64 %48, i64 9, i1 false)
  %50 = call i64 @set_bit_in_int(i64 %49, i64 10, i1 false)
  %51 = call i64 @set_bit_in_int(i64 %50, i64 11, i1 false)
  %52 = call i64 @set_bit_in_int(i64 %51, i64 12, i1 false)
  %53 = call i64 @set_bit_in_int(i64 %52, i64 13, i1 false)
  %54 = call i64 @set_bit_in_int(i64 %53, i64 14, i1 false)
  %55 = call i64 @set_bit_in_int(i64 %54, i64 15, i1 false)
  %56 = call i64 @set_bit_in_int(i64 %55, i64 16, i1 false)
  %57 = call i64 @set_bit_in_int(i64 %56, i64 17, i1 false)
  %58 = call i64 @set_bit_in_int(i64 %57, i64 18, i1 false)
  %59 = call i64 @set_bit_in_int(i64 %58, i64 19, i1 false)
  %60 = call i64 @set_bit_in_int(i64 %59, i64 20, i1 false)
  %61 = call i64 @set_bit_in_int(i64 %60, i64 21, i1 false)
  %62 = call i64 @set_bit_in_int(i64 %61, i64 22, i1 false)
  %63 = call i64 @set_bit_in_int(i64 %62, i64 23, i1 false)
  %64 = call i64 @set_bit_in_int(i64 %63, i64 24, i1 false)
  %65 = call i64 @set_bit_in_int(i64 %64, i64 25, i1 false)
  %66 = call i64 @set_bit_in_int(i64 %65, i64 26, i1 false)
  %67 = call i64 @set_bit_in_int(i64 %66, i64 27, i1 false)
  %68 = call i64 @set_bit_in_int(i64 %67, i64 28, i1 false)
  %69 = call i64 @set_bit_in_int(i64 %68, i64 29, i1 false)
  %70 = call i64 @set_bit_in_int(i64 %69, i64 30, i1 false)
  %71 = call i64 @set_bit_in_int(i64 %70, i64 31, i1 false)
  %72 = call i64 @set_bit_in_int(i64 %71, i64 0, i1 true)
  %73 = call i64 @set_bit_in_int(i64 %72, i64 1, i1 true)
  %74 = call i64 @set_bit_in_int(i64 %73, i64 2, i1 true)
  %75 = call i64 @set_bit_in_int(i64 %74, i64 3, i1 false)
  %76 = call i64 @set_bit_in_int(i64 %75, i64 4, i1 true)
  %77 = call i64 @set_bit_in_int(i64 %76, i64 5, i1 false)
  %78 = call i64 @set_bit_in_int(i64 %77, i64 6, i1 false)
  %79 = call i64 @set_bit_in_int(i64 %78, i64 7, i1 false)
  %80 = call i64 @set_bit_in_int(i64 %79, i64 8, i1 false)
  %81 = call i64 @set_bit_in_int(i64 %80, i64 9, i1 false)
  %82 = call i64 @set_bit_in_int(i64 %81, i64 10, i1 false)
  %83 = call i64 @set_bit_in_int(i64 %82, i64 11, i1 false)
  %84 = call i64 @set_bit_in_int(i64 %83, i64 12, i1 false)
  %85 = call i64 @set_bit_in_int(i64 %84, i64 13, i1 false)
  %86 = call i64 @set_bit_in_int(i64 %85, i64 14, i1 false)
  %87 = call i64 @set_bit_in_int(i64 %86, i64 15, i1 false)
  %88 = call i64 @set_bit_in_int(i64 %87, i64 16, i1 false)
  %89 = call i64 @set_bit_in_int(i64 %88, i64 17, i1 false)
  %90 = call i64 @set_bit_in_int(i64 %89, i64 18, i1 false)
  %91 = call i64 @set_bit_in_int(i64 %90, i64 19, i1 false)
  %92 = call i64 @set_bit_in_int(i64 %91, i64 20, i1 false)
  %93 = call i64 @set_bit_in_int(i64 %92, i64 21, i1 false)
  %94 = call i64 @set_bit_in_int(i64 %93, i64 22, i1 false)
  %95 = call i64 @set_bit_in_int(i64 %94, i64 23, i1 false)
  %96 = call i64 @set_bit_in_int(i64 %95, i64 24, i1 false)
  %97 = call i64 @set_bit_in_int(i64 %96, i64 25, i1 false)
  %98 = call i64 @set_bit_in_int(i64 %97, i64 26, i1 false)
  %99 = call i64 @set_bit_in_int(i64 %98, i64 27, i1 false)
  %100 = call i64 @set_bit_in_int(i64 %99, i64 28, i1 false)
  %101 = call i64 @set_bit_in_int(i64 %100, i64 29, i1 false)
  %102 = call i64 @set_bit_in_int(i64 %101, i64 30, i1 false)
  %103 = call i64 @set_bit_in_int(i64 %102, i64 31, i1 false)
  %104 = call i1 @get_bit_from_int(i64 %103, i64 0)
  %105 = call i64 @set_bit_in_int(i64 %39, i64 0, i1 %104)
  %106 = call i1 @get_bit_from_int(i64 %103, i64 1)
  %107 = call i64 @set_bit_in_int(i64 %105, i64 1, i1 %106)
  %108 = call i1 @get_bit_from_int(i64 %103, i64 2)
  %109 = call i64 @set_bit_in_int(i64 %107, i64 2, i1 %108)
  %110 = call i1 @get_bit_from_int(i64 %103, i64 3)
  %111 = call i64 @set_bit_in_int(i64 %109, i64 3, i1 %110)
  %112 = call i1 @get_bit_from_int(i64 %103, i64 4)
  %113 = call i64 @set_bit_in_int(i64 %111, i64 4, i1 %112)
  %114 = call i1 @get_bit_from_int(i64 %103, i64 5)
  %115 = call i64 @set_bit_in_int(i64 %113, i64 5, i1 %114)
  %116 = call i1 @get_bit_from_int(i64 %103, i64 6)
  %117 = call i64 @set_bit_in_int(i64 %115, i64 6, i1 %116)
  %118 = call i1 @get_bit_from_int(i64 %103, i64 7)
  %119 = call i64 @set_bit_in_int(i64 %117, i64 7, i1 %118)
  %120 = call i1 @get_bit_from_int(i64 %103, i64 8)
  %121 = call i64 @set_bit_in_int(i64 %119, i64 8, i1 %120)
  %122 = call i1 @get_bit_from_int(i64 %103, i64 9)
  %123 = call i64 @set_bit_in_int(i64 %121, i64 9, i1 %122)
  %124 = call i1 @get_bit_from_int(i64 %103, i64 10)
  %125 = call i64 @set_bit_in_int(i64 %123, i64 10, i1 %124)
  %126 = call i1 @get_bit_from_int(i64 %103, i64 11)
  %127 = call i64 @set_bit_in_int(i64 %125, i64 11, i1 %126)
  %128 = call i1 @get_bit_from_int(i64 %103, i64 12)
  %129 = call i64 @set_bit_in_int(i64 %127, i64 12, i1 %128)
  %130 = call i1 @get_bit_from_int(i64 %103, i64 13)
  %131 = call i64 @set_bit_in_int(i64 %129, i64 13, i1 %130)
  %132 = call i1 @get_bit_from_int(i64 %103, i64 14)
  %133 = call i64 @set_bit_in_int(i64 %131, i64 14, i1 %132)
  %134 = call i1 @get_bit_from_int(i64 %103, i64 15)
  %135 = call i64 @set_bit_in_int(i64 %133, i64 15, i1 %134)
  %136 = call i1 @get_bit_from_int(i64 %103, i64 16)
  %137 = call i64 @set_bit_in_int(i64 %135, i64 16, i1 %136)
  %138 = call i1 @get_bit_from_int(i64 %103, i64 17)
  %139 = call i64 @set_bit_in_int(i64 %137, i64 17, i1 %138)
  %140 = call i1 @get_bit_from_int(i64 %103, i64 18)
  %141 = call i64 @set_bit_in_int(i64 %139, i64 18, i1 %140)
  %142 = call i1 @get_bit_from_int(i64 %103, i64 19)
  %143 = call i64 @set_bit_in_int(i64 %141, i64 19, i1 %142)
  %144 = call i1 @get_bit_from_int(i64 %103, i64 20)
  %145 = call i64 @set_bit_in_int(i64 %143, i64 20, i1 %144)
  %146 = call i1 @get_bit_from_int(i64 %103, i64 21)
  %147 = call i64 @set_bit_in_int(i64 %145, i64 21, i1 %146)
  %148 = call i1 @get_bit_from_int(i64 %103, i64 22)
  %149 = call i64 @set_bit_in_int(i64 %147, i64 22, i1 %148)
  %150 = call i1 @get_bit_from_int(i64 %103, i64 23)
  %151 = call i64 @set_bit_in_int(i64 %149, i64 23, i1 %150)
  %152 = call i1 @get_bit_from_int(i64 %103, i64 24)
  %153 = call i64 @set_bit_in_int(i64 %151, i64 24, i1 %152)
  %154 = call i1 @get_bit_from_int(i64 %103, i64 25)
  %155 = call i64 @set_bit_in_int(i64 %153, i64 25, i1 %154)
  %156 = call i1 @get_bit_from_int(i64 %103, i64 26)
  %157 = call i64 @set_bit_in_int(i64 %155, i64 26, i1 %156)
  %158 = call i1 @get_bit_from_int(i64 %103, i64 27)
  %159 = call i64 @set_bit_in_int(i64 %157, i64 27, i1 %158)
  %160 = call i1 @get_bit_from_int(i64 %103, i64 28)
  %161 = call i64 @set_bit_in_int(i64 %159, i64 28, i1 %160)
  %162 = call i1 @get_bit_from_int(i64 %103, i64 29)
  %163 = call i64 @set_bit_in_int(i64 %161, i64 29, i1 %162)
  %164 = call i1 @get_bit_from_int(i64 %103, i64 30)
  %165 = call i64 @set_bit_in_int(i64 %163, i64 30, i1 %164)
  %166 = call i1 @get_bit_from_int(i64 %103, i64 31)
  %167 = call i64 @set_bit_in_int(i64 %165, i64 31, i1 %166)
  %168 = add i64 %103, %167
  %169 = sub i64 %103, %167
  %170 = shl i64 %103, 1
  %171 = lshr i64 %170, 1
  %172 = icmp eq i64 1, %170
  %173 = call i64 @set_bit_in_int(i64 %3, i64 4, i1 %172)
  %174 = icmp sgt i64 2, %170
  %175 = icmp sgt i64 %170, -1
  %176 = and i1 %174, %175
  %177 = call i64 @set_bit_in_int(i64 %173, i64 5, i1 %176)
  %178 = icmp eq i64 0, %170
  %179 = call i64 @set_bit_in_int(i64 %177, i64 6, i1 %178)
  %180 = icmp sgt i64 1, %170
  %181 = icmp sgt i64 %170, -1
  %182 = and i1 %180, %181
  %183 = call i64 @set_bit_in_int(i64 %179, i64 7, i1 %182)
  %184 = icmp sgt i64 0, %170
  %185 = icmp sgt i64 %170, 1
  %186 = and i1 %184, %185
  %187 = call i64 @set_bit_in_int(i64 %183, i64 8, i1 %186)
  %188 = call i1 @get_bit_from_int(i64 %170, i64 0)
  br i1 %188, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %189 = call i1 @get_bit_from_int(i64 %170, i64 0)
  %190 = call i1 @get_bit_from_int(i64 %171, i64 0)
  %191 = xor i1 %189, %190
  %192 = call i64 @set_bit_in_int(i64 %187, i64 1, i1 %191)
  %193 = xor i64 %170, %171
  %194 = and i64 %170, %171
  %195 = or i64 %170, %171
  %196 = icmp eq i64 1, %193
  %197 = call i64 @set_bit_in_int(i64 %192, i64 0, i1 %196)
  %198 = icmp eq i64 1, %194
  %199 = call i64 @set_bit_in_int(i64 %197, i64 2, i1 %198)
  %200 = icmp eq i64 1, %195
  %201 = call i64 @set_bit_in_int(i64 %199, i64 3, i1 %200)
  %202 = call i1 @get_bit_from_int(i64 %201, i64 0)
  br i1 %202, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %203 = call i1 @get_bit_from_int(i64 %201, i64 1)
  br i1 %203, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %204 = call i1 @get_bit_from_int(i64 %201, i64 2)
  br i1 %204, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %205 = call i1 @get_bit_from_int(i64 %201, i64 3)
  br i1 %205, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %206 = call i1 @get_bit_from_int(i64 %170, i64 0)
  br i1 %206, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %207 = call i1 @get_bit_from_int(i64 %201, i64 4)
  br i1 %207, label %contb6, label %condb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %208 = call i1 @get_bit_from_int(i64 %170, i64 0)
  br i1 %208, label %contb7, label %condb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %209 = call i1 @get_bit_from_int(i64 %201, i64 5)
  br i1 %209, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %210 = call i1 @get_bit_from_int(i64 %201, i64 6)
  br i1 %210, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %211 = call i1 @get_bit_from_int(i64 %201, i64 7)
  br i1 %211, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %212 = call i1 @get_bit_from_int(i64 %201, i64 8)
  br i1 %212, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  call void @__quantum__rt__int_record_output(i64 %170, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %171, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %169, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @2, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %201, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @3, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %193, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @4, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %194, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @5, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %195, i8* getelementptr inbounds ([20 x i8], [20 x i8]* @6, i32 0, i32 0))
  ret void
}

declare i1 @get_bit_from_int(i64, i64)

declare i64 @set_bit_in_int(i64, i64, i1)

declare i1 @__quantum__qis__read_result__body(%Result*)

declare i64 @create_int(i64)

declare i64 @mz_to_int(%Qubit*, i64, i64)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__qis__x__body(%Qubit*)

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }

!llvm.module.flags = !{!0, !1, !2, !3}

!0 = !{i32 1, !"qir_major_version", i32 1}
!1 = !{i32 7, !"qir_minor_version", i32 0}
!2 = !{i32 1, !"dynamic_qubit_management", i1 false}
!3 = !{i32 1, !"dynamic_result_management", i1 false}
