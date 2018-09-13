import cv2 as cv
import time


def process_image():
    img = cv.imread("small_image.png")

    height, width = img.shape[:2]

    for i in range(height):
        for j in range(width):
            rgb = img[i, j]
            new_rgb = sum(rgb) // 3
            img[i, j] = [new_rgb, new_rgb, new_rgb]

    cv.imwrite("small_image_grayscale.png", img)


def main():
    start_time = time.time()

    process_image()

    elapsed = time.time() - start_time

    print(elapsed)


if __name__ == "__main__":
    main()
