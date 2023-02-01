from collections import defaultdict

def computing_frequencies(text, k):
    frequency = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        frequency[pattern] += 1
    return frequency

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print("Frequency of all", k, "-mers in", text, ":", computing_frequencies(text, k))

# In this example, the function computing_frequencies loops over all possible k-mers in the input string text and increments the count of each k-mer in the frequency dictionary. The function returns the frequency of all k-mers in the string.
