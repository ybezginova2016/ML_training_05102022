####################################
# 7. Сотрудники с зарплатой больше 50000 рублей
# Есть две таблицы — список сотрудников Employees и их зарплат
# Salaries. В таблице Employees есть столбцы id и name, а в таблице
# Salaries — user_id и value.
# Нужно вывести имена (name) и зарплаты (value) сотрудников,
# которые зарабатывают больше 50000 рублей.

SELECT e.name  AS name, s.value AS salary
FROM Employees AS e

# Добавить код сюда
INNER JOIN Salaries AS s

ON e.id = s.user_id

WHERE s.value > 50000

###############################
# 8. Сотрудники с выплатами больше 10000 рублей
SELECT
    e.name AS name,
    SUM(p.value) AS total_payments
FROM Employees AS e
    JOIN Payments AS p
        ON e.id = p.user_id
GROUP BY e.id
HAVING SUM(p.value) > 10000
# Следует заменить GROUP BY e.id на GROUP BY e.name.

# 10. Дополнительный индекс на таблицу
# В таблице Employees, в которой записаны данные сотрудников,
# есть столбцы id и name. В этой таблице нужно настроить
# поиск по имени. Какой индекс стоит создать поверх таблицы,
# чтобы ускорить поиск?
CREATE INDEX IDX_Employees_name ON Employees (name);

