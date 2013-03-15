# Andrew Quintanilla
# CPSC254
# Command Line Interface for Ratings Manager
import sys, dbmanager

# State Definitions
# 0: Create New List / Select Existing List
state = 0

def DisplayWelcome():
	print('Ratings Manager\n')
	
def DisplayMenu():
	if state == 0:
		print('1. Create New List')
		print('2. Select Existing List')
		print('3. Quit')
		opt = GetOption()
		if opt == 1:
			state = 1
		elif opt == 2:
			state = 2
		elif opt == 3:
			Quit()
		else:
			InvalidOption()
		
def GetOption():
	print('>> ')
	option = input('>> ')
	return option
	
def InvalidOption():
	print('Invalid option')
	
def Quit():
	sys.exit()
	
def main():
	DisplayWelcome():
	while(True):
		DisplayMenu()
		

if __name__ == '__main__':
	main()