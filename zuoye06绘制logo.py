"""
    先读取主图、和logo
    设置分类器
    加载特征文件
    识别主图人像
    计算切片区域，进行切片
    讲切片区域赋值为logo
"""
import cv2


class FaceDetect:
    def __init__(self):
        self.faceImg = cv2.imread('sy.jpg')
        self.logoImg = cv2.imread('logo.jpg')
        self.classifier = cv2.CascadeClassifier()
        self.classifier.load('haarcascade_frontalface_alt.xml')

    def faceIdentify(self):
        faceImg = self.faceImg
        classifier = self.classifier
        faceRects = classifier.detectMultiScale(faceImg)

        for x, y, w, h in faceRects:
            cv2.rectangle(faceImg, (x, y), (x+w, y+w), (0, 0, 255), 3)
            rect = (x, y, w, h)
            self.drawLog(self.logoImg, rect)

    def drawLog(self, logo, rect):
        ratio = logo.shape[0] / logo.shape[1]
        faceX = rect[0]
        faceY = rect[1]
        faceW = rect[2]
        faceH = int(faceW * ratio)

        smallLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smallLogoH = smallLogo.shape[0]
        print(smallLogo)
        self.faceImg[faceY - smallLogoH:faceY + faceH - smallLogoH,faceX:faceX + faceW] = smallLogo

detect = FaceDetect()
detect.faceIdentify()
cv2.imshow('faceImg', detect.faceImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
