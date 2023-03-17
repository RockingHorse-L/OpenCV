import numpy as np
import cv2
#创建白色的图像
# img = np.zeros((1000,1000,3), np.uint8)
# img[0:1000, 0:1000] = 255
st_p = (-1, -1)
end_p = (-1, -1)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 1000, 600)
img = cv2.imread('./bg_imgs/02.png')
def draw(event, x, y, flag, param):
    global st_p, end_p
    if event == cv2.EVENT_LBUTTONDOWN:
        st_p = (x, y)
        print(f'Down-event:{event} - x:{x} - y:{y}')

    if event == cv2.EVENT_LBUTTONUP:
        end_p = (x, y)
        print(f'UP-event:{event} - x:{x} - y:{y}')

        cv2.line(img, st_p, end_p, color=(255, 0, 0), thickness=3)
        cv2.rectangle(img, st_p, end_p, color=(0, 255, 0), thickness=3)
        cv2.circle(img, ((end_p[0]+st_p[0])//2, (end_p[1]+st_p[1])//2), (end_p[0]-st_p[0])//2,color=(0, 0, 255), thickness=3)
        cv2.imshow('img', img)
    pass
def callback(event, x, y, flags, param):
    print(param)
    draw(event, x, y, flags, param)

# 简易画板
def mouseDrawing():

    cv2.setMouseCallback('img', callback, 'hello')
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
mouseDrawing()