import sqlite3
from json import dumps, loads
from sqlite3 import Error


def init_db():
	"""Create User, Furniture, Transaction tables."""
	conn = None
	try:
		conn = sqlite3.connect('sqlite_db')
		create_user_query = """CREATE TABLE IF NOT EXISTS User (
			email TEXT PRIMARY KEY,
			password TEXT NOT NULL,
			name VARCHAR(20) NOT NULL,
			zipcode INTEGER,
			rating DOUBLE DEFAULT 0,
			transcation_count INTEGER NOT NULL,
			phone_number VARCHAR(10)
		);"""
		create_furniture_query = """CREATE TABLE IF NOT EXISTS Furniture (
			fid INTEGER PRIMARY KEY AUTOINCREMENT,
			owner VARCHAR(20) NOT NULL,
			title VARCHAR(50),
			labels TEXT,
			status TEXT NOT NULL DEFAULT "init",
			image_url TEXT,
			description VARCHAR(200),
			FOREIGN KEY(owner) REFERENCES User(email)
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
		print('Database Online, User, furniture and transaction tables created')
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

def clear():
	"""Drop database"""
	# emmm, comment for dropping tables
	# assert 0, "ERROR: how dare you?!"
	conn = None
	try:
		conn = sqlite3.connect('sqlite_db')
		conn.execute("DROP User")
		conn.execute("DROP Furniture")
		conn.execute("DROP Transaction")
		print('Database Cleared, dropped User, Furniture, Transaction Tables')
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

