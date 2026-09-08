import sys
for line in sys.stdin:
    a=line.strip()
    if not a:
        continue
    if a=="0":
        break
    original_num=a
    total=sum(map(int,a))
    count=1
    while total>=10:
        total=sum(map(int,str(total)))
        count+=1
    if total==9:
        print(f"{original_num} is a multiple of 9 and has 9-degree {count}.")
    else:
        print(f"{original_num} is not a multiple of 9.")