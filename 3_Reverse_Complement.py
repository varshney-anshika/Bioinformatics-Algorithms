# Reverse Complement Problem:
# Find the reverse complement of a DNA string.
# Input: A DNA string Pattern.
# Output: Pattern, the reverse complement of Pattern.

# Here's a Python function reverse_complement that finds the reverse complement of a DNA string:

def reverse_complement(dna_string):
    complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement_list = [complement_map[base] for base in dna_string[::-1]]
    return "".join(reverse_complement_list)