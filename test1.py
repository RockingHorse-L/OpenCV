import cv2
import numpy as np


class FaceIndeitify:
    def __init__(self):
        self.faceImg = cv2.imread('sy.jpg')
        self.glassImg = cv2.imread('glass.jpg')
        self.loveImg = cv2.imread('love.jpg')
        self.classifierFace = cv2.CascadeClassifier()
        self.classifierEye = cv2.CascadeClassifier()
        self.classifierFace.load('haarcascade_frontalface_alt.xml')
        self.classifierEye.load('haarcascade_eye.xml')

    def faceDetect(self):
        faceRect = self.classifierFace.detectMultiScale(self.faceImg)
        for x, y, w, h in faceRect:
            rect = (x, y, w, h)
            self.eyeDetect(rect)
            pass

    def eyeDetect(self, rect):
        eyeRect = self.classifierEye.detectMultiScale(self.faceImg)
        faceX = rect[0]
        faceY = rect[1]
        faceW = rect[2]
        faceH = rect[3]
        global eyePoints,data
        eyePoints = []
        data = []
        for x, y, w, h in eyeRect:
            faceMinX = faceX
            faceMaxX = faceX + faceW
            if x < faceMinX or x > faceMaxX:
                continue
            faceMinY = faceY
            faceMaxY = faceY + faceH
            if y < faceMinY or y > faceMaxY:
                continue
            eyeMin = faceY + faceH * 0.5
            if y > eyeMin:
                continue
            rect = (x, y, w, h)
            eyePoints.append(rect)
        # [(511, 255, 69, 69), (408, 262, 67, 67)]
        # print(eyePoint)
        for eyePoint in eyePoints:
            for point in eyePoint:
                data.append(point)
        self.drawGlass(self.glassImg, (data[4], data[5], data[6], data[7]), (data[0], data[1], data[2], data[3]))
        for x, y, w, h in eyeRect:
            faceMinX = faceX
            faceMaxX = faceX + faceW
            if x < faceMinX or x > faceMaxX:
                continue
            faceMinY = faceY
            faceMaxY = faceY + faceH
            if y < faceMinY or y > faceMaxY:
                continue
            eyeMin = faceY + faceH * 0.5
            if y > eyeMin:
                continue
            print(x, y, w, h)
            cv2.rectangle(self.faceImg, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
            rect = (x, y, w, h)
            self.drawLogo(self.loveImg, rect)

        pass

    def drawLogo(self, logo, rect):
        logoGary = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        retval, logoB = cv2.threshold(logoGary, 100, 255, cv2.THRESH_OTSU)
        imgae, contours, hierarchy = cv2.findContours(logoB, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(logoGary.shape, dtype=np.uint8)
        cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)
        ratio = logo.shape[0] / logo.shape[1]
        faceX = rect[0]
        faceY = rect[1]
        faceW = rect[2]
        faceH = int(rect[3] * ratio)
        smollLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smollmask = cv2.resize(mask, dsize=(faceW, faceH))
        smollmaskH, smollmaskW = smollmask.shape[:2]
        for row in range(smollmaskH):
            for col in range(smollmaskW):
                if smollmask[row, col] == 255:
                    self.faceImg[faceY + row, faceX + col] = smollLogo[row, col]
        pass

    def drawGlass(self, image, rect, point):
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        retval, logoB = cv2.threshold(imageGray, 100, 255, cv2.THRESH_OTSU)
        img, contours, hierarchy = cv2.findContours(logoB, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(imageGray.shape, dtype=np.uint8)
        cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)
        eyeX = rect[0]
        eyeY = rect[1]
        pointX = point[0] + point[2]
        pointY = point[1] + point[3]
        smollGlass = cv2.resize(image, dsize=(pointX - eyeX, pointY - eyeY))
        smollmask = cv2.resize(mask, dsize=(pointX - eyeX, pointY - eyeY))
        smollmaskH, smollmaskW = smollmask.shape[:2]
        for row in range(smollmaskH):
            for col in range(smollmaskW):
                if smollmask[row, col] == 255:
                    self.faceImg[eyeY + row, eyeX + col] = smollGlass[row, col]
        pass

detect = FaceIndeitify()
detect.faceDetect()
cv2.imshow('img', detect.faceImg)
cv2.waitKey(0)
cv2.destroyAllWindows()