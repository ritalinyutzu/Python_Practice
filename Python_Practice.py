#!/usr/bin/env python
# coding: utf-8


score = 80


print(score)



fruit = "banana"


print(fruit)



a = b = c = 20


print(a,b,c)


string = "welcome!\nRita" #/n換行


print(string)


print(type(True)) #type命令
print(type(87))
print(type("Hello World!"))
print(type(87.0))



temp = 21+ int("66") #資料型態轉換
print(temp)


del str
math = 60
print("小明的數學成績是" + str(math))


#print 輸出指令 sep為分隔字元,end為結束字元
print(87,"Rita",87,sep="&") #符號$可以自己改成想要的
print(87,"Rita",87,sep=",",end=".") #結尾以.結尾
print(87,"Rita",87,sep="",end="！")


#% 字串格式化 
name = "Rita"
python = 8.7
print("%s 的python程度只有 %8.1f 分" %(name,python))
print("%s 的python程度只有 %8.2f 分" %(name,python))


#print(字串.format(參數列))
print("{}的python程度只有{}分".format("Rita",8.7))



#順序指定參數,從0算起 
print("{0}的python程度只有{1}分".format("Rita",8.7))



#input輸入指令
#變數 = input([提示字串])
score = input(["Rita的python成績"])
print(score)
#會跑出一條空格 可以填東西進去！



#雙向判斷式
password == 5487
password == input("請輸入密碼:")
if password == 5487:
    print("Hello 恭喜成功")
else:
    print("白痴 密碼錯了")



for n in range(2000):
    print(n+1)
break 



for i in range(1,31):
    print(i,end=",")


temp = 2021
n = int(input("月:"))
for i in range (2021,int(n),int(n+1)):
    temp+=i
print("明天的日期%d是%d" %(2021,int(n),int(n+1)))



n = 0
for i in range(1,6):
    print("外部第",i,"次迴圈","內部執行",i,"次迴圈:",end="")
    for j in range(1,i+1): #內部迴圈
        print("#",end="")
    print(n)



#99乘法表
for i in range(1,10):
    for j in range(1,10):
        product = i*j
        print("%d*%d=%2d"%(i,j,product),end="")
    print()


for i in range(1,11):
    if(i==6):
        break
    print(i,end=",") #當i=6時符合條件式,執行break命令離開迴圈,結束程式


total = n = 1
while n <= 10:
    total += n
print(n)


X=10.0
Y=(x<100.0 and isinstance(x,float)
print(y)



def GetArea(width,height):
    area = width*height
    return area
temp = GetArea(6,9)
print(temp)


import datetime as dt

def Current_Date(Next_Date):
    year = int(Next_Date.split('/')[0])
    month = int(Next_Date.split('/')[1])
    day = int(Next_Date.split('/')[2])

    return dt.date(year,month,day) + dt.timedelta(1)


Current_Date('2020/1/1')



#巢狀判斷式
money = int(input("請輸入購物金額:"))
if(money >= 10000):
    if(money >= 100000):
        print(money*0.8, end= "元\n")   #滿十萬打八折
    elif(money >= 50000):
            print(money*0.85, end = "元\n") #滿五萬打八五折
    elif(money >= 30000):
            print(money*0.9, end = "元\n")  #滿三萬打九折
    else:
            print(money*0.95, end = "元\n")  #一萬以上打九五折
else:
            print(money, end = "元\n")  #連一萬都不到,不打折


#將range 函式產生的數列轉換為串列list
Rita1 = range(1,5)
print(list(Rita1))


#range 函式三個參數, 以range函數建立數列
list1 = range(3,8,1) #數列為3,4,5,6,7
list2 = range(3,8,2) #數列為3,5,7
list3 = range(8,3,-1) #數列為8,7,6,5,4 數列每次遞減-1
print(list(list1))
print(list(list2))
print(list(list3))


#continue asking
for i in range(1,11):
    if(i == 8):
        continue
    print(i,end = "")


#從1等差級數加到10
total = n = 0
while n <= 10:
    total += n
    n += 1
print(total)


我最近的心情 = "_"
for i in range(1,14):
    print("被情勒",i,"選擇原諒","又被情勒",i,"還是選擇原諒:",end="")
    for j in range(1,i+1): #內部迴圈
        print("#",end="orz")
    print(我最近)



#如果100分是氣到斷線 95%
#數字打家可以自己填
我的心情 = int(input("我每天的-能量："))
我的理智線斷裂速度 = -(87**0.87)
我的心情 *= 我的理智線
print("兩週後的心情:" + str(我的心情))


'a' + 'x' if '123'.isdigit() else 'y' +'b'


#串列元素 list會從0開始算
list1 = [1,2,3,4,5]
print(list1[0])
print(list1[1:3]) #注意出現數字是3-1
#還可以把索引中的元素內容作更改
list1[0] = 9
print(list1[0])


list2 = ["白癡","腦殘","智障"]
for s in list2:
    print("台北有一堆",s,end=",")


台北 = [87,78,414]
for i in range(len(台北)):
    print(台北[i])


#串列搜尋 list index用法
台北 = ["下雨","無情","冷漠"]
QQ = 台北.index("下雨")
TT = 台北.index("無情")
ZZ = 台北.index("冷漠")
SUN = 台北.index("大太陽") #大太陽不在台北list裡 index找不到


#append() 將元素加在list的最後
list3 = [1,2,3,4,5,6]
list3.append("87")
print(list3[6])
print(len(list3))



#inssert()
台北 = ["1","2","3"]
台北.insert(3,"4")
print(台北)
print(台北[3])
print(len(台北))


#sorted() 排序 不會讓原本的list不見
list4 = [1,2,3,4,5,6,7]
list5 = sorted(list4,reverse = True)
print(list4)
print(list5)



# 引入 pandas 套件，使用別名 pd 可以少打字
import pandas as pd

# 建立 Series 物件，傳入 list 當作參數
series_1 = pd.Series([22, 34, 41, 3])

print(series_1[0])
print(series_1[1:3])



# 引入 pandas 套件，使用別名 pd 可以少打字
import pandas as pd

# 準備傳入 
data = {
    'name': ['王小郭', '張小華', '廖丁丁', '丁小光'],
    'email': ['min@gmail.com', 'hchang@gmail.com', 'laioding@gmail.com', 'hsulight@gmail.com'],
    'grades': [60, 77, 92, 43]
}

# 建立 DataFrame 物件
student_df = pd.DataFrame(data)

print(student_df)



# 列出 DataFrame 的 index/columns
print(student_df.index)
print(student_df.columns)




