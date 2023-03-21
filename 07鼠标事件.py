"""
    简易画板
    鼠标
    位置 坐标（按下去 弹起来 移动）
"""

import cv2

# 回调
"""
    绘制直线
    确定起始点、终点
    鼠标弹起来之后进行显示(绘制)
    
    作业1：绘制线， 矩形， 圆
    拓展
    作业2：绘制线，要看到过程
"""
st_p = (-1, -1)
end_p = (-1, -1)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 1000, 600)
img = cv2.imread('./bg_imgs/02.png')
def drawLine(event, x, y, flags, param):
    global st_p, end_p
    if event == cv2.EVENT_LBUTTONDOWN:
        st_p = (x, y)
        print(f'Down-event:{event} - x:{x} - y:{y}')

    if event == cv2.EVENT_LBUTTONUP:
        end_p = (x, y)
        print(f'UP-event:{event} - x:{x} - y:{y}')
        cv2.line(img, st_p, end_p, color=(0, 0, 255), thickness=2)
        cv2.imshow('img',  img)
    pass
def callback(event, x, y, flags, param):
    print(param)
    drawLine(event, x, y, flags, param)

# 简易画板
def mouseDrawing():

    cv2.setMouseCallback('img', callback, 'hello')
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
mouseDrawing()