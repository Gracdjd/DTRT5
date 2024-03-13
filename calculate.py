import json

# 读取 JSON 文件
with open('./data/realres.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# print(data[0])
# 定义每个间隔的范围
interval_size = 500
max_word_count = max(item[1] for item in data)
intervals = range(0, max_word_count + 1, interval_size)

# 统计每个间隔内符合条件的文章数量
interval_counts = {interval: 0 for interval in intervals}
interval_word_counts = {interval: 0 for interval in intervals}
for item in data:
    word_count = item[1]
    cluster_count = item[0] if item[0] != 0 else 1
    for interval in intervals:
        if word_count < interval + interval_size:
            interval_word_counts[interval] += 1
            if cluster_count >= 2:
                interval_counts[interval] += 1
            break

x1 = []
x2 = []
# 输出统计结果
for interval, count in interval_counts.items():
    x1.append(count)
   
# for index, data in enumerate(interval_counts):
#     print(data)
for interval, count in interval_word_counts.items():
    x2.append(count)

res = []
for index, data in enumerate(x1):
    if(x2[index] != 0):
        res.append([data / x2[index], x2[index]]) 
    else:
        res.append([0, x2[index]]) 

import pandas as pd

df = pd.DataFrame(res)

df.to_excel('res.xlsx', sheet_name='Sheet1')

# print(res)