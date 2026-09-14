price=int(input("請輸入金額:"))
change=100-price
fifty,ten,five,one=0,0,0,0
if change>=50:
    fifty=change//50
    ten=(change%50)//10
    five=(change%10)//5
    one=(change%5)
    print(f"50元{fifty}枚，10元{ten}枚，5元{five}枚，1元{one}枚")
else:
    ten=(change%50)//10
    five=(change%10)//5
    one=(change%5)
    print(f"50元{fifty}枚，10元{ten}枚，5元{five}枚，1元{one}枚")