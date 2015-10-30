# -*- coding: utf-8 -*-
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

aln1='at-gttac'
aln2='atcg-tat'
print alignment_print(aln1,aln2)
