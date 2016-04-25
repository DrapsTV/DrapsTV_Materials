
//code 1//

def Main():
	import sqlite3

	con = sqlite3.connect('test.db')
    
	cur = con.cursor()    
	cur.execute('SELECT SQLITE_VERSION()')
    
	data = cur.fetchone()
    
	print "SQLite version: " + data

	con.close()

if __name__ == '__main__':
	Main()


//code 2//

def Main():
	import sqlite3
	
	try:
		con = sqlite3.connect('test.db')
    
		cur = con.cursor() 
   
		cur.execute("CREATE TABLE Pets(Id INT, Name TEXT, Price INT)")
		cur.execute("INSERT INTO Pets VALUES(1, 'Cat', 400)")
		cur.execute("INSERT INTO Pets VALUES(2, 'Dog', 600)")
		cur.execute("INSERT INTO Pets VALUES(3, 'Rabbit', 200)")
		cur.execute("INSERT INTO Pets VALUES(4, 'Bird', 60)")
    
		con.commit()

		cur.execute("SELECT * FROM Pets")
		data = cur.fetchall()
		
		for row in data:
			print row

	except sqlite3.Error, e:

		if con:
			con.rollback()

	finally:
		
		if con:
			con.close()

if __name__ == '__main__':
	Main()


//code 3//

def Main():
	import sqlite3
	
	try:
		con = sqlite3.connect('test.db')
    
		cur = con.cursor() 
   		
		cur.executescript("""DROP TABLE IF EXISTS Pets;
				CREATE TABLE Pets(Id INT, Name TEXT, Price INT);
				INSERT INTO Pets VALUES(1, 'Cat', 400);
				INSERT INTO Pets VALUES(2, 'Dog', 600);""")
    
		pets = ((3, 'Rabbit', 200),
			(4, 'Bird', 60),
			(5, 'Goat', 500))

		cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", pets)

		
		con.commit()

		cur.execute("SELECT * FROM Pets")
		data = cur.fetchall()
		
		for row in data:
			print row

	except sqlite3.Error, e:

		if con:
			con.rollback()

	finally:
		
		if con:
			con.close()

if __name__ == '__main__':
	Main()

