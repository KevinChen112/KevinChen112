print("小米","大米")
"""
开头注释
"""
# 字段注释
# 整型
a=1
print(type(a))
# 字符型
b=1.845
print(type(b))
# 布尔型
IsMan = True
print(type(IsMan))
# 字符型
c="小米"
print(type(c))
# 列表
d=["as","ad"]
print(type(d))
# 元组
e=("as","ad")
print(type(e))
# 字典
f= {"name":"张三","phone":"18302463889"}
print(type(f))
# 输入，输入内容为字符串
# name = input("请输入你的名字：")
# print("你好",name)
# print(type(name))
#数据类型转换 int
# age=input("请输入一个你的年龄：")
# print("年龄字符类型为",type(a))
# age1=int(age)
# print("年龄整型类型为",type(age1))
#字符串 转换 int
a3="18"
b3=int(a3)
print(type(b3))
#浮点型 转换 int
a4=18.11
# b4=int(a4)
# print(type(b4))
# print(b4)
#int 转换 浮点型
a5=18
b5=float(a5)
print(type(b5))
print(b5)
#数字字符串转浮点型
a6="18"
b6=float(a6)
print(type(b6))
print(b)
#格式化输出 占位符
print("今天的收入是：%s "%(a6))
print("今天的收入是:",a6)
print("今天的收入是：%.1f "%(a4))
print("今天的收入是:",a4)
a6=0.9
print("输出百分比：%f%%"%(a6))
"我的名字"
#格式化输出 字符串格式化
d1="张三"
d2=92.11
print("我的名字是：%s,我的分数是：%d"%(d1,d2))
print(f"我的名字是：{d1}，我的分数是{d2}分")