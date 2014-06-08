def user():
# store the numbers chosen
        picks = []
# store the mega number
        mega_pick = []
   # store the charcters not in the specified range
        invalid_picks = []
# user can only enter integers that are within this range
        int_range = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
# user can only enter an integer within this range for the mega number
        mega_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
        for i in range(1, 6):
                user_choice = None
                try:
                        user_choice = input('\n\tEnter an integer between(1 - 47): ')
                        user_choice = int(user_choice)
# check that the variable entered is an integer
                        if isinstance(user_choice, int):
                                print(user_choice, "is of type:", type(user_choice))
                except ValueError: # if an integer is not entered
                        print("\tNot an integer:", user_choice)
                        user_choice = input('\n\tEnter a valid integer between(1-47): ')
# convert the variable into an intger
                        user_choice = int(user_choice)
# make sure that the integer is within the accepted range of the int_range variable
 #               try:
#                                if user_int in int_range:

# call the function               
user()

