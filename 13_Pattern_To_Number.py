def pattern_to_number(pattern):
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    for i, nucleotide in enumerate(reversed(pattern)):
        number += nucleotides[nucleotide] * (4 ** i)
    return number

pattern = "AGT"

print("Number representation of pattern", pattern, ":", pattern_to_number(pattern))

# In this example, the function pattern_to_number converts a DNA pattern into a number representation. It uses a dictionary nucleotides to map each nucleotide ('A', 'C', 'G', or 'T') to a number (0, 1, 2, or 3). The function then iterates over the pattern, starting from the end, and adds the number representation of each nucleotide to the number variable, multiplied by 4 raised to the power of the position of the nucleotide in the pattern (starting from 0). Finally, the function returns the number variable, which is the number representation of the pattern.



def number_to_pattern(index, k):
    nucleotides = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        nucleotide_index = index % 4
        pattern = nucleotides[nucleotide_index] + pattern
        index = index // 4
    return pattern

index = 45
k = 4

print("Pattern representation of number", index, ":", number_to_pattern(index, k))

# In this example, the function number_to_pattern converts a number into a DNA pattern representation. It uses a list nucleotides to map each number (0, 1, 2, or 3) to a nucleotide ('A', 'C', 'G', or 'T'). The function then iterates k times, starting from 0, and adds the nucleotide representation of the remainder of index divided by 4 to the beginning of the pattern string. The function then updates the index variable by floor-dividing it by 4. Finally, the function returns the pattern string, which is the DNA pattern representation of the number.
