"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""

import cv2

class FaceDetect:
    def __init__(self):
        self.faceImg = cv2.imread('sy.jpg')
        self.logoImg = cv2.imread('logo.jpg')
        # 创建一个级联分类器 用来识别人脸
        self.classifier = cv2.CascadeClassifier()
        # 加载特征文件
        self.classifier.load('haarcascade_frontalface_alt.xml')

        pass

    def faceDetect(self):
        # 赋值
        faceImg = self.faceImg
        classifier = self.classifier
        # 识别图像中的人脸 返回矩形区域 使用list存储
        faceRects = classifier.detectMultiScale(faceImg)
        # 列表里面是左上角 和右下角
        print(faceRects)
        for x, y, w, h in faceRects:
            cv2.rectangle(faceImg, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
            rect = (x, y, w, h)
            self.drawLogo(self.logoImg,rect)
        pass


    # def videoDetect(self):
    #     faceVideo = self.faceVideo
    #     classifier = self.classifier
    #     while True:
    #         retval, image = faceVideo.read()
    #         faceRects = classifier.detectMultiScale(image)
    #         for x, y, w, h in faceRects:
    #             cv2.rectangle(image, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
    #             rect = (x, y, w, h)
    #             self.drawLogo(self.logoImg, rect)
    #         cv2.imshow('image', image)
    #
    #         key = cv2.waitKey(1)
    #         if key == ord('q'):
    #             break
    #         # 释放支援
    #         #faceVideo.release()
    #     pass

    def drawLogo(self, logo, faceRects):
        # 缩放的比例 ratio = h/ w
        ratio = logo.shape[0] / logo.shape[1]
        faceX = faceRects[0]
        faceY = faceRects[1]
        faceW = faceRects[2]
        # 设置为一个正方形再乘以比例，这样好一点
        faceH = int(faceW * ratio)

        smallLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smallLogoH = smallLogo.shape[0]
        smallLogoW = smallLogo.shape[1]
        #矩阵之间赋值
        for row in range(smallLogoH):
            for col in range(smallLogoW):
                self.faceImg[faceY+row-smallLogoH, faceX+col] = smallLogo[row,col]

detect = FaceDetect()
detect.faceDetect()
# detect.videoDetect()
cv2.imshow('faceImg', detect.faceImg)
cv2.waitKey(0)
cv2.destroyAllWindows()