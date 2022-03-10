import random

r = random.randint(1, 100)
count = 0
while True:
    num = input('請猜數字(1~100)： ')
    num = int(num)
    count += 1        # count = count + 1
    if num == r:
        print('恭喜！你猜中了！總共猜了', count, '次。')
        break
    elif num > r and num <= 100:
        print('比答案大')
    elif num < r and num >= 1:
        print('比答案小')
    else:
        print('超出範圍囉，請輸入數字 1~100')
    print('這是你猜的第', count, '次，再試試看吧！')
