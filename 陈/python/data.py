import pandas as pd
import numpy as np
import function as f
import Entropy
import pearson

x_str = input("请问需要找哪场比赛：以形同“match0001”的格式输入")
location = 'D:\\美赛\\2024\matches\\' + x_str + ".xlsx"
df = pd.read_excel(location)
df.loc[(df.p1_score == 'AD'), 'p1_score'] = 50
df.loc[(df.p2_score == 'AD'), 'p2_score'] = 50
df.loc[(df.speed_mph == 'NA'), 'speed_mph'] = 0
# df.speed_mph.to_csv("3.csv")
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
p1_games = (df['p1_games'].astype(int)).values.tolist()
p2_games = (df['p2_games'].astype(int)).values.tolist()
p1_sets = (df['p1_sets'].astype(int)).values.tolist()
p2_sets = (df['p2_sets'].astype(int)).values.tolist()
p1_score = (df['p1_score'].astype(int)).values.tolist()
p2_score = (df['p2_score'].astype(int)).values.tolist()
game_number = (df['game_no'].astype(int)).values.tolist()
point_number = (df['point_no'].astype(int)).values.tolist()
speed_serve = (df['speed_mph'].astype(str)).values.tolist()
serve_width = (df['serve_width'].astype(str)).values.tolist()
serve_depth = (df['serve_depth'].astype(str)).values.tolist()
return_depth = (df['return_depth'].astype(str)).values.tolist()

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
p1_serve_speed_ave = [None] * length_of_competition
p2_serve_speed_ave = [None] * length_of_competition

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
p1_double_fault, p2_double_fault = f.function1(p1_double_fault, p2_double_fault, double_fault_1, double_fault_2, length,
                                               who_to_serve)
p1_unf_err, p2_unf_err = f.function2(p1_unf_err, p2_unf_err, error_1, error_2, length)
p1_net_pt, p2_net_pt = f.function2(p1_net_pt, p2_net_pt, net_1, net_2, length)
p1_net_pt_won, p2_net_pt_won = f.function2(p1_net_pt_won, p2_net_pt_won, net_won_1, net_won_2, length)
p1_break_pt, p2_break_pt = f.function4(p1_break_pt, p2_break_pt, break_1, break_2, length, who_to_serve)
p1_break_pt_won, p2_break_pt_won = f.function4(p1_break_pt_won, p2_break_pt_won, break_pt_won_1, break_pt_won_2, length,
                                               who_to_serve)
p1_break_pt_missed, p2_break_pt_missed = f.function4(p1_break_pt_missed, p2_break_pt_missed, break_pt_missed_1,
                                                     break_pt_missed_2, length, who_to_serve)
p1_serve_speed_ave, p2_serve_speed_ave = f.function3(p1_serve_speed_ave, p2_serve_speed_ave, speed_serve, length,
                                                     who_to_serve)

# data2.to_csv(loc)
# tmp = np.array(list(zip(point_victor, rally_count)))
# tmp = pd.DataFrame(data=tmp, index=None)
# tmp.to_csv("test.csv")
# relevant = Entropy.getCondEntropy(pd.Series(point_victor), pd.Series(rally_count))

# p1_winner,p2_winner = f.function1(p1_winner, p2_winner, winner_1, winner_2, length, who_to_serve)
# 下面分析具体局势
'''
x = int(input("需要找当前比赛中第几次point前的情况："))
x = x - 1
set = [p1_sets[x], p2_sets[x]]
game = [p1_games[x], p2_games[x]]
score = [p1_score[x], p2_score[x]]
print(set, game, score)
# 当前的set，game和score对比
j = x
while j >= 0 and game_number[j] == game_number[x]:
    j = j - 1
this_game = [x - j, p1_score[x], p2_score[x]]
tmp = j
while j >= 0 and game_number[j] == game_number[tmp]:
    j = j - 1
former_game = [tmp - j, p1_score[tmp], p2_score[tmp]]
tmp = j
while j >= 0 and game_number[j] == game_number[tmp]:
    j = j - 1
former_two_game = [tmp - j, p1_score[tmp], p2_score[tmp]]
print(this_game, former_game, former_two_game)
'''

