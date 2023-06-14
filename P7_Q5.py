values ={  
        "A":[13.85 , 20.00 , 1.90],
        "D":[11.61,26.00,1.52],
        "C": [15.37,25,2.04],
        "E": [11.38,33,1.54],
        "F":[13.93,46,1.86],
        "G": [13.34,13,1.90],
        "H": [13.82,37,1.76],
        "I": [15.28,39,1.95],
        "K": [11.58,46,1.37],
        "L": [14.13,35,1.97],
        "M": [13.86,43,1.96],
        "N": [13.02,28,1.56],
        "P": [12.35,22,1.70],
        "Q": [12.61,36,1.52],
        "R":[13.10,55,1.48],
        "S": [13.39,20,1.75], 
        "T": [12.70,28,1.77],
        "V": [14.56,33,1.98],
        "W":[15.48,61,1.87],
        "Y":[13.88,46,1.69]
}
seql = []
s = input("Enter the sequence :\n")
seql.append(s)
dictf={}

sum = 0
finalsum = [[],[],[]]
for i in seql:
    sumhgm = 0
    sumca=0
    sumet = 0
    for j in range(len(i)) :
       if i[j] in values:
         sumhgm+= values[i[j]][0]
         sumca+= values[i[j]][1]
         sumet+=values[i[j]][2]


    finalsum[0].append(sumhgm)
    finalsum[1].append(sumca)
    finalsum[2].append(sumet)

for i in range(len(seql)):
    print("The hydrophobicity of sequence is ",finalsum[0][i] )
    print(" The Helical contact area (Ca) of sequence is: ", finalsum[1][i])
    print(" The Total non-bonded energy(Et) of sequence is: ", finalsum[2][i])    


      
   