####### Boiling Point #######
# Write a function, that given a mapping from material to boiling points, and a boiling point temperature, will return

# The material corresponding to the boiling, if it is within 5% difference.
# Unknown otherwise

# Function signature should look like: boiling_material(boiling_map, boiling_point)

def boiling_material(boiling_map, boiling_point):
    for key, value in boiling_map.items():
        res = abs(value - boiling_point)
        threshold = abs(value * 0.05)
        if threshold >= res:
            return key
    return 'Unknown'

boiling_map = {'Butane': -0.5,
 'Copper': 1187,
 'Gold': 2660,
 'Mercury': 357,
 'Methane': -161.7,
 'Nonane': 150.8,
 'Silver': 2197,
 'Water': 100}

print(boiling_material(boiling_map,359))
print(boiling_material(boiling_map,2000))
print(boiling_material(boiling_map,-161))
print(boiling_material(boiling_map,95))