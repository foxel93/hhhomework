def cache_decorator(funk):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache = {}

    def wrapper(*args):
        line = ''
        for arg in [*args]:
            line += str(arg)
        if line in cache:
            result = cache[line]
        else:
            result = funk(*args)
            cache[line] = result
        return result

    return wrapper
