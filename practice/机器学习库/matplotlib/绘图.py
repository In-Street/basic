"""
pip3 install matplotlib

1. 绘制单条线/ 多条线
		plot()：用于绘制线图和散点图
		hist()：用于绘制直方图
		scatter()：用于绘制散点图
		pie()：用于绘制饼图
		bar()：用于绘制垂直条形图和水平条形图


"""
import matplotlib.pyplot as plt
import numpy as np

# 1 . 绘制单条曲线：提供x y轴的3个点：  (1,4)  (3,8)  (5.10)
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# 1. 绘制单条曲线
# x = np.linspace(-np.pi, np.pi, 100)  # 定义x轴，创建一维数组 -3.14 ～ 3.14 ，取区间100个
# plt.plot(x, np.sin(x))
# plt.show()

# 1.  多条曲线
x_1 = np.linspace(-np.pi * 2, np.pi * 2, 100)  # 创建等差结构的一维数组
plt.figure('图1', dpi=100, edgecolor='red',
           facecolor='yellow')  # 创建一个图表,  num: 图表唯一标识符、dpi: 图标分辨率、edgecolor: 边框颜色、facecolor: 背景颜色
for i in range(1, 5):
	plt.plot(x_1, np.sin(x_1 / i))  # 画四条线
plt.show()

# 1. 直方图
plt.figure('图2', dpi=50)
data = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
plt.hist(data)  # 直方图绘制出统计数据出现的次数
plt.show()


# 1. 散点图
x = np.arange(1, 10)
y = x
plt.figure('图3', dpi=50)
plt.scatter(x, y, c='red',marker='*') # c: 设置散点的颜色  market: 散点形状 o圆形 v三角形 其他形状参考：https://matplotlib.org.cn/stable/api/markers_api.html#module-matplotlib.markers
plt.show()
