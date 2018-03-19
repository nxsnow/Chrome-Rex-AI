from PIL import Image
from PIL import ImageGrab
import numpy as np
import matplotlib.pyplot as plt
def get_dis():
    DEBUG = False
    coordinate = (150, 150, 550,360)
    pic = ImageGrab.grab(coordinate)
    img=np.array(pic)
    x = 88
    y = 146
    y2 = 115
    dx = x
    base_color = img[5][5][0]
    while (dx <= 300):
        dx += 2
        if (abs(img[y][dx][0] - base_color) >= 5):
            return [dx-x,0]
    if (DEBUG):
        print(img[y][x])
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    return [300,0]
def get_over():
    coordinate = (150, 150, 550, 360)
    pic = ImageGrab.grab(coordinate)
    img = np.array(pic)
    base_color = img[5][5][0]
    DEBUG = False
    if (DEBUG):
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    if (abs(img[76][286][0] - base_color)>= 5 and abs(img[81][130][0] - base_color)>= 5):
        return True
    else:
        return False