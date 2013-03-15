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
# 2: Select Existing List
	def __init__(self):
		self.state = 0
		
	def DisplayMenu(self):
		if self.state == 0:
			print('1. Create New List')
			print('2. Select Existing List')
			print('3. Quit')
			opt = int(GetOption(1,3))
			if opt == 1:
				self.state = 1
			elif opt == 2:
				self.state = 2
			elif opt == 3:
				Quit()
			else:
				InvalidOption()
		elif self.state == 2:
			listnames = dbmanager.ListTableNames()
			for n in range(len(listnames)):
				print('%i: %s' % (n+1,listnames[n]))
			print('%i: Quit' % (len(listnames)+1))
			
		else:
			Quit()

# min: Minimum acceptable input number
# max: Maximum acceptable input number			
def GetOption(min, max):
	option = int(input('>> '))
	while (option < min or option > max):
		InvalidOption()
		option = int(input('>> '))
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