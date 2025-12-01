"""
pip3 install bs4
 pip3 install lxml

"""
from bs4 import BeautifulSoup

html  = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

# title标签内容
print(soup.title.string)

#找到所有a标签，返回列表。 从列表中获取链接
all_a = soup.find_all('a')
print(all_a)
for a in all_a:
	print(a.get('href'))


# 根据id找标签
soup.find(id='link2')

# 获取所有文本内容
print(soup.getText)

soup.find_all('div', class_='story')