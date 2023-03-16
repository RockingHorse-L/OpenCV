import cv2
import numpy as np

img = cv2.imread('./bg_imgs/02.png')
h, w, c = img.shape
imgDataList = []
height = [h//2, h]
width = [w//2, w]
for row in height:
    for col in width:
        if row == h and col == w:
            imgCrop = img[h//2:row, w//2:col]
            data = np.array(imgCrop)
            imgDataList.append(data)
            # cv2.imshow('img', imgCrop)
        elif col == w:
            imgCrop = img[:row, w//2:col]
            data = np.array(imgCrop)
            imgDataList.append(data)
            # cv2.imshow('img', imgCrop)
        elif row == h:
            imgCrop = img[h//2:row,:col]
            data = np.array(imgCrop)
            imgDataList.append(data)
            # cv2.imshow('img', imgCrop)
        else:
            imgCrop = img[:row,:col]
            data = np.array(imgCrop)
            imgDataList.append(data)
        #     cv2.imshow('img', imgCrop)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
print(imgDataList)
imgDataUp = np.concatenate((imgDataList[0], imgDataList[1]), axis=1)
imgDataDown = np.concatenate((imgDataList[2], imgDataList[3]), axis=1)
oriImageData = np.concatenate((imgDataUp, imgDataDown), axis=0)
cv2.imshow('img', oriImageData)
cv2.waitKey()
cv2.destroyAllWindows()