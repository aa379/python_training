fib=[1,2]
while True:
    nxt=fib[-1]+fib[-2]
    fib.append(nxt)
    if nxt>100000000:
        break
fib=fib[::-1]
num=int(input())
for i in range(num):
    data=int(input())
    print(f"{data} = ",end="")
    found=0
    for j in fib:
        if data>=j:
            data-=j
            found=1
            print(1,end="")
        elif found:
            print(0,end="")
    print(" (fib)")