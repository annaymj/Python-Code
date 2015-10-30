#  File: BabyNames.py 

#  Description:  This program reads a name ranking file from the website, and prompts the user 6
#different options to see the ranking of a name, it keeps promopts until the user enter 7 or a number
#bigger than 7.

#  Student Name: Mengjie Yu 

#  Student UT EID:  my3852

#  Course Name: CS 313E

#  Unique Number: 53260

#  Date Created: 2/14/13

#  Date Last Modified:2/15/13

import urllib.request

#option 1, search for names
def func1(namedic,decade):    
    name=input("Enter a name: ")
    if name in namedic.keys():
        highrank=min(namedic[name])
        highrank_decade=decade[namedic[name].index(highrank)]
        print ('\nThe matches with their highest ranking decade are: \n%s %d' %(name, highrank_decade))
    else:
        print (name, 'does not appear in any decade.')

#option 2, display data for one name
def func2(namedic,decade):
    name=input("Enter a name: ")
    print ('\n%s:'%name,end=' ')
    if name not in namedic.keys():
        print('Name not in list,check spelling')
    else: 
        for each in namedic[name]:
            print (each,end=' ')
        print()
        for i in range(len(decade)):
            if namedic[name][i]==1001:
                namedic[name][i]=0
            print ('%d: %s'%(decade[i],namedic[name][i]))

#option 3, display all names appear in one decade, in order of rank
def func3(namedic,decade):
    mylist=[]
    year=eval(input("Enter decade: "))
    year_index=decade.index(year)
    for name in namedic:
        rank=namedic[name][year_index]
        if rank<1001:    #select the non-zero (or 1001) rank and its correspondingname
            nametuple=()
            nametuple=rank,name
            mylist.append(nametuple)
    mylist.sort()
    print("\nThe names are in order of rank:")
    for each in mylist:
        print (each[1],each[0])
    

#option 4, display all names that appear in all decades
def func4(namedic):
    namelist=[]  #initiate a namelist to store qualified names
    for name in namedic.keys():
        rank=namedic[name]
        if 1001 not in rank:
            namelist.append(name)
    namelist.sort()         #sort the namelist
    print('%d names appear in every decade. The names are:' %len(namelist))
    for item in namelist:
        print (item)

#option 5, display all names that are more populat in every decade, sorted by name
def func5(namedic):    
    namelist=[]
    for name in namedic:
        rank=namedic[name]
        #find the 1st non 1001 rank
        for i in range(len(rank)):
            if rank[i]<1001:
                f_index=i
                break
            else:
                i+=1
        if f_index not in range(11):
            break
        newrank=rank[f_index:]      #rank get rid of the first 1001s

        flag=True
        if len(newrank)==1:
            flag=True
        else:
            low_rank=newrank[0]
            for i in range(1,len(newrank)):
                if not newrank[i] <low_rank:
                    flag=False
                    break
                else:
                    low_rank=newrank[i]
        if flag:
            namelist.append(name)
        namelist.sort()
    print('\n%d names are more popular in every decade'%len(namelist))
    for name in namelist:
        print (name)
            
#option 6, displays names that are less popular, sorted by name. Basically we just need to reverse the rank order, and use same algorith as func5
def func6(namedic):
    newdic={}
    for name in namedic:
        rank=namedic[name]
        newdic[name]=rank[::-1]
        
    namelist=[]
    for name in newdic:
        rank=newdic[name]
        #find the 1st non 1001 rank
        for i in range(len(rank)):
            if rank[i]<1001:
                f_index=i
                break
            else:
                i+=1
        if f_index not in range(11):
            break
        newrank=rank[f_index:]      

        flag=True
        if len(newrank)==1:
            flag=True
        else:
            low_rank=newrank[0]
            for i in range(1,len(newrank)):
                if not newrank[i] <low_rank:
                    flag=False
                    break
                else:
                    low_rank=newrank[i]
        if flag:
            namelist.append(name)
        namelist.sort()
    print('\n%d names are less popular in every decade'%len(namelist))
    for name in namelist:
        print (name)
#function prompt() prompts options to use 
def prompt():
    print('\nOptions:')
    print('Enter 1 to search for names.')
    print ('Enter 2 to display data for one name.')
    print ('Enter 3 to all names that appear in only one decade')
    print ('Enter 4 to all names that appear in all decades.')
    print('Enter 5 to all names that are more popular in every decade.')
    print ('Enter 6 to all names that are less popular in every decade.')
    print ('Enter 7 to quit.\n')
    
    
            


def main():
    namedic={}                  
    try:
        infile=urllib.request.urlopen('http://www.cs.utexas.edu/~mitra/csSpring2013/cs313/assgn/names.txt')
    except IOError:
        print ("The URL link cannot be accessed")
        return
                 
    for line in infile:
        namefile=line.decode().split()
        namekey=namefile[0]
        namevalue=namefile[1:]
        for i in range(len(namevalue)):
            if namevalue[i]=='0':
                namevalue[i]=1001
            else:
                namevalue[i]=int(namevalue[i])
        namedic[namekey]=namevalue
    decade=[]                   #initiate an decade list to store decade data
    for i in range(1900,2001,10):
        decade.append(i)

    prompt()
    choice=eval(input('Enter choice: '))
    while (choice>=1 and choice<7):
        if choice==1:
            func1(namedic,decade)
        elif choice==2:
            func2(namedic,decade)
        elif choice==3:
            func3(namedic,decade)
        elif choice==4:
            func4(namedic)
        elif choice==5:
            func5(namedic)
        elif choice==6:
            func6(namedic)
        prompt()
        choice=eval(input('Enter choice: '))
    if choice>=7:
        print ('\nGoodbye.')
        
main()        
        
    
    
    

