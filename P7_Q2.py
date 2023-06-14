def calc_molecular_weight(sequence, weights):
   
    # Initialize total weight to 0
    total_weight =0
    temp = 0
    avg_weight = sum(weights.values()) / len(weights)

    # Loop through each character in the sequence
    for aa in sequence:
            temp += weights[aa]
    total_weight = temp - 18*(len(sequence)-1)

    return total_weight

# Define a dictionary with weights for each amino acid
weights = {'A': 85, 'C': 115, 'D': 130, 'E': 145,
           'F': 160, 'G': 70, 'H': 150, 'I': 125,
           'K': 145, 'L': 125, 'M': 143, 'N': 130,
           'P': 110, 'Q': 140, 'R': 170, 'S': 100,
           'T': 115,'V' :110,'W' :200,'Y' :175}

# Define an example sequence
s = input("Enter the sequence: \n")

# Calculate molecular weight using our function
molecular_weight = calc_molecular_weight(s.upper(), weights)

# Print result
print(f"The molecular weight of given sequence is {molecular_weight:.2f}")