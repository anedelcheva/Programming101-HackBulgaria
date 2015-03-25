def fibonacci(n):
    fiblist = []
    a = 1
    b = 1
    for i in range(n):
        fiblist.append(a)
        a, b = b, a + b
    return fiblist


def fib_number(n):
    return ("".join(map(str, fibonacci(n))))
