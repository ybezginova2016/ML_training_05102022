# https://www.udemy.com/course/sefactory-foundations-of-computer-science/learn/quiz/4664354#reviews

temp = 0
while temp <= 4:
    print(temp, end=",")
    temp += 1

print("The temperature is", end=",")
print(temp)

# infinite loop
# n = 0
# temper = 25
# while n < 5:
#     temper //= 2
#     n -= 1
# print("The temperature is: " + str(temper))

for row in range(1, 7):
    for col in range(row):
        # print with end='' avoids adding
        # an extra endline after finishing output
        print('*', end='')
    print('') # add new line here

# Implement a  function that takes a positive number n as parameters,
# and returns the sum of odd integers less than or equal to n.

def odd_sum(n):
    if n < 0:
        return 0
    elif n >= 0:
        result = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                result += i
        return result

# def odd_sum(n):
#     result = 0
#     if n > 0:
#         for i in range(1, n+1):
#             result += i
#         return result
#     elif n <= 0:
#         raise ValueError("n should be positive")

print(odd_sum(0))
print(odd_sum(-10))
print(odd_sum(31))
print(odd_sum(10))

###### TASK 2 #######
# Square a number by successive additions.
# You are given as input the integer n, which you can assume
# is not negative. That is, n >= 0.
# Use successive additions to return the sum in the following
# format (n+n+n..+n) n-times
# Sample output for user_input = 5:
# 5 + 5 + 5 + 5 + 5 = 25
# This function will return a string, instead of outputting
# to the terminal.
# user = input("Enter an integer:")
# print(user)

def sum_user_input(user_input):
    '''Your solution should be written below.
    Assume user_input contains the input provided by the user
    '''
    # REMOVE ME: Code here
    # return '5 + 5 + 5 + 5 + 5 = 25'
    if user_input == 0:
        return str('0 = 0')
    string = ''
    res = user_input * user_input
    for i in range(user_input):
        string += str(user_input)
        if i < user_input-1:
            string += ' + '
    string += ' = ' + str(res)
    return string

print(sum_user_input(0))

###### TASK 3 ######
# 2.5 - Cubic Root
# Print the greatest integer whose cube is smaller or equal to the
# input number without using the power operator.
# You must use the print function, and match the expected
# output as specified by the following examples.

# Examples:
# Print the following for input n = 99,:
# 4, not exact with difference 35 for n = 2000,
# 12, not exact with difference 272 and for n = 1000

def cubic_root(n):
    if n<0:
        n=abs(n)
        cube_root = round(n**(1/3)*(-1))
    else:
        cube_root = round(n**(1/3))
        diff = round(n-(cube_root * cube_root * cube_root))
        print(cube_root, 'not exact with', diff)
    return cube_root

print(int(cubic_root(99)))
print(int(cubic_root(2000)))
print(int(cubic_root(1000)))

def cubic_root1(n):
    n = abs(n)
    result = 1
    x = 2
    if n == 0:
        print('0, exact!')
    elif n == 1:
        print('1, exact!')
    else:
        while result < n:
            result = x * x * x
            if result >= n:
                break
            x = x + 1
        if result != n:
            x = x - 1
        diff = (x * x * x) - n
        if diff == 0:
            print('{0}, exact!'.format(str(x)))
        else:
            diff = abs(diff)
            print('{0}, not exact with difference {1}'.format(str(x), str(diff)))

print(cubic_root1(99))
print(cubic_root1(2000))
print(cubic_root1(1000))