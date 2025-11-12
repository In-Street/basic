list = [1, 2, 3]
li = iter(list)
print(next(li))
print(next(li))

# range(start, stop[, step]) 。只支持int型 从10开始，以步调为3向后遍历，10 13 16 19
for i in range(10, 20, 3):
    print(i)


def range_(start, end,step):
    x=start
    while x<end:
        print(x) # while 会将符合条件值一次性返回所有
        x+=step
range_(10,20,3.5)



# 使用yield 函数称为生成器，是迭代器的一种，当需要自定义迭代器时，使用此关键字
def range_yield(start, end,step):
    x=start
    while x<end:
        yield x  # yield会记录当前位置。当再次调用next时，会从记录的位置开始返回值
        x+=step

for x in range_yield(10,20,3.5):
    print(x)
