# 面向对象编程
# def s(a,b):
#     return a+b
#
# print(s(10,20))


# 对变量和方法的打包

# 类和对象
# 创建一个类
# class str_demo():
#
#     s = "类变量" # 类变量  类加载到内存中就会被创建   类被销毁时，同步被销毁
#
#     def replace(self):
#         self.a = "实例变量" # 实例变量 调用该变量创建的实例方法时 对象被销毁时同步被销毁掉
#         b = "局部变量"  # 局部变量  方法运行结束就被销毁
#         print("字符串替换")
#
#     def split(self):
#         print(str_demo.s) # 访问类变量
#         print(__class__.s) # 访问类变量(推荐)
#         print(self.s) # 不推荐
#         print(self.a) # 访问实例变量





# 实例化
# sd = str_demo() # 实例化 sd就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()

# 类外部访问
# 类变量
# print(str_demo.s) # 通过类名直接访问（推荐）
#
# # 实例变量
# sd = str_demo() # 实例化成一个对象
# sd.replace() # 调用实例方法创建 实例变量
# print(sd.a) # 通过对象访问实例变量
# # 通过对象和类调用类变量
# print(sd.s) # 可以通过对象访问类变量（不推荐） 通过对象调用属性的搜索顺序 实例变量-》类变量
# sd.s="s是一个实例变量" # 创建了一个实例变量
# print(sd.s) # 访问实例变量s
# print(str_demo.s) # 访问类变量s
# 类内部访问实例变量和类变量
# sd = str_demo()
# sd.replace()
# sd.split()

# sd = str_demo()
# st = str_demo()
# str_demo.s="str_demo"
# sd.a = "sd"
# st.a = "st"
# print(sd.a)
# print(st.a)
#
# print(sd.s)
# print(st.s)


class str_demo():
    b = "类变量"
    # 不需要显式调用，程序自动调用的
    def __init__(self):
        self.a="实例变量"
        print("魔法方法")
        self.replace() # 在实例方法中调用实例方法
        __class__.split() # 在实例方法中调用类方法
        __class__.static()  # 在实例方法中调用静态方法
        self.static()  # 在实例方法中调用静态方法


    # 实例方法
    def replace(self): # self代表当前对象本身
        print("实例方法")


    @classmethod
    def class_method(cls):# cls 代表当前类本身
        # 不能调用实例方法
        cls.split() # 调用类方法
        cls.static()# 调用静态方法


    @classmethod # 装饰器
    def split(cls):
        print("类方法")

    @staticmethod
    def static_method():
        # 不能调用实例方法
        __class__.split()  # 调用类方法
        __class__.static()  # 调用静态方法
    @staticmethod
    def static():
        print("静态方法")



# 类外部调用方法
# str_demo.split() # 调用类方法
# str_demo().replace() # 通过对象调用实例方法
# str_demo.static() # 通过类名调用静态方法
# str_demo().static() # 通过对象调用静态方法
# str_demo() # 调用__init__魔法方法

# 在类内部调用方法
# str_demo()# 实例方法
# str_demo.class_method()# 类方法
# str_demo.static_method() # 静态方法


# 类的封装-方法或者属性的访问权限控制

# class Demo():
#
#     __a = "类变量" # __开头，表示是一个私有变量
#     b = "类变量2"
#
#     def __say(self):# __开头，表示是一个私有方法
#         print("hello")
#     def hello(self):
#         print(self.__a)
#         self.__say()

# d = Demo()
# print(d.b)
#
# d.hello()

#
# class PrivateDemo():
#     _a = None
#
#     def set_a(self,value):
#         self._a = value
#     def get_a(self):
#         return self._a
#
# p = PrivateDemo()
# p.set_a("hello")
# print(p.get_a())


# 类的继承

#
# class Parent():
#
#     def __init__(self,a):
#         self.a = a
#
#     first_name = "王"
#     __second_name = "五"
#
#     def name(self):
#         print("我叫" + self.first_name + self.__second_name)
#
#     def ji_neng(self):
#         print("锁匠")
#
#
# class Son(Parent):
#
#     # def __init__(self,a,b):
#     #     super().__init__(a)
#     #     self.b = b
#
#     __second_name = "八"
#
#
#     def name(self):
#         print("我叫" + self.first_name + self.__second_name)
#
#
# # son = Son()
# # print(son.first_name)
# # son.ji_neng()
#
#
#
# p = Parent(19)
# print(p.a)
# s = Son(1)
# print(s.a)

# 多态 - 子类中，对父类方法的重写

# class Parent():
#
#     def ji_neng(self):
#         print("开锁")
#
#
# class Son(Parent):
#
#     def ji_neng(self):
#         super().ji_neng()
#         print("盗窃")
#
# p = Parent()
# p.ji_neng()
# s = Son()
# s.ji_neng()


# import os  # 路径操作

# print(os.listdir(".")) # 获取指定文件夹下所有文件
# print(os.path.exists("a.txt")) # 判断文件或者文件夹是否存在
# print(os.path.abspath("a.txt")) # 获取文件的绝对路径（不会判断文件是否存在）
# print(os.path.basename(os.path.abspath("a.txt"))) # 获取文件或者文件夹的名字
# print(os.path.dirname(os.path.abspath("a.txt"))) # 获取文件或者文件夹的路径
# print(os.path.join("E:\\workspace\\python\\base_2008A\\","a.txt")) # 拼接文件路径
# os.system("dir") # 执行cmd命令

# import random # 随机模块
# print(random.randint(1,20)) # 获取随机整数
# print(random.random()) # 获取随机数 小数
# print(random.choice("0123456789")) # 在指定集合中，随机获取一个数据
# l = random.choices("0123456789",k=10)# 在指定集合中，随机获取一组数据
# print(l)
# print("".join(l)) # 把可迭代对象转成字符串
#
#
# import re
#
# a = "我叫：王大锤,我今年18岁了"
# r = re.compile("年(.*?)岁") # 编译正则表达式
# res = r.findall(a) # 使用正则表达式从原数据中获取匹配结果
# print(res)

# import time
#
# print(time.time()) # 获取秒级时间戳
# t = time.localtime(time.time()) # 把时间戳转换为时间结构体
# str_time = time.strftime("%Y-%m-%d %H:%M:%S",t)# 把时间结构体转换成时间类型的字符串
# print(str_time)
# t = time.strptime(str_time,"%Y-%m-%d %H:%M:%S") # 把字符串时间转成时间结构体
# time_stamp = time.mktime(t)  # 把时间结构体，转时间戳
# print(time_stamp)

# 第三方模块

# requests

# 1、pip 工具下载并安装第三方模块requests
# 2、from import或者import 导入刚安装的第三方模块
# 3、使用其中的代码

import requests

'''
pip install 第三方模块名   下载并安装第三方模块
pip uninstall 第三方模块名   卸载第三方模块
pip list      查看所有已安装的第三方模块
pip freeze > requirements.txt    导出所有已安装的第三方模块名及版本至文件中
pip install -r requirements.txt   安装文件中所有的第三方模块
'''


'''
1、编写一个返回随机手机号的方法
2、编写一个返回指定长度和内容的随机字符串方法
3、编写一个返回随机姓名的方法
'''

























