def ITERATIVENEIGHBORS(Pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    neighborhood = set()
    neighborhood.add(Pattern)
    for i in range(d):
        for seq in neighborhood.copy():
            for j in range(len(seq)):
                for nucleotide in nucleotides:
                    if nucleotide != seq[j]:
                        neighbor = seq[:j] + nucleotide + seq[j+1:]
                        neighborhood.add(neighbor)
        neighborhood.discard(Pattern)
    return neighborhood

# This function takes a string Pattern and an integer d as inputs and returns all d-neighbors of Pattern as a set. The function iteratively generates neighbors by changing a single nucleotide of a d-1 neighbor at a time and adds them to the neighborhood.
