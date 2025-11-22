#match ： 匹配的字符串和正则需一一对应
#seatch :   不要求和元字符完全匹配

import re

p1 = re.compile(r'(\d{4})-(\d{1,2})-(\d+)')

string = 'abc2025-11-22'

print(p1.match(string))
print(p1.search(string).groups())
