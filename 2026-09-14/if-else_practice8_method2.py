total_sec=int(input("請輸入秒數:"))
hours=total_sec//3600
minutes=(total_sec%3600)//60
sec=total_sec%60
print(f"{total_sec:02}秒等於{hours:02}小時{minutes:02}分鐘{sec:02}秒")