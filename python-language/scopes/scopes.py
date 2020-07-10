A = 100

ex1 = [A for A in range(5)]
print("ex1:")
print(ex1)
print(A)

ex2 = list(A for A in range(5))
print("ex2:")
print(ex2)
print(A)

ex3 = dict((A, 2*A) for A in range(5))
print("ex3:")
print(ex3)
print(A)

ex4 = set(A for A in range(5))
print("ex4")
print(ex4)
print(A)

s = 0
for A in range(5):
    s += A
print("for:")
print(s)
print(A)