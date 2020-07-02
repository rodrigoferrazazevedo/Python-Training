cubes = [k**3 for k in range(10)]
print(cubes)
print(type(cubes))

cubes_gen = (k**3 for k in range(10))
print(cubes_gen)
print(type(cubes_gen))

#exhaust the generator
_ = list
print(_(cubes_gen))
#nothing more to give
print(_(cubes_gen))