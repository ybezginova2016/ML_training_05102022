# 3.4 - Boiling Point
# Write a function, that given a mapping from material to boiling points,
# and a boiling point temperature, will return
# The material corresponding to the boiling, if it is within
# 5% difference.
# Unknown otherwise
# Function signature should look like:
# boiling_material(boiling_map, boiling_point)

boiling_map=dict()
boiling_map['Butane']=-0.5
boiling_map['Copper']=1187
boiling_map['Gold']=2660
boiling_map['Mercury']=357
boiling_map['Methane']=-161.7
boiling_map['Nonane']=150.8
boiling_map['water']=100

def boiling_material(boiling_map,boiling_point):
    closest='unknown'
    for material in boiling_map:
        if abs(boiling_map[material]) >=abs(boiling_point-(boiling_point*5//100)) and abs(boiling_map[material]-boiling_point)<=abs(boiling_point+(boiling_point*5//100)) :
            closest=material
    return closest

print(boiling_material(boiling_map,359))
print(boiling_material(boiling_map,-0.475))
print(boiling_material(boiling_map,0))