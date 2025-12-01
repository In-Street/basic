var = 123

def f():
    var = 456
    print(var)

f() # 456 , 只影响函数内部
print(var) # 123 # 对外部变量不影响


var2 = 789
def f2():
    global var2
    var2= 789
    print(var2)

f2()  # 789
print(var2)  # 789