def CLUMPFINDING(Genome, k, t, L):
    frequent_patterns = set()
    clump = [0] * (4**k)
    genome_length = len(Genome)
    
    for i in range(genome_length-L+1):
        window = Genome[i:i+L]
        frequency_array = COMPUTINGFREQUENCIES(window, k)
        for index in range(4**k):
            if frequency_array[index] >= t:
                clump[index] = 1
    
    for i in range(4**k):
        if clump[i] == 1:
            pattern = NUMBERTOPATTERN(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns

