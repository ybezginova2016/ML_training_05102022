# Функция add_element методом append добавляет элемент 0 к
# переданному в качестве аргумента объекту:
def add_element(collection):
    collection.append(0)

some_list = [1,2,3]
add_element(some_list)
print(some_list)

some_tuple = (1,2,3)
add_element(some_tuple)
print(some_tuple)