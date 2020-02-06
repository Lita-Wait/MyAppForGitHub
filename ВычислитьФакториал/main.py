input = int(input())
if input > 0:
    f = 1
    for i in range(2,input+1):
        f *= i
    print(f)
else: print("Нельзя вычислить отрицательный факториал")

