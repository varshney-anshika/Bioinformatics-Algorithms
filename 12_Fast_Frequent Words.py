from collections import defaultdict

def faster_frequent_words(text, k):
    frequent_patterns = set()
    frequency = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        frequency[pattern] += 1
    max_count = max(frequency.values())
    for pattern, count in frequency.items():
        if count == max_count:
            frequent_patterns.add(pattern)
    return frequent_patterns

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print("Most frequent", k, "-mers in", text, ":", faster_frequent_words(text, k))


# In this example, the function faster_frequent_words computes the frequency of all k-mers in the input string text using the same approach as in the computing_frequencies function. Then, it identifies the most frequent k-mers by finding the maximum frequency in the frequency dictionary and adding all k-mers with that frequency to a set of frequent patterns. The function returns the set of frequent patterns.
