from collections import Counter
from math import log2

def unweighted_frequency(msa, position):
    """Calculate the unweighted frequency of residues at a given position in an MSA."""
    counts = Counter(seq[position] for seq in msa)
    return {residue: count / len(msa) for residue, count in counts.items()}

def entropy(msa, position):
    """Calculate the entropy of residues at a given position in an MSA."""
    frequencies = unweighted_frequency(msa, position)
    return -sum(p * log2(p) for p in frequencies.values())

def variance(msa, position):
    """Calculate the variance of residues at a given position in an MSA."""
    frequencies = unweighted_frequency(msa, position)
    mean = sum(frequencies.values()) / len(frequencies)
    return sum((p - mean) ** 2 for p in frequencies.values()) / len(frequencies)

def sum_of_pairs(msa, position):
    """Calculate the sum of pairs-based measure of residues at a given position in an MSA."""
    pairs = Counter((seq[position], seq[position + 1]) for seq in msa if len(seq) > position + 1)
    return sum(count for pair, count in pairs.items() if pair[0] != pair[1])

def conservation_scores(msa):
    """Calculate conservation scores for each position in an MSA."""
    scores = []
    for position in range(len(msa[0])):
        uf = unweighted_frequency(msa, position)
        e = entropy(msa, position)
        v = variance(msa, position)
        sp = sum_of_pairs(msa, position)
        score = {'position': position, 'unweighted_frequency': uf, 'entropy': e, 'variance': v, 'sum_of_pairs': sp}
        scores.append(score)
    return scores

# Define the MSA as a list of strings
msa = [
    "ACGT",
    "AGGT",
    "ACCT",
    "AGGT",
    "ACGT",
]

# Calculate the conservation scores
scores = conservation_scores(msa)

# Output the scores
for score in scores:
    print(score)
