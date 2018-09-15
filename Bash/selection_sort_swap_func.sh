#!/bin/bash

declare -a arr

if [ $# -gt 0 ]; then
    N=$1;
else
    N=1000
fi

swap() {
    t=${arr[$1]}
    arr[$1]=${arr[$2]}
    arr[$2]=$t
}

for ((i=0;i<N;i++)) do
    arr[i]=$RANDOM
done

for ((i=0;i<N;i++)) do
    for ((j=0;j<N;j++)) do
        if [ ${arr[i]} -lt ${arr[j]} ]; then
            swap $i $j
        fi
    done
done
