# Andrew Quintanilla
# CPSC254
# Command Line Interface for Ratings Manager
import sys, dbmanager

def DisplayWelcome():
	print('Ratings Manager\n')

class CLI:
# State Definitions
# 0: Create New List / Select Existing List
# 1: Create New List
# 2: Select List
# 3: List options
	def __init__(self):
		self.state = 0
		self.table = ''
		
	def DisplayMenu(self):
		if self.state == 0:
			print('1. Create New List')
			print('2. Select Existing List')
			print('3. Quit')
			opt = GetOption(3)
			if opt == 1:
				self.state = 1
			elif opt == 2:
				self.state = 2
			elif opt == 3:
				Quit()
			else:
				InvalidOption()
		elif self.state == 1:
			name = input('New table name>> ')
			while(any(name == n for n in dbmanager.ListTableNames())):
				print('Table with that name already exists.')
				name = input('New table name>> ')
			categories = []
			for n in range(int(input('Number of categories>> '))):
				categories.append(input('Name of category %i>> ' % (n+1)))
			dbmanager.CreateTable(name, categories)
			print('List %s created with %i categories.\n' % (name, len(categories)))
			self.state = 0			
		elif self.state == 2:
			listnames = dbmanager.ListTableNames()
			for n in range(len(listnames)):
				print('%i: %s' % (n+1,listnames[n]))
			print('%i: Back' % (len(listnames)+1))
			print('%i: Quit' % (len(listnames)+2))
			opt = GetOption(len(listnames)+2)
			if opt == len(listnames)+2:
				Quit()
			elif opt == len(listnames)+1:
				self.state = 0
			else:
				self.table = listnames[opt-1]
				self.state = 3
		elif self.state == 3:
			print('1. Delete List')
			print('2. Nothing')
			print('3. Quit')
			opt = GetOption(3)
			if opt == 1:
				dbmanager.DropTable(self.table)
				print('%s deleted.' % self.table)
				self.state = 0
			elif opt == 2:
				self.state = 0
			else:
				Quit()
			
		else:
			Quit()

# min: Minimum acceptable input number
# max: Maximum acceptable input number			
def GetOption(max):
	option = int(input('>> '))
	while (option > max):
		InvalidOption()
		option = int(input('>> '))
	print('')
	return option
	
def InvalidOption():
	print('Invalid option')
	
def Quit():
	sys.exit()
	
def main():
	cli = CLI()
	DisplayWelcome()
	while(True):
		cli.DisplayMenu()
		

if __name__ == '__main__':
	main()