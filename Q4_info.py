match_score = 2
mismatch_score = -1
gap_penalty = -2

seq1 = "ACAGTCGAACG"
seq2 = "ACCGTCCG"

# Allocate the memory for the dynamic programming matrices
m = len(seq1)
n = len(seq2)
dp_matrix = [[0] * (n + 1) for _ in range(m + 1)]
pointer_matrix = [[0] * (n + 1) for _ in range(m + 1)]

# Initialize the dynamic programming matrices
for i in range(m + 1):
    dp_matrix[i][0] = i * gap_penalty
    pointer_matrix[i][0] = 1
for j in range(n + 1):
    dp_matrix[0][j] = j * gap_penalty
    pointer_matrix[0][j] = 2

# Fill in the dynamic programming matrices
for i in range(1, m + 1):
    for j in range(1, n + 1):
        match = dp_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
        delete_op = dp_matrix[i-1][j] + gap_penalty
        insert_op = dp_matrix[i][j-1] + gap_penalty
        dp_matrix[i][j] = max(match, delete_op, insert_op)

        if dp_matrix[i][j] == match:
            pointer_matrix[i][j] = 3
        elif dp_matrix[i][j] == delete_op:
            pointer_matrix[i][j] = 1
        else:
            pointer_matrix[i][j] = 2

# Print the dynamic programming matrix
for row in dp_matrix:
    print(row)
