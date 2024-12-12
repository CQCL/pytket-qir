; ModuleID = 'test_pytket_qir_conditional_17-block'
source_filename = "test_pytket_qir_conditional_17-block"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [2 x i8] c"a\00"
@1 = internal constant [2 x i8] c"b\00"
@2 = internal constant [2 x i8] c"d\00"

define void @main() #0 {
entry:
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %1 = zext i1 %0 to i64
  %2 = mul i64 %1, 1
  %3 = or i64 %2, 0
  %4 = sub i64 1, %1
  %5 = mul i64 %4, 1
  %6 = xor i64 9223372036854775807, %5
  %7 = and i64 %6, %3
  %8 = and i64 1, %7
  %9 = icmp eq i64 1, %8
  br i1 %9, label %condb0, label %contb0

condb0:                                           ; preds = %entry
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %10 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %11 = zext i1 %10 to i64
  %12 = mul i64 %11, 1
  %13 = or i64 %12, 0
  %14 = sub i64 1, %11
  %15 = mul i64 %14, 1
  %16 = xor i64 9223372036854775807, %15
  %17 = and i64 %16, %13
  br label %contb0

contb0:                                           ; preds = %condb0, %entry
  %18 = phi i64 [ %17, %condb0 ], [ 0, %entry ]
  %19 = and i64 1, %7
  %20 = icmp eq i64 1, %19
  br i1 %20, label %condb1, label %contb1

condb1:                                           ; preds = %contb0
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %21 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %22 = zext i1 %21 to i64
  %23 = mul i64 %22, 2
  %24 = or i64 %23, %18
  %25 = sub i64 1, %22
  %26 = mul i64 %25, 2
  %27 = xor i64 9223372036854775807, %26
  %28 = and i64 %27, %24
  br label %contb1

contb1:                                           ; preds = %condb1, %contb0
  %29 = phi i64 [ %28, %condb1 ], [ %18, %contb0 ]
  %30 = and i64 1, %7
  %31 = icmp eq i64 1, %30
  br i1 %31, label %condb2, label %contb2

condb2:                                           ; preds = %contb1
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %32 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %33 = zext i1 %32 to i64
  %34 = mul i64 %33, 4
  %35 = or i64 %34, %29
  %36 = sub i64 1, %33
  %37 = mul i64 %36, 4
  %38 = xor i64 9223372036854775807, %37
  %39 = and i64 %38, %35
  br label %contb2

contb2:                                           ; preds = %condb2, %contb1
  %40 = phi i64 [ %39, %condb2 ], [ %29, %contb1 ]
  %41 = and i64 1, %7
  %42 = icmp eq i64 1, %41
  br i1 %42, label %condb3, label %contb3

condb3:                                           ; preds = %contb2
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %43 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %44 = zext i1 %43 to i64
  %45 = mul i64 %44, 8
  %46 = or i64 %45, %40
  %47 = sub i64 1, %44
  %48 = mul i64 %47, 8
  %49 = xor i64 9223372036854775807, %48
  %50 = and i64 %49, %46
  br label %contb3

contb3:                                           ; preds = %condb3, %contb2
  %51 = phi i64 [ %50, %condb3 ], [ %40, %contb2 ]
  %52 = and i64 1, %7
  %53 = icmp eq i64 1, %52
  br i1 %53, label %condb4, label %contb4

condb4:                                           ; preds = %contb3
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %54 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %55 = zext i1 %54 to i64
  %56 = mul i64 %55, 16
  %57 = or i64 %56, %51
  %58 = sub i64 1, %55
  %59 = mul i64 %58, 16
  %60 = xor i64 9223372036854775807, %59
  %61 = and i64 %60, %57
  br label %contb4

contb4:                                           ; preds = %condb4, %contb3
  %62 = phi i64 [ %61, %condb4 ], [ %51, %contb3 ]
  %63 = and i64 1, %7
  %64 = icmp eq i64 1, %63
  br i1 %64, label %condb5, label %contb5

condb5:                                           ; preds = %contb4
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %65 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %66 = zext i1 %65 to i64
  %67 = mul i64 %66, 32
  %68 = or i64 %67, %62
  %69 = sub i64 1, %66
  %70 = mul i64 %69, 32
  %71 = xor i64 9223372036854775807, %70
  %72 = and i64 %71, %68
  br label %contb5

contb5:                                           ; preds = %condb5, %contb4
  %73 = phi i64 [ %72, %condb5 ], [ %62, %contb4 ]
  %74 = and i64 1, %7
  %75 = icmp eq i64 1, %74
  br i1 %75, label %condb6, label %contb6

condb6:                                           ; preds = %contb5
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %76 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %77 = zext i1 %76 to i64
  %78 = mul i64 %77, 64
  %79 = or i64 %78, %73
  %80 = sub i64 1, %77
  %81 = mul i64 %80, 64
  %82 = xor i64 9223372036854775807, %81
  %83 = and i64 %82, %79
  br label %contb6

contb6:                                           ; preds = %condb6, %contb5
  %84 = phi i64 [ %83, %condb6 ], [ %73, %contb5 ]
  %85 = and i64 1, %7
  %86 = icmp eq i64 1, %85
  br i1 %86, label %condb7, label %contb7

condb7:                                           ; preds = %contb6
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %87 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %88 = zext i1 %87 to i64
  %89 = mul i64 %88, 128
  %90 = or i64 %89, %84
  %91 = sub i64 1, %88
  %92 = mul i64 %91, 128
  %93 = xor i64 9223372036854775807, %92
  %94 = and i64 %93, %90
  br label %contb7

contb7:                                           ; preds = %condb7, %contb6
  %95 = phi i64 [ %94, %condb7 ], [ %84, %contb6 ]
  %96 = and i64 1, %7
  %97 = icmp eq i64 1, %96
  br i1 %97, label %condb8, label %contb8

condb8:                                           ; preds = %contb7
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %98 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %99 = zext i1 %98 to i64
  %100 = mul i64 %99, 256
  %101 = or i64 %100, %95
  %102 = sub i64 1, %99
  %103 = mul i64 %102, 256
  %104 = xor i64 9223372036854775807, %103
  %105 = and i64 %104, %101
  br label %contb8

contb8:                                           ; preds = %condb8, %contb7
  %106 = phi i64 [ %105, %condb8 ], [ %95, %contb7 ]
  %107 = and i64 1, %7
  %108 = icmp eq i64 1, %107
  br i1 %108, label %condb9, label %contb9

condb9:                                           ; preds = %contb8
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %109 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %110 = zext i1 %109 to i64
  %111 = mul i64 %110, 512
  %112 = or i64 %111, %106
  %113 = sub i64 1, %110
  %114 = mul i64 %113, 512
  %115 = xor i64 9223372036854775807, %114
  %116 = and i64 %115, %112
  br label %contb9

contb9:                                           ; preds = %condb9, %contb8
  %117 = phi i64 [ %116, %condb9 ], [ %106, %contb8 ]
  %118 = and i64 1, %7
  %119 = icmp eq i64 1, %118
  br i1 %119, label %condb10, label %contb10

condb10:                                          ; preds = %contb9
  %120 = or i64 1, %117
  %121 = and i64 9223372036854775807, %120
  %122 = or i64 2, %121
  %123 = and i64 9223372036854775807, %122
  %124 = or i64 0, %123
  %125 = and i64 9223372036854775803, %124
  %126 = or i64 0, %125
  %127 = and i64 9223372036854775799, %126
  %128 = or i64 0, %127
  %129 = and i64 9223372036854775791, %128
  %130 = or i64 0, %129
  %131 = and i64 9223372036854775775, %130
  %132 = or i64 0, %131
  %133 = and i64 9223372036854775743, %132
  %134 = or i64 0, %133
  %135 = and i64 9223372036854775679, %134
  %136 = or i64 0, %135
  %137 = and i64 9223372036854775551, %136
  %138 = or i64 0, %137
  %139 = and i64 9223372036854775295, %138
  br label %contb10

