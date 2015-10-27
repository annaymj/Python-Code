#  File: TestBinaryTree.py
#  Description:
#  Student Name: Mengjie Yu
#  Student UT EID: my3852
#  Course Name: CS 313E
#  Unique Number: 53260
#  Date Created: 4/1/13
#  Date Last Modified:

#create a class Queue
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

#create a Node class
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
    
#creat a Tree class
class Tree (object):
  def __init__ (self):
    self.root = None
    self.size = 0



  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
        
      self.size+=1

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder(aNode.lChild)
      print (aNode.data,end=' ')
      self.inOrder(aNode.rChild)

  # Returns true if two binary trees are similar
  def isSimilar (self, pNode): 
    if (self.root==None and pNode.root==None):
      return True
    elif self.size != pNode.size:
      return False
    else:
      return (self.isSimilarHelper(self.root,pNode.root))

  def isSimilarHelper(self,node1,node2):
    if node1 == None and node2 == None:
      return True
    elif ( (node1.data == node2.data) and
           self.isSimilarHelper(node1.lChild, node2.lChild) and
           self.isSimilarHelper(node1.rChild, node2.rChild)):
      return True
    else:
      return False

  # Prints out all nodes at the given level
  def printLevel(self,level):
    mylist=[]
    if self.root == None:
      return None
    else:
      self.printLevelHelper(self.root,level,1,mylist)
    for each in mylist:
        print(each,end=' ')
    
  def printLevelHelper(self,r,desired,current,mylist):
      if r == None:
        return
      elif (desired == current):
        mylist.append(r.data)
      else:
        self.printLevelHelper(r.lChild,desired,current+1,mylist)
        self.printLevelHelper(r.rChild,desired,current+1,mylist)

        
  # Returns the height of the tree, height is the numbers of nodes -1
    
  def getHeight (self):
    if self.root == None:
      return 0
    else:
      return (self.getHeightHelper(self.root))

  def getHeightHelper(self,r):
    if (r == None):
      return 0
    else:     
      l_height = self.getHeightHelper(r.lChild)
      r_height = self.getHeightHelper(r.rChild)

      if (l_height > r_height):
        return (l_height + 1)
      else:
        return (r_height +1)
         

  # Returns the number of nodes in the left subtree and right subtree

  def numNodes(self):
    if self.root == None:
      return 0
    else:
      return (self.numNodesHelper(self.root))

  def numNodesHelper(self,r):
    if (r == None):
      return 0
    else:
      return (self.numNodesHelper(r.lChild)+1+self.numNodesHelper(r.rChild))

def main():
  # Create three trees - two are the same and the third is different
  tree1=Tree()
  tree2=Tree()
  tree3=Tree()
  numlist=[50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
   #tree1 and tree2 should be similar, while tree3 is different
  for i in numlist:
    tree1.insert(i)
    tree2.insert(i)
  for i in range(19,-1,-3):
    tree3.insert(i)
    
  print('Testing tree 1 is:')
  tree1.inOrder(tree1.root)
  
  print('\nTesting tree 2 is:')
  tree2.inOrder(tree2.root)
  
  print('\nTesting tree 3 is:')
  tree3.inOrder(tree3.root)

  # Test your method isSimilar()
  print('\n\nTesting for isSimilar')
  if (tree1.isSimilar(tree2)):
    print ('Tree1 is similar with Tree2')
  else:
    print ('Tree1 is not similar with Tree2')

  if tree2.isSimilar(tree3):
    print ('Tree2 is similar with Tree3')
  else:
    print ('Tree2 is not similar with Tree3')
 
  

  # Print the various levels of two of the trees that are different
  print('\nTesting printing level 2 in tree1:')
  tree1.printLevel(2)

  print('Testing printing level 2 in tree3:')
  tree3.printLevel(2)

  # Get the height of the two trees that are different
  print('\nThe height of tree1 is:',tree1.getHeight())
  print('\nThe height of tree3 is:',tree3.getHeight())

  # Get the number of nodes in the left and right subtree
  print('\nNumber of Nodes in tree1 is:',tree1.numNodes())
  print('Number of Nodes in tree2 is:',tree2.numNodes())
  print('Number of Nodes in tree3 is:',tree3.numNodes())
  
main()
