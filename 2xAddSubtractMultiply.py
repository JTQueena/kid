import random

print("******************************")
print("\n**    資優生數學練習程式    **")
print("\n**  僅提供成綪優異學生使用  **")
print("\n******************************")

count=0

def keyinxy(x):
    """ 避免程式錯誤 """
    try:
        x = int(x)
        return x
    except:
        print("請重新輸入")
        return 0

while True: # 連續出題
    n1=random.randint(10,20) #請出題人員設定範圍
    n2=random.randint(1,9) #請出題人員設定範圍
    print("總共答對了",count,"題")
    print("")
    print(n1,"x",n2,"=") #請出題人員設定運算方式
    x = input("請輸入答案：")
    x = keyinxy(x)
    ans=n1*n2 #請出題人員設定運算方式
    print("")

    while x != ans:
        print("答錯了，請再試一次")
        print(n1,"x",n2,"=") #請出題人員設定運算方式
        x = input("請輸入答案：")
        x = keyinxy(x)        
    else:
        print("答對了，下一題")
        count+=1
