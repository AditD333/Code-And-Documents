# Import os, math, and calendar module
import os,math
import calendar
 
# This module will be called after each operation in every single mode, or if the entered input was not a number.
def repeater():
	try:
		print("\n\nHit Enter To Continue!")
		repeat = input()
		main()
	except:
		os.system('clear')
		repeater()
				
# Main Menu
def main():
	try:
		os.system('clear')
		print("----------------YEAR PERIODIZATION CALCULATOR----------------")
		print("\n")
		print("\nSelect Menu!")
		print("1. Start and end of an n - year cycle")
		print("2. Year Description Modifier")
		print("3. New n - year cycle's eve")
		print("4. Calendar Maker")
		print("5. Get date in New Format")
		print("6. Convert year into New Format by (Cycle_no.-Year_no.)")
		print("7. All Factors of inputted Year")
		print("8. i-th Year of the Cycle")
		print("9. Current cycle of the inputted year")
		print("9a. Calculate the next and past periods based on an n - year cycle")
		print("9b. Years left until the next specific calendrical n - cycle")
		print("9c. Calculate the next and past occurences of the i-th year of the particular cycle")
		print("0. Day difference between Gregorian Calendar and Julian Calendar")
		
		print("!. 400-cycle indexing lists first day and last days")
		print("?. Guidelines!")

		print("\nNote: The calendar used in this program is proleptic Perfect Gregorian / Common Era calendar!")
		print("\n\nAnd this completely used Astronomical/ISO 8601 System >> 0-Based Epoch")
		
		print("\nExtra Notes: year 0 = 1 BC/BCE, -1 = 2 BC/BCE, etc!")
		print("For Mode 0, they only show years, not a usual long date format!")
		
		menu = input("\n\nYour selection >> ") #User input to select menu
		

		# Validation if user enters a desired menu
		if menu == '1':
			menu1()
		elif menu == '2':
			menu2()
		elif menu == '3':
			menu3()
		elif menu == '4':
			menu4()
		elif menu == '5':
			menu5()
		elif menu == '6':
			menu6()
		elif menu == '7':
			menu7()
		elif menu == '8':
			menu8()
		elif menu == '9':
			menu9()
		elif menu == '0':
			menu0()
		elif menu == '?':
			guide()
		elif menu == '!':
			yearindexing()

		# Extension Menu (Expansion(s) from mode 9)

		elif menu == '9a' or menu == '9A':
			ext1()
		elif menu == '9b' or menu == '9B':
			ext2()
		elif menu == '9c' or menu == '9C':
			ext3()

		else: # If the user input doesn't correspond to the menu
			os.system('clear')
			main()
	except:
		os.system('clear')
		main()
# If the user inputted '?' and hit enter then call this menu and automatically show the guidine menu.
def guide():
	os.system('clear') # clear the screen first
	print("\"! How to calculate i-th year of the cycle?\"")
	print("----------------------------------------------------------------------------------------------")
	print("\n")
	print("\n\n Astronomical based or nowadays using ISO 8601 (whether in this program not using four digit year) is calculated from year 0000. Hence, each very first cycle of any n - year cycle rumbled up their kickoffs from 0000. And every new cycle starts JUST the year that is divisible by the n, without leaving any remainder STARTS BY. Or in mathematical language as if any digit year has a remainder of 0, than it is the start of the cycle, and has to be end when the remainder is ONE LESS THAN the n in the same cycle.")
	print("\nAside from the widely used Gregorian Calendar, this year numbering is an adaptation to it, with the year 0 (or 1 BC/BCE) being counted as the first year of any n - year cycles.\nThe year is counted cardinally rather than ordinal as well the ordinalization to the year for example if 0 is the 1st, then 2019 for example is 2020th year in this scheme.")
	print("\nSo in fact, it starts from \"the year ([i-1] * the n - year cycle)\"")
	print("\n\nFor Example if a decade is a 10 - year cycle, using this method, it will be running from:")
	print("\n0 - 9, 10 - 19, 20 - 29, or continue the pattern, we get 2020 - 2029")
	print("Or other else a century ~ 100 - year cycle, runs from 0 - 99, 100 - 199, with currently 2000 - 2099")
	print("Or trying other numbers like 69 - year cycle or novemsexegennium, runs from 0 - 68, 69 - 137, or currently this case, 2001 - 2069")
	print("\n\n[*] Calculator Interpretation")
	print("Here, we look only the year number to determine what cycle actually the year belongs to.")
	print("On [+] group, (0 ~ infinity), it will be:")
	print("\n>> [i-1].xxxxxxxxxxxxx......, where i belongs to cycle number and x are any number from 0 - 9.")
	print("\n\nFor Example, Third Decade of 21st Century here in this method in the calculator should be grouped as 2020-2029, because:")
	print("\n>> [203-1].xxxxxxxxxxxxx")
	print("\n>> 2020 / 10 = 202 (exactly), and the last year with the result of 202 (without focusing to decimals) is 2029, because 2030 will no longer result as 202, which is 203. Hence 2030 is the fourth decade of 21st century.")
	print("\n\nFor [-] group, the interpretation will be like this:")
	print("\n[-i-1] - [-i].xxxxx......xy where if x is all zeroes repeating without interruptions of any no zero number, then y must be 1 - 9.")
	print("\nFor example last century of B.C, 1st century B.C, or here the cycle number 0, will go like this")
	print("[-1] - [-0.000000000000001]")
	print("-100 to -1")
	print("However you can demarcate for [1-999] million years as [1-999] decies centennium, but starting from billion,trillion and so on by:")
	print("Replacing llion -> llennium, it must be like that but currently not being stated as official measurements. (e.g. trillion -> trillennium)")


	repeater()

# If user entered '1' and hit enter then execute this menu in menu1 function.
def menu1():
	try:
		os.system('clear') # clear the screen first
		print("1. Start and end of an n - year cycle") # Show the name of the menu each operation
		print("\n")
		ca = int(input("Input Set of Years per Cycle (more than 0)! >> ")) # Input for sets of years per each cycle
		if ca < 1: # If the input was less than 1, then print the error and decide if user wants to try again or not.
			print("Cycle must be at least 1!\n")
			x = input("Press y and enter to try again, or any key plus enter to return to main menu! >> ")
			if x == 'y':
				menu1()
			else:
				main()
		c = int(input("Input Cycle number >> ")) # The cycle number indicates the i-th set of the cycle that inputted by user.
		cycleset = int(ca) # The user input from the variable ca will be assigned in this cycleset variable
		cycleno = int(c) # Also the inputted i-th cycle will be assigned as the the value in the cycleno variable
		
		b1 = (cycleno-1)*cycleset # Variable b1 indicates the first year of the cycle calculated from user inputs
		begin1 = calendar.weekday(b1,1,1) # This will show the name of the day for the 1st of January of the calculated year.
		e1 = b1 + cycleset - 1 # The last year of the cycle
		end1 = calendar.weekday(e1,12,31) # The last day of the last year of the cycle
		
		# Print the result
		print("\nCycle No -", cycleno," of ",cycleset,"- year cycle ranges from")
		print(calendar.day_name[begin1],", January 1st ,", b1, " (00:00:00) - ",calendar.day_name[end1],", December 31st ,", e1," (23:59:59)")
		print("(Ordinalized as Year No.",b1+1,"-",e1+1,")") #The ordinalized as year means the calculated year field + 1, indicates the ordinal mark. 
		repeater()	
	except: # If along the operation, if user input contained at least a non-number (or more) input, or no input has been submitted, then this will force to go to main menu  
		os.system('clear')
		repeater()


