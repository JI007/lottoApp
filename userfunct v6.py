def user_picks():
	# Declare and initialize main variables
	picks = []
	mega_pick = []
	invalid_picks = []
	

	#----------------------------------------------------------
	# Used to store the users choices
	picked_nums =[]
	# stores the count of valid integers chosen
	counter = 0
	#----------------------------------------------------------


	# Greet the user
	user_name = input("\nWhat is your name?: ")
	print('\nHappy Lottery Picking, ',user_name)
	print('\n*** Must be at least 18 years old to play!!!')
	# accepted integers
	int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
	mega_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	while len(picks) != 6:
		try:
			user_int = input("\n\tEnter an integer (1 - 47): ")
			# Convert the entry into an integer
			user_int = int(user_int)
			print('\t-------------------------------')
			# Make sure that the integer is within the accepted range of the int_range variable
			if user_int in int_range:
				picks.append(user_int)
			else:
				print('\n\t\t-- Not in range: ' + str(user_int))
				print('\n')
				invalid_picks.append(user_int)
		except ValueError:
			print('\n\t\t-- Not a valid integer: ' + str(user_int))
			print('\n')
			invalid_picks.append(user_int)
		if len(picks) == 6:
			for i in range(1):
				try:
					mega_choice = input('\n\t***** MEGA PICK - choose between (1 - 27): ')
					# Convert the entry into an integer
					mega_choice = int(mega_choice)
					# Make sure that the integer is within the accepted range of the mega_range variable
					if mega_choice in mega_range:
						mega_pick.append(mega_choice)
					else:
                        # Enter a "try/except" statement to handle the error.
						print('\n\t\t-- Not in range: ' + str(user_int))
						print('\n')
						invalid_picks.append(mega_choice)
				except ValueError:
					print('\n\t\t-- Not a valid integer: ' +  str(mega_choice))
					print('\n')
					invalid_picks.append(mega_choice)

                        # Write and exception to handle the index error of being out of range.
				print('\n\n*** User picks: ', picks[0:5], 'MEGA PICK:', mega_pick[0])
				print("\n\n\t\tGood Luck, ",user_name, '\t$ xxx,$$$,xxx')
				if len(invalid_picks) > 0:
					print('\n----------------------------------------------------------------------\n\tInvalid picks: ', invalid_picks)
				else:
					print('\n----------------------------------------------------------------------\n\tInvalid picks: "[0]"')
