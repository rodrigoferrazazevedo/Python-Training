class Person:
    species = 'Human'

print("Person class:")
print(Person.species)
Person.alive = True
print(Person.alive)

print("man object:")
man = Person()
print(man.species)
print(man.alive)

print("Inherited attribute:")
Person.alive = False
print(man.alive)

print("Instance attributes:")
man.name = 'Darth'
man.surname = 'Valder'
print(man.name, man.surname)