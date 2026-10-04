import sys
for line in sys.stdin:
    if not line.strip():
        continue
    nums=list(map(float,line.split()))
    points=[(nums[i],nums[i+1]) for i in range(0,8,2)]
    unique_points=[]
    common_points=None
    for p in points:
        if points.count(p)==2:
            common_points=p
        else:
            unique_points.append(p)
    dx=unique_points[0][0]+unique_points[1][0]-common_points[0]
    dy=unique_points[0][1]+unique_points[1][1]-common_points[1]
    print(f"{dx:.3f} {dy:.3f}")