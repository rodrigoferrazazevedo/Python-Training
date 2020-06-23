map(lambda *a: a, range(3))

_ = list

_(map(lambda *a: a, range(3)))

_(map(lambda *a: a, range(3), 'abc'))

_(map(lambda *a: a, range(3), 'abc', range(4,7)))

_(map(lambda *a: a, (), 'abc'))

_(map(lambda *a: a, (1,2), 'abc'))

_(map(lambda *a: a, (1, 2, 3, 4), 'abc'))