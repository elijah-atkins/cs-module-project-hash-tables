# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

def letter_count(s):
    dictionary = {}
    special_characters = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\\", "\n", " ", "!", '—', "?", "'", "1"]

    for i in special_characters:
        s = s.replace(i, "")
    for letter in s:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1])
    return sorted_dictionary
''' letter count results for ciphertext
[('R', 4), ('T', 11), ('L', 11), ('V', 26), ('H', 91), ('P', 129), ('Z', 166), ('A', 242), ('F', 310), ('E', 335), ('Y', 336), ('B', 371), ('Q', 381), ('G', 397), ('O', 472), ('S', 602), ('U', 728), ('N', 853), ('I', 896), ('K', 966), ('D', 1033), ('C', 1183), ('X', 1240), ('M', 1299), ('J', 1497), ('W', 1769)]
'''

with open("ciphertext.txt") as f:
    words = f.read()

encode_table = {
    'A': 'C',   'B': 'F',   'C': 'H',   'D': 'N',   'E': 'M',
    'F': 'Y',   'G': 'U',   'H': 'V',   'I': 'I',   'J': 'T',
    'K': 'R',   'L': 'X',   'M': 'A',   'N': 'S',   'O': 'W',
    'P': 'K',   'Q': 'G',   'R': 'K',   'S': 'L',   'T': 'J',
    'U': 'D',   'V': 'Q',   'W': 'E',   'X': 'O',   'Y': 'B',
    'Z': 'P',   
}


def encode(s):
    new_letter = ""
    for i in s:
        if i in encode_table:
            new_letter += encode_table[i]
        else:
            new_letter += i
    return new_letter

print(encode(words))


