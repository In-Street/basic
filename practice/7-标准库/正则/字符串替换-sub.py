import re

# sub(匹配规则，替换内容，原始字符串)

# 将字符串中的c 替换成空串
sub_string = re.sub('c', '', 'acd')
print(sub_string)  # ad



# 提取电话号码:  flags:  re.I (忽略大小写) 、re.M (多行)、re.S (.号匹配包括换行在内的所有字符)
phone = '182-1111-2222 # 电话号码注释\n'
sub_phone = re.sub(r'#.*', '', phone, flags=re.S)  #   从#开始匹配到结尾
print(sub_phone)  # 182-1111-2222

sub_phone_string = re.sub(r'\D', '', sub_phone)  #规则前面加字符r ,Python 会禁用转义解析，将\D 原样传给sub方法
print(sub_phone_string) # 将匹配到的非数字字符替换为空串， 18211112222

