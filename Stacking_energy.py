Energy = {"AA":-4, "AT": -7, "AC": -5, "AG": -11, "TA": -7, "TT": -2, "TC": -3, "TG": -4, "CA": -9, "CT": -5, "CC": -6, "CG": -7, "GA": -9, "GT": -6, "GC": -4, "GG": 11}
Sequence ='CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG'

k=0
temp =''
for i in range(0,len(Sequence)-1):
    temp+=Sequence[i]
    temp+=Sequence[i+1]
    k+=Energy[temp]
    temp =''
print("Base Stacking Energy = ",k/(len(Sequence)-1))