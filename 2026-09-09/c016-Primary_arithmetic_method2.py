import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a,b=line.split()
    if a=="0" and b=="0":
        break
    list_a=[]
    for x in a:
        list_a.append(int(x))
    list_b=[]
    for x in b:
        list_b.append(int(x))
    carry_count=0
    current_carry=0
    while len(list_a)>0 or len(list_b)>0:
        if len(list_a)>0:
            digit_a=list_a.pop()
        else:
            digit_a=0
        if len(list_b)>0:
            digit_b=list_b.pop()
        else:
            digit_b=0
        total=digit_a+digit_b+current_carry
        if total>=10:
            current_carry=1
            carry_count+=1
        else:
            current_carry=0
    if carry_count==0:
        print("No carry operation.")
    elif carry_count==1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")