import cv2

# 创建一个窗口命名为img
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# 设置窗口大小
cv2.resizeWindow('img', 600, 1000)
# 读取图像
img = cv2.imread('./xhr_imgs/01.png')
# 显示图像
cv2.imshow('img', img)
# 等待按键按下
key = cv2.waitKey(0)
# 如果按键是q则释放窗口
if key == ord('q'):
    print(key)
    # 窗口释放
    cv2.destroyAllWindows()