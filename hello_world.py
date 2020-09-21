#
# # a变量名=赋值符 "hello world"值
# a="hello world"
#
#
# # 值类型
# '''
# 字符串 '' ""
# number  整数 小数  111 3.2
# 布尔值  True False
# 空值   None
#
# 列表 list [1,2,3,4,5]   可修改   有序
# 元祖 tuple (1,2,3,4,5)  不可修改  有序
# 集合  set {1,2,3,4,5}   不可重复  无序
#
# 字典  dict {"name":"王大锤","age":18} # key不可修改,key不可重复,无序
# '''
#
# l = [1,2,3,4,3]
# l[0]=10 # 修改列表
# print(l)
#
#
# t=(1,2,3,4,5,2)
# # t[0]=10 # 修改元祖，报错
# print(t)
#
# s = {1,2,3,4,1,2,3,4}
# print(s)
# # print(s[0]) # 无序，所以不支持下标访问
#
# # d = {"name":"王大锤","age":18,"name":"小明"}
# # print(d)
# d = {"name":"王大锤","age":18}
# print(d["name"])
#
#
# # 类型转换
#
# a=10
# b="20"
# print(a + int(b)) # 字符串转整数
# print(str(a) + b)  # 整数转字符串
#
# a=10
# b="2.9"
# print(a + float(b)) # 字符串转小数
# print(str(a) + b)  # 整数转字符串
#
# a=True   # 布尔类型也是数字  True 1 False 0
# b=29
# print(a + b)
#
# l = [1,2,3,4,5,6]
# print(tuple(l)) # list转tuple
# print(set(l)) # list to set
#
# t = (1,2,3,4,5)
# print(list(t)) # tuple转list
# print(set(t)) # tuple to set
#
# s = {1,2,3,4}
# print(list(s)) # set to list
# print(tuple(s)) # set to tuple
#
#
# a = "123456578"
# print(list(a)) # str to list
# print(tuple(a)) # str to tuple
# print(set(a)) # str to set
#
#
# # 运算符
#
# '''
# 算术运算符
# + 加
# - 减
# * 乘
# / 除
# % 取余（取模）
# // 取整
# ** 幂
# '''
# # 字符串
# a="123"
# b="456"
# print(a+b)
# print(a*3)
#
# # 列表
# l = [123,3,4,5]
# m = [1,2,3,4]
# print(l+m)
# print(l*2)
# # 元祖
# t=(1,2,3)
# u=(4,5,6)
# print(t+u)
# print(t*3)
#
# '''
# 比较运算
# == 等于
# != 不等于
# >   大于
# <   小于
# >=  大于等于
# <=  小于等于
# '''
# a="123"
# b="abc"
# print(a<b) # 不推荐用
#
# '''
# 逻辑运算符
# and 且
# or  或
# not 非
# '''
# print(1>2 and 2>1) # False
#
# '''
# 成员运算符
# in
# not in
# '''
# a = "ahelog"
# l=["a","4","g"]
# t=("a","4","g")
# s={"a","4","g"}
# d = {"name":"王大锤","sex":"女"}
#
# print("a" in a)
# print("a" in l)
# print("a" in t)
# print("a" in s)
# print("name" in d) # 字典只能判断key是否存在
#
# '''
# +=
# -=
# *=
# /=
# %=
# //=
# **=
# '''
#
# a = 10
# # a = 1 - a  不可简写
# # a = a -1  可以写成 a -= 1
# a -= 1
# print(a)
#
# # 运算符优先级
# # 算术运算符 > 条件运算符、成员运算符 > 逻辑运算符 > 赋值运算符

# print((4 + 1) > (2 * 3))


# 如果我有500万，买两碗豆浆，喝一碗扔一碗
# 如果有 1000万，把老板裁了
# 如果有1个亿，把公司买了
# 没钱还是洗洗睡把

# money = 500000
# if(money < 5000000):
#     print("洗洗睡把")
#
# elif(money < 10000000):
#     print("买两碗豆浆")
#     print("喝一碗扔一碗")
#
# elif(money < 100000000):
#     print("把老板裁了")
#
# else:
#     print("把公司买了")



# 循环
# for i in [1,2,3,4,5,6]:
#     print(i)
#     print("重要的事情说100遍！")
#
# for i in "123":
#     print(i)


# for i in (1,2,3):
#     print(i)

# for i in {1,2,3}:
#     print(i)

# for i in {"name":"王大锤","sex":"女"}:
#     print(i)

# for i in range(10):
#     print(i)

# print(list(range(100)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,0,-1)))
# print(list(range(10,0,-2)))

'''
range(参数1,参数2,参数3)
第一个参数：起始值，包含边界
第二个参数：终止值，不包含边界
点三个参数：步长 可正 可负
必须是一个区间，非区间就无数据
'''
# print(list(range(10,0,-2)))

# while循环

# i = 1
# while(i<10):
#     print(i)
#     i += 1

# while True:# 死循环
#     print("hello")

# 打印1到10的数据，遇到7不打印
# for i in range(1,11):
#     if(i == 7):
#         pass
#     else:
#         print(i)

# 结束循环 break
# for i in range(1,11):
#     if(i == 7):
#         break
#     print(i)


# 跳过本次循环 跳过continue下方的所有代码，进入下次循环
# 打印1到10的数据，遇到7不打印
# for i in range(1,11):
#     if(i == 7):
#         continue
#     print(i)

# 打印出100以内可以被3整除的数
# for i in range(1,101):
#     if (i % 3 == 0):
#         print(i)
# 计算1-100的和 1+2+3+4....+100 =
# s = 0
# for i in range(1,101):
#     s+=i
# print(s)

# 逢七过 7的倍数或者以7结尾就说过
# for i in range(1,100):
#     if(i % 7 == 0 or i % 10 == 7):
#         print("过")
#     else:
#         print(i)
#
#
# a = 129
# b = a//10
# print(b)
# print(b%10)

# 九九乘法表
# 冒泡排序