consumption_of_strength = [None] * length_of_competition
consumption = [None] * length_of_competition
for i in range(0, length):
    consumption[i] = total_length_1[i] / total_length_2[i]
for i in range(0, 20):
    consumption_of_strength[i] = total_length_1[i] / total_length_2[i]
for i in range(20, length):
    consumption_of_strength[i] = (total_length_1[i] - total_length_1[i - 20]) / (
                total_length_2[i] - total_length_2[i - 20])

'''
print(consumption)
print(consumption_of_strength)
print("技术指标和point获胜的熵相关系数为：")
print("p1_ace", Entropy.getCondEntropy(pd.Series(p1_ace), pd.Series(point_victor)))
print("p2_ace", Entropy.getCondEntropy(pd.Series(p2_ace), pd.Series(point_victor)))
print("p1_double_fault", Entropy.getCondEntropy(pd.Series(p1_double_fault), pd.Series(point_victor)))
print("p2_double_fault", Entropy.getCondEntropy(pd.Series(p2_double_fault), pd.Series(point_victor)))
print("p1_unf_err", Entropy.getCondEntropy(pd.Series(p1_unf_err), pd.Series(point_victor)))
print("p2_unf_err", Entropy.getCondEntropy(pd.Series(p2_unf_err), pd.Series(point_victor)))
print("p1_net_pt", Entropy.getCondEntropy(pd.Series(p1_net_pt), pd.Series(point_victor)))
print("p2_net_pt", Entropy.getCondEntropy(pd.Series(p2_net_pt), pd.Series(point_victor)))
print("p1_net_pt_won", Entropy.getCondEntropy(pd.Series(p1_net_pt_won), pd.Series(point_victor)))
print("p2_net_pt_won", Entropy.getCondEntropy(pd.Series(p2_net_pt_won), pd.Series(point_victor)))
print("p1_break_pt", Entropy.getCondEntropy(pd.Series(p1_break_pt), pd.Series(point_victor)))
print("p2_break_pt", Entropy.getCondEntropy(pd.Series(p2_break_pt), pd.Series(point_victor)))
print("p1_break_pt_won", Entropy.getCondEntropy(pd.Series(p1_break_pt_won), pd.Series(point_victor)))
print("p2_break_pt_won", Entropy.getCondEntropy(pd.Series(p2_break_pt_won), pd.Series(point_victor)))
print("p1_break_pt_missed", Entropy.getCondEntropy(pd.Series(p1_break_pt_missed), pd.Series(point_victor)))
print("p2_break_pt_missed", Entropy.getCondEntropy(pd.Series(p2_break_pt_missed), pd.Series(point_victor)))
print("p1_distance_run", Entropy.getCondEntropy(pd.Series(total_length_1), pd.Series(point_victor)))
print("p2_distance_run", Entropy.getCondEntropy(pd.Series(total_length_2), pd.Series(point_victor)))
print("p1_serve_speed_ave", Entropy.getCondEntropy(pd.Series(p1_serve_speed_ave), pd.Series(point_victor)))
print("p2_serve_speed_ave", Entropy.getCondEntropy(pd.Series(p2_serve_speed_ave), pd.Series(point_victor)))
print("consumption_of_strength", Entropy.getCondEntropy(pd.Series(consumption_of_strength), pd.Series(point_victor)))
print("consumption", Entropy.getCondEntropy(pd.Series(consumption), pd.Series(point_victor)))

print("技术指标和point获胜的pearson相关系数为：")
print("p1_ace", pearson.pearson(p1_ace, point_victor))
print("p2_ace", pearson.pearson(p2_ace, point_victor))
print("p1_double_fault", pearson.pearson(p1_double_fault, point_victor))
print("p2_double_fault", pearson.pearson(p2_double_fault, point_victor))
print("p1_unf_err", pearson.pearson(p1_unf_err, point_victor))
print("p2_unf_err", pearson.pearson(p2_unf_err, point_victor))
print("p1_net_pt", pearson.pearson(p1_net_pt, point_victor))
print("p2_net_pt", pearson.pearson(p2_net_pt, point_victor))
print("p1_net_pt_won", pearson.pearson(p1_net_pt_won, point_victor))
print("p2_net_pt_won", pearson.pearson(p2_net_pt_won, point_victor))
print("p1_break_pt", pearson.pearson(p1_break_pt, point_victor))
print("p2_break_pt", pearson.pearson(p2_break_pt, point_victor))
print("p1_break_pt_won", pearson.pearson(p1_break_pt_won, point_victor))
print("p2_break_pt_won", pearson.pearson(p2_break_pt_won, point_victor))
print("p1_break_pt_missed", pearson.pearson(p1_break_pt_missed, point_victor))
print("p2_break_pt_missed", pearson.pearson(p2_break_pt_missed, point_victor))
print("p1_distance_run", pearson.pearson(total_length_1, point_victor))
print("p2_distance_run", pearson.pearson(total_length_2, point_victor))
print("p1_serve_speed_ave", pearson.pearson(p1_serve_speed_ave, point_victor))
print("p2_serve_speed_ave", pearson.pearson(p2_serve_speed_ave, point_victor))
print("consumption_of_strength", pearson.pearson(consumption_of_strength, point_victor))
print("consumption", pearson.pearson(consumption, point_victor))
'''
width_1 = [None] * length
width_2 = [None] * length
dict_1 = {'B': 1, 'BC': 2, 'BW': 3, 'C': 4, 'W': 5}
dict_2 = {'CTL': 1, 'NCTL': 2}
dict_3 = {'D': 1, 'ND': 2}
for i in range(0, length):
    if (serve_width[i] != 'nan'):
        if who_to_serve[i] == 1:
            width_1[i] = dict_1[serve_width[i]]
            width_2[i] = 0
        else:
            width_2[i] = dict_1[serve_width[i]]
            width_1[i] = 0
    else:
        width_1[i] = 0
        width_2[i] = 0
