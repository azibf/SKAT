import cv2
import numpy as np
from random import choice, randint
from hashlib import sha256


dict_letters = {"1": "letters/1.png",
                "2": "letters/2.png",
                "3": "letters/3.png",
                "4": "letters/4.png",
                "5": "letters/5.png",
                "6": "letters/6.png",
                "7": "letters/7.png",
                "8": "letters/8.png",
                "9": "letters/9.png",
                "10": "letters/10.png",
                "11": "letters/11.png",
                "12": "letters/12.png",
                "13": "letters/13.png",
                "14": "letters/14.png",
                "15": "letters/15.png",
                "16": "letters/16.png",
                "17": "letters/17.png",
                "18": "letters/18.png",
                "19": "letters/19.png",
                "20": "letters/20.png",
                "21": "letters/21.png",
                "22": "letters/22.png",
                "23": "letters/23.png",
                "24": "letters/24.png",
                "25": "letters/25.png",
                "26": "letters/26.png",
                "27": "letters/27.png",
                "28": "letters/28.png",
                "29": "letters/29.png",
                "30": "letters/30.png",
                "31": "letters/31.png",
                "32": "letters/32.png",
                "33": "letters/33.png",
                "34": "letters/34.png",
                "35": "letters/35.png",
                "36": "letters/36.png",
                }


def img_create():
    for i in range(randint(1, 20)):
        image = cv2.imread(f'letters/{randint(1, 36)}.png', cv2.IMREAD_UNCHANGED)
        trans_mask = image[:, :, 3] == 0
        image[trans_mask] = [255, 255, 255, 255]
        circle = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        image = cv2.imread(f'letters/{randint(1, 36)}.png', cv2.IMREAD_UNCHANGED)
        trans_mask = image[:, :, 3] == 0
        image[trans_mask] = [255, 255, 255, 255]
        star = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        subtracted = cv2.subtract(circle, star)
        subtracted = cv2.bitwise_not(cv2.blur(subtracted, (18, 18)))
        subtracted[np.where((subtracted != [255, 255, 255]).all(axis=2))] = [0, 0, 0]
        cv2.imwrite(f'training_images/{sha256(bytes(subtracted))}.png', subtracted)