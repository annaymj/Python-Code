# -*- coding: utf-8 -*-
def matrix_print(m, seq_left, seq_top)
    if len(seq_top) > 30:
        print "Matrix appears too big to display ..."
        return
    new_seq=' '+seq_left
    w = len(str(m[-1][-1]))
    print "    " + ''.join([i.rjust(w+1) for i in seq_top])
    for i in range(0,len(new_seq)):
        print new_seq[i], ''.join([str(i).rjust(w+1) for i in m[i]])
