import sys
import time


def prime_number(n):
    total = 0
    for i in range(2, n + 1):
        prime = 1
        for j in range(2, i):
            if (i % j) == 0:
                prime = 0
                break
        total += prime
    return total


def timestamp():
    print(time.strftime("%d %B %Y %I:%M:%S %p", time.gmtime()))


def test(n_lo, n_hi, n_factor):
    print()
    print("  Call PRIME_NUMBER to count the primes from 1 to N.")
    print()
    print("         N        Pi          Time")
    print()

    n = n_lo

    while n <= n_hi:
        start_time = time.time()

        primes = prime_number(n)

        elapsed = time.time() - start_time

        print("  %8d  %8d  %14f" % (n, primes, elapsed))

        n *= n_factor


def main():
    timestamp()
    print()
    print("PRIME_TEST")

    if len(sys.argv) != 4:
        n_lo = 1
        n_hi = 131072
        n_factor = 2
    else:
        n_lo = int(sys.argv[1])
        n_hi = int(sys.argv[2])
        n_factor = int(sys.argv[3])

    test(n_lo, n_hi, n_factor)

    print()
    print("PRIME_TEST")
    print("  Normal end of execution")
    print()
    timestamp()


if __name__ == "__main__":
    main()
