year=int(input("請輸入一個整數:"))
if year%400==0 or (year%4==0 and year%100!=0):
    print(f"{year}是閏年")
else:
    print(f"{year}是平年")