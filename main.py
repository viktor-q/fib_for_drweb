# Лучший результат показывает последняя функция (5), выполняющая подсчет.

import time
import decimal
import numpy as np


# 1. Посчитать можно, используя генератор с проверкой валидности
def simple_fib(x: int) -> list:
    even_sequence = []
    first, second, fib = 0, 1, 0
    while len(even_sequence) < x:
        if fib % 2 == 0:
            even_sequence.append(fib)
        fib = first + second
        first = second
        second = fib
    return(even_sequence)

print(simple_fib(4))


# 2. Немного ускорить код можно, убрав ненужную переменную
def optimized_simple_fib(x: int) -> list:
    even_sequence = []
    first, second = 0, 1
    while len(even_sequence) < x:
        if first % 2 == 0:
            even_sequence.append(first)
        first, second = second, first+second
    return(even_sequence)

print(optimized_simple_fib(4))


# 3. Если обратить внимание на то, что каждое третье число в ряду Фибоначчи четное,
# можно использовать формулу Бине
# для вычислений десятичного объекта с большим количеством знаков потребуется decimal
def fib_with_bine(x: int) -> list:
    decimal.getcontext().prec = 100
    even_sequence = []
    number_in_fib = 0
    root_for_5 = decimal.Decimal(5 ** 0.5)
    fi = (root_for_5 + 1) / 2
    while len(even_sequence) < x:
        one_fib = (fi ** number_in_fib - ((-fi) ** (-number_in_fib))) / root_for_5
        even_sequence.append(int(one_fib))
        number_in_fib += 3
    return even_sequence

print(fib_with_bine(4))


# 4. Также можно посчитать каждое третье число Фибоначчи путем перемножения матриц. Для удобства используем numpy
def fib_matrix(x: int) -> list:
    even_sequence = []
    initial = 0
    while len(even_sequence) < x:
        fib = np.linalg.matrix_power(np.array([[1, 1], [1, 0]], dtype='O'), initial)[1, 0]
        even_sequence.append(fib)
        initial += 3
    return even_sequence

print(fib_matrix(4))

# 5. Подсчет с генератором
def _fib_yield(x: int):
    first, second = 0, 1
    iters = 0
    while iters < x:
        if first % 2 == 0:
            yield first
            # FREEZE
            iters += 1
        first, second = second, first + second

def fib_with_gen(x: int) -> list:
    even_sequence = []
    for number in _fib_yield(x):
        even_sequence.append(number)
    return even_sequence

print(fib_with_gen(4))


# Проверяем скорость вычислений для каждого варианта
start = time.time()
simple_fib(10000)
end = time.time()
print("simple fib", end-start)

start = time.time()
optimized_simple_fib(10000)
end = time.time()
print("optimized simple fib", end-start)

start = time.time()
fib_with_bine(10000)
end = time.time()
print("fib with bine", end-start)

start = time.time()
fib_matrix(10000)
end = time.time()
print("fib with matrix", end-start)

start = time.time()
fib_with_gen(10000)
end = time.time()
print("fib with gen", end-start)

