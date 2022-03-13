import numpy as np
from PIL import Image
import math

image = np.array(Image.open("C:/Users/joann/Desktop/5616.jpg"))

ori_center_height = round(image.shape[0] / 2)
ori_center_width = round(image.shape[1] / 2)  

def rotate(array, angle_in_degrees):
    import itertools
    (h, w) = array.shape[:2]

    angle = angle_in_degrees * math.pi / 180
    (cosine, sine) = np.cos(angle), np.sin(angle)
    rotation_matrix = [[cosine, sine], [-sine, cosine]]

    new_height = round(abs(image.shape[0] * cosine) + abs(image.shape[1] * sine))
    new_width = round(abs(image.shape[1] * cosine) + abs(image.shape[0] * sine))

    result = np.zeros(new_height, new_width, image.shape[2])

    new_center_height = round(new_height / 2)
    new_center_width = round(new_width / 2)

    for i, j in itertools.product(range(w), range(h)):
        y = image.shape[0] - 1 - j - ori_center_height
        x = image.shape[1] - 1 - i - ori_center_width
        #pixels = array[y, x, :]

        new_x, new_y = np.matmul(rotation_matrix, [x, y])
        new_x, new_y = int(new_x), int(new_y)

        new_y = new_center_height - new_y
        new_x = new_center_width - new_x

        if 0 <= new_x < new_width and 0 <= new_y < new_height:
            result[new_y, new_x, :] = image[j, i,:]

    return result

output = rotate(image, 45)

output=Image.fromarray((output).astype(np.uint8))
output.save("rotated_image.png")