#File: Boxes.py

#Description: In this program it checks the largest subset of boxes (box number >=2) given a list of boxes, and then prints the boxes out.

#Student's Name:Mengjie Yu

#Student's UT EID:my3852

#Course Name: CS 313E 
  
#Unique Number: 53260 

#Date Created:2/16/13

#Date Last Modified: 2/22/13

#this isSubset() function takes 2 argument, box1 and box2, and returns True if box 1 is nested within box2
def isSubset(box1,box2):
    return( box1[0]<box2[0] and box1[1]<box2[1] and box1[2]<box2[2])

#this all_subset() function takes a list of boxes, and returns True if the left box is nested within the next right box
def all_subset(lst):
    flag=True
    for i in range(len(lst)-1):
        if isSubset(lst[i],lst[i+1])==False:
            flag=False
            break
    if flag:
        return True
    else:
        return False

#this subset() recursion gives all combination of boxes     
def subset(a,b,lo):
    global result_list
    hi=len(a)
    if (lo==hi):
        if all_subset(b)==True:
            result_list.append(b)
        return
    else:
        c=b[:]
        b.append(a[lo])
        subset(a,c,lo+1)
        subset(a,b,lo+1)

#this len_subset() function takes a list of nested boxes as argument, store the nested boxes length in a new list 'len_list', and finds the maximum nested box length
def len_subset(lst):
    len_list=[]
    for each in lst:
        len_list.append(len(each))
    max_len=max(len_list)
    return max_len

#this print_subset() function takes a list of nested boxes, and checks whether the maximum length of the nested boxes is longer than or equal to 2,and prints out the nested boxes
def print_subset(lst):
    max_len=len_subset(lst)
    if max_len<2:
        print ('No Nesting Boxes')
    else:
        print('Largest Subset of Nesting Boxes')
        newlist=[]
        for boxes in lst:
            if len(boxes)==max_len:
                for each in boxes:
                    print(each)
                print()
    
#main() function creates a global list 'result_list' and stores all the nested boxes combinations in it.
def main():
    global result_list
    infile=open('boxes.txt','r')
    num_box=int(infile.readline())
    box_list=[]
    for i in range(num_box):
        box=infile.readline().split()
        boxlist=[]
        for each in box:
            boxlist.append(int(each))
        boxlist.sort()
               
        box_list.append(boxlist)
        box_list.sort()

    result_list=[]
    b=[]
    subset(box_list,b,0)
    print_subset(result_list)
main()
            
    
