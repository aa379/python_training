data=[[2,4,5],[5,8,None],[10,3,4]]
j=0
for i in data:
    if None in i:
        print(f"第{j+1}組:Incomplete data")
    else:
        print(f"第{j+1}組:總合為:{sum(i)}")
    j+=1