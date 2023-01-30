# Finding Origin of Replication Problem:
# Input: A DNA string Genome.
# Output: The location of oriC in Genome.

def pattern_count(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count