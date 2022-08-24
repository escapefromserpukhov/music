import psycopg2



def add_client(conn, client_id, first_name, last_name, email, phones=None):
    #Функция, позволяющая добавить нового клиента
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
    cur.execute("""
    UPDATE phones SET phone=%s WHERE client_id=%s;
    """, (phone, client_id))
    conn.commit()  # фиксируем в БД

def change_client(conn, first_name=None, last_name=None, email=None):
    #Функция, позволяющая изменить данные о клиенте
    cur.execute("""
        UPDATE customers SET first_name=%s, last_name=%s, email=%s, phone=%s;
        """, (first_name, last_name, email))
    print(cur.fetchall())
    conn.commit()

def delete_phone(conn, client_id, phone):
    #Функция, позволяющая удалить телефон для существующего клиента
    cur.execute("""
        DELETE phone, SET client_id=%s;
        """, (client_id, phone))
    cur.execute("""
        SELECT * FROM phones;
        """)
    print(cur.fetchall())
    conn.commit()

def delete_client(conn, client_id):
    #Функция, позволяющая удалить существующего клиента
    cur.execute("""
        DELETE FROM customers where client_id=%s;
        """, (client_id))
    cur.execute("""
        SELECT FROM customers;
        """,)
    print(cur.fetchall())
    conn.commit()

    # Функция, позволяющая найти клиента по его данным
def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
    SELECT * FROM customers, phones  where first_name=%s or last_name=%s or email=%s or phone=%s;
    """, (first_name, last_name, email, phone))
    print(cur.fetchall())
    conn.commit()

############################
with psycopg2.connect(database="netology_db", user="postgres", password="1245") as conn:
    with conn.cursor() as cur:
        # Создание таблиц
        def create_db(conn):
            # Функция, создающая структуру БД (таблицы)
            cur.execute("""CREATE TABLE IF NOT EXISTS customers(
            client_id INTEGER UNIQUE PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(60),
            email VARCHAR(60)
            );
            """)
            cur.execute("""CREATE TABLE IF NOT EXISTS phones(
            id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES customers(client_id),
            phone VARCHAR(12)
            );
            """)
            conn.commit()  # фиксируем в БД

            #Вызов функций
        create_db(conn)
        #add_client(conn, 5, "мими","ля","почтапочта")
        #add_phone(conn, 5, "310503")
        #find_client(conn,"Vika")
        #change_client(conn,"Vika")
        #delete_phone(conn, 5, "310503")
        #delete_client(conn, 1)

conn.close()
