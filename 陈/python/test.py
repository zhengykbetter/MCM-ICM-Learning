import pandas as pd
import function
import Entropy

df = pd.read_csv("test.csv")
length = len(df)
victor_point = df["victor"].astype(int).values.tolist()
rally = df["rally"].astype(int).values.tolist()
# print(victor_point,rally)
relevant = Entropy.getCondEntropy(pd.Series(rally), pd.Series(victor_point))
print(relevant)