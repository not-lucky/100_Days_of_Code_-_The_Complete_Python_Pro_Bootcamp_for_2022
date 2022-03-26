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


def create_phonetic_code():
    try:
        word = input('Enter a word.\n').upper()
        nato_list = [alpha[letter] for letter in word]
    except KeyError:
        print('Sorry only letters in the alphabet please.')
        create_phonetic_code()
    else:
        print(nato_list)


create_phonetic_code()
