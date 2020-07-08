from time import time
mx = 5000

# Map
""" 
# Incomplete
t = time() # start time
mp = list(map(lambda a, b: divmod(a, b), range(1, mx), range(1, mx)))
print('List length: {}'.format(len(mp)))
print('map: {:.4f} s'.format(time() - t)) """

# For loop
t = time() # start time
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print('List length: {}'.format(len(floop)))
print('for loop: {:.4f} s'.format(time() - t))

# List comprehension
t = time() # start time
compr = [
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)
]
print('List length: {}'.format(len(compr)))
print('list comprehension: {:.4f} s'.format(time() - t))

# Generator
t = time() # start time
gener = list(
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)
)
print('List length: {}'.format(len(gener)))
print('generator expression: {:.4f} s'.format(time() - t))
