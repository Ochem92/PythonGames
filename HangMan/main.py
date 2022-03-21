
import random
from words import words

def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def playhangman():
    word = get_word(words)
    wordset = set(word)
    used_letters = set()
    counter = 6
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print("Please enjoy your game of hangman!\n")
    while len(wordset) > 0 and counter > 0:
        displayword = [char if char in used_letters else '_' for char in word]
        print(" ".join(displayword))
        print("You have used the following letters")
        print(" ".join(used_letters))
        uguess = input("Enter letter to guess:\n").upper()

        if uguess in alphabet - used_letters:
            used_letters.add(uguess)
            if uguess in wordset:
                wordset.remove(uguess)
                print("That word is correct!")
            else:
                counter -= 1
                print(f"\nSorry your letter is not in the word, you have {counter} tries left")
        elif uguess in used_letters:
            print("This letter has already been used")
        else:
            print("Invalid character")
    if counter == 0:
        print(f"You have lost. The word was {word}")
    else:
        print(f"Congrats you have won with {counter} tries remaining!")

playhangman()
input('Press ENTER to exit')










