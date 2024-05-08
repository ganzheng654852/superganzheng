import cv2 as cv
import numpy as np

# 读取图像并转换为灰度图
img = cv.imread('picture1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 使用Canny边缘检测算法找到图像边缘
edges = cv.Canny(gray, 200, 600, apertureSize=3)

# 图像降噪
denoised_img = cv.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

# 使用降噪后的图像进行边缘检测
edges = cv.Canny(denoised_img, 310, 500, apertureSize=3)

# 查找所有轮廓
contours, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 筛选出矩形轮廓
rectangles = []
for contour in contours:
    epsilon = 0.03 * cv.arcLength(contour, True)  # 调整这里的比例因子
    approx = cv.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4:
        rectangles.append(approx)

# 绘制矩形轮廓和顶点坐标
for rectangle in rectangles:
    cv.drawContours(img, [rectangle], -1, (0, 255, 0), 2)

    # 获取矩形的顶点坐标
    for point in rectangle:
        x, y = point[0]
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)  # 绘制顶点坐标

# 显示结果
cv.imshow('Rectangles', img)
cv.waitKey(0)
cv.destroyAllWindows()

# 显示结果
cv.imshow('Rectangles', img)
cv.waitKey(0)
cv.destroyAllWindows()