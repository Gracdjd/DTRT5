import json
# with open('data.json', 'r') as f:
#   data = json.load(f)

# res = []
# for entry in data:
#   temp = {}
#   for i in entry:
#     if(i in temp):
#       temp[i] += 1
#     else:
#       temp[i] = 1
#   res.append(temp)

# with open('./res.json', 'w') as f:
#   json.dump(res, f)

with open('res.json', 'r') as f:
  data = json.load(f)

path = 'C:\\Users\\WZ\\PycharmProjects\\pythonProject5\\thucnews_data.json'

with open(path, 'r', encoding='utf-8') as f:
  ldata = json.load(f)

res = []

for index,i in enumerate(data):
  sum = 0
  for item in i:
    if(item == '-1'):
      continue
    else:
      if(i[item] >= 4):
        sum += 1
  res.append([sum, len(ldata[index]['content'])])

with open('realres.json', 'w', encoding='utf-8') as f:
  json.dump(res, f)