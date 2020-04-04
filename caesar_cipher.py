# given a string, print the Caeser Cipher of that string
# get user input as a string and lowercase the input
inp = input("Give me a string, please: ").upper()
# set up an empty list for the new string
new_string = []
# convert each letter in the string to ordinal value
for letter in inp:
    letter = ord(letter)
    # subtract 13 from each ordinal value
    letter -= 13
    # letter = ((letter - 13) % 65) + 90
    # convert ordinal value back to character value
    letter = chr(letter)
    new_string.append(letter)
# convert list to string
new_string = ''.join(new_string)
print(new_string)