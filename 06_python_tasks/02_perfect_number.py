# 2.4 - Perfect Number
# https://www.udemy.com/course/sefactory-foundations-of-computer-science/learn/quiz/4664354#reviews

# Write a function to test if a positive integer  is a perfect number.
# Note that a number is said to be perfect if it is equal
# to the sum of its proper divisors.

# Examples: 6 = 1 + 2 + 3 is a perfect number
# 28 = 1 + 2 + 4 + 7 + 14 is a perfect number
# 8 != 1 + 2 + 4  is not a perfect number

def perfect(number):
    # The variable "value" represent the value of the
    # integer number entered by the user
    # Declare a bool variable isperfect and initialize it to false
    is_perfect = False
    # Declare a variable sum and initialize it to zero
    sum = 0
    # 1- Check if "number" is non-positive.
    if number <= 0:
        return 'Sorry, you entered a negative number!'
    # 2- If not, find the proper divisors of "number" and find their sum
    if number > 0:
        for x in range(1, number): # divisor is always less number
            if number % x == 0:
                sum += x
    # 3- Check if their sum is equal to "number"
                if sum == number: # WRITE THE REQUIRED CONDITION HERE
                    is_perfect = True
    return is_perfect

print(perfect(1))