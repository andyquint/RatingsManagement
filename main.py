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

# Assume all potential inputs are sanitized		
# Name (string): Table name (no spaces or special characters, is used to name table
# Categories (list of strings): List of categories for table
def CreateTable(name, categories):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs CREATE TABLE command
	newtable = 'CREATE TABLE '
	newtable += name+' ('
	for i in range(len(categories)):
		newtable += categories[i]
		newtable += ' text'
		if i != len(categories)-1:
			newtable += ', '
		else:
			newtable += ')'
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

# name: name of database to be inserted into
# tuple: list of attributes of new item
def Insert(name, tuple):
	conn = sqlite3.connect(ratingsDB)
	c = conn.cursor()
	
	# Constructs INSERT INTO command
	insertinto = 'INSERT INTO '
	
def main():
	DropTable('test')
	DropTable('test1')
	CreateTable('test',['cat1','cat2','cat3'])
	CreateTable('test1',['cat1','cat2'])
	print(CheckTableNamed('test'))
	print(CheckTableNamed('test2')) 

if __name__ == '__main__':
	main()