def BETTERCLUMPFINDING(Genome, k, t, L):
    frequent_patterns = set()
    clump = [0] * (4**k)
    frequency_array = [0] * (4**k)
    genome_length = len(Genome)
    
    for i in range(genome_length-L+1):
        window = Genome[i:i+L]
        frequency_dict = {}
        for j in range(len(window)-k+1):
            pattern = window[j:j+k]
            index = PATTERNTONUMBER(pattern)
            frequency_dict[index] = frequency_dict.get(index, 0) + 1
        for index in frequency_dict.keys():
            if frequency_dict[index] >= t:
                clump[index] = 1
                frequency_array[index] += 1
    
    for i in range(4**k):
        if clump[i] == 1:
            pattern = NUMBERTOPATTERN(i, k)
            if frequency_array[i] == genome_length-L+1:
                frequent_patterns.add(pattern)
    
    return frequent_patterns