contb10:                                          ; preds = %condb10, %contb9
  %140 = phi i64 [ %139, %condb10 ], [ %117, %contb9 ]
  %141 = and i64 1, %7
  %142 = icmp eq i64 1, %141
  br i1 %142, label %condb11, label %contb11

condb11:                                          ; preds = %contb10
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %143 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %144 = zext i1 %143 to i64
  %145 = mul i64 %144, 1
  %146 = or i64 %145, 0
  %147 = sub i64 1, %144
  %148 = mul i64 %147, 1
  %149 = xor i64 9223372036854775807, %148
  %150 = and i64 %149, %146
  br label %contb11

contb11:                                          ; preds = %condb11, %contb10
  %151 = phi i64 [ %150, %condb11 ], [ 0, %contb10 ]
  %152 = and i64 1, %7
  %153 = icmp eq i64 1, %152
  br i1 %153, label %condb12, label %contb12

condb12:                                          ; preds = %contb11
  %154 = or i64 1, %140
  %155 = and i64 9223372036854775807, %154
  %156 = or i64 2, %155
  %157 = and i64 9223372036854775807, %156
  %158 = or i64 0, %157
  %159 = and i64 9223372036854775803, %158
  %160 = or i64 0, %159
  %161 = and i64 9223372036854775799, %160
  %162 = or i64 0, %161
  %163 = and i64 9223372036854775791, %162
  %164 = or i64 0, %163
  %165 = and i64 9223372036854775775, %164
  %166 = or i64 0, %165
  %167 = and i64 9223372036854775743, %166
  %168 = or i64 0, %167
  %169 = and i64 9223372036854775679, %168
  %170 = or i64 0, %169
  %171 = and i64 9223372036854775551, %170
  %172 = or i64 0, %171
  %173 = and i64 9223372036854775295, %172
  br label %contb12

contb12:                                          ; preds = %condb12, %contb11
  %174 = phi i64 [ %173, %condb12 ], [ %140, %contb11 ]
  %175 = and i64 1, %7
  %176 = icmp eq i64 1, %175
  br i1 %176, label %condb13, label %contb13

condb13:                                          ; preds = %contb12
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %177 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %178 = zext i1 %177 to i64
  %179 = mul i64 %178, 2
  %180 = or i64 %179, %151
  %181 = sub i64 1, %178
  %182 = mul i64 %181, 2
  %183 = xor i64 9223372036854775807, %182
  %184 = and i64 %183, %180
  br label %contb13

contb13:                                          ; preds = %condb13, %contb12
  %185 = phi i64 [ %184, %condb13 ], [ %151, %contb12 ]
  %186 = and i64 1, %7
  %187 = icmp eq i64 1, %186
  br i1 %187, label %condb14, label %contb14

condb14:                                          ; preds = %contb13
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %188 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %189 = zext i1 %188 to i64
  %190 = mul i64 %189, 4
  %191 = or i64 %190, %185
  %192 = sub i64 1, %189
  %193 = mul i64 %192, 4
  %194 = xor i64 9223372036854775807, %193
  %195 = and i64 %194, %191
  br label %contb14

contb14:                                          ; preds = %condb14, %contb13
  %196 = phi i64 [ %195, %condb14 ], [ %185, %contb13 ]
  %197 = and i64 1, %7
  %198 = icmp eq i64 1, %197
  br i1 %198, label %condb15, label %contb15

condb15:                                          ; preds = %contb14
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %199 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %200 = zext i1 %199 to i64
  %201 = mul i64 %200, 8
  %202 = or i64 %201, %196
  %203 = sub i64 1, %200
  %204 = mul i64 %203, 8
  %205 = xor i64 9223372036854775807, %204
  %206 = and i64 %205, %202
  br label %contb15

