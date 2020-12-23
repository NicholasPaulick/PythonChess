import board
import random
x=random.randint(1,2)
playerinput1 = input("Enter p1's name: ")
playerinput2 = input("Enter p2's name: ")
if x == 1:
  player1 = playerinput1
  player2 = playerinput2
elif x == 2:
  player1 = playerinput2
  player2 = playerinput1
pieces=["♖ ", "♘ ", "♗ ", "♔ ", "♕ ", "♗ ", "♘ ", "♖ ", "♙ ", "♜ ", "♞ ", "♝ ", "♚ ", "♛ ", "♝ ", "♞ ", "♜ ", "♟ "]
number=["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
a=["a ", "♖ ", "♘ ", "♗ ", "♔ ", "♕ ", "♗ ", "♘ ", "♖ "]
b=["b ", "♙ ", "♙ ", "♙ ", "♙ ", "♙ ", "♙ ", "♙ ", "♙ "]
c=["c ", "x ", "x ", "x ", "x ", "x ", "x ", "x ", "x "]
d=["d ", "x ", "x ", "x ", "x ", "x ", "x ", "x ", "x "]
e=["e ", "x ", "x ", "x ", "x ", "x ", "x ", "x ", "x "]
f=["f ", "x ", "x ", "x ", "x ", "x ", "x ", "x ", "x "]
g=["g ", "♟ ", "♟ ", "♟ ", "♟ ", "♟ ", "♟ ", "♟ ", "♟ "]
h=["h ", "♜ ", "♞ ", "♝ ", "♚ ", "♛ ", "♝ ", "♞ ", "♜ "]
letterlist = ["a", "b", "c", "d", "e", "f", "g", "h"]
masterlist = [a, b, c, d, e, f, g, h]
checkmate = 0
letterp1='0'
numberp1='s'
moveletterp1='0'
movenumberp1='s'
letterp2='0'
numberp2='s'
moveletterp2='0'
movenumberp2='s'
while checkmate == 0:
  board.bord(number, masterlist, player1, player2)
  while len(letterp1)!=1 or letterp1.islower()==False:
    letterp1=input(player1+", enter the letter of the column of the piece you wish to move.")
  while len(numberp1)!=1 or numberp1.isnumeric()==False:
    numberp1=input(player1+", enter the number of the row of the piece you wish to move.")
  while len(moveletterp1)!=1 or moveletterp1.islower()==False:
    moveletterp1=input(player1+", enter the letter of the column you wish your piece to move to.")
  while len(movenumberp1)!=1 or movenumberp1.isnumeric()==False:
    movenumberp1=input(player1+", enter the number of the row you wish your piece to move to.")
  starletter=(letterlist.index(letterp1))
  endletter=(letterlist.index(moveletterp1))
  pice = masterlist[starletter][int(numberp1)]
  whawas = masterlist[endletter][int(movenumberp1)]
  if whawas in pieces:
    whawas = "x "
    masterlist[endletter][int(movenumberp1)] = pice
    masterlist[starletter][int(numberp1)] = whawas
  else:
    masterlist[endletter][int(movenumberp1)] = pice
    masterlist[starletter][int(numberp1)] = whawas
  print("")
  board.bord(number, masterlist, player1, player2)

  while len(letterp2)!=1 or letterp2.islower()==False:
    letterp2=input(player2+", enter the letter of the column of the piece you wish to move.")
  while len(numberp2)!=1 or numberp2.isnumeric()==False:
    numberp2=input(player2+", enter the number of the row of the piece you wish to move.")
  while len(moveletterp2)!=1 or moveletterp2.islower()==False:
    movenumberp2=input(player2+", enter the letter of the column you wish your piece to move to.")
  while len(movenumberp2)!=1 or movenumberp2.isnumeric()==False:
    movenumberp2=input(player2+", enter the number of the row you wish your piece to move to.")
  starletter=(letterlist.index(letterp2))
  endletter=(letterlist.index(moveletterp2))
  pece = masterlist[starletter][int(numberp2)]
  whtwas = masterlist[endletter][int(movenumberp2)]
  if whtwas in pieces:
    whtwas = "x "
    masterlist[endletter][int(movenumberp2)] = pece
    masterlist[starletter][int(numberp2)] = whtwas
  else:
    masterlist[endletter][int(movenumberp2)] = pece
    masterlist[starletter][int(numberp2)] = whtwas
  print("")
