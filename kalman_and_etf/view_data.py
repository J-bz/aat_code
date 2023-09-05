import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw_date_coloured_scatterplot(etfs, prices, date_info):
    plen = len(prices)
    colour_map = plt.colormaps['Blues']
    colours = np.linspace(0.1, 1, plen)

    # 创建散点图
    scatterplot = plt.scatter(prices[etfs[0]], prices[etfs[1]],
                              s=30, c=colours, cmap=colour_map,
                              edgecolor='k', alpha=0.8)

    # 利用颜色条展示不同时间的价格
    colourbar = plt.colorbar(scatterplot)
    colourbar.ax.set_yticklabels([p for p in date_info[::plen//9]])
    # 5年期国债etf作为x轴
    plt.xlabel(prices.columns[0])
    # 10年期国债etf作为y轴
    plt.ylabel(prices.columns[1])

    plt.figure(dpi=800)
    plt.show()

# 两种国债
etfs = ['511010', '511260']
etf_start_date = "20180901"
etf_end_date = "20221001"

# 读取5年期国债etf和10年期国债etf的数据
etf_5 = pd.read_csv('etf_5.csv')
etf_10 = pd.read_csv('etf_10.csv')

# 提取收盘价格
prices = pd.DataFrame(index=etf_5.index)
prices[etfs[0]] = etf_5["收盘"]
prices[etfs[1]] = etf_10["收盘"]
begin_end_date = etf_5["日期"]

# 绘制散点图
draw_date_coloured_scatterplot(etfs, prices, begin_end_date)