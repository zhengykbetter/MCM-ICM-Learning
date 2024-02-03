import pandas as pd


def getProbSS(s):  # 定义求概率平方和的函数
    if not isinstance(s, pd.core.series.Series):
        s = pd.Series(s)
    prt_ary = s.groupby(by=s).count().values / float(len(s))  # 取它的分布
    return sum(prt_ary ** 2)  # 取它的平方和


def getGini(s1, s2):  # 与条件熵的算法类似
    d = dict()
    for i in range(0,len(s1)):
        d[s1[i]] = d.get(s1[i], []) + [s2[i]]
    #print('Gini', getGini(s1, s2))
    return 1 - sum([getProbSS(d[k]) * len(d[k]) / float(len(s1)) for k in d])


