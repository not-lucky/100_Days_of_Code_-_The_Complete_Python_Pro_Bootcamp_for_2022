import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alpha = {
    row.letter: row.code
    for index, row in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()
}
# print(alpha)

# TODO 2. Create a list of the phonetic code words from a word that the user
# inputs.

word = input('Enter a word.\n').upper()
print([alpha[letter] for letter in word])