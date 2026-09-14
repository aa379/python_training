a,b=sorted(map(int,input("請輸入兩個正整數:").split()))
divisor=1
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        divisor=i
print(divisor)