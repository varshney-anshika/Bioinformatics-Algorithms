# Approximate Pattern Matching Problem:
# Find all approximate occurrences of a pattern in a string.
# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

def approximate_pattern_matching(text, pattern, d):
    positions = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        match = 0
        for j in range(m):
            if text[i + j] != pattern[j]:
                match += 1
        if match <= d:
            positions.append(i)
    return positions

text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
pattern = "TAA"
d = 2

print("Approximate occurrences of", pattern, "in", text, "with at most", d, "mismatches:", approximate_pattern_matching(text, pattern, d))


# In this example, the function approximate_pattern_matching loops over the characters in the text and compares them to the corresponding characters in the pattern. If the characters differ, the match counter is incremented. If the number of mismatches is less than or equal to d, the current position is added to the list of positions. The function returns the list of positions where approximate matches were found.
