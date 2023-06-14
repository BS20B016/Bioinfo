import math
import numpy as np
import pandas as pd
seq1="MVLSPADKTNVKGKVGAHAGEYGAAAW" 
seq2="MKRLPADPPCVKGKVKAKAGDYGATTW" 
seq3="MALSAADKTNVKSKVGGHAGEYGAATS" 
seq4="MVLSAADKTNVKSKAGGNAGEWWAAAW"
seq5="MVLSAADKTNVKSKVLANAGEFGAAAW"
seq6="ALLPIRTTYHKKCASGHIPEEKDLNNV"
seq7="DEASSLKGHHIKKLEADALLIPLSASS"
aa ={'A': 0, 'D': 0, 'C': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
amino = []
pos = [i for i in range(1,28)]
for i in aa:
    amino.append(i)
def check(s):
    values ={'A': 0, 'D': 0, 'C': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
    k2 = []

    for i in range(7):
        k = len([1 for y in range(7) if (s[y]==s[i])])
        values[s[i]] = k
    for i in values:
        k2.append(values[i])    
    return k2  

seq = [seq1,seq2,seq3,seq4,seq5,seq6,seq7]
mat = [[0 for x in range(27)] for i in range(20)]
for i in range(27):
    temp = ""
    for j in range(7):
        temp+=seq[j][i]
    temp2= check(temp)
    for m in range(20):
        mat[m][i] = temp2[m]
for i in range(20):
    for j in range(27):
        mat[i][j] = math.log((mat[i][j]+0.05)/(0.05*(7+1)))
wt_mt = np.array(mat)
print(pd.DataFrame(wt_mt, amino, pos))