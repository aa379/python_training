def add_n(lst,n=0):
    if n.isdigit():
        n=int(n)
        for i in range(len(lst)):
            lst[i]=lst[i]+n
    return lst
print(add_n([1,2,3,4,5,6,7,8,9],input("請數入一個整數:")))