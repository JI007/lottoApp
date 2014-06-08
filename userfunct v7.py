def user():
	picks = []
	mega_pick = []
	int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
	mega_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	double_entry = []
	for i in range(1, 6):
		try:
		# prompt the user to enter an integer within the int_range tuple
			user_entry = int(input("Enter an integer( between 1-47): "))
		# verify that the entry is of the 'integer' type
			if isinstance(user_entry, int):
				pass
			else:
				try:
					user_entry = int(input("Enter a valid integer: "))
		# if the entry is not an integer
				except ValueError as verr:
					print("Not an integer: ", verr)
					valid_entry = input("Enter a valid integer: ")
				except TypeError as terr:
					print("Not an integer: ", terr)
					valid_entry = input("Enter a valid integer: ")
				try:
		# verify that the entry is within the specified range
					if user_entry in int_range:
						print("In range!")
		# if the entry is not in the specified range
					else:
						print("Not in specified range!")
						valid_range = input("Enter an integer between (1-47): ")
		# make sure the users entry has not been entered more than once
					if user_entry not in picks:
						picks.append(user_entry)
		# if the entry has already been chosen by the user
					else:
						print("You chose this already!")
		# all of the users double entries are appended to this list
						double_entry.append(user_entry)
		# prompt the user to enter an integer that they have not chosen already
						user_entry = input("Enter an original integer: ")
		# ------------------------------------------------------------------------------------------------------------
		# Mega number
		for i in range(1):
			try:
			#prompt the user to enter an integer within mega_num tuple
				user_entry = int(input("Enter an integer (between 1-27): "))
				if isinstance(user_entry, int):
					pass
				else:
                                        try:
                                                user_entry = int(input("Enter an integer (between 1-27): "))        
                                        except ValueError as verr:
                                                print("Not an integer: ", verr)
                                                valid_entry = input("Enter a valid integer: ")																				print("type: integer!")
                                        except TypeError as terr:
                                                print("Not an integer: ", terr)
                                                valid_entry = input("Enter a valid integer: ")
                                        try:
                                                if user_entry in mega_num:
							print("In range!")
                                                        mega_pick.append(user_entry)
                                                else:
                                                        print("Not in specified range!")
                                                        valid_range = input("Enter an integer between (1-27): ")
                            print("User picks:", pIcks[0:5], "Mega: ", mega_pick[0])
                            print("\nDouble entries: ", double_entries[])
user()
