import sys
a=[]
for line in sys.stdin:
    if line.strip():
        a.append(line.strip())
if not a:
    sys.exit()
max_x,max_y=map(int,a[0].split())
directions=["N","E","S","W"]
def get_move(direction):
    if direction=="N":
        return (0,1)
    elif direction=="E":
        return(1,0)
    elif direction=="W":
        return (-1,0)
    elif direction=="S":
        return (0,-1)
    else:
        return(0,0)
scents=set()
idx=1
while idx<len(a):
    pos_info=a[idx].split()
    x=int(pos_info[0])
    y=int(pos_info[1])
    d=pos_info[2]
    commands=a[idx+1]
    lost=False
    for i in commands:
        if i=="R":
            d_idx=directions.index(d)
            d=directions[(d_idx+1)%4]
        elif i=="L":
            d_idx=directions.index(d)
            d=directions[(d_idx-1)%4]
        elif i=="F":
            dx,dy=get_move(d)
            next_x=x+dx
            next_y=y+dy
            if next_x<0 or next_x>max_x or next_y<0 or next_y>max_y:
                if (x,y) in scents:
                    continue
                else:
                    scents.add((x,y))
                    lost=True
                    break
            else:
                x,y=next_x,next_y
    if lost:
        print(f"{x} {y} {d} LOST")
    else:
        print(f"{x} {y} {d}")
    idx+=2