        
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

        

seq_left='atgttat'
seq_top='atcgtac'
value_matrix,move_matrix=nw_matrix(seq_left,seq_top)
matrix_print(value_matrix,seq_left,seq_top)
matrix_print(move_matrix,seq_left,seq_top)





