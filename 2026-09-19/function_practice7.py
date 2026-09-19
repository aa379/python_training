def bin2dec(bs):
    a=0
    power=0
    if not bs:
        return "錯誤：不能輸入空字串！"
    for ch in bs:
        if ch not in "01":
            return f"錯誤：輸入包含非法字元，二進位只能包含 0 和 1！"
    for i in reversed(bs):
        a=a+int(i)*(2**power)
        power+=1
    return a
num=input("請輸入一個二進位的數字:")
print(bin2dec(num))