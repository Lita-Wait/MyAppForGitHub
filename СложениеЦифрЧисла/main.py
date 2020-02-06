def sum_digits(num):
    lst = []
    num = str(num)
    for x in range (len(num)):
        lst.append(num[x])
    return sum(list(map(int,lst)))
print(sum_digits(5245))