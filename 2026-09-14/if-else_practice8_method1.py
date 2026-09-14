sec=int(input("請輸入秒數:"))
original_sec=sec
minutes=0
hours=0
if sec>=60:
    minutes=sec//60
    sec=sec%60
if minutes>=60:
    hours=minutes//60
    minutes=minutes%60
print(f"{original_sec} 秒等於{hours:02}小時{minutes:02}分鐘{sec:02}秒")