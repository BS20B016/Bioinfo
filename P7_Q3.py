data = {
    'A': [8.47, 8.95],
    'D': [5.97, 5.91],
    'C': [1.39, 0.47],
    'E': [6.32, 4.78],
    'F': [3.91, 3.68],
    'G': [7.82, 8.54],
    'H': [2.26, 1.25],
    'I': [5.71, 4.77],
    'K': [5.76, 4.93],
    'L': [8.48, 8.78],
    'M': [2.21, 1.56],
    'N': [4.54, 5.74],
    'P': [4.63, 3.74],
    'Q': [3.82, 4.75],
    'R': [4.93, 5.24],
    'S': [5.94, 8.05],
    'T': [5.79, 6.54],
    'V': [7.02, 6.76],
    'W': [1.44, 1.24],
    'Y': [3.58, 4.13]
}

s = input("Enter the sequencde:\n")

occurrence = {"A": [0,85],  "C": [0,115], "R": [0,170], "N": [0,130], "D": [0,130],
        "E": [0,145], "Q": [0,145], "G": [0,70],  "H": [0,150], "I": [0,125],
        "L": [0,125], "K": [0,145], "M": [0,143], "F": [0,160], "P": [0,110],
        "S":[0,100],  "T": [0,115], "W": [0,200], "Y": [0,175], "V": [0,110] }

composition = {}
for i in s:
    occurrence[i][0] += 1   
for i in occurrence:
    composition[i] = (occurrence[i][0]/len(s))*100     
for i in range(2):
    sum1 = 0
    if i == 0:
        sum2 = 0
        for j in occurrence:
            sum2 += abs(data[j][0] - composition[j])
    if i == 1:
        for j in occurrence:
            sum1 += abs(data[j][1] - composition[j])             
if sum2 > sum1:
    print("The given sequence belongs to Group B")
else:
    print("The given sequence belongs to Group A") 

