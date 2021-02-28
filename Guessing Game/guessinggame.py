print("Guessing Game")
import random
randomnumber = random.randint(1,9)
chances = 0
while chances < 5:
    number = int(input("Enter an number between 1-9"))
    if number == randomnumber:
     print("Congratulations.You won")
     break
    elif number < randomnumber:
       print("Your guess is wrong. Try again with a higher number")
    else: 
       print("Your guess is wrong. Try again with a lower number")  
    chances = chances + 1 
if chances > 5 :
    print("You are out of chances. YOU LOSE")
    