contb15:                                          ; preds = %condb15, %contb14
  %207 = phi i64 [ %206, %condb15 ], [ %196, %contb14 ]
  %208 = and i64 1, %7
  %209 = icmp eq i64 1, %208
  br i1 %209, label %condb16, label %contb16

condb16:                                          ; preds = %contb15
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %210 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %211 = zext i1 %210 to i64
  %212 = mul i64 %211, 16
  %213 = or i64 %212, %207
  %214 = sub i64 1, %211
  %215 = mul i64 %214, 16
  %216 = xor i64 9223372036854775807, %215
  %217 = and i64 %216, %213
  br label %contb16

contb16:                                          ; preds = %condb16, %contb15
  %218 = phi i64 [ %217, %condb16 ], [ %207, %contb15 ]
  %219 = and i64 1, %7
  %220 = icmp eq i64 1, %219
  br i1 %220, label %condb17, label %contb17

condb17:                                          ; preds = %contb16
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %221 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %222 = zext i1 %221 to i64
  %223 = mul i64 %222, 32
  %224 = or i64 %223, %218
  %225 = sub i64 1, %222
  %226 = mul i64 %225, 32
  %227 = xor i64 9223372036854775807, %226
  %228 = and i64 %227, %224
  br label %contb17

contb17:                                          ; preds = %condb17, %contb16
  %229 = phi i64 [ %228, %condb17 ], [ %218, %contb16 ]
  %230 = and i64 1, %7
  %231 = icmp eq i64 1, %230
  br i1 %231, label %condb18, label %contb18

condb18:                                          ; preds = %contb17
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %232 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %233 = zext i1 %232 to i64
  %234 = mul i64 %233, 64
  %235 = or i64 %234, %229
  %236 = sub i64 1, %233
  %237 = mul i64 %236, 64
  %238 = xor i64 9223372036854775807, %237
  %239 = and i64 %238, %235
  br label %contb18

contb18:                                          ; preds = %condb18, %contb17
  %240 = phi i64 [ %239, %condb18 ], [ %229, %contb17 ]
  %241 = and i64 1, %7
  %242 = icmp eq i64 1, %241
  br i1 %242, label %condb19, label %contb19

condb19:                                          ; preds = %contb18
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %243 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %244 = zext i1 %243 to i64
  %245 = mul i64 %244, 128
  %246 = or i64 %245, %240
  %247 = sub i64 1, %244
  %248 = mul i64 %247, 128
  %249 = xor i64 9223372036854775807, %248
  %250 = and i64 %249, %246
  br label %contb19

contb19:                                          ; preds = %condb19, %contb18
  %251 = phi i64 [ %250, %condb19 ], [ %240, %contb18 ]
  %252 = and i64 1, %7
  %253 = icmp eq i64 1, %252
  br i1 %253, label %condb20, label %contb20

condb20:                                          ; preds = %contb19
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %254 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %255 = zext i1 %254 to i64
  %256 = mul i64 %255, 256
  %257 = or i64 %256, %251
  %258 = sub i64 1, %255
  %259 = mul i64 %258, 256
  %260 = xor i64 9223372036854775807, %259
  %261 = and i64 %260, %257
  br label %contb20

contb20:                                          ; preds = %condb20, %contb19
  %262 = phi i64 [ %261, %condb20 ], [ %251, %contb19 ]
  %263 = and i64 1, %7
  %264 = icmp eq i64 1, %263
  br i1 %264, label %condb21, label %contb21

condb21:                                          ; preds = %contb20
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %265 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %266 = zext i1 %265 to i64
  %267 = mul i64 %266, 512
  %268 = or i64 %267, %262
  %269 = sub i64 1, %266
  %270 = mul i64 %269, 512
  %271 = xor i64 9223372036854775807, %270
  %272 = and i64 %271, %268
  br label %contb21

