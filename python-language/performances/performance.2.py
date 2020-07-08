from time import time

mx = 2 * 10 ** 7

t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print('List length: {}'.format(len(absloop)))
print('for loop: {:.4f} s'.format(time() - t))

t = time()
abslist = [abs(n) for n in range(mx)]
print('List length: {}'.format(len(abslist)))
print('list comprehension: {:.4f} s'.format(time() - t))

t = time()
absmap = list(map(abs, range(mx)))
print('List length: {}'.format(len(absmap)))
print('map: {:.4f} s'.format(time() - t))