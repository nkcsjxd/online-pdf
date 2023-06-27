# import json


# def read_json(file):
#     with open(file, 'r', encoding='utf-8-sig') as r:
#         data = json.load(r)
#     return data

# def read_jsonl(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         data = f.readlines()
#     return data

# path = './multi.jsonl'

# data = read_jsonl(path)
# # print(data)
# line = data[0]
# # print(line)
# line = json.loads(line)#转化成字符串

# print(line)

# s = '十'
# print(hex(ord(s)))
print(chr(hex(62295)))