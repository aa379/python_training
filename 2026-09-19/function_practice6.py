def factor(x):
    a=[]
    d=2
    while d*d<=x:
        if x%d==0:
            count=0
            while x%d==0:
                x//=d
                count+=1
            a.append([d,count])
        d+=1
    if x>1:
        a.append([x,1])
    return a
num=int(input("請輸入一個正整數:"))
print(factor(num))