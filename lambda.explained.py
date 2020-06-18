def adder(a, b):
    return a + b

# is equivalent to:
adder_lambda = lambda a, b: a + b

def to_upper(s):
    return s.upper()

#is equivalent to:
to_upper_lamda = lambda s: s.upper()

print(adder(1, 2))
print(adder_lambda(1, 2))
print(to_upper('rodrigo'))
print(to_upper_lamda('rodrigo'))
