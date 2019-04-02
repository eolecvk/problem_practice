
# MAP
#-------------------------

items = [1, 2, 3]
squared = list(map(lambda x : x**2, items))

def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)



# FILTER
#-------------------------
items = [-5, 1, -9, 10, 2]
print(list(filter(lambda x : x < 0, items)))



# REDUCE
#-------------------------

from functools import reduce
product = reduce(lambda x, y : x*y, [1, 2, 3])
print(product)