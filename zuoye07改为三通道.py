import cv2
import numpy as np


class FaceDetect:
    def __init__(self):
        self.faceImg = cv2.imread('sy.jpg')
        self.logoImg = cv2.imread('logo.jpg')
        # 创建一个级联分类器 用来识别人脸
        self.classifier = cv2.CascadeClassifier()
        # 识别嘴部
        self.classifierMouth = cv2.CascadeClassifier()
        # 识别眼睛
        self.classifierEye = cv2.CascadeClassifier()
        # 加载特征文件
        self.classifier.load('haarcascade_frontalface_alt.xml')
        self.classifierMouth.load('haarcascade_mcs_mouth.xml')
        self.classifierEye.load('haarcascade_eye.xml')

        pass

    def faceDetect(self):
        # 赋值
        # self.faceImg = faceImg
        faceImg = self.faceImg
        classifier = self.classifier
        # 识别图像中的人脸 返回矩形区域 使用list存储
        faceRects = classifier.detectMultiScale(faceImg)
        # 列表里面前面两个是左上角,后面两个是宽高的距离
        print(faceRects)
        for x, y, w, h in faceRects:
            cv2.rectangle(faceImg, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
            rect = (x, y, w, h)
            self.drawLogoMethod02(self.logoImg, rect)
            self.mouthDetect(rect)
            self.eyeDetect(rect)
            #self.drawLogo(self.logoImg,rect)
        pass

    def mouthDetect(self, faceRect):
        """
        最不区域的检测
        :return:
        """
        mouthRects = self.classifierMouth.detectMultiScale(self.faceImg)
        # 绘制嘴部区域
        faceX = faceRect[0]
        faceY = faceRect[1]
        faceW = faceRect[2]
        faceH = faceRect[3]
        for x, y, w, h in mouthRects:
            # 排除非嘴部的区域
            faceMinX = faceX
            faceMaxX = faceX + faceW
            # 左右两边非嘴部区域
            if x < faceMinX or x > faceMaxX:
                continue
            faceMinY = faceY
            faceMaxY = faceY + faceH
            if y < faceMinY or y > faceMaxY:
                continue
            # 排除脸部区域内的非嘴部区域
            mouthMinY = faceY + faceH * 0.6
            if y < mouthMinY:
                continue
            cv2.rectangle(self.faceImg, (x, y), (x+w, y+h),color=(0, 0, 255),thickness=3)
            rect = (x, y+h//2, w, h+h//2)
            self.drawLogoMethod02(self.logoImg, rect)
            pass

    def eyeDetect(self, faceRect):
        eyeRects = self.classifierEye.detectMultiScale(self.faceImg)
        faceX = faceRect[0]
        faceY = faceRect[1]
        faceW = faceRect[2]
        faceH = faceRect[3]
        for x, y, w, h in eyeRects:
            faceMinX = faceX
            faceMaxX = faceX + faceW
            # 左右两边非眼部区域
            if x < faceMinX or x > faceMaxX:
                continue
            faceMinY = faceY
            faceMaxY = faceY + faceH
            if y < faceMinY or y > faceMaxY:
                continue
            eyeMinY = faceY + faceH * 0.5
            if y > eyeMinY:
                continue
            cv2.rectangle(self.faceImg, (x, y), (x+w, y+h), color=(0, 255, 0), thickness=3)
            rect = (x, y ,w ,h)
            self.drawLogoMethod02(self.logoImg, rect)
            pass

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
        cv2.imshow('faceImg', self.faceImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass

    def drawLogoMethod02(self, logo, faceRect=None):
        """
        绘制logo效果2
        1. 找轮廓
        将RGB彩色图 转换为单通道的灰度图 logoGray 0-255
        将灰度图转换为二值图 0/255
        2. 找轮廓
        3. 绘制轮廓
        """
        # 参数1：被转换的图像
        # 参数2：将RGB转换为Gray
        logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        #logoRBG = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
        # 将灰度图转换为二值图 0/255
        # 参数1：被转换的图像
        # 参数2：阈值 180 小于阈值就是0
        # 参数3: 255 大于阈值就是255
        # 参数4: 阈值类型 cv2.THRESH_BINARY
        # retval, logoBinary = cv2.threshold(logoRBG, 100, 255, cv2.THRESH_BINARY)
        # cv2.THRESH_OTSU 自适应阈值
        retval, logoBinary = cv2.threshold(logoGray, 100, 255, cv2.THRESH_OTSU)
        #print(retval)
        # print(logoBinary)
        # 2、找轮廓
        # 参数1：被查找的图像
        # 参数2：轮廓的存放层级关系
        # 参数3：存储轮廓的拐角点
        image, contours, hierarchy = cv2.findContours(logoBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 3. 绘制轮廓
        # 创建一个黑色背景图
        #print(f'logoBinary.shape:{logoGray.shape}')
        mask_RGB = cv2.merge([logoBinary, logoBinary, logoBinary])
        mask = np.zeros(mask_RGB.shape, dtype=np.uint8)
        cv2.imshow('mask', mask)
        cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)
        cv2.imshow('mask1', mask)
        #缩放的比例 ratio = h/ w
        ratio = logo.shape[0] / logo.shape[1]
        faceX = faceRect[0]
        faceY = faceRect[1]
        faceW = faceRect[2]
        # 设置为一个正方形再乘以比例，这样好一点
        faceH = int(faceRect[3] * ratio)
        smollLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smollmask = cv2.resize(mask, dsize=(faceW, faceH))
        smollmaskH, smollmaskW = smollmask.shape[:2]
        # 返回255的索引
        index = np.where(smollmask == 255)
        # 将所有255的坐标调整一下，再将索引对应的值重新赋值给新坐标
        self.faceImg[index[0]+faceY-smollmaskH, index[1]+faceX] = smollLogo[index[0], index[1]]
        pass


dect = FaceDetect()
dect.faceDetect()
cv2.imshow('logo', dect.faceImg)
cv2.waitKey(0)
cv2.destroyAllWindows()