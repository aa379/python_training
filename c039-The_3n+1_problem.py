import sys
data=sys.stdin.read().split()
for index in range(0,len(data),2):
    original_i=int(data[index])
    original_j=int(data[index+1])
    i,j=original_i,original_j
    max_count=0
    temp=0
    if i>j:
        i,j=j,i
    for n in range(i,j+1):
        count=1 
        while n!=1:
            count+=1
            if n%2==0:
                n/=2
            else:
                n=3*n+1
        if count>max_count:
            max_count=count
    print(original_i,original_j,max_count)