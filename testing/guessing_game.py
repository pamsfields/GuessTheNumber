#Pam Fields ITEC 2905-01 Lab 1 Hello Python
#1/9/2018
# Problem 1 Guess the number
print("Guessing Game")

import random
# pulling random into code
def main():

    x = get_random_number()
    #setting up random number
    guess = get_guess
    #user input for game
    while guess != x:
        if guess < x:
            print("Your guess is too low.")
            input("Pick a number between 1 and 100 ")
            break
        else:
            print("Your guess is too high.")
            input("Pick a number between 1 and 100 ")
            break

        print("You got it right!")

def get_user_guess():
    return int(input("Pick a number between 1 and 100 "))

def get_random_number():
    return random.randint(1,100)

if __name__ == '__main__':
    main()
