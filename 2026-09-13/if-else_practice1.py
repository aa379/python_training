temp=int(input("請輸入現在氣溫:"))
if temp>28:
    print(f"現在溫度為{temp}度，可以開冷氣")
elif temp>15:
    print(f"現在溫度為{temp}度，不開冷暖氣")
else:
    print(f"現在溫度為{temp}度，可以開暖氣")