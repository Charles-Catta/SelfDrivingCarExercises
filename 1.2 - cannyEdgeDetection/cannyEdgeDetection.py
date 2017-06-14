import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

if (len(sys.argv) != 2):
    srcImg = input("Enter the filename of the image: ")
else:
    srcImg = sys.argv[1]

# Load image and convert to grayscale
image = mpimg.imread(srcImg)
gray = cv2.cvtColor(image, cv2.COLORMAP_JET)

# Apply Gaussian blur
KERNEL_SIZE = 5

blur_gray = cv2.GaussianBlur(gray, (KERNEL_SIZE, KERNEL_SIZE), 0)

# Canny edge detection
EDGE_LOW_THRESHOLD = 50
EDGE_HIGH_THRESHOLD = 100

edges = cv2.Canny(blur_gray, EDGE_LOW_THRESHOLD, EDGE_HIGH_THRESHOLD)

# Show result
plt.imshow(edges, cmap='gray')
plt.show()
