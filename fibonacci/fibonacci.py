# The Fibonacci series in Python 3 from a tutorial I found online.
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(0, n):
        c = a
        a = b
        b = c + b
    return a
for _ in range(0, 15):
    print(fibonacci(_))
