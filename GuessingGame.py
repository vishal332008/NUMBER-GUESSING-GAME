
import random


number = random.choice([1,2,3,4,5,6,7,8,9])

chances = 5

while chances>0:
    print(f"YOU HAVE {chances} CHANCES REMAINING")
    guess = int(input("TYPE THE GUESS : "))
    if guess==number:
        print("YOU WON!! It was the Correct Number")
        break
    elif guess>number:
        print(f"YOUR GUESS WAS TOO HIGH. TRY A NUMBER LOWER THAN {guess}")
        chances=chances-1
    elif guess<number:
        print(f"YOUR GUESS WAS TOO LOW. TRY A NUMBER HIGHER THAN {guess}")
        chances=chances-1
        
if chances==0:
    print("YOU HAVE JUST LOST. SAD :(")
