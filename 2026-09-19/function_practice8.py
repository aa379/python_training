def to_numbers(word):
    a=[]
    for i in word:
        if i in "ABC":
            a.append(2)
        elif i in "DEF":
            a.append(3)
        elif i in "GHI":
            a.append(4)
        elif i in "JKL":
            a.append(5)
        elif i in "MNO":
            a.append(6)
        elif i in "PQRS":
            a.append(7)
        elif i in "TUV":
            a.append(8)
        else:
            a.append(9)
    return a
words=input("請輸入一個英文單字(大寫):")
print(*to_numbers(words),sep="")