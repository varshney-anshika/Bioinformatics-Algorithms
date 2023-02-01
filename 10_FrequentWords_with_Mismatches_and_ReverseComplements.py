# Frequent Words with Mismatches and Reverse Complements Problem:
# Find the most frequent k-mers (with mismatches and reverse complements) in a string.
# Input: A DNA string Text as well as integers k and d.
# Output: All k-mers Pattern that maximize the sum COUNTd(Text, Pattern) + COUNTd(Text, Pattern) over all possible k-mers.

from collections import defaultdict

def reverse_complement(text):
    reverse = text[::-1]
    complement = ''
    for char in reverse:
        if char == 'A':
            complement += 'T'
        elif char == 'C':
            complement += 'G'
        elif char == 'G':
            complement += 'C'
        elif char == 'T':
            complement += 'A'
    return complement

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

def frequent_words_with_mismatches_and_reverse_complement(text, k, d):
    frequent_patterns = set()
    frequency_array = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        neighborhood = generate_neighbors(text[i:i + k], d) + generate_neighbors(reverse_complement(text[i:i + k]), d)
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

print("Most frequent", k, "-mers (with mismatches and reverse complements) in", text, ":", frequent_words_with_mismatches_and_reverse_complement(text, k, d))


# In this example, the function frequent_words_with_mismatches_and_reverse_complement generates all the k-mers that differ from a given k-mer by at most d mismatches and their reverse complements, using the generate_neighbors function. The function hamming_distance calculates the Hamming distance between two strings, which is used by generate_neighbors. The frequency_array is a defaultdict that is used to count the frequency of each k-mer. The reverse_complement function generates the reverse complement of a string. The results are the k-mers with the highest count.
