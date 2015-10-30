#  File: Josephus.py
#  Description: This program reads a number of soldiers, a starting soldier and an elimiated number. It starts from the starting soldier, each time it reaches the elinated number
# the soldier is eliminated, it starts counts from the next soldier. The program returns the soldier who finally survived.
#  Student Name: Mengjie Yu
#  Student UT EID: my3852
#  Course Name: CS 313E
#  Unique Number: 53260 
#  Date Created: 3/21/13
#  Date Last Modified: 3/22/13

class Link(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.first=None
      self.size=0

  # Insert an element in the list
  def insert ( self, item ):
      newlink=Link(item)
      if self.first ==None:
          self.first=newlink
          #circulate the list
          self.first.next=self.first
      else:
          previous=self.first
          current=self.first.next
      
          while (previous.next.data!=self.first.data):
              if (previous.data<newlink.data and newlink.data<current.data):
                  newlink.next,current=current,newlink
              #update the current position
              previous,current=current,current.next
        #if it reaches the end of the position
          if current.data==self.first.data:
              previous.next,newlink.next=newlink,self.first
      self.size+=1
      

  # Find the link with the given key
  def find ( self, key ):
      current=self.first
      previous=self.first
      if (current==None):
          return None
      elif current.data==key:
          return current
        
      while current.data!=key:
          previous=current
          current=current.next
      return current

  # Delete a link with a given key
  def delete ( self, key ):
      current=self.first
      previous=self.first

      if (current==None):
          return None
          
      while current.data!=key:
          previous=current
          current=current.next
      if (current.data==self.first.data):
          self.first=self.first.next
      else:
          previous.next=current.next
      return current
    
          
  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  #start is the data of the starting link
  def deleteAfter ( self, start, n ):
      current=self.find(start)
      for i in range(n-1):
          previous=current
          current=current.next
          
      if n==1:
          start=current.next.data
      else:
          previous.next=current.next
          start=current.next.data
      print('Eliminated soldier is',current.data)
      return start      

  # Return a string representation of a Circular List
  def __str__ ( self ):
      result=''
      current=self.first
      for i in range(self.size):
          result+=str(current.data)+' '
          current=current.next
      return result

def main():
    infile=open('josephus.txt','r')
    
    num_soldier=int(infile.readline())
    start=int(infile.readline())
    n=int(infile.readline())
    
    testlist=CircularList()
    for i in range(1,int(num_soldier)+1):
        testlist.insert(i)
    print('The soldier list is:')
    print(testlist)
   
    for i in range(num_soldier-1):
        start=testlist.deleteAfter(start,n)
    print('The last survivor is:', end='')
    print(start)

main()
