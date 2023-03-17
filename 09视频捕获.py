"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""

import cv2
from  face_detect import FaceDetect
class HandleCapture:
    def __init__(self):
        self.faceDetect = FaceDetect()
        self.faceVideo = cv2.VideoCapture('testVideo.mp4')
        pass

    def videoDetect(self):
        faceVideo = self.faceVideo
        while True:
            retval, image = faceVideo.read()
            self.faceDetect.faceDetect(image)
            cv2.imshow('image', image)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        # 释放支援
        faceVideo.release()
        cv2.destroyAllWindows()
        pass
capture = HandleCapture()
capture.videoDetect()


