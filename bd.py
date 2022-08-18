import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="1245",
  host="127.0.0.1",
  port="5432"
)


def create_db(conn):
    #Функция, создающая структуру БД (таблицы)

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
        client_id INTEGER UNIQUE PRIMARY KEY,
        first_name VARCHAR(40),
        last_name VARCHAR(60),
        email VARCHAR(60)
        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER REFERENCES customers(client_id),
        phone VARCHAR(12)
        );""")
    conn.commit()  # фиксируем в БД

def add_client(conn, client_id, first_name, last_name, email, phones=None):
    #Функция, позволяющая добавить нового клиента

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO customers(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);
    """, (client_id, first_name, last_name, email))
    conn.commit()
    cur.execute("""
    SELECT * FROM customers;
    """)
    print(cur.fetchall())
    cur.execute("""
    INSERT INTO phones(client_id, phone) VALUES(%s, %s);
    """, (client_id, phones))
    conn.commit()
    cur.execute("""
    SELECT * FROM phones;
     """)
    print(cur.fetchall())


def add_phone(conn, client_id, phone):
    #Функция, позволяющая добавить телефон для существующего клиента

    cur = conn.cursor()
    cur.execute("""
    UPDATE phones SET phone=%s WHERE client_id=%s;
    """, (phone, client_id))
    conn.commit()  # фиксируем в БД

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    #Функция, позволяющая изменить данные о клиенте
    cur = conn.cursor()
    cur.execute("""
    UPDATE customers SET first_name=%s, last_name=%s, email=%s, phones=%s$;
    """, (first_name, last_name, email, phones))
    conn.commit()

def delete_phone(conn, client_id, phone):
    #Функция, позволяющая удалить телефон для существующего клиента
    cur = conn.cursor()
    cur.execute("""
        DELETE phones SET phone=%s WHERE client_id=%s;
        """, (phone, client_id))
    conn.commit()

def delete_client(conn, client_id):
    #Функция, позволяющая удалить существующего клиента
    cur = conn.cursor()
    cur.execute("""
        DELETE customers SET client_id=%s;
        """, (client_id))
    conn.commit

    # Функция, позволяющая найти клиента по его данным(имени,фамилии, эмейлу, телефону)
def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM * , where first_name=%s or last_name=%s or email=%s or phone=%s;
    """, (first_name, last_name, email, phone))
    
    
con.close()
