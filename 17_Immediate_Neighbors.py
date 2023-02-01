def IMMEDIATENEIGHBORS(Pattern):
    nucleotides = ['A', 'C', 'G', 'T']
    neighborhood = set()
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for nucleotide in nucleotides:
            if nucleotide != symbol:
                neighbor = Pattern[:i] + nucleotide + Pattern[i+1:]
                neighborhood.add(neighbor)
    return neighborhood

# This function takes a string Pattern as an input and returns all the immediate neighbors of Pattern as a set.
