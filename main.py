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

# Assume all potential inputs are sanitized, table doesn't already exist	
# Name (string): Table name (no spaces or special characters, is used to name table
# Categories (list of strings): List of categories for table. Has at least one category. All categories will be strings.
def CreateTable(name, categories):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs CREATE TABLE command
	newtable = 'CREATE TABLE '
	newtable += name+' ('
	newtable += 'ID int, ' # This ID number will be automatically assigned upon insertion.
	for i in range(len(categories)):
		newtable += categories[i]
		newtable += ' text'
		newtable += ', '
	# Put categories for stars and comments here
	newtable += 'STARS real, COMMENTS text)'
	c.execute(newtable)
	conn.commit()
	conn.close()

# name: Database to be deleted
def DropTable(name):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	c.execute('DROP TABLE IF EXISTS %s' % name)
	conn.commit()
	conn.close()

# name: name of table to be inserted into
# tuple: list of attributes of new item
def Insert(name, tuple):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs INSERT INTO command
	insertinto = 'INSERT INTO %s VALUES (\'' % name
	for i in range(len(tuple)):
		insertinto += tuple[i]
		insertinto += '\''
		if i != len(tuple)-1:
			insertinto += ', \''
		else:
			insertinto += ')'
	c.execute(insertinto)
	conn.commit()
	conn.close()
	
def main():
	DropTable('test')
	DropTable('test1')
	CreateTable('test',['cat1','cat2','cat3'])
	CreateTable('test1',['cat1','cat2'])
	Insert('test1',['garbage','moregarbage'])
	print(CheckTableNamed('test'))
	print(CheckTableNamed('test2')) 

if __name__ == '__main__':
	main()