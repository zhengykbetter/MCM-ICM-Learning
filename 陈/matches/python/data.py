import pandas as pd
import numpy as np
import function as f
import Entropy

x_str = input("请问需要找哪场比赛：以形同“match0001”的格式输入")
location = 'D:\\美赛\\2024\matches\\' + x_str + ".xlsx"
df = pd.read_excel(location)
df.loc[(df.p1_score == 'AD'), 'p1_score'] = 50
df.loc[(df.p2_score == 'AD'), 'p2_score'] = 50
# np.save("1.npy",df)
# df.to_csv("1.csv")
# 体力处理
length_1 = (df['p1_distance_run'].astype(float)).values.tolist()
length_2 = (df['p2_distance_run'].astype(float)).values.tolist()
length = len(length_1)
ace_1 = (df['p1_ace'].astype(int)).values.tolist()
ace_2 = (df['p2_ace'].astype(int)).values.tolist()
# ace只有在一方发球时才算数
winner_1 = (df['p1_winner'].astype(int)).values.tolist()
winner_2 = (df['p2_winner'].astype(int)).values.tolist()
winner_shot_type = (df['winner_shot_type'].astype(str)).values.tolist()
double_fault_1 = (df['p1_double_fault'].astype(int)).values.tolist()
double_fault_2 = (df['p2_double_fault'].astype(int)).values.tolist()
error_1 = (df['p1_unf_err'].astype(int)).values.tolist()
error_2 = (df['p2_unf_err'].astype(int)).values.tolist()
net_1 = (df['p1_net_pt'].astype(int)).values.tolist()
net_2 = (df['p2_net_pt'].astype(int)).values.tolist()
net_won_1 = (df['p1_net_pt_won'].astype(int)).values.tolist()
net_won_2 = (df['p2_net_pt_won'].astype(int)).values.tolist()
break_1 = (df['p1_break_pt'].astype(int)).values.tolist()
break_2 = (df['p2_break_pt'].astype(int)).values.tolist()
break_pt_won_1 = (df['p1_break_pt_won'].astype(int)).values.tolist()
break_pt_won_2 = (df['p2_break_pt_won'].astype(int)).values.tolist()
break_pt_missed_1 = (df['p1_break_pt_missed'].astype(int)).values.tolist()
break_pt_missed_2 = (df['p2_break_pt_missed'].astype(int)).values.tolist()
who_to_serve = (df['server'].astype(int)).values.tolist()
rally_count = (df['rally_count'].astype(int)).values.tolist()
point_victor = (df['point_victor'].astype(int)).values.tolist()
p1_points_won = (df['p1_points_won'].astype(int)).values.tolist()
p2_points_won = (df['p2_points_won'].astype(int)).values.tolist()
game_victor = (df['game_victor'].astype(int)).values.tolist()
set_victor = (df['set_victor'].astype(int)).values.tolist()
# winner不一样，发球方和接发球方都能打出
length_of_competition = len(length_1)
total_length_1 = [None] * length_of_competition
total_length_2 = [None] * length_of_competition
p1_ace = [None] * length_of_competition
p2_ace = [None] * length_of_competition
p1_winner = [None] * length_of_competition
p2_winner = [None] * length_of_competition
p1_double_fault = [None] * length_of_competition
p2_double_fault = [None] * length_of_competition
p1_unf_err = [None] * length_of_competition
p2_unf_err = [None] * length_of_competition
p1_net_pt = [None] * length_of_competition
p2_net_pt = [None] * length_of_competition
p1_net_pt_won = [None] * length_of_competition
p2_net_pt_won = [None] * length_of_competition
p1_break_pt = [None] * length_of_competition
p2_break_pt = [None] * length_of_competition
p1_break_pt_won = [None] * length_of_competition
p2_break_pt_won = [None] * length_of_competition
p1_break_pt_missed = [None] * length_of_competition
p2_break_pt_missed = [None] * length_of_competition
p1_distance_run = [None] * length_of_competition
p2_distance_run = [None] * length_of_competition
total_length_1[0] = length_1[0]
total_length_2[0] = length_2[0]
p1_serve_num = 0
p2_serve_num = 0
for i in range(0, length):
    if who_to_serve[i] == 1:
        p1_serve_num = p1_serve_num + 1
    else:
        p2_serve_num = p2_serve_num + 1
print(p1_serve_num, p2_serve_num)
for i in range(1, len(length_1)):
    total_length_1[i] = length_1[i] + total_length_1[i - 1]
    total_length_2[i] = length_2[i] + total_length_2[i - 1]
p1_ace, p2_ace = f.function1(p1_ace, p2_ace, ace_1, ace_2, length, who_to_serve)
p1_winner, p2_winner = f.function2(p1_winner, p2_winner, winner_1, winner_2, length)
p1_double_fault, p2_double_fault = f.function2(p1_double_fault, p2_double_fault, double_fault_1, double_fault_2, length)
p1_unf_err, p2_unf_err = f.function2(p1_unf_err, p2_unf_err, error_1, error_2, length)
p1_net_pt, p2_net_pt = f.function2(p1_net_pt, p2_net_pt, net_1, net_2, length)
p1_net_pt_won, p2_net_pt_won = f.function2(p1_net_pt_won, p2_net_pt_won, net_won_1, net_won_2, length)
p1_break_pt, p2_break_pt = f.function2(p1_break_pt, p2_break_pt, break_1, break_2, length)
p1_break_pt_won, p2_break_pt_won = f.function2(p1_break_pt_won, p2_break_pt_won, break_pt_won_1, break_pt_won_2, length)
p1_break_pt_missed, p2_break_pt_missed = f.function2(p1_break_pt_missed, p2_break_pt_missed, break_pt_missed_1,
                                                     break_pt_missed_2, length)
res = np.array(list(
    zip(p1_ace, p2_ace, p1_winner, p2_winner, p1_double_fault, p2_double_fault, p1_unf_err, p2_unf_err, p1_net_pt,
        p2_net_pt, p1_net_pt_won, p2_net_pt_won, p1_break_pt, p2_break_pt, p1_break_pt_won, p2_break_pt_won,
        p1_break_pt_missed, p2_break_pt_missed, )))
data2 = pd.DataFrame(data=res, index=None)
loc = x_str + "_dealted.csv"
data2.to_csv(loc)
tmp = np.array(list(zip(point_victor,rally_count)))
tmp = pd.DataFrame(data=tmp,index = None)
tmp.to_csv("test.csv")
# relevant = Entropy.getCondEntropy(pd.Series(point_victor), pd.Series(rally_count))

# p1_winner,p2_winner = f.function1(p1_winner, p2_winner, winner_1, winner_2, length, who_to_serve)
