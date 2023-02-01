# Frequent Words with Mismatches Problem:
# Find the most frequent k-mers with mismatches in a string.
# Input: A string Text as well as integers k and d.
# Output: All most frequent k-mers with up to d mismatches in Text

from collections import defaultdict

def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

def generate_neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighbors = []
    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nucleotide in nucleotides:
                neighbors.append(nucleotide + neighbor)
        else:
            neighbors.append(pattern[0] + neighbor)
    return neighbors

def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = set()
    frequency_array = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        neighborhood = generate_neighbors(text[i:i + k], d)
        for neighbor in neighborhood:
            frequency_array[neighbor] += 1
    max_count = max(frequency_array.values())
    for pattern in frequency_array.keys():
        if frequency_array[pattern] == max_count:
            frequent_patterns.add(pattern)
    return frequent_patterns

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

print("Most frequent", k, "-mers with at most", d, "mismatches in", text, ":", frequent_words_with_mismatches(text, k, d))


# In this example, the function frequent_words_with_mismatches uses a recursive function generate_neighbors to generate all the k-mers that differ from a given k-mer by at most d mismatches. These k-mers are then counted and the k-mers with the highest count are returned as the result. The function hamming_distance calculates the Hamming distance between two strings, which is used by generate_neighbors. The frequency_array is a defaultdict that is used to count the frequency of each k-mer.

#CODE ALTERNATE
from itertools import combinations

def FREQUENTWORDSWITHMISMATCHES(Text, k, d):
    frequent_patterns = set()
    close = [0] * (4**k)
    frequency_array = [0] * (4**k)
    neighborhood = []
    for pattern in combinations(['A', 'C', 'G', 'T'], k):
        neighborhood.extend(NEIGHBORS(''.join(pattern), d))
    for pattern in neighborhood:
        index = PATTERNTONUMBER(pattern)
        close[index] = 1
    for i in range(len(Text)-k+1):
        neighborhood = NEIGHBORS(Text[i:i+k], d)
        for pattern in neighborhood:
            index = PATTERNTONUMBER(pattern)
            frequency_array[index] += 1
    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count and close[i] == 1:
            pattern = NUMBERTOPATTERN(i, k)
            frequent_patterns.add(pattern)
    return frequent_patterns

# Note: PATTERNTONUMBER, NUMBERTOPATTERN and NEIGHBORS functions are helper functions for this algorithm. You can find their implementation in my previous answers.