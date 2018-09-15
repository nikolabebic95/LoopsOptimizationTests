#!/bin/bash

usage() {
    echo "Usage: $0 -i input_file [-b <start>] [-e <end>] [-s <step>] {<file_parameter>}" 1>&2; exit 1;
}

input=""
start=1
end=131072
step=2

while getopts "i:b:e:s" opt; do
    case "${opt}" in
        i)
            input=${OPTARG}
            ;;
        b)
            start=${OPTARG}
            ;;
        e)
            end=${OPTARG}
            ;;
        s)
            step=${OPTARG}
            ;;

        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ ! -f "${input}" ]; then
    echo "File ${input} does not exist!"
    exit 1
fi

n=$start

echo ""
echo "  Benchmark ${input} from ${start} to ${end} with step ${step}."
echo ""
echo "         N          Time"
echo ""

while [ $n -le $end ]; do
    t=$({((/usr/bin/time -f "%e" ./${input} $n $@)>/dev/null)} 2>&1)
    printf "  %8s  %12s\n" $n $t
    n=$((n*step))
done
