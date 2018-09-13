#!/bin/bash

if [ $# -eq 0 ]; then
    n=100000;
else
    n=$1;
fi

even=0
odd=0

for ((i=0; i<n; i++)) do
    if [ $(($i % 2)) -eq 0 ]; then
        ((even+=i));
    else
        ((odd+=i));
    fi
done

echo Even: $even
echo Odd: $odd
