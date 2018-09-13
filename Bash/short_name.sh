#!/bin/bash

n=1000000

if [ $# -gt 0 ]; then
    n=$1;
fi

v=0

for ((i=0;i<n;i++)) do
    v=$((v + 1))
done

echo $v
