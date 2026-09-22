def r_pow(base,n):
    if n>0:
        return base*r_pow(base,n-1)
    else:
        return 1
a,b=map(int,input("請輸入底數(可為整數)和指數(須為正整數):").split())
print(r_pow(a,b))