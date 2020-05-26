surnames = ['Rivest', 'Shamir', 'Adleman']
print("Starting from 0")
for position, surname in enumerate(surnames):
    print(position, surname)
print("Starting from 1")
for position, surname in enumerate(surnames, 1):
    print(position, surname)

