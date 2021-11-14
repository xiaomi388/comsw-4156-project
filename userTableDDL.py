import sqlite3
from sqlite3 import Error

def init_db():
    # creates User Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE IF NOT EXISTS User (\
	                email text PRIMARY KEY,\
   	                password text NOT NULL,\
	                name text,  \
	                zipcode integer,\
                    rating integer,\
                    transaction_count integer,\
                    phone_number integer) ;')
        print('User Table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


def insert_mock_user():
    try:
        mock_user = ("zj2304@columbia.edu", "passwd", "Zhihao Jiang", "10025", "10", "1", "6466466646")
        conn = sqlite3.connect("sqlite_db")
        conn.execute(
            "INSERT INTO User "
            "(email, password, name, zipcode, rating, transaction_count, phone_number) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)", mock_user
        )

        conn.commit()
        print(f"mock user inserted {mock_user}")
    except Error as e:
        print(e)
    return


def check_User_Table():
    try:
        conn = sqlite3.connect("sqlite_db")
        users = conn.execute(
            "Select * from User "
        )
        conn.commit()
        print(f"user table has ")
        for user in users:
            print(user)
    except Error as e:
        print(e)
    return

def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE User")
        print('Table User cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

clear()
init_db()
insert_mock_user()
check_User_Table()