contb21:                                          ; preds = %condb21, %contb20
  %273 = phi i64 [ %272, %condb21 ], [ %262, %contb20 ]
  %274 = and i64 1, %7
  %275 = icmp eq i64 1, %274
  br i1 %275, label %condb22, label %contb22

condb22:                                          ; preds = %contb21
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %276 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %277 = zext i1 %276 to i64
  %278 = mul i64 %277, 1024
  %279 = or i64 %278, %273
  %280 = sub i64 1, %277
  %281 = mul i64 %280, 1024
  %282 = xor i64 9223372036854775807, %281
  %283 = and i64 %282, %279
  br label %contb22

contb22:                                          ; preds = %condb22, %contb21
  %284 = phi i64 [ %283, %condb22 ], [ %273, %contb21 ]
  %285 = and i64 1, %7
  %286 = icmp eq i64 1, %285
  br i1 %286, label %condb23, label %contb23

condb23:                                          ; preds = %contb22
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %287 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %288 = zext i1 %287 to i64
  %289 = mul i64 %288, 2048
  %290 = or i64 %289, %284
  %291 = sub i64 1, %288
  %292 = mul i64 %291, 2048
  %293 = xor i64 9223372036854775807, %292
  %294 = and i64 %293, %290
  br label %contb23

contb23:                                          ; preds = %condb23, %contb22
  %295 = phi i64 [ %294, %condb23 ], [ %284, %contb22 ]
  %296 = and i64 1, %7
  %297 = icmp eq i64 1, %296
  br i1 %297, label %condb24, label %contb24

condb24:                                          ; preds = %contb23
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %298 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %299 = zext i1 %298 to i64
  %300 = mul i64 %299, 4096
  %301 = or i64 %300, %295
  %302 = sub i64 1, %299
  %303 = mul i64 %302, 4096
  %304 = xor i64 9223372036854775807, %303
  %305 = and i64 %304, %301
  br label %contb24

contb24:                                          ; preds = %condb24, %contb23
  %306 = phi i64 [ %305, %condb24 ], [ %295, %contb23 ]
  %307 = and i64 1, %7
  %308 = icmp eq i64 1, %307
  br i1 %308, label %condb25, label %contb25

condb25:                                          ; preds = %contb24
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %309 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %310 = zext i1 %309 to i64
  %311 = mul i64 %310, 8192
  %312 = or i64 %311, %306
  %313 = sub i64 1, %310
  %314 = mul i64 %313, 8192
  %315 = xor i64 9223372036854775807, %314
  %316 = and i64 %315, %312
  br label %contb25

contb25:                                          ; preds = %condb25, %contb24
  %317 = phi i64 [ %316, %condb25 ], [ %306, %contb24 ]
  %318 = and i64 1, %7
  %319 = icmp eq i64 1, %318
  br i1 %319, label %condb26, label %contb26

condb26:                                          ; preds = %contb25
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %320 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %321 = zext i1 %320 to i64
  %322 = mul i64 %321, 16384
  %323 = or i64 %322, %317
  %324 = sub i64 1, %321
  %325 = mul i64 %324, 16384
  %326 = xor i64 9223372036854775807, %325
  %327 = and i64 %326, %323
  br label %contb26

contb26:                                          ; preds = %condb26, %contb25
  %328 = phi i64 [ %327, %condb26 ], [ %317, %contb25 ]
  %329 = and i64 1, %7
  %330 = icmp eq i64 1, %329
  br i1 %330, label %condb27, label %contb27

condb27:                                          ; preds = %contb26
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %331 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %332 = zext i1 %331 to i64
  %333 = mul i64 %332, 32768
  %334 = or i64 %333, %328
  %335 = sub i64 1, %332
  %336 = mul i64 %335, 32768
  %337 = xor i64 9223372036854775807, %336
  %338 = and i64 %337, %334
  br label %contb27

