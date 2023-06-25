# import requests

# url = 'https://book.sciencereading.cn/shop/book/Booksimple/list.do'
# response = requests.get(url)
# if response.status_code == 200:
#     page_source = response.text
#     print(page_source)  # 输出电子书列表页面的HTML源代码，以便后续解析
# else:
#     print('请求失败：', response.status_code)

from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = 'https://book.sciencereading.cn/shop/book/Booksimple/list.do'
session = HTMLSession()
response = session.get(url)

if response.status_code == 200:
    page_source = response.html.html
    soup = BeautifulSoup(page_source, 'html.parser')
    # 'bookList' 是电子书列表的容器 div 的 ID
    book_list_div = soup.find('div', {'id': 'bookList'})
    book_list_items = book_list_div.find_all('li')
    for item in book_list_items:
        # 'BookId'、'pdf' 分别是电子书详情页和下载链接所在的关键字
        book_id = item.a['href'].split("'")[1]  
        pdf_link = 'https://book.sciencereading.cn/bookfile/' + book_id + '.pdf'
        # 将 pdf 文件下载到本地并保存
        pdf_response = requests.get(pdf_link)
        with open(f'{book_id}.pdf', 'wb') as f:
            f.write(pdf_response.content)
        print(f'{book_id} 下载成功')
else:
    print('请求失败：', response.status_code)