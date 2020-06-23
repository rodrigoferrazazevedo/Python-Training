grades=[18, 23, 30, 27]
avgs=[22,21,29,24]

_ = list

print(_(zip(avgs, grades)))

print(_(map(lambda *a: a, avgs, grades))) #lambda equivalent to zip