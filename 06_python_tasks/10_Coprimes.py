# 2.4 - Coprimes
# Co-prime numbers have no common integer divisors other
# than the integer 1.
# The integers 12 and 25 are co-prime, for example.

# The integers 12 and 100 are not co-prime, with 2 being
# an example of an integer that divides both.
# Write a function that accepts two integer inputs, and returns
# a boolean value of whether they are co-prime.

# Function signature: coprime(a, b) which returns a
# boolean value (either True or False).

# Note that 1 is coprime with all other positive integers.


# Create the gcd of two positive integers.

def coprime(a, b):
    # Returns a boolean value
    # Returns true if a and b are in fact coprime
    def gcd(p, q):
        while q != 0:
            p, q = q, p%q
        return p
    return gcd(a, b) == 1

print(coprime(3, 18))

# version 2

def coprime2(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf == 1

print(coprime2(5, 15))

# Count of integers up to N which are non divisors and non coprime
# with N
# Given an integer N, the task is to find the count of all possible integers less than N satisfying the following properties:
#
# The number is not coprime with N i.e their GCD is greater than 1.
# The number is not a divisor of N.

#### EXPLANATION ####
# Input: N = 10
# Output: 3

# All possible integers which are less than 10 and
# are neither divisors nor coprime with 10, are {4, 6, 8}.
# Therefore, the required count is 3.
# Input: N = 42
# Output: 23

def count(n):
    # Stores Euler counts
    phi = [0] * (n + 1)

    # Store Divisor counts
    divs = [0] * (n + 1)

    # Based on Sieve of Eratosthenes
    for i in range(1, n + 1):
        phi[i] += i

        # Update phi values of all
        # multiples of i
        for j in range(i * 2, n + 1, i):
            phi[j] -= phi[i];

        # Update count of divisors
        for j in range(i, n + 1, i):
            divs[j] += 1

    # Return the final count
    return (n - phi[n] - divs[n] + 1)

print(count(1455))