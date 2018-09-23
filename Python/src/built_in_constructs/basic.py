import sys
import numpy as np
import time


def f(arr):
    s = 0
    for i in range(len(arr)):
        s += i * arr[i]
    return s


def generate_arr(n):
    return np.random.rand(n)


def timestamp():
    print(time.strftime("%d %B %Y %I:%M:%S %p", time.gmtime()))


def test(n_lo, n_hi, n_factor):
    print()
    print("  Call F to find the minimum from 0 to N - 1.")
    print()
    print("         N                     Sum         Time")
    print()

    n = n_lo

    while n <= n_hi:
        arr = generate_arr(n)

        start_time = time.time()

        m = f(arr)

        elapsed = time.time() - start_time

        print("  %8d  %22f  %14f" % (n, m, elapsed))

        n *= n_factor


def main():
    timestamp()
    print()
    print("FOR_TEST")

    if len(sys.argv) != 4:
        n_lo = 1
        n_hi = 8388608
        n_factor = 2
    else:
        n_lo = int(sys.argv[1])
        n_hi = int(sys.argv[2])
        n_factor = int(sys.argv[3])

    test(n_lo, n_hi, n_factor)
    print()
    print("FOR_TEST")
    print("  Normal end of execution")
    print()
    timestamp()


if __name__ == '__main__':
    main()
