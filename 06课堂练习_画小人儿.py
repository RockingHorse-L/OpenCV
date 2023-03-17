import numpy as np
import cv2
# 创建白色的图像
img = np.zeros((1000,1000,3), np.uint8)
img[0:1000, 0:1000] = 255


# 头
cv2.circle(img,(500,300), 100, (0, 0, 255), 3)
# 左眼睛
cv2.circle(img,(465,270), 20, (0, 255, 255), -1)
# 右眼睛
cv2.circle(img,(535,270), 20, (0, 255, 255), -1)

ptsEye = np.array([(430, 300), (465, 270), (500, 300), (535, 270), (565, 300)])
cv2.polylines(img, [ptsEye],isClosed=False, color=(0, 0, 0), thickness=2)

# 嘴巴
cv2.ellipse(img,(500, 340),(20,10),0,0,180,255,2)
# 身体
ptsBoby = np.array([(350, 450), (650, 450), (600, 660), (400, 660)])
cv2.polylines(img, [ptsBoby],isClosed=True, color=(0, 255, 0), thickness=3)
# 左手
ptsLHand = np.array([(350, 450), (260, 540), (170, 445)])
cv2.polylines(img, [ptsLHand],isClosed=False, color=(255, 255, 0), thickness=3)
cv2.circle(img,(145,425), 30, (0, 255, 255), 2)
# 右手
ptsRHand = np.array([(650, 450), (740, 540), (830, 445)])
cv2.polylines(img, [ptsRHand],isClosed=False, color=(255, 255, 0), thickness=3)
cv2.circle(img,(855,425), 30, (0, 255, 255), 2)
# 左腿
ptsLLeg = np.array([(400, 660), (350, 800), (400, 940)])
cv2.polylines(img, [ptsLLeg],isClosed=False, color=(255, 255, 0), thickness=3)
cv2.rectangle(img,(320, 940),(400, 980),(0, 255, 0), 3)
# 右腿
ptsRLeg = np.array([(600, 660), (650, 800), (600, 940)])
cv2.polylines(img, [ptsRLeg],isClosed=False, color=(255, 255, 0), thickness=3)
cv2.rectangle(img,(680, 940),(600, 980),(0, 255, 0), 3)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()