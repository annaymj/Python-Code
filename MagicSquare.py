#  File: MagicSquare.py

#  Description: This program prints out a magic matrix, and also prints out all possible solutions of a 3x3 magic matrix.

#  Student's Name: Mengjie (Anna) Yu

#  Student's UT EID: my3852
 
#  Course Name: CS 313E 

#  Unique Number: 53260

#  Date Created: 2/28/13

#  Date Last Modified: 3/1/13
            
# Populate a 2-D list with numbers from 1 to n2, n is an odd number
def makeSquare (n):
    square_list=[]
    for i in range(n):
        row=[0]*n
        square_list.append(row)
    #make the middle number in the bottom line 1
    row=n-1
    col=n//2
    square_list[row][col]=1
    #assign value 2 to 25 to the rest blank space
    for value in range(2,n**2+1):
        nrow=(row+1)%n
        ncol=(col+1)%n
        #go right and down
        if square_list[nrow][ncol]==0 and (not (nrow==0 and ncol==0)):
            row,col=nrow,ncol
            square_list[row][col]=value
        #if right and down is taken, go upper
        else:
            row-=1
            square_list[row][col]=value
    return square_list
            
# Print the magic square in a neat format where the numbers are right justified
def printSquare (magicSquare):
    for lst in magicSquare:
        for each in lst:
            print(repr(each).rjust(5),end='')
        print()

# Check if a list is a magic square and print
def checkSquare (magicSquare):
    n=len(magicSquare)
    total=n*(n**2+1)/2
    row_totals=[sum(x) for x in magicSquare]
    col_totals=[sum(x) for x in zip(*magicSquare)]
    diag1_total=0
    diag2_total=0
    for i in range(n):
        diag1_total+=magicSquare[i][i]
    for i in range(n):
        diag2_total+=magicSquare[i][n-1-i]
    
    for i in row_totals:
        if i!=total:
            return False
    for j in col_totals:
        if j !=total:
            return False
    if diag1_total!=total or diag2_total!=total:
        return False
    else:
        return True

# Generate all 3x3 magic squares
def permute(a,lo):
    global magic_list
    hi=len(a)
    if lo==hi:
        newlist=[a[x:x+3] for x in range(0,9,3)]
        if checkSquare(newlist)==True:
            printSquare(newlist)
            print()
    else:
        for i in range(lo,hi):
            a[lo],a[i]=a[i],a[lo]
            permute(a,lo+1)
            a[lo],a[i]=a[i],a[lo]


def main():
    global magic_list
    magic_list=[]
    # Prompt the user to enter an odd number 3 or greater
    number=eval(input("Please enter an odd number:"))
    # Check the user input
    while (number%2==0 or number <3):
        number=eval(input("Please enter an odd number:"))
    magicSquare=makeSquare(number)
    printSquare(magicSquare)
    
    # Print all 3x3 magic squares
    mylist=[x for x in range(1,3**2+1)]
    print ('All 3x3 magic square:')
    permute(mylist,0)

main()
