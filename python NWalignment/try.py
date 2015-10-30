
seq_top='atactgt'
seq_left='atagtat'
value_matrix=[[0]*(len(seq_top)+1) for i in range(len(seq_left)+1)]
move_matrix=[[0]*(len(seq_top)+1) for i in range(len(seq_left)+1)]
value_matrix[0][0]=0
for r in range(1,len(seq_left)+1):
    for c in range(1,len(seq_top)+1):
        value_matrix[r][0]=-3*r
        value_matrix[0][c]=-3*c
        move_matrix[r][0]='|'
        move_matrix[0][c]='-'
        


def matrix_print(m, seq_left, seq_top):
    if len(seq_top) > 30:
        print "Matrix appears too big to display ..."
        return
    new_seq=' '+seq_left
    w = len(str(m[-1][-1]))
    print "      " + ''.join([i.rjust(w+3) for i in seq_top])
    for i in range(0,len(new_seq)):
        print new_seq[i], ''.join([str(i).rjust(w+3) for i in m[i]])

move_matrix[1][1]= 'S'
print matrix_print(value_matrix,seq_left,seq_top)
print matrix_print(move_matrix,seq_left,seq_top)
