##### DICTIONARIES #####

# Dictionaries associate a value to a key
# Keys are unique and must be hashable (all mutable types are hashable:
# int, float, string, bool, tuple

# Every key has a value associated with it
# Values can appear repeatedly for multiplr keys
# Keys and values in a dictionary have no notion of order

temps = dict()
print(temps)

temps['Beirut'] = 20
print(temps)

temps['Bekaa'] = 45
temps['Arz'] = 32
print(temps)

# changing the value
temps['Beirut'] = 15
print(temps)

print(temps.get('Beirut'))
print(temps.get('Saida'))

