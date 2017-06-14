import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

if (len(sys.argv) != 2):
    srcImg = input("Enter the name of the image file: ")
else:
    srcImg = sys.argv[1]

image = mpimg.imread(srcImg)

y_size = image.shape[0]
x_size = image.shape[1]

print("Loaded", srcImg, "with dimensions", x_size, "x", y_size)

color_select = np.copy(image)
line_image = np.copy(image)


# Define color thresholds
R_THRESHOLD = 210
G_THRESHOLD = 210
B_THRESHOLD = 210

# Masking area of interest (triangle)

X_APEX_POS = 0.5
Y_APEX_POS = 0.57       # Percentage from top

left_bottom = [0, y_size]
right_bottom = [x_size, y_size]
apex = [X_APEX_POS * x_size, Y_APEX_POS * y_size]

# Fit linearly all the sides of the triangle
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Get pixels below RGB threshold
color_thresholds = (image[:, :, 0] < R_THRESHOLD) | (image[:, :, 1] < G_THRESHOLD) \
        | (image[:, :, 2] < B_THRESHOLD)

# Get the enclosing region
XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))


# Black/Mask out anything below RGB threshold
color_select[color_thresholds] = [0, 0, 0]


# Apply mask to image
line_image[~color_thresholds & region_thresholds] = [255, 0, 0]

plt.imshow(line_image)
plt.show()
