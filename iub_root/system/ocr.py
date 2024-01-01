import cv2
from pytesseract import *


def ocr(image):
    image_path = "image.jpg"

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, lang="eng")

    print("Extracted Text:")
    print(text)
    cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fun():
    import cv2
    import numpy as np

    # Load the image
    image = cv2.imread("IMG_20230313_225001_293.jpg")

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load the image.")
    else:
        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get the height and width of the image
        height, width = grayscale_image.shape

        # Create a mirror image by copying the upper half to the lower half (mirrored)
        mirror_image = np.copy(grayscale_image)

        # Mirror the upper half to the lower half
        mirror_image[: height // 2, :] = np.flipud(grayscale_image[: height // 2, :])

        # Save the mirrored image to disk
        cv2.imwrite("mirrored_image.jpg", mirror_image)

        # Display the mirrored image (optional)
        cv2.imshow("Mirrored Image", mirror_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


fun()
