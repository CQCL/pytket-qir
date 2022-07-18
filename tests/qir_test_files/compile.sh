#!/bin/sh

FILES="./tests/qir_test_files/*.ll"

for file in $FILES
do
    new_name=$(echo ${file} | sed -r 's/ll/bc/g')
    echo "Compile $file --> $new_name"
    llvm-as ${file} -o $new_name
done

echo "--Test files compilation complete--"
