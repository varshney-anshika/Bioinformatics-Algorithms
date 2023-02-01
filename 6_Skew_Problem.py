# Minimum Skew Problem:
# Find a position in a genome where the skew diagram attains a minimum.
# Input: A DNA string Genome.
# Output: All integer(s) i minimizing SKEWi(Genome) among all values of i
# (from 0 to |Genome|)

def minimum_skew(genome):
    n = len(genome)
    skew = [0] * (n + 1)
    for i in range(1, n + 1):
        if genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        elif genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        else:
            skew[i] = skew[i-1]
    min_skew = min(skew)
    return [i for i, x in enumerate(skew) if x == min_skew]


# This function takes one parameter:

# genome: a string representing the genome to calculate the skew for
# The function returns a list of integers representing the positions in the genome where the skew attains a minimum.