#!/bin/bash

if [ $# -eq 0 ]; then
    n=100000;
else
    n=$1;
fi

even=0

for ((i=0; i<n; i+=2)) do
    ((even+=i));
done

odd=0

for ((i=1; i<n; i+=2)) do
    ((odd+=i));
done

echo Even: $even
echo Odd: $odd
