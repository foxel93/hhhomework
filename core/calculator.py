from core.decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '-': lambda x, y: x - y,
        '**': lambda x, y: x ** y
    }
    return operations[operation](a, b)


if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        operation = input('Введите операцию: ')
        res = calculator(a, b, operation)
    except ValueError:
        print('Ошибка при вводе чисел. Введите корректные данные')
    except KeyError:
        print('Ошибка при вводе оператора. Введите корректные данные')
    except ZeroDivisionError:
        print('Результат: NaN')
    else:
        print('Результат: ', res)
