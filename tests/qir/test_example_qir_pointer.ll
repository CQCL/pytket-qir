declare i1 @read_bit_from_reg(i64*, i64)

declare void @set_one_bit_in_reg(i64*, i64, i1)

declare void @set_all_bits_in_reg(i64*, i64)

declare i64 @read_all_bits_from_reg(i64*)

declare i64* @create_reg(i64)