import time
from math import sqrt
from joblib import Parallel, delayed


def main():
    n = 10000

    start_time = time.time()

    #arr = [sqrt(i ** 2) for i in range(n)]

    arr = Parallel(n_jobs=8)(delayed(sqrt)(i ** 2) for i in range(n))

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == '__main__':
    main()
