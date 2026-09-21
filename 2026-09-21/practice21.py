def find_max(*args):
    if args:
        return max(args)
    else:
        return None
print(find_max(6,5,3))
print(find_max())