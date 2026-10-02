num=int(input())
for i in range(num):
    data = list(map(int, input().split()))
    a=data.pop(0)
    data.sort()
    mid = data[len(data)//2]
    ans=sum(abs(mid - j) for j in data)
    print(ans)