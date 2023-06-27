import requests
import json

# 获取文献阅读页码和PDF文件名称
url = 'http://pdf.nlc.cn'
fromCode = 'ymh'
fromName = '读者云门户'
id = '1258.0'
indexName = 'data_011'
title = '新鐫海上醫宗心領全帙'
identifier = '008434118'
servercode = '3'
pdfname = 'data09/sbgj_shanbenguji/zhyc20170411_01/duixiang/SBGJ15610_00001/SBGJ15610/00001/SBGJ15610_00001.pdf'
pressName = '釋清高'
data = {
    'dataId': id,
    'indexName': indexName,
    'title': title,
    'identifier': identifier,
    'serviceId': servercode,
    'pdfName': pdfname,
    'fromCode': fromCode,
    'fromName': fromName,
    'pressName': pressName
}
response = requests.post('http://pdf.nlc.cn/allSearch/permissionNew', data=data)
json_data = json.loads(response.text)
readpageLast = json_data['obj']['readPageNum']

# 构造PDF文件链接并下载
pdf_url = '{}/webpdf/web/viewer.html?file=pdf/{}/{}#page={}'.format(url, pressName, pdfname, readpageLast)
response = requests.get(pdf_url)
with open('output.pdf', 'wb') as f:
    f.write(response.content)

print('PDF文件已保存为：output.pdf')