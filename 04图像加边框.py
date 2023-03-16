import cv2



# 创建一个窗口命名为img
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# 设置窗口大小
cv2.resizeWindow('img', 1000, 600)

img = cv2.imread('./bg_imgs/02.png')
h , w, c = img.shape
padding = 20
# img[:padding, :] = [255, 0 ,0]
# img[h-padding:h, :] = [0, 255, 0]
# img[:, :padding] = [0, 255, 255]
# img[:, w-padding:w] = [0, 0, 255]
for row in range(padding):
    for col in range(w):
        img[row, col] = [255, 0 ,0]
        img[h-row, col] = [0, 255, 0]
        print(h-row)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()