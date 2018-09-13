import cv2 as cv
import time
import math
import numpy as np


def process_image():
    img = cv.imread("image.jpeg")

    height, width = img.shape[:2]

    new_img = np.empty((height, width, 3), np.uint8)

    for y in range(1, height - 1):
        for x in range(1, width - 1):

            # initialise Gx to 0 and Gy to 0 for every pixel
            Gx = 0
            Gy = 0

            # top left pixel
            p = img[y - 1, x - 1]
            r = p[0]
            g = p[1]
            b = p[2]

            # intensity ranges from 0 to 765 (255 * 3)
            intensity = (int(r) + int(g) + int(b))

            # accumulate the value into Gx, and Gy
            Gx += -intensity
            Gy += -intensity

            # remaining left column
            p = img[y, x - 1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -2 * (int(r) + int(g) + int(b))

            p = img[y + 1, x - 1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -(int(r) + int(g) + int(b))
            Gy += (int(r) + int(g) + int(b))

            # middle pixels
            p = img[y - 1, x]
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += -2 * (int(r) + int(g) + int(b))

            p = img[y + 1, x]
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += 2 * (int(r) + int(g) + int(b))

            # right column
            p = img[y - 1, x + 1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (int(r) + int(g) + int(b))
            Gy += -(int(r) + int(g) + int(b))

            p = img[y, x + 1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += 2 * (int(r) + int(g) + int(b))

            p = img[y + 1, x + 1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (int(r) + int(g) + int(b))
            Gy += (int(r) + int(g) + int(b))

            # calculate the length of the gradient (Pythagorean theorem)
            length = math.sqrt((Gx * Gx) + (Gy * Gy))

            # normalise the length of gradient to the range 0 to 255
            length = length / 4328 * 255

            length = int(length)

            # draw the length in the edge image
            new_img[y, x] = [length, length, length]

    cv.imwrite("image_edges.jpeg", new_img)


def main():
    start_time = time.time()

    process_image()

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == "__main__":
    main()
