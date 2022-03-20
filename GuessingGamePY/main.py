import random

def getrange():
    nrange = int(input("Enter max value for guessing game: \n"))
    return nrange

def user_guess(x):
    uguess = 0
    cnum = random.randint(0,x)
    counter = 0
    while uguess != cnum:
        uguess = int(input(f"Enter your guess between 0 and {x}: \n"))
        if uguess > cnum:
            print("Your guess is too high!")
            counter += 1
        elif uguess < cnum:
            print("Your guess is too low!")
            counter += 1
    print(f"You have guessed the correct number in {counter} attempts!")
    select_game()

#Feedback computer if result is correct, low, or high
#user enters c for correct, l for low and h for high
def comp_guess(x):
    #initalize feedback string, high and low values
    feedback = ''
    low_num = 1
    high_num = x
    counter = 1
    while feedback != 'c':
        cnum = random.randint(low_num, high_num)
        feedback = input(f"Computer has guessed {cnum}, is this correct? \n Yes = c, Too low = l , Too high = h \n").lower()
        if feedback == 'l':
            low_num = cnum + 1
            counter += 1
        elif feedback == 'h':
            high_num = cnum - 1
            counter += 1
    print(f"The computer has guessed your number in {counter} attempts")
    select_game()

def select_game():
    selection = int(input("Welcome to the guessing game!\nEnter 0 to exit\nEnter 1 to find the computers hidden number!\nEnter 2 to have have the computer find your hidden number!\n"))
    if selection == 1:
        print("Time to guess the computers hidden number!")
        return user_guess(getrange())
    elif selection == 2:
        print("Pick a hidden number for the computer to guess!")
        return comp_guess(getrange())
    elif selection == 0:
        pass
    else:
        print("Please enter an appropriate number")
        select_game()
try:
    select_game()
except:
    print("Sorry, Please enter an appropriate number")
    select_game()
print("Thanks for playing!")



