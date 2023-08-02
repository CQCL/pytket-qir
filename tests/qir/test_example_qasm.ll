OPENQASM 2.0;
include "hqslib1.inc";

qreg q[2];
creg a[2];
creg b[5];
creg c[7];
c = 121;
h q[0];
cx q[0],q[1];
measure q[0] -> a[0];
measure q[1] -> a[1];
if(a[0]==1) c = (c - b);
if(a[1]==1) b = (c - a);
a = (c - b);
