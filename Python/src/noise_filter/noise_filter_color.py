import cv2 as cv
import time
import numpy as np


def process_image():
    img = cv.imread("image_color.jpg")

    height, width = img.shape[:2]

    new_img = np.empty((height, width, 3), np.uint8)

    n = 10

    for k in range(n):
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                members = [img[i - 1, j - 1], img[i - 1, j], img[i - 1, j + 1], img[i, j - 1], img[i, j], img[i, j + 1],
                           img[i + 1, j - 1], img[i + 1, j], img[i + 1, j + 1]]

                members.sort(key=lambda x: int(x[0]))
                new_img[i, j, 0] = members[4][0]

                members.sort(key=lambda x: int(x[1]))
                new_img[i, j, 1] = members[4][1]

                members.sort(key=lambda x: int(x[2]))
                new_img[i, j, 2] = members[4][2]

        img = new_img
        print("Finished iteration " + str(k + 1))

    cv.imwrite("image_color_without_noise_" + str(n) + ".jpg", new_img)


def main():
    start_time = time.time()

    process_image()

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == "__main__":
    main()
