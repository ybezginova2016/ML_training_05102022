def sum_n(n):
    total = 0 # initial value
    for i in range(1, n+1):
        total += i
    return total

print(sum_n(200))

# Functions call other functions, and even can call themselves
# Recursive function is a function which call the different instance of itself
# Or recursive function can invoke itself with different arguments

# Fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))