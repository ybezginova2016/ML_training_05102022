# Mindbox0+ — платформа автоматизации маркетинга

# C 2006 года разрабатываем и внедряем облачную платформу автоматизации
# маркетинга. Помогаем собирать и обрабатывать данные о клиентах из
# онлайна и офлайна, автоматизировать и персонализировать коммуникации,
# управлять ими из одного окна и увеличивать выручку маркетинга.
# По независимым оценкам, входим в десятку крупнейших
# B2B SaaS-сервисов России.

'''

Вопросы взяты из каждодневной практики, по ним вы можете оценить рабочие задачи.
Ожидается что вы вложите разумные усилия в их выполнение

Нашей компании нужно сгруппировать клиентов для АБ-тестов. Алгоритм группировки очень простой - взять ID клиента
(состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. Получившееся число и является номером группы,
в которую входит данный клиент.

Для того, чтобы понять, насколько хорош такой простой алгоритм,
тебе нужно написать следующие диагностические функции:

1) Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация
ID сквозная и начинается с 0. На вход функция получает целое число n_customers (количество клиентов).

2) Функция, аналогичная первой, если ID начинается с произвольного числа. На вход функция получает целые числа:
n_customers (количество клиентов) и n_first_id (первый ID в последовательности).

'''

############ ФУНКЦИЯ 1 ############

# Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация
# ID сквозная и начинается с 0. На вход функция получает целое число n_customers (количество клиентов).

# вариант 1
def count_cust_dict(n_customers: int):
    grouped_customers = {}
    for customer_id in range(n_customers):
        group = sum(map(lambda x: int(x), list(str(customer_id))))
        if group in grouped_customers:
            grouped_customers[group] += 1
        else:
            grouped_customers[group] = 1

    return grouped_customers

print(count_cust_dict(3432))


# вариант 2
def count_cust_array(n_customers: int):
    grouped_list= []
    for customer_id in range(n_customers):
        group = sum(map(lambda x: int(x), list(str(customer_id))))
        grouped_list.append(group)
    return grouped_list

a = count_cust_array(21355)
print(a)

# import matplotlib.pyplot as plt
# plt.figure(figsize=(9, 5))
# plt.xlabel('Номер группы для А/В-тестирования')
# plt.ylabel('Число клиентов в группе для А/В-тестирования')
# plt.hist(a)
# plt.show()


############ ФУНКЦИЯ 2 ############
# Функция, аналогичная первой, если ID начинается с произвольного числа.
# На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id (первый ID в последовательности).

# def function_2(n_customers: int, n_first_id: int):
#     grouped_list= []
#     for customer_id in range(n_customers):
#         group = sum(map(lambda x: int(x), list(str(customer_id))))
#         grouped_list.append(group)
#     return grouped_list

def function_2(n_customers: int, n_first_id: int):
    grouped_list= []
    customer_id = n_first_id
    for customer in range(n_customers):
        group = sum(map(lambda x: int(x), list(str(customer_id))))
        grouped_list.append(group)
        customer_id += 1
    return grouped_list

# вызовем функцию
b = function_2(188885, 55)

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
plt.xlabel('Номер группы для А/В-тестирования')
plt.ylabel('Число клиентов в группе для А/В-тестирования')
plt.hist(b)
plt.show()
