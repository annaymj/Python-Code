#  File: EightQueens.py

#  Description:This program prompts the user to enter the size of the board, and prints out all
# the solutions of magic square given that board.

#  Student's Name: Mengjie Yu

#  Student's UT EID: my3852
 
#  Course Name: CS 313E 

#  Unique Number: 53260

#  Date Created:3/4/13

#  Date Last Modified: 3/5/13
#initiate a class 'EnghtQueens'
class EightQueens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # check if no queen captures another
  def isValid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        rowDiff = abs (row - i)
        colDiff = abs (col - j)
        if (rowDiff == colDiff) and (self.board[i][j] == 'Q'):
          return False
    return True

#find all posible solutsions recursively
  def recursiveSolve (self, col):
    global count
    if (col == self.n):
      count+=1
      print()
      return self.printBoard()
      
    else:
      for i in range (self.n):
        if (self.isValid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursiveSolve (col + 1)):
            return True
          self.board[i][col] = '*'
      return False

  # solve the problem, starts at 0 and traverse through all possible solutions
  def solve (self):
    self.recursiveSolve (0)


  # print the board
  def printBoard (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ' )
      print ()

def main():
  global count
  count=0
  n=eval(input('Enter the size of board:'))
  while n<1 or n>8:
      n=eval(input('Enter the size of board:'))
  print()
  #create object
  queens = EightQueens (n)
  queens.solve()
  print('\nThere are %d solutions for a %d x %d board.'%(count,n,n))
  

main()
