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
# 替换 ASCII 之外的字符
replace_chars = {'(cid:{})'.format(i): int(i)-62294}
for k, v in replace_chars.items():
    content = content.replace(k, v)