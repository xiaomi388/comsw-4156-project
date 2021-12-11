import sqlite3
from sqlite3 import Error


def init_db():
    """Create User, Furniture, Transaction tables."""
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        create_user_query = """CREATE TABLE IF NOT EXISTS User (
            email VARCHAR(20) NOT NULL PRIMARY KEY,
            password TEXT NOT NULL,
            name VARCHAR(20) NOT NULL,
            zipcode INTEGER,
            rating DOUBLE DEFAULT 0,
            transaction_count INTEGER DEFAULT 0,
            phone_number VARCHAR(10)
        );"""
        create_furniture_query = """CREATE TABLE IF NOT EXISTS Furniture (
            fid INTEGER PRIMARY KEY AUTOINCREMENT,
            owner VARCHAR(20) NOT NULL,
            buyer VARCHAR(20),
            title VARCHAR(50),
            labels TEXT,
            status TEXT NOT NULL DEFAULT "init",
            image_url TEXT,
            description VARCHAR(200),
            FOREIGN KEY(owner) REFERENCES User(email),
            FOREIGN KEY(buyer) REFERENCES User(email)
        );"""
        create_transaction_query = """CREATE TABLE IF NOT EXISTS Transactions (
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            fid INTEGER NOT NULL,
            seller VARCHAR(20) NOT NULL,
            buyer VARCHAR(20) NOT NULL,
            FOREIGN KEY(fid) REFERENCES Furniture(fid),
            FOREIGN KEY(seller) REFERENCES User(email),
            FOREIGN KEY(buyer) REFERENCES User(email)
        );"""
        conn.execute(create_user_query)
        conn.execute(create_furniture_query)
        conn.execute(create_transaction_query)
        print('Database Online, User, furniture and '
              'transaction tables created')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def clear():
    """Drop database"""
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP Table User")
        conn.execute("DROP Table Furniture")
        conn.execute("DROP Table Transactions")
        print('Database Cleared, dropped User, Furniture, Transaction Tables')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def populate_testing_data():
    """Populate testing data in 3 tables."""
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("INSERT INTO User VALUES(?,?,?,?,?,?,?);",
                     ("Bob@gmail.com", "hashedpassword", "Bob",
                      10025, 4.5, 2, "7348829897"))
        conn.execute("INSERT INTO Furniture(owner, title, labels,"
                     "status, image_url, description) VALUES(?,?,?,?,?,?);",
                     ("Bob@gmail.com", "Alienware Gaming Monitors", "monitor",
                      "init", "www.googlecom", "This is a monitor"))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_mock_user():
    try:
        mock_user = ("zj2304@columbia.edu", "password",
                     "Zhihao Jiang", 10025, 10, 1, "6466466646")
        conn = sqlite3.connect("sqlite_db")
        conn.execute(
            "INSERT INTO User "
            "(email, password, name, zipcode,"
            " rating, transaction_count, phone_number) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)", mock_user
        )

        conn.commit()
        print(f"mock user inserted {mock_user}")
    except Error as e:
        print(e)
    return


def insert_mock_furniture():
    try:
        mock_furniture = (1, "zj2304@columbia.edu",
                          "Lamp", "cheap", "http", "very good")
        conn = sqlite3.connect("sqlite_db")
        conn.execute(
            "INSERT INTO Furniture "
            "(fid, owner, title,"
            " labels , image_url, description ) "
            "VALUES (?, ?, ?, ?, ?, ?)", mock_furniture
        )

        conn.commit()
        print(f"mock furniture inserted {mock_furniture}")
    except Error as e:
        print(e)
    return

def insert_mock_buyer():
    try:
        mock_user = ("buyer_zj@columbia.edu", "password",
                     "Buyer_Sause", 10025, 10, 1, "6466466646")
        conn = sqlite3.connect("sqlite_db")
        conn.execute(
            "INSERT INTO User "
            "(email, password, name, zipcode,"
            " rating, transaction_count, phone_number) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)", mock_user
        )

        conn.commit()
        print(f"mock user for buying inserted {mock_user}")
    except Error as e:
        print(e)
    return

def mock_buy(status):
    try:
        conn = sqlite3.connect("sqlite_db")
        cur = conn.cursor()
        cur.execute(
            "UPDATE Furniture "
            "SET buyer = 'buyer_zj@columbia.edu', "
            "status = ? " 
            "where fid = 1", [status])
        conn.commit()
        print(f"mock buying behavior")
    except Error as e:
        print(e)
    return
