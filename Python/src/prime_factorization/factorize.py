import sys
import time


def is_factor(n, factor):
    return n % factor == 0


def factorize(n):
    ret = []
    factor = 2
    while n > 1:
        if is_factor(n, factor):
            ret.append(factor)
            n //= factor
        else:
            factor += 1
    return ret


def main():
    argc = len(sys.argv)
    n = 10000019*10000079
    if argc > 1:
        n = int(sys.argv[1])

    start = time.time()

    num = factorize(n)

    elapsed = time.time() - start

    print("Number:", num)
    print("Elapsed:", elapsed)


if __name__ == '__main__':
    main()
