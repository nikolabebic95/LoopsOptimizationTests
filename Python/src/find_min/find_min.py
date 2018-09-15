import sys
import numpy as np
import time


def find_min(arr, n):
    for i in range(n):
        if i == 0:
            m = arr[i]
        elif arr[i] < m:
            m = arr[i]
    return m


def generate_arr(n):
    return np.random.rand(n)


def timestamp():
    print(time.strftime("%d %B %Y %I:%M:%S %p", time.gmtime()))


def test(n_lo, n_hi, n_factor, arr):
    print()
    print("  Call FIND_MIN to find the minimum from 0 to N - 1.")
    print()
    print("         N        Min         Time")
    print()

    n = n_lo

    while n <= n_hi:
        start_time = time.time()

        m = find_min(arr, n)

        elapsed = time.time() - start_time

        print("  %8d  %8f  %14f" % (n, m, elapsed))

        n *= n_factor


def main():
    timestamp()
    print()
    print("MIN_TEST")

    if len(sys.argv) != 4:
        n_lo = 1
        n_hi = 33554432
        n_factor = 2
    else:
        n_lo = int(sys.argv[1])
        n_hi = int(sys.argv[2])
        n_factor = int(sys.argv[3])

    arr = generate_arr(n_hi)
    print("Array generated")

    test(n_lo, n_hi, n_factor, arr)
    print()
    print("MIN_TEST")
    print("  Normal end of execution")
    print()
    timestamp()


if __name__ == '__main__':
    main()
