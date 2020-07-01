cubes = [k**3 for k in range(10)]
print(cubes)
print(type(cubes))

cubes_gen = (k**3 for k in range(10))
print(cubes_gen)
print(type(cubes_gen))

_ = list # alias
print(_(cubes_gen))
print(type(_(cubes_gen)))