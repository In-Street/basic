r"""
 参考： https://www.runoob.com/python3/python-re.html

.  单个字符
^  开头
$  结尾
*  该符号前面的字符出现 0次或多次
+  该符号前面的字符出现 1次或多次
?  该符号前面的字符出现 0次或1次
{m}  该符号前面的字符出现 m次
{m,n}  该符号前面的字符出现 m次 到n次
[]  出现括号里的任意一个字符就算匹配成功。 如 c[bcd]t ,可匹配 cbt、cct、cdt


\d  匹配单个数字
\d+  匹配多个连续数字
\d{5} 匹配指定个数(5个)的数字
\D 匹配非数字
\s  匹配空白字符（空格、制表符等）
\S  匹配非空白字符
\w 匹配单词字符（字母、数字、下划线）。 \w+  -> 'Ab_1'
\W  匹配非单词字符。 \W+ -> '!@#'

^$  匹配空行,什么也不包含
.*  匹配整个字符串

"""

import re

p = re.compile('ca*t')
result = p.match('caaaat')
print(result)

p2 = re.compile('jpg$')
print(p2.match('aa.jpg'))

#匹配空行
p3 = re.compile('^$')
print(p3.match(''))


#匹配出现三个字符
p4 = re.compile('.{3}')
print(p4.match('aabc'))


