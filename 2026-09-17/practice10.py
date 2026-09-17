lower_limit=0
upper_limit=255
num=input("請輸入一串數字，用逗號隔開:").split(sep=",")
for i in num:
    if int(i)<=lower_limit or int(i)>=upper_limit:
        print("最少有一個數不在[0,255]之內")
        break
else:
    print("輸入的數全部在範圍之內")