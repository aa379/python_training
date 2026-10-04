import sys
data=sys.stdin.read().splitlines()
n=int(data[0])
idx=1
while idx<len(data) and data[idx]=="":
    idx+=1
for i in range(n):
    tree={}
    total_trees=0
    while idx<len(data) and data[idx]!="":
        a=data[idx]
        tree[a]=tree.get(a,0)+1
        total_trees+=1
        idx+=1
    for name in sorted(tree.keys()):
        percentage=(tree[name]/total_trees)*100
        print(f"{name} {percentage:.4f}")
    print()
    while idx<len(data) and data[idx]=="":
        idx+=1