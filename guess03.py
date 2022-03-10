import random

start = input('請輸入隨機整數範圍的開始值： ')
end = input('請輸入隨機整數範圍的結束值： ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    num = input('請猜數字： ')
    num = int(num)
    count += 1        # count = count + 1
    if num == r:
        print('恭喜！你猜中了！總共猜了', count, '次。')
        break
    elif num > r and num <= end:
        print('比答案大')
    elif num < r and num >= start:
        print('比答案小')
    else:
        print('超出範圍囉，請輸入數字', start, '~', end)
    print('這是你猜的第', count, '次，再試試看吧！')
