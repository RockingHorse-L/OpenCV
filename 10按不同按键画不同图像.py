"""
简易画板
鼠标
位置 事件(按下去 弹起来 移动)
"""
import cv2
# 回调
st_p = (-1, -1)
end_p = (-1, -1)
img = cv2.imread('sy.png')
copyImg = img.copy()
WINDOWNAME = "board"
# 定义绘制的类型
# 绘制线
DRAWTYPELINE = 1
# 绘制线
DRAWTYPERECTANGLE = 2
# 绘制线
DRAWTYPECIRCLE = 3
# 默认绘制的类型是线
drawType = DRAWTYPELINE
"""
绘制直线
确定起始点、终点
鼠标弹起来之后进行显示(绘制)
作业1: 绘制线、矩形、圆
扩展
作业2: 扩展作业能够看见绘制的过程
"""
def drawLine(event, x, y, flags, param):
    global st_p, end_p, img
    if event == cv2.EVENT_LBUTTONDOWN:
        st_p = (x, y)
        print(f'DOWN-event:{event} - x:{x} - y:{y}')
    if event == cv2.EVENT_MOUSEMOVE:
        if st_p[0] > 0 and st_p[1] > 0:
            end_p = (x, y)
            img = copyImg.copy()
            # 频繁读取文件很好性能
            # img = cv2.imread('./media/sy.png')
            print(f'UP-event:{event} - x:{x} - y:{y}')
            cv2.line(img, st_p, end_p, color=(0, 0, 255), thickness=2)
            cv2.imshow(WINDOWNAME, img)
            pass
    if event == cv2.EVENT_LBUTTONUP:
        # 结束情况
        st_p = (-1, -1)
        # end_p = (x, y)
        # print(f'UP-event:{event} - x:{x} - y:{y}')
        # cv2.line(img, st_p, end_p, color=(0, 0, 255), thickness=2)
        # cv2.imshow(WINDOWNAME, img)
        pass
def drawRectangle(event, x, y, flags, param):
    global st_p, end_p, img
    if event == cv2.EVENT_LBUTTONDOWN:
        st_p = (x, y)
        print(f'DOWN-event:{event} - x:{x} - y:{y}')
    if event == cv2.EVENT_MOUSEMOVE:
        if st_p[0] > 0 and st_p[1] > 0:
            end_p = (x, y)
            img = copyImg.copy()
            # 频繁读取文件很好性能
            # img = cv2.imread('./media/sy.png')
            print(f'UP-event:{event} - x:{x} - y:{y}')
            cv2.rectangle(img, st_p, end_p, color=(0, 0, 255), thickness=2)
            cv2.imshow(WINDOWNAME, img)
            pass
    if event == cv2.EVENT_LBUTTONUP:
        # 结束情况
        st_p = (-1, -1)
        # end_p = (x, y)
        # print(f'UP-event:{event} - x:{x} - y:{y}')
        # cv2.line(img, st_p, end_p, color=(0, 0, 255), thickness=2)
        # cv2.imshow(WINDOWNAME, img)
        pass
def callback(event, x, y, flags, param):
    if drawType == DRAWTYPELINE:
        drawLine(event, x, y, flags, param)
    elif drawType == DRAWTYPERECTANGLE:
        drawRectangle(event, x, y, flags, param)
    elif drawType == DRAWTYPECIRCLE:
        pass
    else:
        pass
# 简易画板
def mouseDrawing():
    global drawType
    cv2.namedWindow(WINDOWNAME, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('board', 1000, 600)
    # img = cv2.imread('./media/sy.png')
    # 参数1： windowName
    # 参数2: onMouse 函数
    # 参数3： param 参数
    # 将函数callback注册在窗口(board)上 我想要得到那些信息 event x y flags params
    cv2.setMouseCallback(WINDOWNAME, callback, 'hello')
    cv2.imshow(WINDOWNAME, img)
    while True:
        key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('l'):
            drawType = DRAWTYPELINE
            pass
        elif key == ord('r'):
            drawType = DRAWTYPERECTANGLE
            pass
        elif key == ord('c'):
            drawType = DRAWTYPECIRCLE
            pass
        else:
            pass
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
mouseDrawing()