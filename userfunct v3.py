def user_picks():
	picks = []
	mega_pick = []
	invalid_picks = []
	# accepted integers
	int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
	mega_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	while len(picks)!= 5:
		user_int = input('Enter an integer(1 - 47): ')
		
                # DELETE -->  for i in range(5): 
		# prompt the user to enter an number
		user_int = input('Enter an integer (1 - 47): ')
		#----try:
		# convert the entry to an integer
		user_int = int(user_int) 
		# type entered is an integer
                if type(user_int) == int:
				#-----try:
					if user_int not in int_range:
						print('Not in range!')
						invalid_picks.append(user_int)
						user_int = int(input('Enter an integer (1 - 47): '))

						# verify that the entry is in the accepted integers tuple
					elif user_int in int_range: 
							break                              
						# add it to the list of picks the user wants
							picks.append(user_int)
						# add it to the list of picks not valid
						
				except:
						print('Unknown exception!')
						#pass  
		# type entered is not an integer                                                       
		#----except ValueError as verr:		
			if type(user_int) != int:
		# add the entry to the list of invalid picks
				invalid_picks.append(user_int)
				print('Invalid type!', user_int)
				#user_int = int(input('Enter an integer (1 - 47): '))
			#print('Value error: ' + str(verr))
		if len(picks) == 5:
			print('User picks:', picks)
			print('\nInvalid choice:', invalid_picks)
