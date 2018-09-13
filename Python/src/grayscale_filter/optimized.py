import cv2 as cv
import time


def process_image():
    img = cv.imread("small_image.png")

    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imwrite("small_image_optimized.png", gray_image)


def main():
    start_time = time.time()

    process_image()

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == "__main__":
    main()
