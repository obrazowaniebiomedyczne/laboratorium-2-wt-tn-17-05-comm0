import numpy as np
import cv2


def func(index, cv2, kernel, img):
    if (index == 1):
        img.append(cv2.imread('figures/crushed.png', 0))
    else:
        img.append(cv2.imread('figures/crushed'+str(index)+'.png', 0))

    opening = cv2.morphologyEx(img[index-1], cv2.MORPH_OPEN, kernel, iterations=1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=2)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel, iterations=3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    if (index == 1):
        cv2.imwrite('results/crushed.jpg', closing)
    else:
        cv2.imwrite('results/crushed'+str(index)+'.png', closing)



# Zadanie na ocene dostateczna
def renew_pictures():
    img = []
    kernel = np.ones((3,3),np.uint8)

    for i in range(1, 5):
        func(i, cv2, kernel, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


# Zadanie na ocene dobra
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    # ---------------
    # Do uzupelnienia
    # ---------------

    return new_image


# Zadanie na ocene bardzo dobra
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    # ---------------
    # Do uzupelnienia
    # ---------------

    return new_image
