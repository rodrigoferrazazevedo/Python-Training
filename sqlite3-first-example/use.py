from crud import db_insert, db_select, db_update

""" db_insert('Ted','1111-2222','ted@gmail.com')
db_insert('Barney','3333-4444','barney@gmail.com')
db_insert('Robin','5555-6666','robin@gmail.com')
db_insert('Marshall','7777-8888','marshal@gmail.com')
db_insert('Lili','9999-0000','lili@gmail.com') """
print(db_select('id','1'))