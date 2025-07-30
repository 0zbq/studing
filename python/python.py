#输出print()
'''
print("hello")
print(1)
print(1.5,1,True,"hello"+" world")
print('hh \nHe said "Let\'s go!"')
print("""
hhhhh
sac
ref """)
'''

#变量
'''
greet_c="你好"
greet_e="Hello"
name_c="张三"
namw_e="ZhangSan"
print("hello"[2])
print(greet_e[0])
c=None  	#空值类型
c=True		#布尔类型
c=False
print(type(1.5))
print(type(1))
print(len("55555"))
print(greet_c+name_c)
'''

#数字模块
'''
import math
print(math.log2(8))
print(math.sin(1))
print(6**2)
'''


'''
多行
注释
'''
"""
多行
注释
"""

#输入inpust
'''
user=input("请输入：")
print(type(user))
fuser=float(user)
print(type(fuser))
iuser=int(user)
print(type(iuser))
buser=bool(user)
print(type(buser))
'''

#判断
'''
x=float(input("请输入一个数"))
if x>0:
    print("正数")
    print("大于0")
elif x<0:
    print("负数")
    print("小于0")
else :
    print("0")

if 10<x<20:
    print("10~20")
elif -10<=x<=10:
    print("-10~10")
elif -20<x<-10:
    print("-20~-10")
else:
    print("0000")
    
if -10<x<10 and not x==0:
    print("-10~10并且不为0")
elif x==0:
    print(0)
elif x==10 or x==-10:
    print("端点")
else:
    print("0000")
''' 
 
#列表(可变)
'''
shopping_list=["键盘","键帽","鼠标"]
print(shopping_list)
shopping_list.append("显示器")
print(shopping_list)
print(len(shopping_list))
shopping_list.remove("显示器")
print(shopping_list)
s="Hello"
print(s.upper())
print(s)
shopping_list[0]=0
shopping_list[1]=True
shopping_list[2]=None
shopping_list.append(1.1)
print(shopping_list)
num_list=[1,10,-7,96]
print(max(num_list))
print(min(num_list))
print(sorted(num_list))
print(num_list)
'''

#字典（可变）：键和值（不可变）
#元组（用于平替列表做键，不可变）
'''
contacts={"小明":"137","小花":"138"}
print(contacts["小明"])
contacts={("张伟",23):"15065",("张伟",24):"11111"}
print(contacts)
contacts["小明"]="156418"
print(contacts)
contacts["小明"]="5468"
print(contacts)
print("小明" in contacts)
print("晓红" in contacts)
str="小明"
if str in contacts:
    print("存在")
del contacts["小明"]
print(contacts)
print(len(contacts))
'''

#for循环
list=[36.1,37.2,37.7,36.5]
for temperature in list:
    if temperature>37:
        print("发烧了")
        
dict={"111":36.1,"112":37.2,"113":37.7,"114":36.5}
for num in dict.keys():
    if (dict[num]>37):
        print(num,"发烧了")
for tem in dict.values():
    if tem>37:
        print("发烧了")
for num,tem in dict.items():
    if(tem>37):
        print(num,"发烧了")

for i in range(5,10):
    print(i)
for i in range(1,11,2):
    print(i)
















