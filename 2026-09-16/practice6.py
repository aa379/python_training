while True:
    password=input("請輸入密碼:")
    is_valid=True
    for i in password:
        if ord(i)<48 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or ord(i)>=123:
            print("密碼只能包含英文字母或數字")
            is_valid=False
            break
    if len(password)<6:
        print("密碼長度至少6個字元")
        is_valid=False
    if is_valid:
        print("密碼設定成功")
        break