welcome = """
  Welcome to the haunted house.
  Prepare to be amazed or die.
  The frights might turn your hair white.
  And survivor takes the prize.
"""
print(welcome)
print("Choose which room to explore: 
print("1. living room") 
print("2. study room")
room = input("> ")

if room == "1" or room == "living room":
  print("You see the ghost of the owner of the house.")
  print("What do you do next?")
  print("1. Run away.")
  print("2. Stay and chat.")
  owner_ghost = input("> ")

  if owner_ghost == "1":
    print("You don't win the prize.")
  elif owner_ghost == "2":
    print("You're very brave and win the prize.")
  else:
    print("You must make a choice.") #need a way to loop back until a choice is made

if room == "2" or room == "study room":
  print("You meet the ghost of the family's child.")
  print("What do you do next?")
  print("1. Run away.")
  print("2. Stay and play with the kid ghost.")
  print("3. Move onto the living room.")
  kid_ghost = input("> ")

  if kid_ghost == "1":
    print("You lost this game. No prize.")
  elif kid_ghost == "2":
    print("Choose a game to play:")
    print("1. Hide and seek")
    print("2. Checkers")
    game_to_play = input("> ")

    if game_to_play == "1":
      print("You'll never get out of this house now!")
      print("Game over!")
    if game_to_play == "2":
      print("This is the never-ending game of checkers! Muahaha!")
      print("Game over!")
  else:
    print("You must now face the owner of the house!")
    print("What do you do?")
    print("1. Run away.")
    print("2. Pour yourself a scotch for a staring contest with a ghost.")
    print("3. Say a prayer.")
    last_choice = input("> ")

    if last_choice == "1":
      print("You lose this game.")
    elif last_choice == "2":
      print("Congrats! You win!")
    else:
      print("Sorry, pal, that ain't gonna work here.")
