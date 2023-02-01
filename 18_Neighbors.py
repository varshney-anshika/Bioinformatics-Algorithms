def NEIGHBORS(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()
    suffix_neighbors = NEIGHBORS(Pattern[1:], d)
    for text in suffix_neighbors:
        if HammingDistance(Pattern[1:], text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(Pattern[0] + text)
    return neighborhood

# This function takes a string Pattern and an integer d as inputs and returns all d-neighbors of Pattern as a set. The function uses a helper function HammingDistance to calculate the Hamming distance between two strings.


