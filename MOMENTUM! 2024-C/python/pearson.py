import random
import pandas as pd
from scipy.stats import pearsonr

n = 10000


def pearson(X, Y):
    Z = [i * j for i, j in zip(X, Y)]
    df = pd.DataFrame({"X": X, "Y": Y, "Z": Z})

    r = pearsonr(df['X'], df['Y'])
    print("pearson系数：", r[0])
    print("   P-Value：", r[1])
