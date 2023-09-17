import random #I'm giving up on one lining it for now
print("Win" if int(input("What would you like to play Rock (0) Paper (1) or Scissors (2)")) - 1 == random.randint(0,2) else "Try Again")