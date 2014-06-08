def user():
        picks = []
        double_entries = []
        n = int(input("Total entries: "))
        while len(picks)!= n:
                user_choice = input("Enter an integer: ")
                try:
                        if user_choice not in picks and isinstance(user_choice,int):
                                picks.append(user_choice)
                        elif user_choice in picks:
                                double_entries.append(user_choice)
                                valid_choice = int(input("Please choose a different integer: "))
                        else:
                                print("No comprende!")
                except TypeError:
                        valid_int = int(input("Please enter an integer between 1-47: "))
        print('PIcks:', picks)
        print('\nDouble entries:', double_entries)
user()
