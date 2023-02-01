# Clump Finding Problem:
# Find patterns forming clumps in a string.
# Input: A string Genome, and integers k, L, and t.
# Output: All distinct k-mers forming (L, t)-clumps in Genome.


def clump_finding(genome, k, L, t):
    clumps = set()
    for i in range(len(genome) - L + 1):
        window = genome[i:i+L]
        frequency_map = {}
        for j in range(len(window) - k + 1):
            pattern = window[j:j+k]
            if pattern in frequency_map:
                frequency_map[pattern] += 1
            else:
                frequency_map[pattern] = 1
        for pattern, count in frequency_map.items():
            if count >= t:
                clumps.add(pattern)
    return clumps

# This function takes four parameters:

# genome: a string representing the genome to search for clumps in
# k: the length of the pattern to search for
# L: the length of the window to consider for each search
# t: the minimum number of times a pattern must appear within the window to be considered a clump
# The function returns a set of strings representing the patterns that form clumps in the genome.