import sys
for line in sys.stdin:
    if not line.strip():
        continue
    a,b=map(int,line.split())
    if a==0 and b==0:
        break
    carry_count=0
    current_count=0
    while a>0 or b>0:
        digit_sum=(a%10+b%10)+current_count
        if digit_sum>=10:
            carry_count+=1
            current_count=1
        else:
            current_count=0
        a//=10
        b//=10
    if carry_count==0:
        print("No carry operation.")
    elif carry_count==1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")