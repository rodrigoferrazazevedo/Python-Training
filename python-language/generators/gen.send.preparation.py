def counter(start=0):
    n = start
    while True:
        yield n
        n += 1

c = counter()
print(next(c))
print(next(c))
print(next(c))