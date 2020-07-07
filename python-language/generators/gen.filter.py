cubes = [x**3 for x in range(10)]
print(cubes)

odd_cubes1 = filter(lambda cube: cube%2, cubes)
print(list(odd_cubes1))

odd_cubes2 = (cube for cube in cubes if cube%2)
print(list(odd_cubes2))