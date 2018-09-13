import numpy as np
import sys
import time


def init(width, height):
    return np.random.choice(a=[False, True], size=(height, width)), np.empty((height, width), dtype=bool)


def evolve(matrix, new_matrix):
    width, height = matrix.shape
    for y in range(height):
        for x in range(width):
            n = 0
            for y1 in range(y - 1, y + 2):
                for x1 in range(x - 1, x + 2):
                    if matrix[(y1 + height) % height][(x1 + width) % width]:
                        n += 1
            if matrix[y][x]:
                n -= 1
            new_matrix[y][x] = (n == 3 or (n == 2 and matrix[y][x]))


def game(m1, m2, iterations):
    iterations = iterations // 2
    for i in range(iterations):
        width, height = m1.shape
        for y in range(height):
            for x in range(width):
                n = 0
                for y1 in range(y - 1, y + 2):
                    for x1 in range(x - 1, x + 2):
                        if m1[(y1 + height) % height][(x1 + width) % width]:
                            n += 1
                if m1[y][x]:
                    n -= 1
                m2[y][x] = (n == 3 or (n == 2 and m1[y][x]))
        width, height = m2.shape
        for y in range(height):
            for x in range(width):
                n = 0
                for y1 in range(y - 1, y + 2):
                    for x1 in range(x - 1, x + 2):
                        if m2[(y1 + height) % height][(x1 + width) % width]:
                            n += 1
                if m2[y][x]:
                    n -= 1
                m1[y][x] = (n == 3 or (n == 2 and m2[y][x]))


def main():
    c = len(sys.argv)
    width = 5
    height = 5
    iterations = 1024 * 16 * 4 * 2
    if c > 1:
        width = int(sys.argv[1])
    if c > 2:
        height = int(sys.argv[2])
    if c > 3:
        iterations = int(sys.argv[3])

    print("Width:", width, "\tHeight:", height, "\tIterations:", iterations)
    m1, m2 = init(width, height)

    start_time = time.time()

    game(m1, m2, iterations)

    elapsed = time.time() - start_time

    print("Elapsed:", elapsed)


if __name__ == '__main__':
    main()
