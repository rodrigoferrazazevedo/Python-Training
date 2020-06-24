import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        cur.execute(func(*args))
        con.commit()
        con.close()
    return decorator    

@commit_close
def db_insert(name, phone, email):
    return """
    INSERT INTO users(name, phone, email)
        VALUES('{}', '{}', '{}')
    """.format(name, phone, email)

@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}' 
    """.format(name, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email = '{}' 
    """.format(email)

def db_select(field, data):
    sql = """
    SELECT id, name, phone, email FROM users WHERE {} = '{}' 
    """.format(field, data)
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data




