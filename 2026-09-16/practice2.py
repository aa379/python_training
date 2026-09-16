sum=0
n=1
while True:
    sum+=n
    if sum>=100:
        break
    n+=1
print(f"最後加進去讓總和超過 100 的數是: {n}")
print(f"此時總和為: {sum}")