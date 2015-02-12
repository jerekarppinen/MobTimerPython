import sqlite3

try:
	db = sqlite3.connect("usersDB")
	cursor = db.cursor()
	cursor.execute(''' CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)''')
	db.commit()

except Exception as e:
	# Rollback any changes if something went wrong
	db.rollback()
	raise e

#finally:
	#db.close()

def addUser(name):
	cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
	db.commit()

def getUsers():
	cursor.execute("SELECT id, name FROM users")
	return cursor.fetchall()

#addUser("touko")

#print getUsers()

#cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)''')
#db.commit()

#cursor.execute(''' DROP TABLE users ''')
#db.commit()

#cursor.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='users' ''')

#if cursor.fetchone() is None:
#		print "is empty"
#else:
#	print "not empty"
#	print len(cursor.fetchall())

#print db.commit()


#cursor.execute(''' INSERT INTO users ())

#db.close()