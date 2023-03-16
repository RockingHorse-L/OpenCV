import random
import cv2

# 设置画布
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# 设置画布大小
cv2.resizeWindow('img', 1000, 600)
# 读取图片
xhrImg = cv2.imread('./xhr_imgs/02.png')
bgImg = cv2.imread('./bg_imgs/02.png')
# 获取形状
h, w, c = xhrImg.shape
# 缩小图片
xhrImage = cv2.resize(xhrImg, dsize=(100, int(w * 0.08)))
xhrImageH, xhrImageX = xhrImage.shape[:2]
# 设置随机坐标
y = random.randint(0, h - xhrImageH)
x = random.randint(0, w - xhrImageX)
y1 = y+xhrImageH
x1 = x+xhrImageX
# 粘贴图片
bgImg[y:y1,x:x1] = xhrImage[:xhrImageH, :xhrImageX]
cv2.imshow('img', bgImg)
cv2.waitKey()
cv2.destroyAllWindows()