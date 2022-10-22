# 2.1 - Palindrome Strings
# Write the function palindrome that takes as input a string.
# palindrome returns True if the input string is equal to its reverse, False if it is not.
# Also write the function max_sub_palindrome that takes as
# input a string, s. It must return a substring of s that is
# a palindrome, that has maximal length amongst all the possible
# such strings. If there are multiple such substrings, return
# the one that occurs first in s.

# Examples:

# max_sub_palindrome("aaabaaac") return aaabaaa.
# for "abe" it returns "a"
# for "ccABBAd" it returns "ABBA"
# for "XYZZYX" it returns "XYZZYX"

# Function to pra subString str[low..high]
def palindrome(input_str):
    return input_str == input_str[::-1]

def max_sub_palindrome(input_str):
    pass
# This function prints the
# longest palindrome subString
# It also returns the length
# of the longest palindrome

def max_sub_palindrome(input_str):
    longest = ""
    for i in range(len(input_str)):
        for j in range(0, i):
            chunk = input_str[j:i + 1]
            if chunk == chunk[::-1]:
                if len(chunk) > len(longest):
                    longest = chunk
    if longest == '':
        return input_str[0]
    return longest


print(max_sub_palindrome('abe'))