import pandas as pd
import numpy as np
from pykalman import KalmanFilter
import matplotlib.pyplot as plt

def cal_slope_intercept(etfs, prices):
    delta = 1e-5
    trans_cov = delta / (1 - delta) * np.eye(2)
    obs_mat = np.vstack([prices[etfs[0]], np.ones(prices[etfs[0]].shape)]).T[:, np.newaxis]

    kf = KalmanFilter(n_dim_obs=1,
                      n_dim_state=2,
                      initial_state_mean=np.zeros(2),
                      initial_state_covariance=np.ones((2, 2)),
                      transition_matrices=np.eye(2),
                      observation_matrices=obs_mat,
                      observation_covariance=1.0,
                      transition_covariance=trans_cov)

    state_means, state_covs = kf.filter(prices[etfs[1]].values)
    return state_means, state_covs

def draw_slope_intercept_changes(prices, state_means):
    pd.DataFrame(dict(slope=state_means[:, 0],
                      intercept=state_means[:, 1]),
                 index=prices.index).plot(subplots=True)
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

state_means, state_covs = cal_slope_intercept(etfs, prices)
draw_slope_intercept_changes(prices, state_means)