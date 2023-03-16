from PIL import Image, ImageFont, ImageDraw

# 打开图片
img = Image.open('./bg_imgs/02.png')

draw = ImageDraw.Draw(img)
#加载字体
font = ImageFont.truetype(r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf",
size=36)
# 4、在画布上绘制文本
draw.text((100, 100), text="你好世界", fill=(0, 255, 0), font=font)
img.show()

