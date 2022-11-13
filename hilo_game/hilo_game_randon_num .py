import random as r 

play_again = "Y"
while play_again == "Y":
      #Play Hilo
      random_num = r.randint(1, 300) # Random integer from 1 to 100

      guess = input ("Enter a number:") # is a sring

      while int(guess) != random_num: 
          print("Incorrect!")
          if int(guess) > random_num:
             print("Too high!")
          else:
             print("Too low!")
            
          guess = input("Enter a number: ") # is a string

      print("Congratulations! You got it") 
      play_again = input("Do you want to play again? (Y/N) ") 