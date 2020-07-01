stop = False

def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

c = counter()
print(next(c))
print(next(c))
stop = True
print(next(c)) #raises StopIteration