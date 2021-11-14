import sqlite3
from sqlite3 import Error


class User:
    def __init__(self, email, password, name, zipcode, rating, transaction_count, phone_number):
        self.email = email
        self.password = password
        self.name = name
        self.zipcode = zipcode
        self.rating = rating
        self.transaction_count = transaction_count
        self.phone_number = phone_number

    def get_password(self):
        return self.password


def select_user_by_email(email: str) -> User:
    try:
        conn = sqlite3.connect("sqlite_db")
        users = conn.execute(
            "Select * from User where email = ?", (email,)
        ).fetchall()
        conn.commit()
        print(users)
        if len(users) != 1:
            return None
        else:
            email, password, name, zipcode, rating, transaction_count, phone_number = users[0]
            return User(email, password, name, zipcode, rating, transaction_count, phone_number)
    except Error as e:
        print(e)
        return None
