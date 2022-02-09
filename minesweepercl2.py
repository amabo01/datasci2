import numpy as np 

class minesweeper:
  def __init__(self, r, c):
    self.r = r
    self.c = c
    self.boardArray = np.random.randn(r,c)
    self.boardList = [['_' for x in range (c)] for i in range(r)]
  
  def __str__(self):
    return str(self.boardArray)

  def playGame(self):

    row = int(input("Which row would you like to select?\n")) - 1
    col = int(input("Which column would you like to select?\n")) - 1 
    if self.boardArray[row][col] < 0:
      print("BOMB DETECTED!!!! Good job!!")
      print(self)
    else:
      continuegame = input("🥺.. dang you didn't find a bomb yet.\nDo you want to continue the game? Y/N ")
      if continuegame.lower() == 'y':
        self.playGame()
      else:
        print("thanks for playing <3 ")
        print(self)