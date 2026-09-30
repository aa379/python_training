num=int(input())
for i in range(num):
    b=int(input())
    c=list(map(int,input().split()))
    count=0
    for k in range(b-1):
        for j in range(b-1-k):
            if c[j]>c[j+1]:
                c[j],c[j+1]=c[j+1],c[j]
                count+=1
    print(f"Optimal train swapping takes {count} swaps.")