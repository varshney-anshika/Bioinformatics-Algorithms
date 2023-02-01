def finding_frequent_words_by_sorting(text, k):
    frequency_array = compute_frequency_array(text, k)
    max_count = max(frequency_array.values())
    frequent_words = []
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_words.append(pattern)
    return frequent_words

def compute_frequency_array(text, k):
    frequency_array = {}
    for i in range(4**k):
        frequency_array[i] = 0
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array

def pattern_to_number(pattern):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    for i, nucleotide in enumerate(reversed(pattern)):
        number += nucleotides[nucleotide] * (4 ** i)
    return number

def number_to_pattern(index, k):
    nucleotides = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        nucleotide_index = index % 4
        pattern = nucleotides[nucleotide_index] + pattern
        index = index // 4
    return pattern

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print("Frequent ", k, "-mers in text:", finding_frequent_words_by_sorting(text, k))

# In this example, the finding_frequent_words_by_sorting function finds the most frequent k-mers in a DNA text. It first calls the compute_frequency_array function to compute the frequency array of all possible k-mers in the text. The function then finds the maximum frequency by using the max function on the values of the frequency array. The function then iterates over all possible k-mers represented as numbers, and adds the k-mer represented by a number to the frequent_words list if its frequency is equal to the maximum frequency. Finally, the function returns the frequent_words list, which contains all the most frequent k-mers. The compute_frequency_array function computes the frequency array by initializing a frequency array of all possible k-mers represented as numbers, and then updating the frequency of each k-mer as it iterates over the text. The pattern_to_number and number_to_pattern functions are used to convert between k-mer patterns and their number representations.
