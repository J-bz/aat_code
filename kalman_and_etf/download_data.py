import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 511010：上证5年期国债指数
# 511260：上证10年期国债指数
etfs = ['511010', '511260']
etf_start_date = "20180901"
etf_end_date = "20221001"

# 利用akshare获得两种etf的后复权数据
etf_5 = ak.fund_etf_hist_em(symbol=etfs[0], period="daily", start_date=etf_start_date, end_date=etf_end_date,
                            adjust="hfq")
etf_10 = ak.fund_etf_hist_em(symbol=etfs[1], period="daily", start_date=etf_start_date, end_date=etf_end_date,
                             adjust="hfq")
# 保存为csv格式文件
etf_5.to_csv('etf_5.csv')
etf_10.to_csv('etf_10.csv')