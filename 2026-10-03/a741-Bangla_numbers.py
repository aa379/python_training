import sys
def convert_bangla(num):
    if num==0:
        return ""
    part=[]
    if num>=10000000:
        part.append(convert_bangla(num//10000000)+" kuti")
        num%=10000000
    if num>=100000:
        part.append(f"{num//100000} lakh")
        num%=100000
    if num>=1000:
        part.append(f"{num//1000} hajar")
        num%=1000
    if num>=100:
        part.append(f"{num//100} shata")
        num%=100
    if num>0:
        part.append(str(num))
    return " ".join(part)
case_num=1
for line in sys.stdin:
    if not line.strip():
        continue
    num=int(line)
    if num==0:
        result="0"
    else:
        result=convert_bangla(num)
    print(f"{case_num:>4}. {result}")
    case_num+=1