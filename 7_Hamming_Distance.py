# Hamming Distance Problem:
# Compute the Hamming distance between two strings.
# Input: Two strings of equal length.
# Output: The Hamming distance between these strings.

def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

str1 = "AGCTA"
str2 = "AGCTC"

print("Hamming distance between", str1, "and", str2, "is:", hamming_distance(str1, str2))


# In this example, the Hamming distance between the two strings is calculated by looping over the characters in each string and counting the number of positions where the characters are different. If the two strings have different lengths, an error will be raised. You can add an error check for this case if needed.
