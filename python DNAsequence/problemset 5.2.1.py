book={}  #generate a dictionary called book

store=open('human_rna_subset.fa','r')

for line in store:                  
    if line[0]== '>':
       name = line.rstrip()         #remove'/n'
       book[name]=''                #initial value in key is null
    else:
       book[name]+=line.rstrip()
store.close()

print book.keys()

