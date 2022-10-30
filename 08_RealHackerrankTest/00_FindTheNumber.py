"""
1. Find the number!

Given an unsorted array of n elements, find the element k is present in the
array or not.

Complete the findNumber function in the editor below. It has 2 parameters:
1) Anarray of integers, arr, denoting the elements in the array.
2) An integer, k, denoting the element to be searched in the array.

The function must return a string "YES" or "NO" denoting if the element
is present in the array or not.

"""
def findNumber(arr, k):
    if k in arr:
        return 'YES'
    else:
        return 'NO'

print(findNumber([3, 4, 5, 6, 11, 24, 22, 23, 2,], 6))
print(findNumber([3, 4, 5, 6, 11, 24, 22, 23, 2,], 7))