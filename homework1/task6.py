# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a(0) = 0, a(1) = 1, a(k0 = a(k-1) + a(k-2) (k > 1).

# Требуется найти N-е число Фибоначчи.

def fibonacci(k):
    if k == 0:
        return 0
    elif k in (1, 2):
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)


k = int(input('enter k: '))
print(fibonacci(k))
