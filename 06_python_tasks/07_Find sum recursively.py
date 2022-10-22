# Write a recursive function that takes a positive number n as
# a parameter and calculates the sum of numbers from 1 to n.

def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

print(recursive_sum(-5))

# Write a function that counts the digits of a given
# number recursively.
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(50))
