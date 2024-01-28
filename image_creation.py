from PIL import Image 
import numpy as np
import random

# create a 2D list, randomize
size = 50
mat = []
# print("zeros 2d list:", mat)

# print("2d list:", mat)


# save to image
result = Image.fromarray(np.uint8(mat))
result.save("u12functions/image.png")