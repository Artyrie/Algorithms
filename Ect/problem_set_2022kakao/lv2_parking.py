import math
from datetime import datetime, timedelta


def solution(fees, records):
    # 100점, t16 max 9.27ms
    delta = timedelta(days=1)
    max_time = delta + datetime.strptime("23:59", "%H:%M")
    inout_dic = {}
    time_dic = {}

    for rec in records:
        tmp = rec.split(' ')
        if tmp[2] == 'IN':
            t = datetime.strptime(tmp[0], "%H:%M")
            inout_dic[tmp[1]] = t + delta
        else:
            t = datetime.strptime(tmp[0], "%H:%M")
            t -= inout_dic[tmp[1]]
            try:
                time_dic[tmp[1]] += (t + delta).seconds
            except:
                time_dic[tmp[1]] = (t + delta).seconds
            inout_dic[tmp[1]] = 'OUT'

    for k, v in inout_dic.items():
        if v != 'OUT':
            try:
                time_dic[k] += (max_time - inout_dic[k] + delta).seconds
            except:
                time_dic[k] = (max_time - inout_dic[k] + delta).seconds

    answer = []
    time_dic = sorted(time_dic.items())

    for k, v in time_dic:
        if v - fees[0] * 60 > 0:
            t = v - fees[0] * 60
            t = math.ceil(t / (fees[2] * 60))
        else:
            t = 0
        answer.append(fees[1] + t * fees[3])

    return answer