num=input("請輸入一個帶有千分位符號的整數:")
clean_s=""
i=0
while i<len(num):
    if num[i]!=",":
        clean_s+=num[i]
    i+=1
ans=int(clean_s)
print(ans*2)