contb27:                                          ; preds = %condb27, %contb26
  %339 = phi i64 [ %338, %condb27 ], [ %328, %contb26 ]
  %340 = and i64 1, %7
  %341 = icmp eq i64 1, %340
  br i1 %341, label %condb28, label %contb28

condb28:                                          ; preds = %contb27
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %342 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %343 = zext i1 %342 to i64
  %344 = mul i64 %343, 65536
  %345 = or i64 %344, %339
  %346 = sub i64 1, %343
  %347 = mul i64 %346, 65536
  %348 = xor i64 9223372036854775807, %347
  %349 = and i64 %348, %345
  br label %contb28

contb28:                                          ; preds = %condb28, %contb27
  %350 = phi i64 [ %349, %condb28 ], [ %339, %contb27 ]
  %351 = and i64 1, %7
  %352 = icmp eq i64 1, %351
  br i1 %352, label %condb29, label %contb29

condb29:                                          ; preds = %contb28
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %353 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %354 = zext i1 %353 to i64
  %355 = mul i64 %354, 131072
  %356 = or i64 %355, %350
  %357 = sub i64 1, %354
  %358 = mul i64 %357, 131072
  %359 = xor i64 9223372036854775807, %358
  %360 = and i64 %359, %356
  br label %contb29

contb29:                                          ; preds = %condb29, %contb28
  %361 = phi i64 [ %360, %condb29 ], [ %350, %contb28 ]
  %362 = and i64 1, %7
  %363 = icmp eq i64 1, %362
  br i1 %363, label %condb30, label %contb30

condb30:                                          ; preds = %contb29
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %364 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %365 = zext i1 %364 to i64
  %366 = mul i64 %365, 262144
  %367 = or i64 %366, %361
  %368 = sub i64 1, %365
  %369 = mul i64 %368, 262144
  %370 = xor i64 9223372036854775807, %369
  %371 = and i64 %370, %367
  br label %contb30

contb30:                                          ; preds = %condb30, %contb29
  %372 = phi i64 [ %371, %condb30 ], [ %361, %contb29 ]
  %373 = and i64 1, %7
  %374 = icmp eq i64 1, %373
  br i1 %374, label %condb31, label %contb31

condb31:                                          ; preds = %contb30
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  %375 = call i1 @__quantum__qis__read_result__body(%Result* null)
  %376 = zext i1 %375 to i64
  %377 = mul i64 %376, 524288
  %378 = or i64 %377, %372
  %379 = sub i64 1, %376
  %380 = mul i64 %379, 524288
  %381 = xor i64 9223372036854775807, %380
  %382 = and i64 %381, %378
  br label %contb31

contb31:                                          ; preds = %condb31, %contb30
  %383 = phi i64 [ %382, %condb31 ], [ %372, %contb30 ]
  %384 = and i64 1, %7
  %385 = icmp eq i64 1, %384
  br i1 %385, label %condb32, label %contb32

condb32:                                          ; preds = %contb31
  %386 = add i64 %7, %174
  br label %contb32

contb32:                                          ; preds = %condb32, %contb31
  %387 = phi i64 [ %386, %condb32 ], [ %383, %contb31 ]
  call void @__quantum__rt__array_record_output(i64 3, i8* null)
  call void @__quantum__rt__int_record_output(i64 %7, i8* null)
  call void @__quantum__rt__int_record_output(i64 %174, i8* null)
  call void @__quantum__rt__int_record_output(i64 %387, i8* null)
  ret void
}

declare i1 @__quantum__qis__read_result__body(%Result*)

declare void @__quantum__rt__int_record_output(i64, i8*)

declare void @__quantum__rt__array_record_output(i64, i8*)

declare void @__quantum__qis__mz__body(%Qubit*, %Result* writeonly) #1

attributes #0 = { "entry_point" "output_labeling_schema" "qir_profiles"="custom" "required_num_qubits"="1" "required_num_results"="1" }
attributes #1 = { "irreversible" }

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
