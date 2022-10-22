# Reverse a number
# Write a function to reverse a number recursively.

# Procedure to find reverse of a number,
# 1) Take a number
# 2) Declare a temporary variable and initialize it with 0
# 3) Find the last digit of the number
# 4) Multiply the temporary variable by 10
# 5) Add that last digit to the temporary variable
# 6) Remove the last digit of the number.
# 7) Repeat this process from 3 to 6 until the number becomes 0.

# Python program to reverse a number using recursion

reverse, base = 0, 1
def findReverse(num):
    global reverse  #function definition
    global base   #function definition
    if(num > 0):
        findReverse((int)(num/10))
        reverse += (num % 10) * base
        base *= 10
    return reverse

# take inputs
num = int(input('Enter a number: '))

# calling function and display result
print('The reverse number is =', findReverse(num))

############################
def reverse_digits(n):
    rev_num = 0

    while(n > 0):
        remainder = n % 10
        rev_num = (rev_num * 10) + remainder
        n = n // 10
    # Display the result
    return rev_num

print(reverse_digits(157))
