def user_picks():
	picks = []
	mega_pick = []
	invalid_picks = []
	# accepted integers
	int_range =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
	mega_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	while len(picks) != 5:
		user_int = input('Enter an integer between (1 - 47): ')
		try:
			user_int = int(user_int)
		except ValueError as verr:
			print('Value error: ' + str(verr))
			print(user_int, ': is not a valid entry!')
		try:
		#verify that the entry is in the accepted range
		                if user_int in int_range:
					picks.append(user_int)
		except:
			# user_int not in int_range
				invalid_picks.append(user_int)
		if len(picks) == 5:
			print('User picks: ', picks)
			print('Invalid choices: ', invalid_picks)
			

