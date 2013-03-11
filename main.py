# Andrew Quintanilla
# CPSC254
# Manages Ratings Databases
import os, glob, sqlite3

# If no databases, return false.
# If there are databases, return list of database names
def CheckDatabase():
	database = glob.glob('ratings.db')
	if (not database):
		return False
	else:
		return True

# Assume all potential inputs are sanitized		
# Name (string): Table name (no spaces or special characters, is used to name table
# Categories (list of strings): List of categories for table
def CreateTable(name, categories):
	conn = sqlite3.connect(name + '.db')
	c = conn.cursor()
	
	# Constructs CREATE TABLE command
	newtable = 'CREATE TABLE '
	newtable += name+' ('
	for i in range(len(categories)):
		newtable += categories[i]
		newtable += ' text'
		if i != len(categories)-1:
			newtable += ', '
	
	conn.commit()
	conn.close()

# name: Database to be deleted
def DropTable(name):
	os.remove(name+'.db')

# name: name of database to be inserted into
# tuple: list of attributes of new item
def Insert(name, tuple):
	conn = sqlite3.connect(name+'.db')
	c = conn.cursor()
	
	# Constructs INSERT INTO command
	insertinto = 'INSERT INTO ' + 
	
def main():
	CreateTable('test', ['cat1', 'cat2', 'cat3'])
	l = CheckDatabases()
	print(l)
	DeleteDatabase('test')
	l=CheckDatabases()
	print(l)

if __name__ == '__main__':
	main()