# If user entered '2' and hit enter then execute this menu in menu2 function.
def menu2():
	try:
		os.system('clear') # clear the screen first
		print("2. Year Description Modifier") # Show the name of the menu each operation
		print("\n")
		year = int(input("Enter Year no. >> ")) # User freely input any digit year field for calculation
		firstday = calendar.weekday(year,1,1) # Automatically return its January 1st of inputted year
		lastday = calendar.weekday(year,12,31) # Automatically return its December 31st of inputted year
		desc = int(input("\nEnter no. of Descriptions! (up to 5!) >> ")) # User enter number of descriptions with a limit up to five.
		
		if desc == 5: # If it is 5, then 5 unique n - year cycles must be inputted by user.
			
			print("\nEnter 5 Year Cycles For Description, more than 1 - year cycle!")
			print("\n")
			c1 = int(input("1/5 >> "))
			if c1 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()

			# Starting from the next (number of descriptions - 1) inputs, it will validate if each cycles has same values as the previous inputs or not.
			c2 = int(input("2/5 >> "))
			if c2 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()



			
			c3 = int(input("3/5 >> "))
			if c3 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()

			
			c4 = int(input("4/5 >> "))
			if c4 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c3:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			
			c5 = int(input("5/5 >> "))
			if c5 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c3:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c5 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c5 == c2:
				print("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu])")
				choice = input()
				if choice == 'y':
					menu2()
				else:
					main()
			elif c5 == c3:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c5 == c4:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()

		
			# Result, including of the calculation result from the user inputs
			print("\n\n")
			print(year)
			print("\n")
			print("Starts on",calendar.day_name[firstday],
			", January 1st ,",year,"(00:00:00)")
			print("And Ending On",calendar.day_name[lastday],", December 31st ,",year,"(23:59:59)")
			print("\n")
			print("year no.",year+1)
			print("year no.",((year%c1)+1),"of the ",c1,"- year cycle no.",(year//c1)+1)
			print("year no.",((year%c2)+1),"of the ",c2,"- year cycle no.",(year//c2)+1)
			print("year no.",((year%c3)+1),"of the ",c3,"- year cycle no.",(year//c3)+1)
			print("year no.",((year%c4)+1),"of the ",c4,"- year cycle no.",(year//c4)+1)
			print("year no.",((year%c5)+1),"of the ",c5,"- year cycle no.",(year//c5)+1)

			repeater()

		elif desc == 4: # If it is 4, then 4 unique n - year cycles must be inputted by user.
			
			print("\nEnter 4 Year Cycles For Description, more than 1 - year cycle!")
			print("\n")
			c1 = int(input("1/4 >> "))
			if c1 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			
			# Starting from the next (number of descriptions - 1) inputs, it will validate if each cycles has same values as the previous inputs or not.
			c2 = int(input("2/4 >> "))
			if c2 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()


			c3 = int(input("3/4 >> "))
			if c3 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			
			c4 = int(input("4/4 >> "))
			if c4 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			if c4 < 2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				print("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu])")
				choice = input()
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c4 == c3:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			
			# Result, including of the calculation result from the user inputs
			print("\n\n")
			print(year)
			print("\n")
			print("Starts on",calendar.day_name[firstday],
			", January 1st ,",year,"(00:00:00)")
			print("And Ending On",calendar.day_name[lastday],", December 31st ,",year,"(23:59:59)")
			print("\n")
			print("year no.",year+1)
			print("year no.",((year%c1)+1),"of the ",c1,"- year cycle no.",(year//c1)+1)
			print("year no.",((year%c2)+1),"of the ",c2,"- year cycle no.",(year//c2)+1)
			print("year no.",((year%c3)+1),"of the ",c3,"- year cycle no.",(year//c3)+1)
			print("year no.",((year%c4)+1),"of the ",c4,"- year cycle no.",(year//c4)+1)

			repeater()

		elif desc == 3: # If it is 3, then 3 unique n - year cycles must be inputted by user.
			
			print("\nEnter 3 Year Cycles For Description, more than 1 - year cycle!")
			c1 = int(input("1/3 >> "))
			if c1 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			# Starting from the next (number of descriptions - 1) inputs, it will validate if each cycles has same values as the previous inputs or not.
			c2 = int(input("2/3 >> "))
			if c2 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()

			c3 = int(input("3/3 >> "))
			if c3 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c3 == c2:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
		
			
			# Result, including of the calculation result from the user inputs
			print("\n\n")
			print(year)
			print("\n")
			print("Starts on",calendar.day_name[firstday],
			", January 1st ,",year,"(00:00:00)")
			print("And Ending On",calendar.day_name[lastday],", December 31st ,",year,"(23:59:59)")
			print("\n")
			print("year no.",year+1)
			print("year no.",((year%c1)+1),"of the ",c1,"- year cycle no.",(year//c1)+1)
			print("year no.",((year%c2)+1),"of the ",c2,"- year cycle no.",(year//c2)+1)
			print("year no.",((year%c3)+1),"of the ",c3,"- year cycle no.",(year//c3)+1)

			repeater()
			
		elif desc == 2: # If it is 2, then 2 unique n - year cycles must be inputted by user
			
			print("\nEnter 2 Year Cycles For Description, more than 1 - year cycle!")
			c1 = int(input("1/2 >> "))
			if c1 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			print() # This input has to be unique than the first one
			c2 = int(input("2/2 >> "))
			if c2 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
			elif c2 == c1:
				choice = input("Cycle must be unique! Repeat?(y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()


			
			# Result, including of the calculation result from the user inputs
			print("\n\n")
			print(year)
			print("\n")
			print("Starts on",calendar.day_name[firstday],
			", January 1st, ",year,"(00:00:00)")
			print("And Ending On",calendar.day_name[lastday],", December 31st ,",year,"(23:59:59)")
			print("\n")
			print("year no.",year+1)
			print("year no.",((year%c1)+1),"of the ",c1,"- year cycle no.",(year//c1)+1)
			print("year no.",((year%c2)+1),"of the ",c2,"- year cycle no.",(year//c2)+1)
			
			repeater()
			
			
		elif desc == 1: # If it is only 1, just input the desired year-cycle to calculate.
			
			print("\nEnter a Year Cycle For Description, more than 1 - year cycle!")
			c1 = int(input("1/1 >> "))
			if c1 < 2:
				choice = input("Cycle must be at least 2! Repeat? (y [for repeat]/any key[to go back to menu]) >> ")
				if choice == 'y':
					menu2()
				else:
					main()
		
			print("\n\n")
			print(year)
			print("\n")
			print("Starts on",calendar.day_name[firstday],
			", January 1st ,",year,"(00:00:00)")
			print("And Ending On",calendar.day_name[lastday],", December 31st ,",year,"(23:59:59)")
			print("\n")
			print("year no.",year+1)
			print("year no.",((year%c1)+1),"of the ",c1,"- year cycle no.",(year//c1)+1)
			
			repeater()
		
		elif desc > 5 or desc < 1: #If number of description that inputted by user exceeds the limit or less than 1.
			choice = input("You have to input and up to 5 unique year descriptions! Try Again? (y [for repeat] / any key[to go back to menu]) >> ")
			if choice == 'y':
				menu2()
			else:
				main()
		repeater()
	except: #If the input is not a number or no input has been submitted
		os.system('clear')
		repeater()

# If user entered '3' and hit enter then execute this menu in menu3 function.
def menu3():
	try:
		os.system('clear')
		print("3. New n - year cycle's eve") # Show the name of the menu each operation
		print("\n")
		cycleset = int(input("Input Set of Years per Cycle (more than 0) >> ")) # User input for set of years per each cycle

		if cycleset < 1: # If user input was less than 1, than prompt if user wants to try again or not
			print("Cycle must be at least 1!\n")
			x = input("Press y and enter to try again, or any key plus enter to return to main menu! >> ")
			if x == 'y':
				menu3()
			else:
				main()
		
		cycleno = int(input("Input Cycle no. >> ")) # User freely input what cycle will be determined

		# Get the 31st December of the calculated year, followed by the next day (1st January) on the next year.
		b1 = (cycleno-1)*cycleset - 1 
		e1 = b1 + 1
		begin1 = calendar.weekday((b1),12,31)
		end1 = calendar.weekday((e1),1,1) 

		print("\nThe turn of",cycleset,"- year cycle no. ",cycleno-1,"to no.",cycleno,"commences on")
		print(">>>",calendar.day_name[begin1],", December 31st ,",b1)
		print("\n(Ordinalized as Year No.",b1+1,")")
		print("\n\nAnd Bring The New ",cycleset,"- year cycle no. ",cycleno,"on")
		print(">>>",calendar.day_name[end1],", January 1st ,",e1)
		print("\n(Ordinalized as Year No.",e1+1,")")
		repeater()
	except: # If User Input was not a number or either none
		os.system('clear')
		repeater()

# If user entered '4' and hit enter then execute this menu in menu4 function.
def menu4():
	try:
		os.system('clear') # clear the screen first
		print("4. Calendar Maker") # Show the name of the menu each operation
		print("\n")

		#At the beginning of the operation, user can pick how will the calendar will be calculated
		print("You can Select 2 Options! Pick One You Like! (Ignore the word \"None\" at the end of the calendar!)")
		print("1. Manual Input")
		print("2. By format (Cycle_no.-Year_no.) of n -  year cycle")
		
		sel = input("\nGo Ahead! >> ")
		
		if sel == '1': # If user wants to check the calendar manually then user just enter the year and the user desired first day of the week
			w = int(input("\nEnter Year >> "))
			print("\n\n0 = Saturday, 1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday")
			d = input("\nEnter Starting day of the week! >> ")
			
			# If user entered 0 as the starting day of the week, the calendar will have the first day of the week as Saturday, 1 for Sunday, 2 for Monday, and so on until 6 for Friday.

			#This also aligned with its 1st January of the origin year , year 0 , which falls on Saturday

			if d == '0':
				c = calendar.setfirstweekday(calendar.SATURDAY)
			elif d == '1':
				c = calendar.setfirstweekday(calendar.SUNDAY)
			elif d == '2':
				c = calendar.setfirstweekday(calendar.MONDAY)
			elif d == '3':
				c = calendar.setfirstweekday(calendar.TUESDAY)
			elif d == '4':
				c = calendar.setfirstweekday(calendar.WEDNESDAY)
			elif d == '5':
				c = calendar.setfirstweekday(calendar.THURSDAY)
			elif d == '6':
				c = calendar.setfirstweekday(calendar.FRIDAY)
			else: # If the first day of the week is out of range from 1 to 7, than prompt if user wants to try again or not
				print("\n")
				print("0 - 6 Only!")
				choice2 = input("\nTry Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					menu4()
				else:
					main()
			print("\n")
			print(calendar.prcal(w)) # Print the whole calendar of the user inputted year with format of three months each line
		elif sel == '2': # If user wants to find a calendar based on the i-th year of the n - year cycle
			x = int(input("\n\nEnter no. of n - year cycle! (more than 0!) >> "))
			if x < 1: # If the year cycle is less than 1, then prompt the user to try again or not
				print("\n")
				print("Must be more than 0!")
				choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					menu4()
				else:
					main()

			y = int(input("Enter Cycle no. >> ")) # Enter the desired i-th set of the cycle

			# print the start of the cycle, last year of the cycle

			print("\n\nThis cycle starts from",x*(y-1))
			print("(Ordinalized as Year No.",x*(y-1)+1,")")
			print("\n\nAnd ends in",x*(y-1)+x-1)
			print("(Ordinalized as Year No.",x*(y-1)+x,")") 
			print("\n")
			print("Enter Year no. of the cycle! (Must be from 1 to ",x,"!)") # Enter the j-th year of the i-th cycle from range 1 to the user inputted year cycles.
			z = int(input(">> "))
			if z < 1 or z > x: # If the j-th year is less than one or exceeded the user inputted year cycles, prompt for try again or not
				print("Must be in range 1 to",x,"!")
				print("Try Again? (y[for repeat] / any key to main menu) >> ")
				choice2 = input()
				if choice2 == 'y':
					menu4()
				else:
					main()

			res = ((y-1)*x)+z-1 # Calculate the resulting year from the user inputs
			print("\n")
			# Print the result that corresponds the last calculation
			 
			print("\n\nThe year is ",res,"!")
			print("(Ordinalized as Year No.",res+1,")")

			print("\n\n0 = Saturday, 1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday")
			d = input("\nEnter Starting day of the week! >> ")
			# If user entered 0 as the starting day of the week, the calendar will have the first day of the week as Saturday, 1 for Sunday, 2 for Monday, and so on until 6 for Friday.

			#This also aligned with its 1st January of the origin year , year 0 , which falls on Saturday 
			
			if d == '0':
				c = calendar.setfirstweekday(calendar.SATURDAY)
			elif d == '1':
				c = calendar.setfirstweekday(calendar.SUNDAY)
			elif d == '2':
				c = calendar.setfirstweekday(calendar.MONDAY)
			elif d == '3':
				c = calendar.setfirstweekday(calendar.TUESDAY)
			elif d == '4':
				c = calendar.setfirstweekday(calendar.WEDNESDAY)
			elif d == '5':
				c = calendar.setfirstweekday(calendar.THURSDAY)
			elif d == '6':
				c = calendar.setfirstweekday(calendar.FRIDAY)
			else: # If the first day of the week is out of range from 1 to 7, than prompt if user wants to try again or not
				print("\n")
				print("0 - 6 Only!")
				choice2 = input("\nTry Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					menu4()
				else:
					main()
			
			print("\n")
			print(calendar.prcal(res)) # Print the whole calendar of the resulting year with format of three months each line
		repeater()
	except:
		os.system('clear')
		repeater()

# If user entered '5' and hit enter then execute this menu in menu5 function.
def menu5():
	try:
		os.system('clear') # clear the Screen First
		print("5. Get date in New Format") # Show the name of the menu each operation
		print("\n")
		a = int(input("Enter Year >> ")) # Firstly user input the desired year
		ab = int(input("\nEnter Month >> ")) # User input the month of the desired year from month 1 to 12 (January - December)
		if ab < 1 or ab > 12: # If the month number is less than 1 or more than 12, than prompt for try again or not
			print("\nMonth must be in range of January(1) to December(12)!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		abc = int(input("Enter Date >> ")) # Enter specified date to calculate!

		# Date Validation corresponding to the month that inputted by user, for month 2 (February) two validations occured due to leap year validation 

		# So if the corresponding year number was not a leap year but user entered 29 as a date in February, it automatically prompt for try again or not.
		if ab == 1 and (abc > 31 or abc < 1):
			print("\nJanuary Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		elif ab == 2 and (a%400 != 0 and a%100==0) and (abc > 28 or abc < 1):
			print("\nFebruary Must Be 1 - 28 in Common Year!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		elif ab == 2 and (a%400 == 0 or a%4 == 0) and (abc > 29 or abc < 1):
			print("\nFebruary Must Be 1 - 29 in Leap Year!")
			print("Try Again? (y[for repeat] / any key to main menu)")
			choice2 = input()
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 3 and (abc > 31 or abc < 1):
			print("\nMarch Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 4 and (abc > 30 or abc < 1):
			print("\nApril Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 5 and (abc > 31 or abc < 1):
			print("\nMay Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 6 and (abc > 30 or abc < 1):
			print("\nJune Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 7 and (abc > 31 or abc < 1):
			print("\nJuly Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 8 and (abc > 31 or abc < 1):
			print("\nAugust Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 9 and (abc > 30 or abc < 1):
			print("\nSeptember Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 10 and (abc > 31 or abc < 1):
			print("\nOctober Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 11 and (abc > 30 or abc < 1):
			print("\nNovember Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()
		if ab == 12 and (abc > 31 or abc < 1):
			print("\nDecember Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()

		c = int(input("Enter Year Cycle (more than 0) >>  ")) # User input for desired year-cycle
		if c < 1: # If it is less than 1, than prompt for try again or not
			print("\nYear cycle must more than 0!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu5()
			else:
				main()

		# Find the name of the day from corresponding year, month, and the date
		day = calendar.weekday((a),ab,abc)
		showday = calendar.day_name[day]
		
		# Print the result
		print("\n\n")
		print("This cycle starts from",(a//c)*c)
		print("(Ordinalized as Year No.",((a//c)*c)+1,")")
		print("\n\nAnd ends in",((a//c)*c)+c-1)
		print("(Ordinalized as Year No.",((a//c)*c)+c,")")  
		print("\n\nThe year is ",a,"!")
		print("(Ordinalized as Year No.",a+1,")") 
		
		print("\n\n")
		print("\nmm/dd/yyyy Format :\n")
		print(showday, ", ",ab,".",abc,".",a)
		print(showday, ", ",ab,"-",abc,"-",a)
		print(showday, ", ",ab,"/",abc,"/",a)

		print("\ndd/mm/yyyy Format :\n")
		print(showday, ", ",abc,".",ab,".",a)
		print(showday, ", ",abc,"-",ab,"-",a)
		print(showday, ", ",abc,"/",ab,"/",a)

		print("\nyyyy/mm/dd Format :\n")
		print(a,".",ab,".",abc, "   ",showday)
		print(a,"-",ab,"-",abc, "   ",showday)
		print(a,"/",ab,"/",abc, "   ",showday)

		print("\n\nCardinal Format (Likewise completed years) :")
		print(c,".",((a//c)),".",(a%c),".",ab,".",abc,"   ",showday)
		print(c,"-",((a//c)),"-",(a%c),"-",ab,"-",abc,"   ",showday)
		print(c,"/",((a//c)),"/",(a%c),"/",ab,"/",abc,"   ",showday)
		print("\n")
		print(showday, "   ", abc,".",ab,".",(a%c),".",((a//c)),".",c)
		print(showday, "   ", abc,"-",ab,"-",(a%c),"-",((a//c)),"-",c)
		print(showday, "   ", abc,"/",ab,"/",(a%c),"/",((a//c)),"/",c)

		# The ordinalized format here is the same format as the cardinal format one
		# However, some of them will be shown 1 higher to describe the "j-th year of the i-th cycle"
		print("\n\nOrdinalized Format :")
		print("O",c,".",((a//c)+1),".",(a%c)+1,".",ab,".",abc,"   ",showday)
		print("O",c,"-",((a//c)+1),"-",(a%c)+1,"-",ab,"-",abc,"   ",showday)
		print("O",c,"/",((a//c)+1),"/",(a%c)+1,"/",ab,"/",abc,"   ",showday)
		print("\n")
		print(showday, "   ", abc,".",ab,".",(a%c)+1,".",((a//c)+1),".",c,"O")
		print(showday, "   ", abc,"-",ab,"-",(a%c)+1,"-",((a//c)+1),"-",c,"O")
		print(showday, "   ", abc,"/",ab,"/",(a%c)+1,"/",((a//c)+1),"/",c,"O")

		

		repeater()
	except:
		os.system('clear')
		repeater()

# If user entered '6' and hit enter then execute this menu in menu6 function.
def menu6():
	try:
		os.system('clear') # clear the screen first
		print("6. Convert year into New Format by (Cycle_no.-Year_no.)") # Show the name of the menu each operation
		print("\n")
		x = int(input("\n\nEnter no. of n - year cycle! (more than 0!) >> ")) # This will prompt user for inputting desired year cycle for calculation
		if x < 1: # While if the year-cycle that user input is less than 1, prompt for user to try again or not.
			print("\nMust be more than 0!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()

		y = int(input("Enter Cycle no. >> ")) # This will prompt the i-th cycle of the user inputted sets of years per cycle

		# Print the start of the cycle, last year of the cycle and the result that corresponds the last calculation
		print("\n\nThis cycle starts from",x*(y-1)+0)
		print("(Ordinalized as Year No.",x*(y-1)+1,")")
		print("\n\nAnd ends in",(x*(y-1)+x-1))
		print("(Ordinalized as Year No.",(x*(y-1)+x),")")   
		print("\n")
		print("Enter Year number of the cycle! (Must be from 1 to ",x,"!)") # Enter the j-th year of the i-th cycle from range 1 to the user inputted year cycles.
		z = int(input(">> "))
		
		if z < 1 or z > x: # If the j-th year is less than 1 or exceeded the user inputted year-cycles, then prompt to try again or not.
			print("\n Must be in range 1 to",x,"!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()

		showyear = x*(y-1)+z-1 # Calculate the resulting year
		print("\n\n")
		
		print("\n\nThe year is ",showyear,"!") #Here's the result which is the calculated yearm so it can be determined as leap year or not
		print("(Ordinalized as Year No.",showyear+1,")") 
		print("\n")

		#After the resulting year has determined
		ab = int(input("Enter Month >> ")) # User input the month of the desired year from month 1 to 12 (January - December)
		if ab < 1 or ab > 12: # If the month number is less than 1 or more than 12, than prompt for try again or not
			print("\nMonth must be in range of January(1) to December(12)!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		abc = int(input("Enter Date >> ")) # Enter specified date to calculate!

		# Date Validation corresponding to the month that inputted by user, for month 2 (February) two validations occured due to leap year validation 

		# So if the corresponding year number was not a leap year but user entered 29 as a date in February, it automatically prompt for try again or not.
		if ab == 1 and (abc > 31 or abc < 1):
			print("\nJanuary Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		elif ab == 2 and (showyear%400 != 0 and showyear%100==0) and (abc > 28 or abc < 1):
			print("\nFebruary Must Be 1 - 28 in Common Year!")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		elif ab == 2 and (showyear%400 == 0 or showyear%4 == 0) and (abc > 29 or abc < 1):
			print("\nFebruary Must Be 1 - 29 in Leap Year!")
			print("Try Again? (y[for repeat] / any key to main menu)")
			choice2 = input()
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 3 and (abc > 31 or abc < 1):
			print("\nMarch Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 4 and (abc > 30 or abc < 1):
			print("\nApril Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 5 and (abc > 31 or abc < 1):
			print("\nMay Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 6 and (abc > 30 or abc < 1):
			print("\nJune Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 7 and (abc > 31 or abc < 1):
			print("\nJuly Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 8 and (abc > 31 or abc < 1):
			print("\nAugust Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 9 and (abc > 30 or abc < 1):
			print("\nSeptember Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 10 and (abc > 31 or abc < 1):
			print("\nOctober Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 11 and (abc > 30 or abc < 1):
			print("\nNovember Must Be 1 - 30")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		if ab == 12 and (abc > 31 or abc < 1):
			print("\nDecember Must Be 1 - 31")
			choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
			if choice2 == 'y':
				menu6()
			else:
				main()
		
		#Get the name of the day based on calculations, and print the rest of the result.
		day1 = calendar.weekday(showyear,ab,abc)
		showday = calendar.day_name[day1]

		print("\nmm/dd/yyyy Format :")
		print(showday, ", ",ab,".",abc,".",showyear)
		print(showday, ", ",ab,"-",abc,"-",showyear)
		print(showday, ", ",ab,"/",abc,"/",showyear)

		print("\ndd/mm/yyyy Format :")
		print(showday, ", ",abc,".",ab,".",showyear)
		print(showday, ", ",abc,"-",ab,"-",showyear)
		print(showday, ", ",abc,"/",ab,"/",showyear)

		print("\nyyyy/mm/dd Format :")
		print(showyear,".",ab,".",abc, "   ",showday)
		print(showyear,"-",ab,"-",abc, "   ",showday)
		print(showyear,"/",ab,"/",abc, "   ",showday)

		print("\n\nCardinal Format (Likewise completed years) :")
		print(x,".",y-1,".",z-1,".",ab,".",abc,"   ",showday)
		print(x,"-",y-1,"-",z-1,"-",ab,"-",abc,"   ",showday)
		print(x,"/",y-1,"/",z-1,"/",ab,"/",abc,"   ",showday)
		print("\n")
		print(showday, "   ", abc,".",ab,".",z-1,".",y-1,".",x)
		print(showday, "   ", abc,"-",ab,"-",z-1,"-",y-1,"-",x)
		print(showday, "   ", abc,"/",ab,"/",z-1,"/",y-1,"/",x)

		print("\n\nOrdinalized Format :")
		print("O",x,".",y,".",z,".",ab,".",abc,"   ",showday)
		print("O",x,"-",y,"-",z,"-",ab,"-",abc,"   ",showday)
		print("O",x,"/",y,"/",z,"/",ab,"/",abc,"   ",showday)
		print("\n")
		print(showday, "   ", abc,".",ab,".",z,".",y,".",x,"O")
		print(showday, "   ", abc,"-",ab,"-",z,"-",y,"-",x,"O")
		print(showday, "   ", abc,"/",ab,"/",z,"/",y,"/",x,"O")
		repeater()
	except: # If user input is not a number or none of the value given
		os.system('clear')
		repeater()

def factors(x):
	distinct = 0 # This will be used as the number of divisors that divides the user inputted year 
	#The iteration will be run from 1 to square root of the user inputted year
	for i in range(1,int(math.sqrt(x))+1):
		if x%i == 0:
		    print(i,"-------",x//i)
		    if (x//i == i): #This happens when user inputted year is considered as the perfect square number
		    	distinct += 1
		    else:	
		    	distinct += 2
	
	print("\nTotal Distinct Year-Cycles ->",distinct)

# If user entered '7' and hit enter then execute this menu in menu7 function.
def menu7():
	try:
		os.system('clear') # clear the screen first
		print("7. All Factors of inputted Year") # Show the name of the menu each operation
		print("\n")
		print("\nWARNING!!!\n\nBig numbers cannot be handled faster! Are you sure want to do this??") # A Warning message because this operation deals with many iterations.
		warn = input(("Yes(y) or No(n)?? >> "))
		if warn == 'y':
			print("\nRead the results from (top-bottom) left to (bottom-top) right to get the sorted numbers!")
			print("Just ignore the \"None\" word at the end of total distinct year-cycles!")
			year = int(input("\nEnter year you wish to calculate! >> "))
			if year < 0: # If you entered the year that less than 0, then the result would still be the same
				fixyear = year*(-1)
			elif year > 0:
				fixyear = year
			day1 = calendar.weekday(year,1,1)
			daylast = calendar.weekday(year,12,31)
			d_name1 = calendar.day_name[day1]
			d_namelast = calendar.day_name[daylast]
			
			#First year of the first cycle of any year cycle is 0 
			if year == 0:
				print("\n\n")
				print(year,"Starts from",d_name1,", January 1st ,",year,"And lasts",d_namelast,", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")")
				print("\nIt is always new beginning of any year cycle!")
			elif year == -1:
				print("\n\n")
				print(year,"Starts from",d_name1,", January 1st ,",year,"And lasts",d_namelast,", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")")
				print("\nIn minus numbered years, it is always the last of any year cycle, but a new 1 - year cycle!")
			else: #If the year number is not 0 or -1, than it will print all the factors of the user inputted year
				print("\n\n")
				print(year,"Starts from",d_name1,", January 1st ,",year,"And lasts",d_namelast,", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")")
				print("\nIt is new beginning of n - year cycle as follows:")
				print(factors(fixyear)) #Calling factores function
				print("\nAnd the final/last year of n - year cycle:")
				print(factors(fixyear+1))
			repeater()

		elif warn == 'n':
			os.system('clear')
			main()
		else:
			os.system('clear')
			menu7()
		repeater()
	except: # If user input is not a number or no input has been given
		os.system('clear')
		repeater()

# If user entered '8' and hit enter then execute this menu in menu8 function.
def menu8():
	try:
		os.system('clear') # clear the screen first
		print("8. i-th Year of the Cycle") # Show the name of the menu each operation
		print("\n")
		n = int(input("Enter n - year cycles (more than 0)! >> ")) # Enter the set of years per cycle
		if n < 1: # If the user inputted year cycles is less than 1, than prompt for trying again or not
			x = input("Press y and enter to try again, or any key plus enter to return to main menu! >> ")
			if x == 'y':
				menu8()
			else:
				main()
		i = int(input("Enter the i-th cycle of the year cycle! >> "))
		print("\n")
		# This will print the first and last year of the cycle based on the set of years inputted by user
		print("This cycle starts from",n*(i-1))
		print("(Ordinalized as Year No.",n*(i-1)+1,")")
		print("\n\nAnd ends in",n*(i-1)+n-1)
		print("(Ordinalized as Year No.",n*(i-1)+n,")")
		print("\n")
		print("1 -",n,"!") 
		print("\n\n")
		j = int(input("Enter j-th year of the cycle >> ")) # Enter the corresponding j-th year of the cycle ranging from 1 to user inputted year cycles
		if j < 1 or j > n: # If the j-th year less than 1 or exceeded the user inputted year cycles..
			x = input("Press y and enter to try again, or any key plus enter to return to main menu! >> ")
			if x == 'y':
				menu8()
			else:
				main()
		#Calculate the first and last day of the resulting year, and print the rest of the result
		getdate1 = calendar.weekday((n*(i-1)) + (j-1),1,1) 
		getdate2 = calendar.weekday((n*(i-1)) + (j-1),12,31)
		dn1 = calendar.day_name[getdate1]
		dn2 = calendar.day_name[getdate2]
		print("\n\n")
		print("Known inputs:")
		print("n =",n)
		print("i =",i)
		print("j =",j)
		print("\n")
		print("J - constraints:")
		print(1,"<= j <=",n)
		print("\n")
		print("Result >> Year No.",j,"of",n,"- year cycle No.",i)
		print("\n\n")
		print("Formula >> n * [ i - 1 ] + [ j - 1 ]")
		print("\n")
		print(">>>",n,"* [",i,"- 1 ] + [",j,"- 1 ]")
		print(">>>",n,"* [",i-1,"] + [",j-1,"]")
		print(">>>","[",n*(i-1),"] + [",j-1,"]")
		print("\n")
		print(">>", (n*(i-1)) + (j-1))
		print(">>",dn1,", January 1st ,",(n*(i-1)) + (j-1),"-",dn2,", December 31st ,",(n*(i-1)) + (j-1))
		print("\n(Ordinalized as Year No.",(n*(i-1)) + (j-1)+1,")")

		repeater()
	except: # If user input is not a number or no input has been given
		os.system('clear')
		repeater()


# If user entered '9' and hit enter then execute this menu in menu9 function.
def menu9():
	try:
		os.system('clear') # clear the screen first
		print("9. Current cycle of the inputted year") # Show the name of the menu each operation
		print("\n")
		year = int(input("Enter year to calculate -> "))
		cycle = int(input("Enter number n - year cycles to determine (more than 0!) -> "))
		if cycle < 1: # If year cycle is less than 1
			print("Cycle Must Be More than 0!")
			x = input("Try Again? (y for yes and other key to menu) >> ")
			if x == 'y' or x == 'Y':
				menu9()
			else:
				main()

		#Calculate and automatically specify where the year belongs to the specified cycle
		cnoa = (year//cycle) + 1
		startA = (cnoa-1)*cycle
		endA = (cnoa*cycle) - 1
		getdate1 = calendar.weekday(year,1,1) 
		getdate2 = calendar.weekday(year,12,31)
		dn1 = calendar.day_name[getdate1]
		dn2 = calendar.day_name[getdate2]

		
		print("\n\n")
		print("--> You entered year ->",year)
		print("\n(Ordinalized as Year No.",year+1,")")
		print("\n--> You want to check where that year in the group, based on",cycle,"- year cycle")
		print("\n")
		print(year,"is in the group of the",cycle,"- year cycle of:")
		print(">>",dn1,", January 1st ,",year,"-",dn2,", December 31st ,",year)
		print("\n\n")
	
		print(">> Previous Cycle No:",cnoa-1)
		print(">> Previous Ranged Years ->      ",startA-cycle,"-",endA-cycle)
		print("(Ordinalized as Year No.",startA-cycle+1,"-",endA-cycle+1,")")
		print("\n")
		print(">> Current Cycle No:",cnoa)
		print(">> Current Ranged Years ->      ",startA,"-",endA)
		print("(Ordinalized as Year No.",startA+1,"-",endA+1,")")
		print(">> Current year number in this cycle for year",year,"is ->  ",((year)%cycle)+1,"of",cycle)
		print("\n")
		print(">> Next Cycle No:",cnoa+1)
		print(">> Next Ranged Years ->      ",startA+cycle,"-",endA+cycle)
		print("(Ordinalized as Year No.",startA+cycle+1,"-",endA+cycle+1,")")

		repeater()
	except: # If user input is not a number or no input has been given
		os.system('clear')
		repeater()

# If user entered '0' and hit enter then execute this menu in menu0 function.
def menu0():
	try:
		os.system('clear') # clear the screen first
		print("0. Day difference between Gregorian Calendar and Julian Calendar") # Show the name of the menu each operation
		print("\n")
		year = int(input("Enter year >> "))
		result = -2 # The result is -2 means the default of Gregorian calendar is 2 days later than the preceeding Julian calendar
		# Finding difference of Gregorian Calendar and Julian Calendar in terms of days
		fourhundredyc = (year//400)*3
		remainder = year%400
		total = fourhundredyc + result + remainder//100
		if total < 0:
			if year%400 == 100 or year%400 == 200 or year%400 == 300:
				print("\n")
				print((total*-1)+1,"days ahead of Gregorian Calendar until End of February")
				print("\n")
				print((total*-1),"days ahead of Gregorian Calendar At The start of March")
			else:
				print(total*-1,"days ahead of Gregorian Calendar") # For years less than 200
		elif total == 0:
			if year%400 == 100 or year%400 == 200 or year%400 == 300:
				print("\n")
				print((total)-1,"days ahead of Julian Calendar until End of February")
				print("\n")
				print((total),"days ahead of Julian Calendar At The start of March")
			else:
				print("\n")
				print("Same as Julian Calendar") # This happens on years 201 - 299
		elif total > 0:
			if year%400 == 100 or year%400 == 200 or year%400 == 300:
				print("\n")
				print((total)-1,"days ahead of Julian until End of February")
				print("\n")
				print((total),"days ahead of Julian Calendar At The start of March")
			else:
				print("\n")
				print(total,"days ahead of Julian Calendar") # For years 300 and above
		repeater()
	except: # If user input is not a number or no input has been given
		os.system('clear')
		repeater()

# If user entered '!' and hit enter then execute this menu in yearindexing function.
def yearindexing():
	try:
		os.system('clear') # clear the screen first
		print("!. Year Indexing!\n") # Show the name of the menu each operation
		#It also features four selections, the actual purpose of this menu is to list every perfect 400 - year cycle list.
		print("1. 400-year cycle indexing, or")
		print("2. Custom-year cycle indexing, or")
		print("3. User defined input [from year x to year y] listing, or with the")
		print("4. User defined input [from first year x to until y-th year since x] listing")
		print("\n")
		print("For option(s) 2, 3 and 4, don't enter number too big to save your time!")
		sel = input("\nYour selection here! (Default : 1) >> ")
		if sel == "1":
			print("\nDefault: ",(2020//400)+1) # The default is what i-th cycle of this year belongs to the 400 - year cycle
			x = int(input("Enter i-th 400-year cycle to find out! >> "))
			# Print the result
			print("\nResult:\n")
	
			for year in range ((x-1)*400,x*400):
				l1 = calendar.weekday(year,1,1)
				l2 = calendar.weekday(year,12,31)
				print("[*]",(year%400)+1)
				print(calendar.day_name[l1],", January 1st ,",year,"-",calendar.day_name[l2],", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")\n")
		elif sel == "2":
			print("\n")
			w = int(input("Enter n-year cycle (more than 0!)>> "))
			if w < 1:
				print("Cycle must be more than 0!")
				x = input("Try Again? (y for yes and other key to menu) >> ")
				if x == 'y' or x == 'Y':
					yearindexing()
				else:
					main()
			print("\nDefault: ",(2020//w)+1) # The default is what i-th cycle of this year belongs to the n - year cycle
			x = int(input("Enter i-th cycle of n-year cycle to find out! >> "))
			print("\nResult:\n")
	
			for year in range ((x-1)*w,x*w):
				l1 = calendar.weekday(year,1,1)
				l2 = calendar.weekday(year,12,31)
				print("[*]",(year%w)+1)
				print(calendar.day_name[l1],", January 1st ,",year,"-",calendar.day_name[l2],", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")\n")
		elif sel == "3":
			print("\n")
			x = int(input("Enter first year to calculate >> "))
			y = int(input("Enter last year to calculate >> "))
			for year in range (x,y+1):
				l1 = calendar.weekday(year,1,1)
				l2 = calendar.weekday(year,12,31)
				print("[*]",(year-x+1))
				print(calendar.day_name[l1],", January 1st ,",year,"-",calendar.day_name[l2],", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")\n")
		elif sel == "4":
			print("\n")
			x = int(input("Enter first year to calculate >> "))
			x1 = int(input("Enter Number of years for the list >> "))
			y = x-1+x1
			for year in range (x,y+1):
				l1 = calendar.weekday(year,1,1)
				l2 = calendar.weekday(year,12,31)
				print("[*]",(year-x+1))
				print(calendar.day_name[l1],", January 1st ,",year,"-",calendar.day_name[l2],", December 31st ,",year)
				print("(Ordinalized as Year No.",year+1,")\n")

		else:

			x = input("Try Again? (y for yes and other key to menu) >> ")
			if x == 'y' or x == 'Y':
				yearindexing()
			else:
				main()
		
		repeater()
	except: # If user input is not number or no input given
		os.system('clear')
		repeater()


	# Extension Menu Functions

# If user entered '9a' or '9A' and hit enter then execute this menu in ext1 function.
def ext1():
	try:
		os.system('clear') #clear the screen first
		print("9a. Calculate the next and past periods based on an n - year cycle") # Show the name of the menu each operation
		print("\n\n")
		sel = input("By direct enter i-th cycle (x) or by manually enter year to detect the cycle automatically (y) ? >> ")
		if sel == "x" or sel == "X": 
			print("\n")
			y = int(input("Enter n - year cycle (more than 0!) >> ")) #10
			if y < 1:
				print("Cycle must be more than 0!")
				choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					ext1()
				else:
					main()

			first = int(input("Enter current i-th cycle! >> "))
			startcurrent = (first - 1) * y
			endcurrent = (first - 1) * y + (y-1) 
			getdate1 = calendar.weekday(startcurrent,1,1) 
			getdate2 = calendar.weekday(endcurrent,12,31)
			dn1 = calendar.day_name[getdate1]
			dn2 = calendar.day_name[getdate2]
			#Print the first and last day of the current cycle
			print("\n\n! Current Cycle is:\n")
			print("[",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")
			# Every 400 cycles it always repeats at the same format but with the different year
			nextcycle = int(input("Enter number of next cycle(s) ranges (1 - 400) >> ")) 
			if nextcycle < 1 or nextcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext1()
				else:
					main()

			pastcycle = int(input("Enter number of past cycle(s) ranges (1 - 400) >> ")) #10
			if pastcycle < 1 or pastcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext1()
				else:
					main()

			print("\n\n<<< Past Cycles / Periods:\n")
			for z in range (-(pastcycle),0):
					z1 = calendar.weekday(startcurrent+(z*y),1,1)
					z2 = calendar.weekday(endcurrent+(z*y),12,31)
					print(z,". [",first+z,"]",calendar.day_name[z1],", January 1st ,",startcurrent+(z*y),"-",calendar.day_name[z2],", December 31st ,",endcurrent+(z*y))
					print("(Ordinalized as year no.",startcurrent+(z*y)+1,"-",endcurrent+(z*y)+1,")")
					print("\n")

			print("\n\n! Current Cycle is:\n")
			print("0 . [",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")

			print("\n\n>>> Next Cycles / Periods:")
			for x in range (1,nextcycle+1):
					l1 = calendar.weekday(startcurrent+(x*y),1,1)
					l2 = calendar.weekday(endcurrent+(x*y),12,31)
					print(x,". [",first+x,"]",calendar.day_name[l1],", January 1st ,",startcurrent+(x*y),"-",calendar.day_name[l2],", December 31st ,",endcurrent+(x*y))
					print("(Ordinalized as year no.",startcurrent+(x*y)+1,"-",endcurrent+(x*y)+1,")")
					print("\n")
			repeater()

		elif sel == "y" or sel == "Y":
			print("\n")
			year = int(input("Enter Year >> "))
			y = int(input("Enter n - year cycle (more than 0!) >> "))
			if y < 1:
				print("Cycle must be more than 0!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext1()
				else:
					main()

			first = (year//y) + 1
			startcurrent = (first - 1) * y
			endcurrent = (first - 1) * y + (y-1) 
			getdate1 = calendar.weekday(startcurrent,1,1) 
			getdate2 = calendar.weekday(endcurrent,12,31)
			dn1 = calendar.day_name[getdate1]
			dn2 = calendar.day_name[getdate2]

			#Print the first and last day of the current cycle
			print("\n\n! Current Cycle is:\n")
			print("[",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")
			nextcycle = int(input("Enter number of next cycle(s) ranges (1 - 400) >> "))
			if nextcycle < 1 or nextcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext1()
				else:
					main()

			pastcycle = int(input("Enter number of past cycle(s) ranges (1 - 400) >> "))
			if pastcycle < 1 or pastcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext1()
				else:
					main()

			# Every 400 cycles it always repeats at the same format but with the different year
			print("\n\n<<< Past Cycles / Periods:\n")
			for z in range (-(pastcycle),0):
					z1 = calendar.weekday(startcurrent+(z*y),1,1)
					z2 = calendar.weekday(endcurrent+(z*y),12,31)
					print(z,". [",first+z,"]",calendar.day_name[z1],", January 1st ,",startcurrent+(z*y),"-",calendar.day_name[z2],", December 31st ,",endcurrent+(z*y))
					print("(Ordinalized as year no.",startcurrent+(z*y)+1,"-",endcurrent+(z*y)+1,")")
					print("\n")

			print("\n\n! Current Cycle is:\n")
			print("0 . [",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")

			print("\n\n>>> Next Cycles / Periods:")
			for x in range (1,nextcycle+1):
					l1 = calendar.weekday(startcurrent+(x*y),1,1)
					l2 = calendar.weekday(endcurrent+(x*y),12,31)
					print(x,". [",first+x,"]",calendar.day_name[l1],", January 1st ,",startcurrent+(x*y),"-",calendar.day_name[l2],", December 31st ,",endcurrent+(x*y))
					print("(Ordinalized as year no.",startcurrent+(x*y)+1,"-",endcurrent+(x*y)+1,")")
					print("\n")
			repeater()

		else: #If it the user input is not x or y (lowercase or not)
			print("Wrong argument!")
			print("Try Again? (y[for repeat] / any key to main menu)")
			choice2 = input()
			if choice2 == 'y':
				ext1()
			else:
				main()



	except: # If user input is not number or no input given
		os.system('clear')
		repeater()

# If user entered '9b' or '9B' and hit enter then execute this menu in ext2 function.
def ext2():
	try:
		os.system('clear')
		print("9b. Years left until the next specific calendrical n - cycle\n\n")
		year = int(input("Enter Year >> ")) #2020
		cycle = int(input("Enter n - year cycle (more than 0) >> ")) #10
		if cycle < 1:
			print("Cycle must be more than 0!")
			print("Try Again? (y[for repeat] / any key to main menu)")
			choice2 = input()
			if choice2 == 'y':
				ext2()
			else:
				main()

		first = (year//cycle) + 1
		startcurrent = (first - 1) * cycle
		endcurrent = (first - 1) * cycle + (cycle-1) 
		getdate1 = calendar.weekday(startcurrent,1,1) 
		getdate2 = calendar.weekday(endcurrent,12,31)
		getdate3 = calendar.weekday(startcurrent+cycle,1,1) 
		getdate4 = calendar.weekday(endcurrent+cycle,12,31)
		dn1 = calendar.day_name[getdate1]
		dn2 = calendar.day_name[getdate2]
		dn3 = calendar.day_name[getdate3]
		dn4 = calendar.day_name[getdate4]

		#Calculate how many days left to next cycle
		print("\nCurrent Cycle has years:")
		print("[",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
		print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")

		print("\nNext One is:")
		print("[",first+1,"]",dn3,", January 1st ,",startcurrent+cycle,"-",dn4,", December 31st ,",endcurrent+cycle)
		print("(Ordinalized as year no.",startcurrent+cycle+1,"-",endcurrent+cycle+1,")")

		print("\n\nNext cycle from this year",year,", to next cycle",startcurrent+cycle)
		print("Is less or equal to:",(startcurrent+cycle) - year,"year(s)")
		
		print("\n")

		repeater()
		

	except: # If the user input is not a number or no input given
		os.system('clear')
		repeater()

def ext3():
	try:
		os.system('clear') #clear the screen first
		print("9c. Calculate the next and past occurences of the i-th year of the particular cycle") # Show the name of the menu each operation
		print("\n\n")
		sel = input("By direct enter i-th cycle (x), or by manually enter year to detect the cycle automatically (y),\nor direct detect the cycle along with the i-th year of the cycle (z) ? >> ")
		if sel == "x" or sel == "X": 
			print("\n")
			y = int(input("Enter n - year cycle (more than 0!) >> ")) #10
			if y < 1:
				print("Cycle must be more than 0!")
				choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					ext3()
				else:
					main()

			first = int(input("Enter current i-th cycle! >> "))
			startcurrent = (first - 1) * y
			endcurrent = (first - 1) * y + (y-1) 
			getdate1 = calendar.weekday(startcurrent,1,1)
			getdate2 = calendar.weekday(endcurrent,12,31)
			dn1 = calendar.day_name[getdate1]
			dn2 = calendar.day_name[getdate2]
			#Print the first and last day of the current cycle
			print("\n\n! Current Cycle is:\n")
			print("[",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")

			
			print("From 1 up to",y,",")
			print("\n")
			detect = int(input("Please enter i-th year of the cycle! >> "))
			if detect < 1 or detect > y:
				print("\nOut of range!\n")
				choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					ext3()
				else:
					main()

			getdate1a = calendar.weekday(startcurrent+detect-1,1,1) 
			getdate2a = calendar.weekday(startcurrent+detect-1,12,31)
			dn1a = calendar.day_name[getdate1a]
			dn2a = calendar.day_name[getdate2a]
			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("[",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")




			# Every 400 cycles it always repeats at the same format but with the different year
			nextcycle = int(input("Enter number of next occurence(s) from ranges (1 - 400) >> ")) 
			if nextcycle < 1 or nextcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			pastcycle = int(input("Enter number of past occurence(s) ranges (1 - 400) >> ")) #10
			if pastcycle < 1 or pastcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			print("\n\n<<< Past occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for z in range (-(pastcycle),0):
					z1 = calendar.weekday(startcurrent+(z*y)+detect-1,1,1)
					z2 = calendar.weekday(startcurrent+(z*y)+detect-1,12,31)
					print(z,". [",first+z,"]",calendar.day_name[z1],", January 1st ,",startcurrent+(z*y)+detect-1,"-",calendar.day_name[z2],", December 31st ,",startcurrent+(z*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(z*y)+detect,")")
					print("\n")

			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("0 . [",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1	)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")

			print("\n\n>>> Next occurences as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for x in range (1,nextcycle+1):
					l1 = calendar.weekday(startcurrent+(x*y)+detect-1,1,1)
					l2 = calendar.weekday(startcurrent+(x*y)+detect-1,12,31)
					print(x,". [",first+x,"]",calendar.day_name[l1],", January 1st ,",startcurrent+(x*y)+detect-1,"-",calendar.day_name[l2],", December 31st ,",startcurrent+(x*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(x*y)+detect,")")
					print("\n")
			repeater()

		elif sel == "y" or sel == "Y":
			print("\n")
			year = int(input("Enter Year >> "))
			y = int(input("Enter n - year cycle (more than 0!) >> "))
			if y < 1:
				print("Cycle must be more than 0!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			first = (year//y) + 1
			startcurrent = (first - 1) * y
			endcurrent = (first - 1) * y + (y-1) 
			getdate1 = calendar.weekday(startcurrent,1,1)
			getdate2 = calendar.weekday(endcurrent,12,31)
			dn1 = calendar.day_name[getdate1]
			dn2 = calendar.day_name[getdate2]

			#Print the first and last day of the current cycle
			print("\n\n! Current Cycle is:\n")
			print("[",first,"]",dn1,", January 1st ,",startcurrent,"-",dn2,", December 31st ,",endcurrent)
			print("(Ordinalized as year no.",startcurrent+1,"-",endcurrent+1,")")
			print("\n")
			print("From 1 up to",y,",")
			print("\n")
			detect = int(input("Enter i-th year of the cycle! >> "))
			if detect < 1 or detect > y:
				print("\nOut of range!\n")
				choice2 = input("Try Again? (y[for repeat] / any key to main menu) >> ")
				if choice2 == 'y':
					ext3()
				else:
					main()

			getdate1a = calendar.weekday(startcurrent+detect-1,1,1) 
			getdate2a = calendar.weekday(startcurrent+detect-1,12,31)
			dn1a = calendar.day_name[getdate1a]
			dn2a = calendar.day_name[getdate2a]
			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("[",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")




			# Every 400 cycles it always repeats at the same format but with the different year
			nextcycle = int(input("Enter number of next occurence(s) from ranges (1 - 400) >> ")) 
			if nextcycle < 1 or nextcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			pastcycle = int(input("Enter number of past occurence(s) ranges (1 - 400) >> ")) #10
			if pastcycle < 1 or pastcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			print("\n\n<<< Past occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for z in range (-(pastcycle),0):
					z1 = calendar.weekday(startcurrent+(z*y)+detect-1,1,1)
					z2 = calendar.weekday(startcurrent+(z*y)+detect-1,12,31)
					print(z,". [",first+z,"]",calendar.day_name[z1],", January 1st ,",startcurrent+(z*y)+detect-1,"-",calendar.day_name[z2],", December 31st ,",startcurrent+(z*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(z*y)+detect,")")
					print("\n")

			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("0 . [",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1	)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")

			print("\n\n>>> Next occurences as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for x in range (1,nextcycle+1):
					l1 = calendar.weekday(startcurrent+(x*y)+detect-1,1,1)
					l2 = calendar.weekday(startcurrent+(x*y)+detect-1,12,31)
					print(x,". [",first+x,"]",calendar.day_name[l1],", January 1st ,",startcurrent+(x*y)+detect-1,"-",calendar.day_name[l2],", December 31st ,",startcurrent+(x*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(x*y)+detect,")")
					print("\n")
			repeater()

		elif sel == "z" or sel == "Z":
			print("\n")
			year = int(input("Enter Year >> "))
			y = int(input("Enter n - year cycle (more than 0!) >> "))
			if y < 1:
				print("Cycle must be more than 0!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			first = (year//y) + 1
			startcurrent = (first - 1) * y
			
			detect = (year%y) + 1
			getdate1a = calendar.weekday(startcurrent+detect-1,1,1) 
			getdate2a = calendar.weekday(startcurrent+detect-1,12,31)
			dn1a = calendar.day_name[getdate1a]
			dn2a = calendar.day_name[getdate2a]
			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("[",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")




			# Every 400 cycles it always repeats at the same format but with the different year
			nextcycle = int(input("Enter number of next occurence(s) from ranges (1 - 400) >> ")) 
			if nextcycle < 1 or nextcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			pastcycle = int(input("Enter number of past occurence(s) ranges (1 - 400) >> ")) #10
			if pastcycle < 1 or pastcycle > 400:
				print("Too much or too less!")
				print("Try Again? (y[for repeat] / any key to main menu)")
				choice2 = input()
				if choice2 == 'y':
					ext3()
				else:
					main()

			print("\n\n<<< Past occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for z in range (-(pastcycle),0):
					z1 = calendar.weekday(startcurrent+(z*y)+detect-1,1,1)
					z2 = calendar.weekday(startcurrent+(z*y)+detect-1,12,31)
					print(z,". [",first+z,"]",calendar.day_name[z1],", January 1st ,",startcurrent+(z*y)+detect-1,"-",calendar.day_name[z2],", December 31st ,",startcurrent+(z*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(z*y)+detect,")")
					print("\n")

			print("\n\n! Current occurence as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			print("0 . [",first,"]",dn1a,", January 1st ,",startcurrent+detect-1,"-",dn2a,", December 31st ,",startcurrent+detect-1	)
			print("(Ordinalized as year no.",startcurrent+detect,")")
			print("\n")

			print("\n\n>>> Next occurences as year no.",detect,"(or a",detect-1,"- remaindered year) of",y,"- year cycle is:\n")
			for x in range (1,nextcycle+1):
					l1 = calendar.weekday(startcurrent+(x*y)+detect-1,1,1)
					l2 = calendar.weekday(startcurrent+(x*y)+detect-1,12,31)
					print(x,". [",first+x,"]",calendar.day_name[l1],", January 1st ,",startcurrent+(x*y)+detect-1,"-",calendar.day_name[l2],", December 31st ,",startcurrent+(x*y)+detect-1)
					print("(Ordinalized as year no.",startcurrent+(x*y)+detect,")")
					print("\n")
			repeater()


		else: #If it the user input is not x or y (lowercase or not)
			print("Wrong argument!")
			print("Try Again? (y[for repeat] / any key to main menu)")
			choice2 = input()
			if choice2 == 'y':
				ext3()
			else:
				main()



	except: # If user input is not number or no input given
		os.system('clear')
		repeater()

#Calling the main function to start the program if it has a main function
if __name__ == '__main__':
 	main()