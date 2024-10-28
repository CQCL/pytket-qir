OPENQASM 2.0;
include "hqslib1.inc";

qreg q[10];

creg p[1];

creg s[3];

if(s == 2) p[0] = p[0] ^ 1;
