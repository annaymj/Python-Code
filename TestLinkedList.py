#  File: TestLinkedList.py
#  Description: In this program, it builds its own data structure function for linkedlist, and applys to list. 
#  Student Name: Mengjie Yu
#  Student UT EID: my3852
#  Course Name: CS 313E
#  Unique Number: 53260
#  Date Created:3/18/13
#  Date Last Modified: 3/18/13

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    def __init__ (self):
        self.first = None
        
    # get number of links 
    def getNumLinks (self):
        size=0
        current=self.first
        if(current==None):
            return size
        while (current!=None):
            size+=1
            current=current.next
        return size
        
  
    # Add data at the beginning of the list
    def addFirst (self, data):
        newLink=Link(data)
        newLink.next,self.first=self.first, newLink
        #newLink.next=self.first
        #self.first=newLink

    # Add data at the end of a list
    def addLast (self, data):
        newLink=Link(data)
        current=self.first

        if(current==None):
            self.first=newLink
            return
        while(current.next!=None):
           
            current=current.next
        current.next=newLink

    # Add data in an ordered list in ascending order
    def addInOrder (self, data):
        newlink=Link(data)
        current=self.first
        if (current==None or current.data>newlink.data):
            self.addFirst(newlink.data)
            return
            
        while (current.next!=None and current.next.data<=newlink.data):
            current=current.next

        newlink.next,current.next=current.next,newlink
        #newlink.next=current.next
        #current.next=newlink
                   

    # Search in an unordered list, return None if not found
    def findUnordered (self, data):
        current=self.first
        if (current==None):
            return None
        while (current.data!=data):
            if (current.next==None):
                return None
            else:
                current=current.next
        return current.data

    # Search in an ordered list, return None if not found
    #stop if found a number >data, return None
    def findOrdered (self, data):
        current=self.first
        if (current==None):
            return None
        while (current.data!=data):
            if(current.next==None):
                return None
            elif current.data >data:
                return None
                break
            else:
                current=current.next
        return current.data

    # Delete and return Link from an unordered list or None if not found
    def delete (self, data):
        current=self.first
        previous=self.first

        if(current==None):
            return None
        while (current.data!=data):
            if(current.next==None):
                return None
            else:
                previous=current
                current=current.next
                
        if (current==self.first):
            self.first=self.first.next
        else:
            previous.next=current.next

        return current
 
    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        result=''
        count=0
        current=self.first 
        length=self.getNumLinks()
            
        for i in range(length):
            result+=str(current.data)+'  '
            current=current.next
            count+=1
            
            if count%10==0:
                result+='\n'
        return result
            

    # Copy the contents of a list and return new list
    def copyList (self):
        newlist=LinkedList()
        current=self.first
        while (current!=None):
            newlist.addLast(current.data)
            current=current.next
        return newlist

    # Reverse the contents of a list and return new list
    def reverseList (self):
        newlist=LinkedList()
        current=self.first
        while (current!=None):
            newlist.addFirst(current.data)
            current=current.next
        return newlist

    # Sort the contents of a list in ascending order and return new list
    def sortList (self):
        newlist=LinkedList()
        current=self.first
        while (current!=None):
            newlist.addInOrder(current.data)
            current=current.next
        return newlist
            

    # Return True if a list is sorted in ascending order or False otherwise
    def isSorted (self):
        current=self.first
        while(current.next!=None):
            if not (current.data<=(current.next).data):
                return False
                break
            else:
                current=current.next
        return True
        
        
    # Return True if a list is empty or False otherwise
    def isEmpty (self):
        return self.first==None

    # Merge two sorted lists and return new list in ascending order
    def mergeList (self, b):
        newlist=LinkedList()
        current=self.first
        while (current!=None):
            newlist.addLast(current.data)
            current=current.next

        current_b=b.first
        while(current_b!=None):
            newlist.addLast(current_b.data)
            current_b=current_b.next
        newlist=newlist.sortList()
        return newlist
        
    # Test if two lists are equal, item by item and return True
    def isEqual (self, b):
        length=self.getNumLinks()
        current=self.first
        current_b=b.first
        if b.getNumLinks()!=length:
            return False
        
        for i in range(length):
            if current!=current_b:
                return False
                break
            else:
                current=current.next
                current_b=current_b.next
        return True

    # Return a new list, keeping only the first occurence of an element and removing all duplicates. Do not change the order of the elements.
    def removeDuplicates (self):
        newlist=LinkedList()
        count=0
        myset=set([])
        current=self.first
        length=self.getNumLinks()
        if length==0:
            return None     
        while (current!=None):
            myset.add(current.data)
            count+=1
            if len(myset)==count:
                newlist.addLast(current.data)
            else:
                current=current.next
                count-=1
        return newlist
                
                
def main():
    testlist=LinkedList()
  # Test methods addFirst() and __str__() by adding more than 10 items to a list and printing it.
    for i in range(40,1,-3):
        testlist.addFirst(i)
    print('Testing for addFirst')
    print(testlist)
    
  # Test method addLast()
    testlist.addLast(99)
    print('\nTesting for addLast')
    print (testlist)

  # Test method addInOrder()
    print('\nThis is addInOrder')
    testlist.addInOrder(26)
    print(testlist)

  # Test method getNumLinks()
    num=testlist.getNumLinks()
    print('\nThe total number of the list is',num)

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there
    print('\nTesting for findUnordered()')
    testnumber=[0,10]
    for num in testnumber:
        if testlist.findUnordered(num)!=None:
            print(num,' is there')
        else:
            print(num,' is not there')

  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there
    print('\nTesting for findOrdered()')
    testnumber=[10,999]
    for num in testnumber:
        if testlist.findOrdered(num)!=None:
            print(num,' is there')
        else:
            print(num,' is not there')
            
  # Test method delete()
  # Consider two cases - item is there, item is not there
    print('\nTesting for delete()')
    testnumber=[1001,10]
    for num in testnumber:
        if testlist.delete(num)!=None:
            print(num,'is deleted, below is the deleted list')
            print(testlist)
        else:
            print(num,' is not there')


  # Test method copyList()
    print('\nThis is testing copylist')
    print(testlist.copyList())

  # Test method reverseList()
    print('\nThis is testing for reversed list')
    print(testlist.reverseList())

  # Test method sortList()
    print('\n This is testing for Sortlist')
    testlist.addFirst(1001)
    print(testlist.sortList())

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
    print('\n This is testing for isSorted()')
    print(testlist)
    if testlist.isSorted()==True:
        print ('Above list is sorted')
    else:
        print('Above list is not sorted')
    newlist=testlist.sortList()
    print(newlist)
    if newlist.isSorted()==True:
        print ('Above list is sorted')
    else:
        print('Above list is not sorted')

  # Test method isEmpty()
    print('\nTesting for method isEmpty()')
    print(testlist.isEmpty())

  # Test method mergeList()
    print('\nTesting for mergeList()')
    b=LinkedList()
    b.addFirst(-1)
    b.addLast(12345)
    print(testlist.mergeList(b))

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
    print('\nTesting for isEqual()')
    print('testlist and testlist are Equal(True) or NotEqual(False):',testlist.isEqual(testlist))
    print('testlist and b are Equal(True) or NotEqual(False):', testlist.isEqual(b))

  # Test removeDuplicates()
    print('\nTesting for removeDuplicates')
    for i in range(40,1,-3):
        testlist.addFirst(i)    
    print(testlist) 
    testlist.removeDuplicates()
    print('Duplicates removed')
    print (testlist.removeDuplicates())


main()
