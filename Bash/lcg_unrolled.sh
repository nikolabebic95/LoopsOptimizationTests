#!/bin/bash

n=1000000
seed=0
a=1664525
c=1013904223
m=4294967296

if [ $# -gt 0 ]; then
    n=$1;
fi
if [ $# -gt 1 ]; then
    seed=$2;
fi
if [ $# -gt 2 ]; then
    a=$3;
fi
if [ $# -gt 3 ]; then
    c=$4;
fi
if [ $# -gt 4 ]; then
    m=$5;
fi

n_before=$((n%8))
n_loop=$((n/8))

for ((i=0; i<n_before; i++)) do
    seed=$(((a*seed+c)%m))
done

for ((i=0; i<n_loop; i++)) do
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    seed=$(((a*seed+c)%m))
    
done

echo $seed
