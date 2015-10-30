book={}  #generate a dictionary called book

store=open('human_rna_subset.fa','r')

for line in store:                  
    if line[0]== '>':
       name = line[1:13]            #begin from line[4] the first digit of ID
       book[name]=''                #initial value in key is null
    else:
       book[name]+=line.rstrip()
store.close()

print book.keys()
#print book['157412239']           #for test purpose
