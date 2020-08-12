from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def display_info():
    addresses = session.query(Address).all()

    for address in addresses:
        print(f'{address.person.name} <{address.email}>')

    print('people: {}, addresses: {}'.format(
        session.query(Person).count(),
        session.query(Address).count())
    )

anakin = Person(name='Anakin Skywalker', age=32)
obil = Person(name='Obi-Wan Kenobi', age=40)

# You can use different techniques to add
obil.addresses = [
    Address(email='obil@example.com'),
    Address(email='wanwan@example.com')
]

anakin.addresses.append(Address(email='ani@example.com'))
anakin.addresses.append(Address(email='evil.dart@example.com'))
anakin.addresses.append(Address(email='vader@example.com'))

# Insert into database
session.add(anakin)
session.add(obil)
session.commit()

# Query
obil = session.query(Person).filter(
    Person.name.like('Obi%')
).first()
print(obil, obil.addresses)

anakin = session.query(Person).filter(
    Person.name == 'Anakin Skywalker'
).first()
print(anakin, anakin.addresses)

# delete
anakin_id = anakin.id
del anakin

print('')

display_info()

print('')

anakin = session.query(Person).get(anakin_id)
session.delete(anakin)
session.commit()

display_info()