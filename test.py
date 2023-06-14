import numpy as np

# Define example sequences
sequences = [
    "ACGT",
    "AGGT",
    "ACCT",
    "AGGT",
    "ACGT",
]

def calculate_scores(sequences):
    """Calculate conservation scores for each position in an MSA."""
    # Convert sequences to a 2D array
    seq_array = np.array([list(seq) for seq in sequences])
    
    # Calculate frequency matrix
    freq_matrix = np.apply_along_axis(lambda x: np.bincount(x, minlength=20), axis=0, arr=seq_array)
    
    # Calculate entropy vector
    entropy_vector = -np.sum(freq_matrix * np.log2(freq_matrix), axis=1)
    
    # Calculate variance vector
    mean_freqs = np.mean(freq_matrix, axis=1)
    variance_vector = np.sum((freq_matrix - mean_freqs[:, None])**2, axis=1) / freq_matrix.shape
    
    # Calculate sum-of-pairs score vector
    sop_vector = []
    num_seqs, seq_len = seq_array.shape
    for i in range(seq_len):
        sop_score = 0
        for j in range(num_seqs):
            residue_j = seq_array[j,i]
            for k in range(j+1,num_seqs):
                residue_k = seq_array[k,i]
                if residue_j != '-' and residue_k != '-':
                    sop_score += 1 if residue_j == residue_k else 0
        sop_vector.append(sop_score)
    
    # Combine scores into final conservation score vector
    calculate_scores = (freq_matrix.max(axis=1) + entropy_vector + variance_vector + sop_vector) / 4
    
    return calculate_scores

# Example usage:
conservation_scores = calculate_scores(sequences)
print(conservation_scores)