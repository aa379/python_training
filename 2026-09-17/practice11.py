a=[i**2 for i in range(1,11)]
b=[i for i in range(1,50) if i%3==0 and i%4==0]
c=[i for i in "List comprehension" if i.lower() in "aeiou"]
d=[1 if i>0 else -1 for i in [3,-1,4,7,-3,2]]
print(a)
print(b)
print(c)
print(d)