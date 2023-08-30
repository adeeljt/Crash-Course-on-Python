# if statement intro example 1
def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at least 3 characters long")
    else:
        print ("Valid username")


hint_username("ADEEL")
