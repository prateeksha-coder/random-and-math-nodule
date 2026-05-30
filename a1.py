import random #importing module
playing = True #initialise
number = random.randint(10,20) #random in-built function   
while playing:
  guess = int(input("Give me your best guess! \n"))
  if number == guess:
    print("You win the game")
    print("The number was",number)
    break 
    
  else:
    print("Your guess isn't quite right, try again. \n")