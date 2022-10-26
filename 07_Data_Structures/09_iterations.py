# Напишите функцию gen_seq так, чтобы при выполнении
# этого цикла параметр i принял 10 значений: от 0 до 9.
def gen_seq():
    return range(10)

for i in gen_seq(): # исходный код

###########################
def gen_seq():
    return [num for num in range(10)]


for i in gen_seq():  # исходный код

###########################
def gen_seq():
    return (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


for i in gen_seq():  # исходный код
###########################
def gen_seq():
    num = 0
    while num < 10:
        yield num
        num += 1


for i in gen_seq():  # исходный код
