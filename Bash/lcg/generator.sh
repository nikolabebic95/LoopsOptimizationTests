#!/bin/bash

file="lcg.sh"
n=256

if [ $# -gt 0 ]; then
    file=$1;
fi
if [ $# -gt 2 ]; then
    n=$2;
fi

file=$(echo $file | sed 's:\(.*\)\..*:\1:')

start=$'#!/bin/bash

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
'

middle='
for ((i=0; i<n_prologue; i++)) do
    seed=$(((a*seed+c)%m))
done

for ((i=0; i<n_loop; i++)) do'

loop='    seed=$(((a*seed+c)%m))'

end='done

echo $seed
'

for ((i=2;i<n;i++)) do
    n_prologue="n_prologue=\$((n%$i))"
    n_loop="n_loop=\$((n/$i))"
    unrolled="_unrolled_"
    file_name="$file$unrolled$i.sh"
    echo "$start">"$file_name"
    echo "$n_prologue">>"$file_name"
    echo "$n_loop">>"$file_name"
    echo "$middle">>"$file_name"

    for ((j=0;j<i;j++)) do
        echo "$loop">>"$file_name"
    done

    echo "$end">>$file_name
done
