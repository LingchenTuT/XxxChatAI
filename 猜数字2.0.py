# 行百里者半九十
# 学习日期：2023/6/29 18:53
import random
num = random.randint(1, 100)
print("欢迎来到猜数字游戏，每次游戏会随机生成一个1~100之间的数字，看看你几次能猜对吧")
guess_num = int(input("请输入你的第一次猜测结果：\n"))
i = 2
while guess_num != num:
    if guess_num < num:
        print("诶呀你猜小了哦", end='，')
    elif guess_num > num:
        print("诶呀你猜大了哦", end='，')
    guess_num = int(input(f"请输入你的第{i}次猜测结果：\n"))
    i += 1
print(f"恭喜你猜对啦，共猜测{i-1}次")


