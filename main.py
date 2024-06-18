from PIL import Image
import numpy as np
from skimage import filters, morphology, measure
import matplotlib.pyplot as plt


image = np.array(Image.open('figure2.jpg'))


gray_image = np.mean(image, axis=2)


white_threshold = 180
binary_image = gray_image > white_threshold


binary_image = morphology.remove_small_objects(binary_image, min_size=100)


labeled_image = measure.label(binary_image)


num_persons = 0
for region in measure.regionprops(labeled_image):
    if region.area > 100:
        num_persons += 1
        minr, minc, maxr, maxc = region.bbox
        rect = plt.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
        plt.gca().add_patch(rect)


plt.imshow(image)
plt.title('Image with Bounding Boxes')
plt.axis('off')
plt.show()

print("Number of persons detected:", num_persons)
