#python7.3_traceback

def delta(a,b):
    if a==b:
       t=4
    elif a=='-'or b=='-':
       t=-3
    else:
       t=-2
    return t 


def best_score(value_matrix,r,c,nuc_left,nuc_top):
    mvalue=max(value_matrix[r-1][c-1]+delta(nuc_left,nuc_top),
               value_matrix[r][c-1]+delta('-',nuc_top),
               value_matrix[r-1][c]+delta(nuc_left,'-'))
    
    if mvalue==value_matrix[r-1][c]+delta(nuc_left,'-'):
                direction='|'
    if mvalue==value_matrix[r][c-1]+delta('-',nuc_top):
                direction='-'
    if mvalue==value_matrix[r-1][c-1]+delta(nuc_left,nuc_top):
                direction='D'
                
    return mvalue,direction
                

def nw_matrix(seq_left,seq_top):
    value_matrix=[[0]*(len(seq_top)+1) for i in range(len(seq_left)+1)]
    move_matrix=[[0]*(len(seq_top)+1) for i in range(len(seq_left)+1)]
       
    for r in range(1,len(seq_left)+1):
        for c in range(1,len(seq_top)+1):
            value_matrix[r][0]=-3*r
            value_matrix[0][c]=-3*c
            move_matrix[r][0]='|'     #upper
            move_matrix[0][c]='-'     #left

            value_matrix[r][c],move_matrix[r][c]=best_score(value_matrix, r, c, list(seq_left)[r-1], list(seq_top)[c-1])
                      
           
    return value_matrix, move_matrix
            
            

def matrix_print(m, seq_left, seq_top):
    if len(seq_top) > 30:
        print "Matrix appears too big to display ..."
        return
    new_seq=' '+seq_left
    w = len(str(m[-1][-1]))
    print "      " + ''.join([i.rjust(w+3) for i in seq_top])
    for i in range(0,len(new_seq)):
        print new_seq[i], ''.join([str(i).rjust(w+3) for i in m[i]])
  

def traceback(move_matrix,seq_left,seq_top):
    aln_left=''
    aln_top=''
    l=len(seq_left)
    t=len(seq_top)
    while l>0 and t>0:
        if move_matrix[l][t]=='D':
            aln_left=seq_left[l-1]+aln_left
            aln_top=seq_top[t-1]+aln_top
            l-=1
            t-=1
        elif move_matrix[l][t]=='-':
            aln_left='-'+aln_left
            aln_top=seq_top[t-1]+aln_top
            t-=1
        else:
            aln_left=seq_left[l-1]+aln_left
            aln_top='-'+aln_top
            l-=1
    return aln_left,aln_top


def alignment_print(aln1, aln2):
    M, N = len(aln1), len(aln2)
    comp = []
    total = max(M, N)
    if M == N:
        for i in range(M):
            m, n = aln1[i], aln2[i]
            if m == '-' or n == '-':
                comp.append('-')
            elif m != n:
                comp.append('*')
            else:
                comp.append(' ')
        comp = ''.join(comp)
    else:
        comp = ' ' * total
    pad = ' ' * len(str(total))
    width = 80
    p = 1
    while p < int(total):
        print str(p).rjust(len(pad)), aln1[p-1:p+80]
        print pad, aln2[p-1:p+80]
        print pad, comp[p-1:p+80]
        print
        p += 80
        
seq_left='atgttat'
seq_top='atcgtac'
value_matrix,move_matrix=nw_matrix(seq_left,seq_top)
matrix_print(value_matrix,seq_left,seq_top)
print''                                                         #space
matrix_print(move_matrix,seq_left,seq_top)

aln=traceback(move_matrix,seq_left,seq_top)
print alignment_print(aln[0],aln[1])
                
