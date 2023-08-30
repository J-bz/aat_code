import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw_date_coloured_scatterplot(etfs, prices):
    plen = len(prices)
    colour_map = plt.colormaps['YlOrRd']
    colours = np.linspace(0.1, 1, plen)

    # Create the scatterplot object
    scatterplot = plt.scatter(prices[etfs[0]], prices[etfs[1]],
                              s=30, c=colours, cmap=colour_map,
                              edgecolor='k', alpha=0.8)

    # Add a colour bar for the date colouring and set the
    # corresponding axis tick labels to equal string-formatted dates
    colourbar = plt.colorbar(scatterplot)
    #colourbar.ax.set_yticklabels([str(p.date()) for p in prices[::plen//9].index])
    plt.xlabel(prices.columns[0])
    plt.ylabel(prices.columns[1])
    plt.show()

# 两种国债
etfs = ['511010', '511260']
etf_start_date = "20180901"
etf_end_date = "20221001"

# 读取5年期国债etf和10年期国债etf得数据
etf_5 = pd.read_csv('etf_5.csv')
etf_10 = pd.read_csv('etf_10.csv')

# 提取收盘价格
prices = pd.DataFrame(index=etf_5.index)
prices[etfs[0]] = etf_5["收盘"]
prices[etfs[1]] = etf_10["收盘"]
draw_date_coloured_scatterplot(etfs, prices)