import numpy as np
import pandas as pd
import math
'''
s1 = pd.Series(['X1', 'X1', 'X2', 'X2', 'X2', 'X2'])
s2 = pd.Series(['Y1', 'Y1', 'Y1', 'Y2', 'Y2', 'Y2'])
'''

# 建立两个数组
def getEntropy(s):  # 定义熵

    if not isinstance(s, pd.core.series.Series):
        s = pd.Series(s)  # 把不是数组的数据转化为数组
    prt_ary = s.groupby(by=s).count().values / float(len(s))  # 得到概率分布
    return sum(-(np.log2(prt_ary) * prt_ary))  # 求和，得出熵


# print('Entropy:', getEntropy(s1))  # 输出s1的熵


def getCondEntropy(s1, s2):  # 定义s1的条件s2的熵
    d = dict()  # 定义一个字典结构体
    for i in list(range(len(s1))):
        d[s1[i]] = d.get(s1[i], []) + [s2[i]]  # key是s1的值，value是一个数组，为s2的值，记录了s1的值下s2的分布
    length = 0
    for k in d:
        # print(d[k])
        length = length + len(d[k])

    return sum([getEntropy(d[k]) * len(d[k]) / length for k in d])
    print('CondEntropy', getCondEntropy(s1, s2))  # 输出条件熵


def getEntropyGain(s1, s2):
    return getEntropy(s2) - getCondEntropy(s1, s2)  # s2的熵减s2条件下s1的熵
    print('EntropyGain', getEntropyGain(s1, s2))


def getEntropyGainRatio(s1, s2):
    return getEntropyGainRatio(s1, s2) / getEntropy(s2)  # 熵增益除以熵
    print('EntropyGainRatio', getEntropyGainRatio(s1, s2))


def getDiscreteCorr(s1, s2):
    return getEntropyGain(s1, s2) / math.sqrt(getEntropy(s1) * getEntropy(s2))
    print('DiscreteCorr', getDiscreteCorr(s1, s2))
