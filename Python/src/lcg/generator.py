import sys
import re


def main():
    file="lcg.py"
    n=256

    if len(sys.argv) > 1:
        file=sys.argv[1]
    if len(sys.argv) > 2:
        n=int(sys.argv[2])

    file = re.sub("(.*)\\.py", "\\1", file)

    start = """import sys
import time


def lcg_random(seed, a, c, m, n):"""

    loop = "        seed = (a * seed + c) % m"

    start_main = """    return seed


def main():"""

    end_main = """    argc = len(sys.argv)
    n = 10_000_000
    seed = 0
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    if argc > 1:
        n = int(sys.argv[1])
    if argc > 2:
        seed = int(sys.argv[2])
    if argc > 3:
        a = int(sys.argv[3])
    if argc > 4:
        c = int(sys.argv[4])
    if argc > 5:
        m = int(sys.argv[5])

    start = time.time()

    num = lcg_random(seed, a, c, m, n)

    elapsed = time.time() - start

    print("  %8d  %12d  %14f" % (k, num, elapsed))


if __name__ == '__main__':
    main()
"""

    for i in range(2, n):
        file_name = "%s_unrolled_%d.py" % (file, i)
        prologue_bound = "    for i in range(n %% %d):" % i
        loop_bound = "    for i in range(n // %d):" % i
        k_line = "    k = %d" % i
        with open(file_name, "w") as out_file:
            print(start, file=out_file)
            print(prologue_bound, file=out_file)
            print(loop, file=out_file)
            print(loop_bound, file=out_file)
            for j in range(i):
                print(loop, file=out_file)
            print(start_main, file=out_file)
            print(k_line, file=out_file)
            print(end_main, file=out_file)


if __name__ == '__main__':
    main()
