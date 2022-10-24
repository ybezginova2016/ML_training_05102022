# Lists are mutable

def sum_of_items(w):
    total = 0
    for n in w:
        total += n
    return total

print(sum_of_items([1, 2, 1, 5, 6, 13]))

# adding a new elements
list = [1, 3, 2]

list += [13]
list += [5, 1]
list += [8]
list.append(11)
list.extend([12, 13, 14, 15])
list.extend((111, 113))
print(list)

# removing elements
r = ['red', 'blue', 'orange', 'violet', 'yellow']
del(r[1])
r.remove('orange')
# print(r)

# .pop() operator is going to return the element
last = r.pop()
print(last)
print(r)
