#!/bin/bash

if [ $# -eq 0 ]; then
    n=100000;
else
    n=$1;
fi

even=0
odd=0

for ((i=0; i<n/2; i++)) do
    ((even+=i));
    ((odd+=i));
done

echo Even: $even
echo Odd: $odd
