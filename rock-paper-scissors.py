from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()

print("***Welcome to the legendary game of Rock (R), Paper (P), Scissors (S)***")
print()

game_rounds = 1
rounds_to_win = 3
player1_score = 0
player2_score = 0

rocky = "Rock smashes Scissors."
sci = "Scissors cuts Paper."
paper = "Paper covers Rock." 

while True:
  print(f"Round {game_rounds}\n")

  print("Select your move (R, P or S)")
  print()

  player1Move = input("Player 1 > ")
  player2Move = input("Player 2 > ")

  print()
  
  if player1Move.upper() == "R":
    if player2Move.upper() == "R":
      print("It's", player1Move, "and", player2Move, ". Thats a draw")
      
    elif player2Move.upper() == "S":
      print(rocky, "Player1 wins!")
      player1_score += 1
      # continue
      
    elif player2Move.upper() == "P":
      print(paper, "Player2 wins!")
      player2_score += 1
      # continue
      
    else:
      print("Invalid Move Player 2!")
  
  elif player1Move.upper() == "P":
    if player2Move.upper() == "R":
      print(paper, "Player1 wins!")
      player1_score += 1
      # continue
      
    elif player2Move.upper()=="S":
      print(sci, "Player2 wins!")
      player2_score += 1
      # continue
      
    elif player2Move.upper()=="P":
      print("It's", player1Move, "and", player2Move, ". Thats a draw")
    else:
      print("Invalid Move Player 2!")
  
  elif player1Move.upper()=="S":
    if player2Move.upper()=="R":
      print(rocky, "Player2 wins!")
      player2_score += 1
      # continue
      
    elif player2Move.upper()=="S":
      print("It's", player1Move, "and", player2Move, ". Thats a draw")
    elif player2Move.upper()=="P":
      print(sci, "Player1 wins!")
      player1_score += 1
      # continue
      
    else:
      print("Invalid Move Player 2!")
  
  else:
    print("Invalid Move Player 1!")

  print(f"Player 1 Score: {player1_score} | Player 2 Score: {player2_score}\n")

  if player1_score == rounds_to_win or player2_score == rounds_to_win:
    break

  game_rounds += 1

  # if player1_score == 2 or player2_score == 2 and game_rounds == 3:
  #   break

if player1_score > player2_score:
  print("Player 1 is the overall winner!")
else:
  print("Player 2 is the overall winner!")


  
#   break

# if player1_score == 2 and game_rounds == 3:
#   print("Player 1 has", player1_score, "wins.")

# if player2_score == 2 and game_rounds == 3:
#   print("Player 2 has", player2_score, "wins.")
  
