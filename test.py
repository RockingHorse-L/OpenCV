import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 1000, 600)
img = cv2.imread('sy.jpg')
sta_p = -1
end_p = -1

def drawLine(event, x , y, flag, param):
    global sta_p, end_p
    if event == cv2.EVENT_LBUTTONDOWN:
        sta_p = (x, y)

    if event == cv2.EVENT_LBUTTONUP:
        end_p = (x, y)
        cv2.line(img, sta_p, end_p, color=(0, 255, 0), thickness=3)
        cv2.imshow('img', img)

    pass

def callback(event, x , y, flag, param):
    drawLine(event, x , y, flag, param)
    print(param)
    pass

def mouseDrawing():
    cv2.setMouseCallback('img', callback, 'hello')
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass
mouseDrawing()