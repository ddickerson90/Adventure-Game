print('''             _                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_|      ''')
print("Welcome to the World of Pokemon!")
print("Can you catch them all?")

choice1 = input('Do you want to become a Pokemon Master? Type "yes" or "no \n').lower()
if choice1 == "yes":
  choice2 = input('Do you want to fill the PokeDex? Type "yes". Type "no". \n').lower()
  if choice2 == "yes":
    choice3 = input("Thank you for agreeing to help with my research. There are three balls here, will you choose Bulbasaur, Charmander or Squirtle?. \n").lower()
    if choice3 == "charmander":
      print("Charmander burned your map. You lose!")
    elif choice3 == "bulbasaur":
      print("Bulbasaur has ignored your request! You lose!")
    elif choice3 == "squirtle":
      print("You chose the best Pokemon. You Win!.")
    else:
      print("You did not choose a Pokemon. Game Over.")
  else:
    print("A wild Mewtwo appeared! Game Over.")
else:
  print("Snorlax has eaten your shoes. Game Over.")
