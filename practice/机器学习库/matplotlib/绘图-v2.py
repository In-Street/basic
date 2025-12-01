import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""
 pip3 install seaborn  # Seaborn 美化matplotlib 效果图
 
 
"""

data_csv = pd.read_csv('../../../doc/iris_training.csv')
print(data_csv.head())  # 读取前5行

data_csv.plot(kind='scatter', x='120', y='4')  # kind：指定散点图类型  x: 取csv文件中的120列  y：取csv文件中的4列
plt.show()

# 利用sns 绘制散点图
sns.set_style('dark')
sns.set_color_codes('deep')

sns.scatterplot(data=data_csv, x='120', y='4')
plt.show()

# 绘制散点图，利用数据的分类来展示不同的颜色
grid = sns.FacetGrid(data=data_csv, hue='virginica' ,height=5 ,aspect=5)  # 创建 FacetGrid 对象，设置数据源，hue参数设定以数据源中的 virginica 字段来分类展示不同颜色
grid.map(plt.scatter, '120', '4')  # map 方法在面板上绘制散点图 , args:  指定数据源中的列名，用于标识具有要绘制数据的变量
grid.add_legend(title='cvs分类散点图')

plt.show()
