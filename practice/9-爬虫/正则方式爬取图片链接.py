import requests,re

content = requests.get('http://www.cnu.cc/users/1823671').text
# print(content)

#根据上面的content获取爬取的图片的网页格式：
"""
<a href="http://www.cnu.cc/works/668076" class="thumbnail" target="_blank">
                    <div class="title">
                        生活的本意是平淡且知足
                    </div>
"""

re_compile = re.compile(r'<a href="(.*?)".*?class="title">(.*?)</div>', flags=re.S)
find_result = re.findall(re_compile, content)
# print(find_result)

for item in find_result:
	url,name = item
	sub_name = re.sub(r'\s','', name)
	print(f'{url}  {sub_name}')






#  测试匹配方式：
"""
     1.     <a href="(.*)" (.*)target="(.*)"   -  .*匹配字符串会直接匹配到target前，将   http://www.cnu.cc/works/674642" class="thumbnail  当作一整个
            匹配结果  [ ('http://www.cnu.cc/works/674642" class="thumbnail', '', '_blank')  ]
            
     2.   <a href="(.*?)" (.*)target="(.*)" -  .*?  非贪婪模式，只将 http://www.cnu.cc/works/674642 作为单独一个
            匹配结果 [('http://www.cnu.cc/works/674642', 'class="thumbnail" ', '_blank')]
            

"""
#  括号（()、[]、{}）内的多个字符串会自动拼接，换行时无需手动加 + 号，适合长字符串拆分书写（避免一行代码过长），但不会自动换行（需手动加 \n 控制换行）
str_a = ('<a href="http://www.cnu.cc/works/674642" \n'
                    'class="thumbnail" target="_blank">' )
p = re.compile(r'<a href="(.*?)"')  # 只匹配单行
p_1 = re.compile(r'<a href="(.*?)"', flags=re.S)  # re.S  匹配换行符在内的所有字符。这样就去匹配可多行文本
# str_a = '<a href="http://www.cnu.cc/works/674642" class="thumbnail" target="_blank">'
# p = re.compile(r'<a href="(.*?)" (.*)target="(.*)"')
print(re.findall(p, str_a) )
print(re.findall(p_1, str_a) )


list_b = [('http://www.cnu.cc/selectedPage', '\n                        这个冬天\n                    '), ('http://www.cnu.cc/works/674642', '\n                        说了再见\n                    ')]

for i in list_b:
	url,name = i
	print(f'{url} - {re.sub(r'\s','',  name)}') #  \s 匹配空白字符，包括空格、制表符


