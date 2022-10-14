#!/bin/sh

LL_FILES="./tests/qir_test_files/*.ll"
BC_FILES="./tests/qir_test_files/*.bc"

for ll_file in $LL_FILES
do
    bc_file=$(echo ${ll_file} | sed -r 's/ll/bc/g')
    if [ -f "$bc_file" ]; then
	echo "$ll_file --> $bc_file exists."
    else
	echo "No .bc file for $ll_file."
	break
    fi
done

echo "--Test files check complete for .ll files.--"

for bc_file in $BC_FILES
do
    ll_file=$(echo ${bc_file} | sed -r 's/bc/ll/g')
    if [ -f "$ll_file" ]; then
	echo "$bc_file --> $ll_file exists."
    else
	echo "No .ll file for $bc_file."
	break
    fi
done

echo "--Test files check complete for .bc files.--"
