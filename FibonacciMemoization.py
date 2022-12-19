fibonacciCache = {}

def fibonacci(n: int):

    if n in fibonacciCache:
        return fibonacciCache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        
    fibonacciCache[n] = value
    return value

# #n = int(input("Enter an n "))

Memo = {}

def fib(n: int):
    if n in Memo:
        return Memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    Memo[n] = fib(n - 1) + fib(n - 2)
    return Memo[n]

print(fib(15))
print(fibonacci(15))

