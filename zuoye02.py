"""
    分析:
        先取出文件里的信息
            按照空格进行分裂
            再读取列表里的元素
        把dataInfo[0]添加到字典的图片里，并采用字典里的坐标
"""
import json
import cv2



file = open('labels.txt', 'r', encoding='utf-8')
fileInfo = file.readlines()
datasInfo = []
# 读取文件里的信息保存为列表
for info in fileInfo:
    # print(type(info))
    dataInfo = info.strip().split('\t')
    datasInfo.append(dataInfo)

for data in datasInfo:
    # print(data)
    # 设置画布
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 1000, 600)
    # 读取小黄人图片
    img_copy = cv2.imread(f'./xhr_imgs/{data[0]}')
    # 获取形状
    h, w, c = img_copy.shape
    # 缩小图片
    xhrImage = cv2.resize(img_copy, dsize=(100, 100))
    xhrImageH, xhrImageX = xhrImage.shape[:2]
    # 转为pyhon格式
    datas = json.loads(data[1])
    imgDic = datas[0]
    # 读取字典里的图片和坐标
    img = imgDic['img']
    point = imgDic['point']
    # 读取背景图
    image = cv2.imread(f'./bg_imgs/{img}')
    # 粘贴小黄淫到背景图
    image[point[1]:point[3],point[0]:point[2]] = xhrImage[:xhrImageH, :xhrImageX]
    # print(img)
    cv2.imshow('img', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
file.close()
