##### TUPLES #####

# Ordered sequence of elements, possibly of different types
# Immutable, meaning elements cannot change

t = (10, 20, 'se')
s = ('factory', 15)

print(t[0])
print(t+s)
print(t[1:])
print(len(t))
###############
print((1, 2) == (2, 1))
print((1, 2, 3) == (1, 2, 3))
print(('a') == ('a', 'b'))
print((1, 1) < (1, 1))
print((1, ) < (1, 1))

################
def min_max_avg(scores):
    lo = scores[0]
    hi = scores[0]
    total = 0

    for g in scores:
        if g < lo:
            lo = g
        if g > hi:
            hi = g
        total += g
    return (lo, hi, total / len(scores))

# let's execute the function
student_scores = (10, 12, 14, 16, 18)
t = min_max_avg(student_scores)
lowest, highest, average = t
print(lowest, highest, average)

########################
def squares(n):
    ts = ()
    for i in range(n):
        singleton = (i * i, )
        ts = ts + singleton
    return ts
print(squares(6))


