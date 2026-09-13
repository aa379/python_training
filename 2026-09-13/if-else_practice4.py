edge=sorted(map(int,input("請輸入三個整數:").split()))
if edge[0]+edge[1]>edge[2]:
    print(f"({edge[0]},{edge[1]},{edge[2]})可以形成三角形")
else:
    print(f"({edge[0]},{edge[1]},{edge[2]})無法形成三角形")