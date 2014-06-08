def quick_picks(): # auto generated integers
        import random
        picks = []
        mega_pick = []
        for i in range(1, 6):
                nums = random.randint(1, 47)
                picks.append(nums)
        for i in range(1):
                mega_num = random.randint(1, 27)
                mega_pick.append(mega_num)
                print('\n\tQuick picks:','(',picks[0],')','(',picks[1],')','(',picks[2],')','(',picks[3],')','(',picks[4],')','\tMEGA:', '(',mega_pick[0],')')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def manual_picks(): # numbers chosen by the user
	picks = []
	mega_pick = []
	# user can only choose integers within this range for regular picks
	#int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
        # user can only choose an integer within this range for the mega choice
        #mega_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	for i in range(1, 6):
		choice = int(input("\n\tEnter an integer (1 -47):"))
		picks.append(choice)
	for i in range(1):
		mega_choice = int(input("\n\tEnter an integer (1 -27): "))
		mega_pick.append(mega_choice)
	print("\n\tUser picks:", '(',picks[0:5],')', "Mega Pick:", mega_pick[0])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	
##        while len(picks) != 5:
##                try:
##                        # for each_pick in range(5, 0, -1):
##                                chosen_integer = input("\n\tEnter an integer (1 - 47): ")               
### Convert the entry int o an integer
##                                chosen_integer = int(chosen_integer)
##                                print('\t------------------------------------')
### Make sure that the integer is within the accepted range of the int_range variable
##                                if chosen_integer in int_range:
##                                        picks.append(chosen_integer)
##                                else:
##                                        print('\n\t\t--- Not in range ---> ' + str(chosen_integer))
##                                        print('\n')
##                                        invalid_picks.append(chosen_integer)
##                except ValueError:
##                        print('\n\t\t--- Not a valid integer ---> ' + str(chosen_integer))
##                        invalid_picks.append(chosen_integer)
##                        if len(picks) == 5:
##                                for i in range(1):
##                                        try:
##                                                mega_integer = input('\n\t***** MEGA NUMBER - choose between (1 - 27): ')
##                # Convert the entry into an integer
##
##                                                mega_integer = int(mega_integer)
##                # Make sure that the integer is within the accepted range of the mega_range variable
##                                                if mega_integer in mega_range:
##                                                        mega_pick.append(mega_integer)
##                                                else:
##                                                        print('\n\t\t--- Not in range ---> ' + str(chosen_integer))
##                                                        print('\n')
##                                                        invalid_picks.append(mega_integer)
##                                        except ValueError:
##                                                print('\n\t\t--- Not a valid integer ---> ' +  str(mega_integer))
##                                                print('\n')
##                                                invalid_picks.append(mega_integer)
##                                                print('\n\n*** User picks: ',picks[0:5], 'MEGA NUMBER:', mega_pick[0])
##                                                print("\n\n\t\t$$$-Good Luck-$$$\t\tInvalid picks: ", invalid_picks)
##                                                if len(invalid_picks) == 0:
##                                                        print('\n----------------------------------------------\n\t\tInvalid picks: "[0]"')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
def welcome(): # Welcome the user to the program
# Greet the user
        print("""\t\t
--------------------------------
|Welcome to the Lottery Picker!|
--------------------------------
""")
        print('\n\t*** Must be at least 18 years old to claim any prize!')
        user_name = input("\n\tWhat is your name?: ")
        print('\n\tGood Luck, ', str(user_name))

# Beginning of program
welcome()
userChoice = None
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
while userChoice != 0: # Prompt the user to make a choice
        print('\n\t\tPlease make a selection:','\n\t\t-------------------------\n\t\t0. Exit\n\t\t1. Quick Picks\n\t\t2. Manual Picks\n')
        userChoice = int(input('\tChoice: '))
        if userChoice == 1: #Quick pick
                        quick_picks()
        elif userChoice == 2: # User pick
                        manual_picks()
        elif userChoice == 0: # Exit
                        input('\n\t\tPress the enter key to exit.')
        else:
                        print('\t\tInvalid choice!')



