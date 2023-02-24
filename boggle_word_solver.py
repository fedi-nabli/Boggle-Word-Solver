class Tree():
  def __init__(self):
    return
  
  def add(self, word):
    return

def main():
  # Initialise game board based on user input
  board = []
  for i in range(0, 4):
    # append empty row
    board.append([])
    for j in range(0, 4):
      board[i].append(input().strip().upper())

  # print board
  for i in range(0, 4):
    for j in range(0, 4):
      print(board[i][j], end=" ")
    print()
  
  # load dictianry
  dict = open("dictinary-yawl.txt", "r")

  tree = Tree()
  for line in dict:
    word = line.rstrip().upper()
    tree.add(word)

main()