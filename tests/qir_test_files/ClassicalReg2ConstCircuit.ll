; ModuleID = 'Generated from input pytket circuit'
source_filename = "Generated from input pytket circuit"

declare i64 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

define void @main() #0 {
entry:
  %0 = call i64 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = add i64 %0, 3
  %2 = sub i64 %0, 3
  %3 = mul i64 %0, 3
  %4 = shl i64 %0, 3
  %5 = lshr i64 %0, 3
  %6 = icmp eq i64 %0, 3
  %7 = icmp ne i64 %0, 3
  %8 = icmp ugt i64 %0, 3
  %9 = icmp uge i64 %0, 3
  %10 = icmp ult i64 %0, 3
  %11 = icmp ule i64 %0, 3
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="9" }
