import cv2 as cv
import time


def process_image():
    file = "hram"
    img = cv.imread(file + ".jpg")

    height, width = img.shape[:2]

    for i in range(height):
        for j in range(width):
            bgr = img[i, j]
            new_bgr = 0.11 * bgr[0] + 0.59 * bgr[1] + 0.3 * bgr[2]
            img[i, j] = [new_bgr, new_bgr, new_bgr]

    cv.imwrite(file + "_grayscale.jpg", img)


def main():
    start_time = time.time()

    process_image()

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == "__main__":
    main()
