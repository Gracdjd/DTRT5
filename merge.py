import json
with open('./原始数据/data0data.json', 'r') as f:
  data = json.load(f)
with open('./原始数据/data100000data.json', 'r') as f:
  data1 = json.load(f)

with open('./原始数据/data200000data.json', 'r') as f:
  data2 = json.load(f)

with open('./原始数据/data500000data.json', 'r') as f:
  data3 = json.load(f)

data.extend(data1)
data.extend(data2)
data.extend(data3)

print(len(data))
with open('./data/data.json', 'w') as f:
  json.dump(data, f)


