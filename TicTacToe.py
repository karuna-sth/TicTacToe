from IPython.display import clear_output

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
checkEmpty = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def displayOutput():
  clear_output()
  print(board[0]+ ' | '+board[1]+ ' | ' +board[2])
  print('---------')
  print(board[3]+ ' | '+board[4]+ ' | ' +board[5])
  print('---------')
  print(board[6]+ ' | '+board[7]+ ' | ' +board[8])

def playerInput(player):
  inputSymbol = ['X', 'O']
  position = int(input('\nPlayer {player} turn!! Enter the position for inserting {symbol}\t' .format(player = player+1, symbol = inputSymbol[player])))
  if board[position] == 'X' or board[position] == 'O':
    print("The position is not empty\n")
    playerInput(player)
  else:
    board[position] = inputSymbol[player]
    checkEmpty.remove(position)
  return 1
 

def checkForWinner():
  inputSymbol = ['X', 'O']
  winingPosition = [[0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
  for check in winingPosition:
    firstSymbol = board[check[0]]
    if firstSymbol != ' ':
      won = True
      for position in check:
        if firstSymbol != board[position]:
          won = False
          break
      if won:
        if firstSymbol == inputSymbol[0]:
          displayOutput()
          print("Player 1 wins")
          break
        else: 
          displayOutput()
          print("Player 2 wins") 
          break
    else:
      won = False
  if won:
    return 1
  else:
    return 0 


#main 
player = 0
while checkEmpty and not checkForWinner():
  displayOutput()
  playerInput(player)
  player = int(not player)
if not checkEmpty:
  displayOutput()
  print("Draw ;)")


