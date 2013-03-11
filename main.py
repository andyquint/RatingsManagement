# Andrew Quintanilla
# CPSC254
# Manages Ratings Databases
import glob, sqlite3

# If no databases, return false.
# If there are databases, return list of database names
def CheckDatabases():
	databaselist = glob.glob('*.db')
	if (not databaselist):
		return False
	else:
		return databaselist
		
# Name: Database name (no spaces, special characters, is used to name database file
# Categories: List of categories for database
def CreateNewDatabase(name, categories):
	conn = sqlite3.connect(name + '.db')
	
def main():
	

if __name__ == '__main__':
	main()