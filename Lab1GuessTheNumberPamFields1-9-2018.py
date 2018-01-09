#Pam Fields ITEC 2905-01 Lab 1 Hello Python
#1/9/2018
# Problem 1 Guess the number
print("Guessing Game")

import random
# pulling random into code

x = random.randint(1,100)
#setting up random number
guess = int(input("Pick a number between 1 and 100 "))
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
