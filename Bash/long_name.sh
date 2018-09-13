#!/bin/bash

n=1000000

if [ $# -gt 0 ]; then
    n=$1;
fi

variable_with_really_long_name=0

for ((i=0;i<n;i++)) do
    variable_with_really_long_name=$((variable_with_really_long_name + 1))
done

echo $variable_with_really_long_name
