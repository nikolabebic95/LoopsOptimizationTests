import sys
import time


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    argc = len(sys.argv)
    n = 500_000
    if argc > 1:
        n = int(sys.argv[1])

    start = time.time()

    num = fibonacci(n)

    elapsed = time.time() - start

    print("Number:", num)
    print("Elapsed:", elapsed)


if __name__ == '__main__':
    main()
