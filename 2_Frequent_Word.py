# Frequent Words Problem:
# Find the most frequent k-mers in a string.
# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.


# Here is a Python function frequent_words that finds the most frequent k-mers (substrings of length k) in a text Text:
def frequent_words(Text, k):
    frequency_map = {}
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i + k]
        if pattern in frequency_map:
            frequency_map[pattern] += 1
        else:
            frequency_map[pattern] = 1

    max_count = max(frequency_map.values())
    frequent_patterns = [k for k, v in frequency_map.items() if v == max_count]
    return frequent_patterns
