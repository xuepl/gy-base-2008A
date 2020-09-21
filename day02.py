
# # 除法运算
# a = 10 # 除数
# b = 20 # 被除数
# if b == 0:
#     print("被除数不能为0")
# else:
#     print(a/b)
#
# a = 30 # 除数
# b = 10 # 被除数
# if b == 0:
#     print("被除数不能为0")
# else:
#     print(a/b)


# 函数（方法）
# def 关键字； div：方法名；a,b 接收外界参数，参数变量必须写在()；: 表示下方包含一个代码块（方法体）
# def div(a,b):
#     if b == 0:
#         print("被除数不能为0")
#     else:
#         print(a / b)
#
# div(10,20)
# div(40,10)
# div(60,130)

'''
def 方法名(参数1，参数2，...):
	方法体
	return 返回值

def: 定义方法关键字
方法名：类似变量名，储存方法的地址
():参数列表，里边存放方法的参数
参数:运行该方法需要的外部数据
方法体: 方法的代码块
return:表示一个方法的结束，方法返回数据的关键字
'''

# def jiu_jiu():
#     print("九九乘法表")
#
# jiu_jiu()

# 方法的定义
# def select_data(sql):
#     res = "查询结果"
#     return res
#
# result = select_data("") # 方法调用使用变量接收方法返回值
# print(result)

# 参数定义

# 位置参数 调用时，参数有一个传一个
# def s(a,b):
#     return a+b
# print(s(1,2))

# 关键字参数 给参数设置默认值，
# 如果调用时没有传参则用默认值
# 关键字、位置同时存在，位置参数在前边，关键字参数在后边
# def s(a=1,b=10):
#     return a+b
# print(s(1,3))

# 调用传参
# 按照位置传参
# print(s(1,2))

# 按照关键字传参
# print(s(b=20))

# 位置和关键字同时存在，位置在前，关键字在后
# print(s(10,b=20))
# print(s(10,a=20)) # 错误，不能对同一个变量重复传参

# 动态参数定义

# def ar(a,*args,b=10,**kwargs):
#     print(args)
#     print(kwargs)

# ar(1,2,3,4,5,6,7,8,9,0,c=10,b=20)



# def case1(a,b=2):
#     print(a)
#     print(b)
#     print("这是一个测试用例1")
#
# def case2(a,b,c=20):
#     print(a)
#     print(b)
#     print("这是一个测试用例2")

#
# print("执行用例之前",10,20)
# r=case1(10,20)
# print("用例执行之后",r)
#
# print("执行用例之前",2,4)
# r=case2(2,4)
# print("用例执行之后",r)

#
# def log(func,*args,**kwargs):
#     print("执行用例之前",args,kwargs)
#     r = func(*args,**kwargs)
#     print("用例执行之后", r)
#
#
# log(case1,10,20)
# log(case2,1,2)

# 内置函数
#
# a = 1000
# print(id(a)) # 获取变量内存地址
#
# # i = input("请输入一个数据")# 获取控制台输入
# # print(i)
#
# print(type(a)) # 获取变量类型
# print(type("sdf"))
#
# print(isinstance("",int)) # 判断变量类型
#
#
# l = [1,2,3,4]
# print(len(l)) # 获取变量值的个数 支持list tuple set dict str
#
# # # 操作文件
# # f = open("a.txt",'w') # 以写入的形式打开文件 a追加写入 b打开二进制文件
# # f.write("hello")  # 写入数据
# # f.close() # 关闭文件
#
#
# f = open("a.txt",'r') # 以写入的形式打开文件
# res = f.read()  # 写入数据
# print(res)
# f.close() # 关闭文件

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,'=',i*j,end='\t')
#     print()
# c = 10 # 全局变量
#
# def aaa():
#     b = 20 # 局域变量
#     c = 30
#     print(b)
#     print(c)
#
#
# aaa()


# c = 10
#
# def aaa():
#     global c # 在局部作用域中声明全局作用域的变量
#     c = 20
#
# aaa()
# print(c)
#
# d={"name":"王小锤"}
# def ddd():
#     d["name"]="王大锤"
#
# ddd()
# print(d)
#
# a = 10
# b = a
# print(id(a))
# print(id(b))
# a=11
# print(b)

