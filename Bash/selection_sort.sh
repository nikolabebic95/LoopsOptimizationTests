#!/bin/bash

declare -a arr

N=1000

for ((i=0;i<N;i++)) do
    arr[i]=$RANDOM
done

for ((i=0;i<N;i++)) do
    for ((j=0;j<N;j++)) do
        if [ ${arr[i]} -lt ${arr[j]} ]; then
            t=${arr[i]}
            arr[i]=${arr[j]}
            arr[j]=$t
        fi
    done
done
