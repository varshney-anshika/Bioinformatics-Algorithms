# Pattern Matching Problem:
# Find all occurrences of a pattern in a string.
# Input: Strings Pattern and Genome.
# Output: All starting positions in Genome where Pattern appears as a sub-string.

def find_occurrences(text, pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences
