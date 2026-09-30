import sys
is_quote=True
for line in sys.stdin:
    if not line.strip():
        continue
    for i in line:
        if i!="\"":
            print(i,end="")
        elif i=="\"" and is_quote:
            print("``",end="")
            is_quote=False
        else:
            print("\'\'",end="")
            is_quote=True