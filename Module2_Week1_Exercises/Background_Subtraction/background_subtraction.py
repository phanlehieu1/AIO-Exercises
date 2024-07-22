import numpy as np
import cv2
import os


def compute_difference(bg_img, input_img):
    difference = cv2.absdiff(bg_img, input_img)
    difference_single_channel = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    _, difference_binary = cv2.threshold(
        difference_single_channel, 50, 255, cv2.THRESH_BINARY)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    binary_mask_inv = cv2.bitwise_not(binary_mask)

    fg = cv2.bitwise_and(ob_image, ob_image, mask=binary_mask)
    bg = cv2.bitwise_and(bg2_image, bg2_image, mask=binary_mask_inv)
    output = cv2.add(fg, bg)

    return output


def main():
    base_path = os.path.dirname(__file__)

    green_background_path = os.path.join(base_path, 'GreenBackground.png')
    object_image_path = os.path.join(base_path, 'Object.png')
    new_background_path = os.path.join(base_path, 'NewBackground.jpg')

    bg1_image = cv2.imread(green_background_path, 1)
    if bg1_image is None:
        print(f"Failed to load image at {green_background_path}")
        return

    ob_image = cv2.imread(object_image_path, 1)
    if ob_image is None:
        print(f"Failed to load image at {object_image_path}")
        return

    bg2_image = cv2.imread(new_background_path, 1)
    if bg2_image is None:
        print(f"Failed to load image at {new_background_path}")
        return

    bg1_image = cv2.resize(bg1_image, (678, 381))
    ob_image = cv2.resize(ob_image, (678, 381))
    bg2_image = cv2.resize(bg2_image, (678, 381))

    output_image = replace_background(bg1_image, bg2_image, ob_image)
    cv2.imshow('Output Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
