def user_picks():
	picks = []
	mega_pick = []
	invalid_picks = []
	# accepted integers
	int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
	mega_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
	while len(picks)!= 5:
		# prompt the user to enter an number
		user_int = int(input('Enter an integer(1 - 47): '))
		if user_int in int_range:
			picks.append(user_int)
		else:
			print('--Not in range--')
			invalid_picks.append(user_int)
	if len(picks) == 5:
		print('User picks: ', picks)
		print('Invalid picks: ', invalid_picks)
