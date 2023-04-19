; ModuleID = 'Generated from input pytket circuit'
source_filename = "Generated from input pytket circuit"

declare i32 @reg2var(i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1, i1)

define void @main() #0 {
entry:
  %0 = call i32 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %1 = call i32 @reg2var(i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false, i1 false)
  %2 = and i32 %0, %1
  %3 = or i32 %0, %1
  %4 = xor i32 %0, %1
  %5 = add i32 %0, %1
  %6 = sub i32 %0, %1
  %7 = mul i32 %0, %1
  %8 = shl i32 %0, %1
  %9 = lshr i32 %0, %1
  %10 = icmp eq i32 %0, %1
  %11 = icmp ne i32 %0, %1
  %12 = icmp ugt i32 %0, %1
  %13 = icmp uge i32 %0, %1
  %14 = icmp ult i32 %0, %1
  %15 = icmp ule i32 %0, %1
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="2" "requiredResults"="9" }
