i=1
num=[]
while True:
    if i%3==2 and i%5==3 and i%7==2:
        num.append(i)
    if len(num)==3:
        break
    i+=1
print(*num,sep=",")