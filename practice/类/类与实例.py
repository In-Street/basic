class Player:


    def __init__(self, name, hp, phone):
        self.name = name
        self.hp = hp
        self.__phone = phone  # 将属性为 __xx  形式时，此属性不能被实例修改，只能通过方法进行修改


    def print_hp(self):
        print("%s : %s ,  %s" % (self.name, self.hp,self.__phone))

    def update_name(self, new_name):
        self.name = new_name

    def update_phone(self, new_phone):
        self.__phone = new_phone


# 冗余一个空class，暂时不用时，可以使用pass关键字
class Monster:
    pass

user_1 = Player("Jay", 100,'182')
user_2 = Player("Taylor", 80,'135')

user_1.print_hp()

# 通过方法来修改name
user_1.update_name("Jay_2")
user_1.print_hp()

# 通过属性赋值
user_1.name = "Jay_3"
user_1.print_hp()


user_1.update_phone("151")
user_1.print_hp()

user_1.__phone = '152'  #没有改变，仍是151. __xx属性只能通过方法进行修改
user_1.print_hp()