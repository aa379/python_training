import math
num=int(input())
for i in range(num):
    S1=int(input(),2)
    S2=int(input(),2)
    if math.gcd(S1,S2)>1:
        print(f"Pair #{i+1}: All you need is love!")
    else:
        print(f"Pair #{i+1}: Love is not all you need!")