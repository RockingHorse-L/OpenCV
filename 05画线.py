import numpy as np
import cv2
# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)

# 绘制矩形
# 左上角和右下角的点(384,0),(510,128)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 绘制圆
cv2.circle(img,(447,63), 63, (0,0,255), -1)
# 绘制一条厚度为5的蓝色对角线
# 参数1：画布
# 参数2：(0,0),(511,511)两点的坐标
# 参数3：颜色
# 参数4：线的大小
cv2.line(img,(384,0),(510,128),(255,0,0),5)
# 绘制几何图形
pts = np.array([(100, 100), (300, 100), (400, 300), (300, 500), (100, 500), (0, 300)])
cv2.polylines(img, [pts],isClosed=True, color=(0, 255, 255), thickness=2)
cv2.fillPoly(img, [pts], color=(255, 255, 0))
# 绘制文字
cv2.putText(img, text='shurui', org=(110, 140), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 0, 255), thickness=2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()