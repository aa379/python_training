a,b,c=sorted(map(int,input("請輸入三個整數:").split()))
if a<=0 or a+b<=c:
    print("不能成為三角形")
elif a**2+b**2!=c**2:
    print("為直角三角形")
else:
    print("可成為三角形，但不是直角三角形")