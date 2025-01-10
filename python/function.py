def function1(p1, p2, data1, data2, length, who_to_serve):
    p1[0] = data1[0]
    p2[0] = data2[0]
    p1_serve_num = 0
    p2_serve_num = 0
    if who_to_serve[0] == 1:
        p1_serve_num = 1
    else:
        p2_serve_num = 1
    for i in range(1, length):
        if who_to_serve[i] == 1:
            p1[i] = (p1[i - 1] * p1_serve_num + data1[i])
            p1_serve_num = p1_serve_num + 1
            p1[i] = p1[i] / p1_serve_num
            p2[i] = p2[i - 1]
        else:
            p2[i] = (p2[i - 1] * p2_serve_num + data2[i])
            p2_serve_num = p2_serve_num + 1
            p2[i] = p2[i] / p2_serve_num
            p1[i] = p1[i - 1]
    return p1, p2


# 和发球方相关的技术指标处理

def function2(p1, p2, data1, data2, length):
    p1[0] = data1[0]
    p2[0] = data2[0]
    for i in range(1, length):
        p1[i] = (p1[i - 1] * (i - 1) + data1[i]) / i
        p2[i] = (p2[i - 1] * (i - 1) + data2[i]) / i
    return p1, p2


# 和发球方无关的技术指标处理

def function3(p1, p2, data, length, who_to_serve):
    p1[0] = 0
    p2[0] = 0
    p1_serve_num = 0
    p2_serve_num = 0
    if(data[0] != 'nan'):
        if who_to_serve[0] == 1:
            p1_serve_num = 1
            p1[0] = float(data[0])
        else:
            p2_serve_num = 1
            p2[0] = float(data[0])
    for i in range(1, length):
        if data[i] != 'nan':
            if who_to_serve[i] == 1:
                p1[i] = (p1[i - 1] * p1_serve_num + float(data[i]))
                p1_serve_num = p1_serve_num + 1
                p1[i] = p1[i] / p1_serve_num
                p2[i] = p2[i - 1]
            else:
                p2[i] = (p2[i - 1] * p2_serve_num + float(data[i]))
                p2_serve_num = p2_serve_num + 1
                p2[i] = p2[i] / p2_serve_num
                p1[i] = p1[i - 1]
        else:
            p1[i] = p1[i - 1]
            p2[i] = p2[i - 1]
    return p1, p2


#针对破发，只有不在发球时才回有破发的说法
def function4(p1, p2, data1, data2, length, who_to_serve):
    p1[0] = data1[0]
    p2[0] = data2[0]
    p1_unserve_num = 0
    p2_unserve_num = 0
    if who_to_serve[0] == 2:
        p1_unserve_num = 1
    else:
        p2_unserve_num = 1
    for i in range(1, length):
        if who_to_serve[i] == 2:
            p1[i] = (p1[i - 1] * p1_unserve_num + data1[i])
            p1_unserve_num = p1_unserve_num + 1
            p1[i] = p1[i] / p1_unserve_num
            p2[i] = p2[i - 1]
        else:
            p2[i] = (p2[i - 1] * p2_unserve_num + data2[i])
            p2_unserve_num = p2_unserve_num + 1
            p2[i] = p2[i] / p2_unserve_num
            p1[i] = p1[i - 1]
    return p1, p2