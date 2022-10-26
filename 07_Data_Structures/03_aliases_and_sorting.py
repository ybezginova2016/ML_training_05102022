m = ['yellow', 'red', 'blue']

n = m
print(n)
m.append('orange')
print(n)
print(m)

c = m[:]
print(c)
m.remove('red')
print(m)
print(n)
print(c)

##### SORTING #####
any_list = [5, 7, 4, 4, 3, 1, 0, 4, 8]
print(sorted(any_list)) # sorted list
print(any_list)
print(any_list.sort())

y = any_list.sort()
print(y is True)

y = sorted(any_list)
print(y)
