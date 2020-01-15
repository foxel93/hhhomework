from random import randint
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100

def gen(N):
    res = []
    for i in range(N):
        res.append(randint(1, 100))
    return res


# написать генераторное выражение, которое делает то же самое
res = [randint(1, 100) for i in range(int(input('Введите количество чисел: ')))]