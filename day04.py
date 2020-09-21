# 1、编写一个返回随机手机号的方法

'''
用一个列表，存储所有的有效号段字符串
随机生成一个长度8位的数字字符串

'''
import random
#
#
# def phone():
#     hao_duan_list = ["131",'185','181','183','182','184','186','187','188','189',"131","130","132","133","134","135","136"]
#     hao_duan = random.choice(hao_duan_list)
#     res = random.choices("0123456789",k=8)
#     ba_wei = "".join(res)
#     return hao_duan + ba_wei
#
# print(phone())


# 2、编写一个返回指定长度和内容的随机字符串方法
# def random_str(str, length):
#     res = random.choices(str, k=length)
#     return "".join(res)
#
#
# print(random_str("abcdefghijklmnopqrstuvwxyz1234568790",10))

# 3、编写一个返回随机姓名的方法

'''
姓
名字 1 - 2

姓列表
名字 字的取值范围列表
随机获取1-2的随机整数
获取名字的字


'''

#
# def random_name():
#     xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
#     zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
#     xing = random.choice(xing_list)
#     zi_length = random.randint(1,2)
#     zi = random_str(zi_list,zi_length)
#     return xing + zi
#
# print(random_name())


# NameError
# SyntaxError 语法错误
# print("hello")

# print(1/0) # ZeroDivisionError 运行时错误   异常: 报错，结束代码的运行
# print("asdf")
# try:
#     # r = open("b.txt","r") # 报错 FileNotFoundError
#     print(1 / 2)  # ZeroDivisionError
# except (FileNotFoundError,)  as e: # 捕获指定异常，并获取异常信息
#     print(e)
#     print("程序执行遇到了问题")
#     print("重新打开文件")
# except ZeroDivisionError as e:
#     print("除数不能为0")
# else:
#     print("程序运行没报错")
# finally:
#     print("不管程序有没有报错都会运行")
#
#
# print("文件已经打开")
#



'''
代码多人协同
svn
git

git 环境搭建
1、本机电脑 （一次）
安装一个git的软件

2、远程代码仓库账号准备 （一次）
github  https://github.com/
gitee  阿里巴巴
gitlab 腾讯


3、用户认证，需要设置ssh秘钥 （只要不换电脑一次）

4、新建一个远程仓库备用 （没有新项目，建一次就够了）

5、初始化本地仓库 （有就行，没必要做第二次）

6、新建.gitignore文件，填入不想上传的文件





'''






