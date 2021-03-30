colorsToToken = {
  'rouge': 'R',
  'jaune': 'J'
}
tokensToColor = {
  'R': 'rouge',
  'J': 'jaune'
}

# self.__board[0][0] is bottom left
class Board:
  def __init__(self, w, h):
    self.__width = w
    self.__height = h
    self.__ended = False
    self.__board = [["O" for _ in range(h)] for _ in range(w)]
  
  def play(self, turn, col):
    if self.__ended:
      return
    try:
      color = colorsToToken[turn]
      for h, a in enumerate(self.__board[col]):
        if a == "O":
          self.__board[col][h] = color
          return True
      print("Cette colonne est pleine")
      return False
    except KeyError:
      print("Couleur invalide")
      
  def print(self):
    display = [[None for _ in range(self.__width)] for _ in range(self.__height)]
    for a, column in enumerate(self.__board):
      for b, slot in enumerate(column):
        display[b][a] = slot
    display.reverse()
    for a in display:
      for b in a:
        print(f"{b} ", end='')
      print()
      
  def win(self, color):
    self.__ended = True
    print(f"Le gagnant est le joueur {color}")
      
  def checkWin(self):
    # print(self.__board)
    w = self.__width
    h = self.__height
    
    # Check each column
    lastColor = None
    streak = 0
    for column in self.__board:
      for token in column:
        if token != "O":
          color = tokensToColor[token]
          if color != lastColor:
            streak = 1
          elif color == lastColor:
            streak += 1
          lastColor = color
          if streak > 3:
            winner = color
            return self.win(color)
            
    # Check each row
    formatted = [[None for _ in range(self.__width)] for _ in range(self.__height)]
    for a, column in enumerate(self.__board):
      for b, slot in enumerate(column):
        formatted[b][a] = slot
    lastColor = None
    streak = 0
    for row in formatted:
      for token in row:
        if token != "O":
          color = tokensToColor[token]
          if color != lastColor:
            streak = 1
          elif color == lastColor:
            streak += 1
          lastColor = color
          if streak > 3:
            winner = color
            return self.win(color)
    
    # Check from bottom left
    winner = checkDiag(self.__board, w, h)
    if winner:
      return self.win(winner)
    
    # Check from bottom right
    test = self.__board.copy()
    test.reverse()
    for i, l in enumerate(test):
      test[i] = list(l)
      test[i].reverse()
    winner = checkDiag(test, w, h)
    if winner:
      return self.win(winner)
    # for k in range(w + h - 2, 0, -1):
    #   for j in range(k):
    #     i = k - j
    #     if i < h and j < w:
    #       print(f"{self.__board[i][j]} ", end='')
    #   print()
      
def checkDiag(l, w, h):
  lastColor = None
  streak = 0
  for k in range(w + h - 1):
    for j in range(k + 1):
      i = k - j
      if i < h and j < w:
        token = l[i][j]
        # print(f'{token} ', end='')
        if token != "O":
          color = tokensToColor[token]
          if color != lastColor:
            streak = 1
          elif color == lastColor:
            streak += 1
          lastColor = color
          if streak > 3:
            return color
    # print()
  return None
  
board = Board(8, 8)

board.play("rouge", 0)
board.play("rouge", 1)
board.play("rouge", 2)
board.play("rouge", 3)

# Verticale
# board.play("rouge", 3)
# board.play("rouge", 3)
# board.play("rouge", 3)
# board.play("rouge", 3)

# Diagonalle
# board.play("jaune", 7)
# board.play("rouge", 6)
# board.play("jaune", 6)
# board.play("rouge", 5)
# board.play("rouge", 5)
# board.play("jaune", 5)
# board.play("rouge", 4)
# board.play("rouge", 4)
# board.play("rouge", 4)
# board.play("jaune", 4)

board.print()
print()
board.checkWin()