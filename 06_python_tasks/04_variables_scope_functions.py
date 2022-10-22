# Localised basis
x = 10

def foo():
    x = 20 # ini
    print('foo():', x) # printing value from inside the function foo()
foo()
print('global:', x) # printing value from the global scope
print()

y = 10
def foo_y():
    global y
    y = 20
    print('foo_y:', y)

foo_y()
print('global:', y)

print()
def double(w):
    w = w * 2
    print('double:', w)

w = 10 # global value
double(w)
print('global:', w)