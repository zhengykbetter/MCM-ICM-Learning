import numpy as np
import pandas as pd


# 计算ab在s中出现的次数
def find_count(s, ab):
    ab_sum = 0
    for i in range(0, len(s) - 1):
        if s[i:i + 2] == ab: ab_sum += 1
    return ab_sum


# 转移矩阵
def str_count_df(s):
    # 获得里面不重复的元素
    unique_items = np.unique(list(s))
    # 获得不重复元素个数
    n = unique_items.size
    # 默认行是这一次的，列是下一次的。类容是他们的转换情况
    df_ = pd.DataFrame(index=unique_items, columns=unique_items)
    for i in unique_items:
        for j in unique_items:
            df_.loc[i, j] = find_count(s, i + j)
    return df_


# 转移矩阵，概率
def str_count_df_p(s):
    # 获得里面不重复的元素
    unique_items = np.unique(list(s))
    # 获得不重复元素个数
    n = unique_items.size
    # 默认行是这一次的，列是下一次的。类容是他们的转换情况
    df_ = pd.DataFrame(index=unique_items, columns=unique_items)
    for i in unique_items:
        for j in unique_items:
            df_.loc[i, j] = find_count(s, i + j)
    df_ = df_.div(df_.sum(axis=1), axis='index')
    return df_


x_str = input("请问需要找哪场比赛：以形同“match0001”的格式输入")
location = 'D:\\美赛\\2024\matches\\' + x_str + ".xlsx"
df = pd.read_excel(location)
point_victor = (df['point_victor'].astype(int)).values.tolist()


