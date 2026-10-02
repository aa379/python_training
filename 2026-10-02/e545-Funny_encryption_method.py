num=int(input())
for i in range(num):
    data=input()
    b1=bin(int(data)).count("1")
    b2=bin(int(data,16)).count("1")
    print(f"{b1} {b2}")