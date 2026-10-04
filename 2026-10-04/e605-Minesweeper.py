import sys
data=sys.stdin.read().split()
idx=0
case_number=1
while idx<len(data):
    n=int(data[idx])
    m=int(data[idx+1])
    idx+=2
    if n==0 and m==0:
        break
    field=[]
    for i in range(n):
        field.append(data[idx])
        idx+=1
    if case_number>1:
        print()
    print(f"Field #{case_number}:")
    directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(n):
        result=""
        for j in range(m):
            if field[i][j]=="*":
                result+="*"
            else:
                count=0
                for dx,dy in directions:
                    ni=i+dx
                    nj=j+dy
                    if 0<=ni<n and 0<=nj<m:
                        if field[ni][nj]=="*":
                            count+=1
                result+=str(count)
        print(result)
    case_number+=1