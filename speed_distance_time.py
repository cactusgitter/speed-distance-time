import random #to use random numbers
import os     #For clear screen
import msvcrt #For single character input

LINE = "==========================================="

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def exception_msg():
	print(LINE)
	print("You have entered an invalid character, or caused division by zero.")
	print("Try again.")
	print(LINE)

def jobs_done__msg():
	print(LINE)
	print(LINE)
	print("Job complete, press enter to return to the main menu...")
	input()
	
def speed():
	jobs_done = False
	while jobs_done == False:
		try:
			print("Please enter the distance in miles:")
			d = int(input())
			print("Enter the time in minutes:")
			t = int(input())
			t = t/60
			s = d/t
			print(LINE + "\n")
			print("  *** Speed *** = {0:.1f}".format(s) + " MPH\n  ")
		except:
			exception_msg()
			continue
		jobs_done = True
	jobs_done__msg()
					
def distance():
	jobs_done = False
	while jobs_done == False:
		try:
			print("Please enter the speed in MPH:")
			s = int(input())
			print("Enter the time in minutes:")
			t = int(input())
			t = t/60
			d = s * t
			print(LINE + "\n")
			print("  *** Distance *** = {0:.1f}".format(d) + " miles\n  ")
		except:
			exception_msg()
			continue
		jobs_done = True
	jobs_done__msg()
	
def time():
	jobs_done = False
	while jobs_done == False:
		try:
			print("Please enter the distance in miles:")
			d = int(input())
			print("Enter the speed in MPH:")
			s = int(input())
			t = (d/s) * 60
			print(LINE + "\n")
			print("  *** Time *** = {0:.1f}".format(t) + " minutes\n  ")
			
		except:
			exception_msg()
			continue
		jobs_done = True
	jobs_done__msg()
	
def main_menu():
	print(
"""################################################################
# *** Speed, distance, time calculator ***
# ----------------------------------------
# 1) Speed
# 2) Distance
# 3) Time
# 4) Exit Program
#
# Type a number to choose an option, then press [Enter]...
	""")
	correct_choice = False
	while correct_choice == False:
		try:
			i = int(input())
		except:
			print("You have entered an invalid character, or caused division by zero.")
			print("Try again.")
			continue
		
		if i in (1,2,3): # Test for these possibilities
			correct_choice = True
			cls()
			print(LINE)
		if i == 1:
			speed()
		elif i == 2:
			distance()
		elif i == 3:
			time()
		if i == 4:
			import sys	  #To end the program
			sys.exit()
			return
		else:
			print(str(i) + " wasn't a choice, try again.")
		
def main(args):
	while True:
		cls()
		main_menu()
	return 0 # End of program

if __name__ == '__main__':
	import sys	  #To end the program
	sys.exit(main(sys.argv))
