import re 
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
history = dict()
my_file = "ciphertext.txt"
charFrequency = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z']
decipherKey = dict()

def decoder(file):
    with open(file) as f:
        # read the whole file
        text = f.read()

    # pattern with regex
    chars = re.compile('[^A-Za-z0-9 ]+')
    # returns new string with all replacements
    words = re.sub(chars, ' ', text)
    # create an array of chars
    every_letter = [char for char in words]
    # count the letters and add to history
    for l in every_letter:
        # characters in the string are alphabets?
        if not l.isalpha():
            continue
        if l in history:
            history[l] += 1
        else:
            history[l] = 1


    count = 0
    # get the decipher keys
    for l in sorted(history.items(), key = lambda e: e[1], reverse=True):
        decipherKey[l[0]] = charFrequency[count]
        count += 1

    deciphered = ''

    for c in text:
        if c == 'â':
            deciphered += 'â'
            continue
        if not c.isalpha():
            deciphered += c
            continue

        deciphered += decipherKey[c]

    return deciphered


decrypted_text = decoder(my_file)

with open("decrypted_text.txt", "w") as file:
    file.write(decrypted_text)

# print(history)
# print('decipherKey ', decipherKey)


# Your code here
# charFrequency = {
#     'E': 11.53,
#     'T': 9.75,
#     'A': 8.46,
#     'O': 8.08,
#     'H': 7.71,
#     'N': 6.73,
#     'R': 6.29,
#     'I': 5.84,
#     'S': 5.56,
#     'D': 4.74,
#     'L': 3.92,
#     'W': 3.08,
#     'U': 2.59,
#     'G': 2.48,
#     'F': 2.42,
#     'B': 2.19,
#     'M': 2.18,
#     'Y': 2.02,
#     'C': 1.58,
#     'P': 1.08,
#     'K': 0.84,
#     'V': 0.59,
#     'Q': 0.17,
#     'J': 0.07,
#     'X': 0.07,
#     'Z': 0.03
# }