# FizzBuzzプログラム

# ユーザーから最大数を入力
ookoshi = int(input("数える最大数を入力してください: "))

# 1からmax_numまで数えてFizzBuzzを実行
for kousei in range(1, ookoshi + 1):
    if kousei % 15 == 0:
        print("Fizz Buzz")
    elif kousei % 3 == 0:
        print("Fizz")
    elif kousei % 5 == 0:
        print("Buzz")
    else:
        print(kousei)
