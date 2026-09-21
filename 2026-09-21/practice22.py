counter=0
def increment():
    global counter
    counter+=1
def get_counter():
    return counter
increment()
increment()
increment()
print(get_counter())