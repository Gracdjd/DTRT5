# 生成一个count文件，知道main簇是哪个
import json
from collections import Counter

with open('./data/data.json', 'r') as f:
  data = json.load( f)

count = []
for item in data:
  item = [x for x in item if x != -1]
  cnt = Counter(item)

  if(len(cnt) != 0):
    max_key, max_count = cnt.most_common(1)[0]
  else:
    max_key = -1
  count.append(max_key)

with open("count.json", 'w') as f:
  json.dump(count, f)

 

  # print(max_key, )
