import random

print("******************************")
print("\n**    資優生數學練習程式    **")
print("\n**  僅提供成綪優異學生使用  **")
print("\n******************************")
#v2.0
count=0
while True: # 連續出題
    n1=random.randint(1000,9999) #請出題人員設定範圍
    n2=random.randint(100,999) #請出題人員設定範圍
    print("總共答對了",count,"題")
    print("")
    print(n1,"x",n2,"=") #請出題人員設定運算方式
    keyin=int(input("請輸入答案："))
    ans=n1*n2 #請出題人員設定運算方式
    print("")

    while keyin != ans:
        print("答錯了，請再試一次")
        print(n1,"x",n2,"=") #請出題人員設定運算方式
        keyin=int(input("請輸入答案："))
    else:
        print("答對了，下一題")
        count+=1
