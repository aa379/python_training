s1,s2,s3=map(int,input("請輸入三個整數:").split())
if s1>s2:
    s1,s2=s2,s1
if s2>s3:
    s2,s3=s3,s2
if s1>s2:
    s1,s2=s2,s1
print(f"({s1},{s2},{s3})")