# 变量作用域  def class lambda
# 变量搜索规则 就近原则
# 局部变量，无法在外部使用
# global可以在局部作用域中声明变量为全局变量
# python中变量赋值是对存储空间的引用，而不是对存储空间的拷贝

# 字符串
# a="1234567890"
# b="456"
#
#
# print(a+b) # 拼接
# print(a*3) # 复制
# ## 截取
# print(a[0]) # 根据下标获取单个字符
# print(a[2:6]) # 截取3-6的字符
# print(a[:6]) # 截取1-6的字符
# print(a[4:]) # 截取5-0的字符
# print(a[-2:]) # 倒着数
# print(a[1:-2])
# print(a[::2])
# print(a[::-1]) # 反序
# print(a) # 截取操作不会修改原字符串
# '''
# 语法格式 变量名[参数一:参数二:参数三]
# 类比range函数
# 第一个参数:截取字符串的起始下标，默认为0
# 第二个参数：截取字符串的结束下标，开区间
# 第三个参数：步长，默认为1
# '''
# a = " sadfasdf " # 字符串对象
# a = a.strip()
# print(a.strip()) # 去除前后空格
# print(a.lstrip()) # 去除左空格
# print(a.rstrip()) # 去除右空格
# line = "用例名,账户名，充值金额,预期结果"
# line = line.replace("，",",") # 替换
# print(line)
# print(line.split(',')) # 切片
# print(line.find("预期")) # 查找，找到返回第一个字符的下标，找不到返回-1
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         # 1 X 2 = 2
#         print("{} X {} = {}".format(j,i,i*j),end='\t') # format格式化字符串
#     print()



# 列表

# 遍历列表
# l = [1,2,3,4,5,6,7,8]
# # for i in l :
# #     print(i)
#
# l[0]=20 # 根据下标修改列表元素的值
# l.append(9) # 往列表末尾添加数据
# l.insert(2,30) # 根据下标往列表中插入数据
# l.extend((1,2,3,4,5)) # 往列表末尾添加多个数据
# l.pop()#删除列表末尾最后一个元素
# l.pop(0) # 根据下标删除数据
# l.remove(2) # 根据内容删除列表中的数据，有重复只会删除第一个
# print(l.index(6)) # 查询某个元素的下标，多个值，只查询第一个
# l.sort() # 默认升序，会修改原列表中的数据
# l.sort(reverse=True) # 降序

# print(l)
# s = [1]
# print(s)
# 元祖
# t = (1,)
# print(t)
## 遍历，拼接，截取 和字符串列表一样
# 不支持修改，所以不支持其他操作

# 集合
# s = set()
# ## 遍历
# ## 不支持下标索引，所以不支持其他操作
# # 字典
# d = {"name":"小明","age":"20","sex":"男"}
#
# print(d["name"]) # 访问字典值
# d["name"] = "小红" # 修改value
# d["sex"] = "女" # 因为sex在原字典中不存在，所以是新增
# d.pop("sex") # 删除字典中的数据
#
# d2 = {"sex":"女"}
# d.update(d2) # 合并两个字典
# print(dict(d,addr="上海闵行",phone="1856954125")) # 创建一个新字典，并把数据放进去
#
# print(d)

# 冒泡排序


l = [10,1,35,61,89,36,55]
# 依次比较相邻的两个数据，如果前边的数据比后边的大， 则交换两个数据的位置，直到把最大的数据都放到最后第一次排序结束，
# 第二次排序重复第一次排序的动作，把第二大的放到倒数第二的位置，依次类推，直到所有的数据都排好序为止


for i in range(len(l)-1,0,-1): # i代表最后一个未排好序的数据下标
    for j in range(0,i): # j 代表每次循环时，当前位置的下标
        if(l[j] > l[j+1]): # 比较当前位置和下一个位置的数据大小，如果当前位置大于下个位置，则交换两个数据的位置
            l[j],l[j+1] = l[j+1],l[j]  # 交换两个数据的位置

print(l)
