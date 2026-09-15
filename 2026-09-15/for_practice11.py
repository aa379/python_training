num=0
for i in range(5):
    for j in range(i+1):
        if num<10:
            char=str(num)
        else:
            char=chr(ord("a")+(num-10))
        print(char,end="")
        num+=1
    print()