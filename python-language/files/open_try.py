try:
    fh = open('fear.txt') #open('fear.txt', 'rt')
    for line in fh: #fh.readlines():
        print(line.strip())

finally:
    fh.close()