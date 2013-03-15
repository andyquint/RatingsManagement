# Andrew Quintanilla
# CPSC254
# Manages Ratings Databases
import os, glob, sqlite3
ratingsDB = 'ratings.db'

# If database exists, returns True, otherwise, returns False.
def CheckDatabase():
	database = glob.glob(ratingsDB)
	if (not database):
		return False
	else:
		return True
		
# Checks if there exists a table matching name. Returns True if so, False otherwise.
def CheckTableNamed(name):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	c.execute("SELECT name FROM sqlite_master WHERE name='%s'" % name)
	nameslist = c.fetchall()
	conn.close()
	if nameslist:
		return True
	else:
		return False
		
# Returns a list containing the names of all the tables
def ListTableNames():
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	c.execute("SELECT name FROM sqlite_master WHERE type='table'")
	names = []
	for n in c.fetchall():
		names.append(n[0])
	return names
	
# Returns a list containing all the categories in the table
# name: name of table
def ListTableCategories(name):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	c.execute('PRAGMA table_info(%s)' % name)
	
	l = []
	for t in c.fetchall():
		l.append(t[1])
	return l

# Assume all potential inputs are sanitized, table doesn't already exist	
# Name (string): Table name (no spaces or special characters, is used to name table
# Categories (list of strings): List of categories for table. Has at least one category. All categories will be strings.
def CreateTable(name, categories):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs CREATE TABLE command
	newtable = 'CREATE TABLE '
	newtable += name+' ('
	newtable += 'ID integer primary key, ' # This ID number will be automatically assigned upon insertion.
	for i in range(len(categories)):
		newtable += categories[i]
		newtable += ' text'
		newtable += ', '
	newtable += 'STARS real, COMMENTS text)' # Creates categories for stars rating and comments
	c.execute(newtable)
	conn.commit()
	conn.close()

# Drops table matching name
# name: Table to be dropped
def DropTable(name):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	c.execute('DROP TABLE IF EXISTS %s' % name)
	conn.commit()
	conn.close()

# Generates ID number as the highest ID in the table incremented by 1
# name: name of table to be inserted into
# tuple: list of attributes of new item. Assumes strings are surrounded
#	by escaped apostrophes (')
def Insert(name, tuple):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs INSERT INTO command
	insertinto = 'INSERT INTO %s VALUES (null,' % name
	for i in range(len(tuple)):
		insertinto += '%s' % tuple[i]
		if i != len(tuple)-1:
			insertinto += ', '
		else:
			insertinto += ')'
	c.execute(insertinto)
	conn.commit()
	conn.close()
	
# Returns list of items matching selection criteria
# name: name of table to be selected from
# category: category that is being matched
# key: search key
def Select(name, category, key):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	select = 'SELECT * FROM %s WHERE %s=%s' % (name, category, key)
	
	c.execute(select)
	return c.fetchall()
	
# Deletes row with id matching delID
# name: name of table to delete from
# delID: ID of row to delete
def Delete(name, delID):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	delete = 'DELETE FROM %s WHERE ID=%d' % (name, delID)
	
	c.execute(delete)
	conn.commit()
	conn.close()