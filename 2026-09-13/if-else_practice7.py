month=int(input("請輸入月份:"))
if 3<=month<=5:
    print(f"{month} 月是春季")
elif 6<=month<=8:
    print(f"{month} 月是夏季")
elif 9<=month<=11:
    print(f"{month} 月是秋季")
else:
    print(f"{month} 月是冬季")