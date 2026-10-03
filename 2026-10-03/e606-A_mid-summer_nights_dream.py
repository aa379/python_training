import sys
data=list(map(int,sys.stdin.read().split()))
i=0
while i<len(data):
    n=data[i]
    i+=1
    nums=data[i:i+n]
    i+=n
    nums.sort()
    mid1=nums[(n-1)//2]
    mid2=nums[n//2]
    A=mid1
    count=sum(1 for x in nums if mid1<=x<=mid2)
    possible_A = mid2 - mid1 + 1
    print(f"{A} {count} {possible_A}")