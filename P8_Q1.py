import matplotlib.pyplot as plt


h_val={"A": 13.85, "D": 11.61 ,'C': 15.37 ,'E': 11.38, 'F': 13.93 ,'G': 13.34, 'H': 13.82, 'I': 15.28 ,'K': 11.58 ,'L': 14.13 ,
'M': 13.86 ,'N': 13.02 ,'P': 12.35 ,'Q': 12.61, 'R': 13.10, 'S': 13.39, 'T': 12.70, 'V': 14.56 ,'W': 15.48, 'Y': 13.88}


seq1 = "FDCAEYRSTNIYGYGLYEVSMKPAKNTGIVSSFFTYTGPAHGTQWEIDIEFLGKDTTKVQFNYYTNGVGGHEKVISLGFDASKGFHTYAFDWQPGYIKWYVDGVLK"
seq2 ="KASEDLVKKHAGVLGAILKKKGHHEAELKPLAQSHATKAHKNIFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGY"
seq3 = "TVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA"
def plot(s):
  x = [i for i in range(len(s))]
  x1 = [i for i in s]
  y = []
  for i in s:
    y.append(h_val[i])
  plt.figure()
  plt.xlim(0,len(s))
  plt.plot(x,y,c="blue")
  plt.xticks(x)
  plt.xlabel('AA sequence')
  plt.ylabel('Hydrophobicity Index')
  plt.title('Relationship b/w Seq. no. & hydrophobocity profile')
  return y
y1 = plot(seq1)
y2 =plot(seq2)
y3=plot(seq3)
def Beta(seq,a):
    y = [h_val[i] for i in seq]
    ans_ran=[]
    for i in range(0,len(seq)-9):
        temp = [k for k in range(i,i+6,2) if y[k]>a]
        temp2 = [k for k in range(i+1,i+7,2) if y[k]<a]
        if len(temp)==len(temp2) and len(temp) >= 3:
            ans_ran.append((temp[0],temp2[-1]))
    return ans_ran


b1 = Beta(seq1,13.46)
b2 = Beta(seq2,13.46)
b3 = Beta(seq3,13.46)
print("beta strand in seq1 is in range",b1 )
print("beta strand in seq2 is in range",b2 )
print("beta strand in seq3 is in range",b3 )
def alpha_seq1(seq,a):
    y = [h_val[i] for i in seq]
    temp = []
    temp2 = []
    alpha = []
    for i in range(0, len(seq)-7):
      if (y[i] < a and y[i+1] < a) and (y[i+2] > a and y[i+3] > a) and (y[i+4] < a and y[i+5] < a) and (y[i+6] > a and y[i+7] > a):
        alpha.append((i,i+7))
      elif ((y[i] > a and y[i+1] > a) and (y[i+2] < a and y[i+3] < a)) and (y[i+4] > a and y[i+5] > a) and (y[i+6] < a and y[i+7] < a):
        alpha.append((i,i+7))
        
      else:
         continue  
    return alpha
al1=alpha_seq1(seq1,13.46)
al2=alpha_seq1(seq2,13.46)
al3=alpha_seq1(seq3,13.46)
print("alpha strand in seq1 is in range",al1 )
print("alpha strand in seq2 is in range",al2 )
print("alpha strand in seq3 is in range",al3 )

