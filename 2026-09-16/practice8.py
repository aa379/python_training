string=input("請輸入一個字串(不包含單引號或雙引號):")
for i in string:
    if 48<=ord(i)<=57:
        print("輸入的數包含不合法字元")
        break
else:
    print(string)