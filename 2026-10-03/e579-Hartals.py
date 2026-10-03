num=int(input())
for i in range(num):
    N=int(input())
    P=int(input())
    a=[]
    count=0
    for i in range(P):
        a.append(int(input()))
    for j in range(1,N+1):
        if j%7==0 or j%7==6:
            continue
        for k in a:
            if j%k==0:
                count+=1
                break
    print(count)