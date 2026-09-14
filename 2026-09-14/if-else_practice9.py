hour=int(input("請輸入停車的時數:"))
if hour>12:
    fee=(hour-12)*30+12*40
    print(fee)
else:
    fee=hour*40
    print(fee)