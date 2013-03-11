# Andrew Quintanilla
# CPSC254
# Manages Ratings Databases
import os, glob, sqlite3

# If no databases, return false.
# If there are databases, return list of database names
def CheckDatabases():
	databaselist = glob.glob('*.db')
	if (not databaselist):
		return False
	else:
		return databaselist

# Assume all potential inputs are sanitized		
# Name (string): Database name (no spaces, special characters, is used to name database file
# Categories (list of strings): List of categories for database
def CreateNewDatabase(name, categories):
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
def DeleteDatabase(name):
	os.remove(name+'.db')

# 
def InsertIntoTable(name
	
def main():
	CreateNewDatabase('test', ['cat1', 'cat2', 'cat3'])
	l = CheckDatabases()
	print(l)
	DeleteDatabase('test')
	l=CheckDatabases()
	print(l)

if __name__ == '__main__':
	main()