# -*- coding: utf-8 -*-
import pandas as pd

# 读取Excel文件
df = pd.read_excel("1.xlsx")

# 获取第G列的所有数据
data = df["1、闲暇时间喜欢做什么？"].tolist()

# 将每个元素根据"┋"进行分割
for i in range(len(data)):
    data[i] = list(data[i].split('┋'))

# 将分割后的元组放入列表result中
result = list(data)
print(result)
# 输出统计结果
#for k, v in count.items():
#    print(f"{k}: {v}")
#结果：看书: 24
#打游戏: 24
#听音乐、玩乐器: 20
#运动: 24
#看电视剧、电影: 46
#出去玩: 32
#睡觉: 43
#其他: 4
#其他〖约会〗: 1
#11212
