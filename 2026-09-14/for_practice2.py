year=int(input("請輸入年分(西元):"))
count=0
for i in range(1,year+1):
    if i%400==0 or (i%4==0 and i%100!=0):
        count+=1
print(count)