import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 设置画布
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# 设置画布大小
cv2.resizeWindow('img', 800, 400)
# 读取图片
img = cv2.imread('./xhr_imgs/02.png')

# 在图片的指定位置绘制英文
cv2.putText(img, "draw chinese", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
# 绘制中文
cv2.putText(img, "书瑞", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
# 导入字体文件
fontpath = "simsun.ttc"
# 设置字体的颜色
b, g, r, a = 0, 255, 0, 0
# 设置字体大小
font = ImageFont.truetype(fontpath, 15)
# 将numpy array的图片格式转为PIL的图片格式
img_pil = Image.fromarray(img)
# 创建画板
draw = ImageDraw.Draw(img_pil)
# 在图片上绘制中文
draw.text((10, 150), "绘制中文", font=font, fill=(b, g, r, a))
# 将图片转为numpy array的数据格式
img = np.array(img_pil)
# 保存图片
cv2.imshow('中文', img)
cv2.waitKey()
cv2.destroyAllWindows()