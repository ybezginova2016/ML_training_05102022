# Given two integers l and r, print all the odd numbers between l and r (l and r inclusive).
def oddNumbers(l, r):
    # Write your code here
    odd = []
    for i in range(l, r + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd

print(oddNumbers(-10, -32))