depth_1 = [None] * length
depth_2 = [None] * length
for i in range(0, length):
    if (serve_depth[i] != 'nan'):
        if who_to_serve[i] == 1:
            depth_1[i] = dict_2[serve_depth[i]]
            depth_2[i] = 0
        else:
            depth_2[i] = dict_2[serve_depth[i]]
            depth_1[i] = 0
    else:
        depth_1[i] = 0
        depth_2[i] = 0
depth_return_1 = [None] * length
depth_return_2 = [None] * length
for i in range(0, length):
    if (return_depth[i] != 'nan'):
        if who_to_serve[i] == 1:
            depth_return_1[i] = dict_3[return_depth[i]]
            depth_return_2[i] = 0
        else:
            depth_return_2[i] = dict_3[return_depth[i]]
            depth_return_1[i] = 0
    else:
        depth_return_1[i] = 0
        depth_return_2[i] = 0
res = np.array(list(
    zip(point_victor, who_to_serve, consumption_of_strength, consumption, p1_ace, p2_ace, p1_winner, p2_winner,
        p1_double_fault, p2_double_fault,
        p1_unf_err, p2_unf_err, p1_net_pt,
        p2_net_pt, p1_net_pt_won, p2_net_pt_won, p1_break_pt, p2_break_pt, p1_break_pt_won, p2_break_pt_won,
        p1_break_pt_missed, p2_break_pt_missed, p1_serve_speed_ave, p2_serve_speed_ave, width_1, width_2, depth_1,
        depth_2, depth_return_1, depth_return_2)))
data2 = pd.DataFrame(data=res, index=None)
loc = x_str + "_dealted.csv"
data2.to_csv(loc)