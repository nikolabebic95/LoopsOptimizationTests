#/bin/bash

usage() {
    echo "Usage: $0 -i input_file [-b <start>] [-e <end>] {<file_parameter>}" 1>&2; exit 1;
}

input="lcg"
start=1
end=256

while getopts "i:b:e:" opt; do
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

n=$start

echo ""
echo "  Benchmark ${input} from ${start} to ${end} with step 1."
echo ""
echo "         N            Ri            Time"
echo ""

while [ $n -lt $end ]; do
    unrolled="_unrolled_"
    file_name=$input$unrolled$n.py
    python3 "$file_name"
    n=$((n+1))
done
