print(list([n**2 for n in range(10)]))


# Equivalent to:

#squares = []
# for n in range(10):
#     squares.append(n ** 2)
# print(squares)

# or

# squares = map(lambda x: x**2, range(10))
# print(list(squares))