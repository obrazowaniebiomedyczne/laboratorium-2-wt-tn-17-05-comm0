from solution import *
from obpng import read_png, write_png
import cv2 


print("- Ocena dostateczna")
renew_pictures()



print("- Ocena dobra")
image = cv2.imread("figures/result.png", 0)
# own_simple_erosion(image)
cv2.imwrite("figures/own_erosion.png", own_simple_erosion(image))




print("- Ocena bardzo dobra")
# read_png("figures/crushed.png")
# kernel = np.array([[0, 1, 1, 1, 0],
#                    [0, 1, 1, 1, 0],
#                    [1, 1, 1, 1, 1],
#                    [0, 1, 1, 1, 0],
#                    [0, 1, 1, 1, 0]])
# cv2.imwrite("figures/own_erosionzkernelem.png", own_erosion(image,kernel))
# # erosion = own_erosion(image, kernel)
# # write_png("results/own_erosion.png")

