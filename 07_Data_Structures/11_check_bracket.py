# 5. Как проверить расстановку скобок?
# Вам нужно создать функцию check_bracket. Функция должна принимать
# строку, состоящую только из скобок, и проверять, правильно ли
# расставлены эти скобки. Если скобки расставлены верно,
# то функция выдаст True, а если неверно — False.
# Правильной считается та расстановка, при которой каждой
# открывающей скобке соответствует закрывающая с учётом вложенности.

def check_bracket(str):
    open_cnt = 0
    close_cnt = 0

    for c in str:
        if c == '(':
            open_cnt += 1
        else:
            close_cnt += 1

    return open_cnt == close_cnt

print(check_bracket('()'))
print(check_bracket('()))))'))
######### OPTIONS 2 ############
def check_bracket1(str):
    stack = []
    for c in str:
        if c == "(":
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0
print(check_bracket1('()'))
print(check_bracket1('())))'))

######### OPTION 3 ##########
def check_bracket3(str):
    if not str:
        return True

    first = str[0]
    last = str[-1]
    if first != '(' or last != ')':
        return False

    return check_bracket(str[1: -1])
print(check_bracket3('()'))
print(check_bracket3('())))'))

########### OPTION 4 ############
def check_bracket4(str):
    if not str:
        return True

    first = str[0]
    last = str[-1]
    if first != '(' or last != ')':
        return False

    return check_bracket(str[1: -1])
print(check_bracket4('()'))
print(check_bracket4('())))'))

########### OPTION 5 ############
from functools import reduce
def check_bracket5(str):
    reduce_str = reduce(lambda accum, cur: accum[:-1] if accum and accum[-1] + cur == '()' else accum + cur, str)
    return not reduce_str

print(check_bracket5('()'))
print(check_bracket5('())))'))