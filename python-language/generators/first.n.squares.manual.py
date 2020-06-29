def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(4)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# print(next(squares)) # error