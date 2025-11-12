with  open("../../doc/weapon.txt", encoding="utf-8") as file:
    print(file.read().replace("\n", " "))


def fina_in_text(param):
    with open("../../doc/sanguo_utf8.txt", "r", encoding="utf-8") as f:
        s = f.read().replace("\n", "")
        count = len(re.findall(param, s))
        print("人物 %s , 总共出现 %s 次" % (param, count))
    return count


# 统计各个主角在文本中出现的次数
import re

dict = {}
with open("../../doc/name.txt", encoding="utf-8") as file:
    names = file.read().split("|")
    for name in names:
        dict[name] = fina_in_text(name)
print(dict)

sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

# 文字处理标准库，re.findall(pattern, string, flags=0)，返回 pattern 在 string 中的所有非重叠匹配，以字符串列表或字符串元组列表的形式。对 string 的扫描从左至右，匹配结果按照找到的顺序返回
pp = re.findall("aa", ",bb,cc。aa")
print(pp)

# 排序
dict_test = {"1": "4", "2": "3", "3": "2"}
sorted_dict_test = sorted(dict_test.items(), key=lambda x: x[1])
print(sorted_dict_test)
