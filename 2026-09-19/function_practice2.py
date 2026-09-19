def pow(x,n):
    ans=1
    for i in range(n):
         ans*=x
    return ans
x,n=map(int,input("請輸入兩個正整數:").split())
print(pow(x,n))