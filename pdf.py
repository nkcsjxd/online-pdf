import pdfplumber
import re
import PyPDF2
import json

# path = "./pdf/neikejizhenxue_1549-1580.pdf"

import os

folder_path = "D:\\Workspace\\PycharmProjects\\online-pdf\\pdf\\"

def convert_pdf_to_txt(path):
    with pdfplumber.open(path) as pdf:
        total_pages = len(pdf.pages)
        text = ""
        for i in range(total_pages):
            page = pdf.pages[i]
            content = page.extract_text()
            
            patterns = ["\(cid:62294\)", "\(cid:62295\)", "\(cid:62296\)", "\(cid:62297\)", "\(cid:62298\)", "\(cid:62299\)", "\(cid:62300\)", "\(cid:62301\)", "\(cid:62302\)", "\(cid:62303\)"]
            replacements = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            for i in range(len(patterns)):
                pattern = re.compile(patterns[i])
                content = pattern.sub(replacements[i], content)
            # 删除每页的表头
            if i == 0:
                content = re.sub(r'\n\d+\n', '\n', content)
                print(content)
            else:
                content = re.sub(r'^.*?\n', '', content, count=1)
            text += content + "\n"
    # 删除所有的[ ]
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\［.*?\］', '', text)
    # text = re.sub(r'\n(\d)(?!D)', r'*\1', text)
    # print("text2: " + text)
    text = re.sub(r'\u0007', ' ', text)
    text = re.sub(r'参考⽂献[\s\S]*', '', text)
    # text = text.replace('\n', '')

    # pattern = r'\n0'
    # match = re.search(pattern, text)
    # if match:
    #     print("match")
    #     text = text[match.end():].strip()
    return text

def txt_to_list(file_path):
    
    text = convert_pdf_to_txt(file_path)
    pattern = re.compile('\n⼗+[⼀⼆三四五六七八⼋九十⼗/u4E00/u4E8C/u4E8C/u56DB/u4E94/u516D/u4E03/u516B/u4E5D/u5341]+、|\n+[⼀⼆三四五六七八⼋九十⼗/u4E00/u4E8C/u4E8C/u56DB/u4E94/u516D/u4E03/u516B/u4E5D/u5341]+、|\n\d+[.]|\n\d |\n（⼗+[⼀⼆三四五六七八⼋九十⼗]+）|\n【.*?】|\n+（+[⼀⼆三四五六七八⼋九十⼗]+）')
    # 获取模式的匹配列表
    matches = re.findall(pattern, text)
    # 按照正则表达式对文本进行分段
    segments = re.split(pattern, text)
    print(segments[0])
    # segments = re.split(r'\*', convert_pdf_to_txt(file_path))

        
    segments[1:] = [matches[i] + segment + '\n' for i, segment in enumerate(segments[1:])]

    return segments

# def num_to_list(file_path):
#     pattern = r'\b(10\.\d+\.\d+)\b'
#     segments = re.split(pattern, convert_pdf_to_txt(file_path))

#     # 提取分段后的结果
#     result = []
#     for i in range(0, len(segments), 2):
#         if i + 1 < len(segments):
#             s = re.sub(r'\.\d', '', segments[i])
#             result.append(s.strip())  # 添加到结果列表中
#     return result

# def page_to_list(file_path):
#     with pdfplumber.open(file_path) as pdf:
#         total_pages = len(pdf.pages)
#         list = []
#         for i in range(total_pages):
#             page = pdf.pages[i].extract_text()
#             content1 = re.sub(r'5\d\d+(\n)?', '', page)
#             content2 = re.sub(r'^.*?\n', '', content1, count=1)
#             list.append(content2)
#     return list

def list_to_json(list):

    for item in list:
        dict = {"raw_content": item}
        # 打开文件，以写入模式写入数据
        with open("./json/data.json", "a", encoding='utf-8') as f:
            # 将字典对象写入文件
            json_str = json.dumps(dict, ensure_ascii=False)
            f.write(json_str + '\n')

for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            print(file_name)
            list_to_json(txt_to_list(file_path))

