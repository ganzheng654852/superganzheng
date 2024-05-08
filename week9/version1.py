import cv2 as cv
import numpy as np

# 读取图像并转换为灰度图
img = cv.imread('picture1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 预处理：模糊和边缘检测
blurred = cv.GaussianBlur(gray, (5, 5), 0)
edges = cv.Canny(blurred, 50, 150)

# 查找轮廓
contours, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

## 筛选矩形轮廓
rectangles = []
points = []  # 存储矩形的顶点坐标
for contour in contours:
    epsilon = 0.03 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4 and cv.contourArea(contour) > 1000:  # 添加面积阈值
        rectangles.append(approx)
        for point in approx:
            x, y = point[0]
            points.append((x, y))  # 存储顶点坐标
            cv.circle(img, (x, y), 5, (255, 0, 0), -1)  # 绘制顶点
            cv.putText(img, f'({x}, {y})', (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # 显示顶点坐标

        cv.drawContours(img, [approx], 0, (0, 255, 0), 2)  # 绘制矩形轮廓

# 计算矩形的中心点
if points:  # 确保points列表不为空
    cx = int(sum([p[0] for p in points]) / len(points))
    cy = int(sum([p[1] for p in points]) / len(points))
    cv.circle(img, (cx, cy), 5, (0, 0, 255), -1)  # 绘制中心点
    cv.putText(img, f'Center: ({cx}, {cy})', (cx + 10, cy - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # 显示中心点坐标

# 显示结果
cv.imshow('Rectangles', img)
cv.waitKey(0)
cv.destroyAllWindows()

