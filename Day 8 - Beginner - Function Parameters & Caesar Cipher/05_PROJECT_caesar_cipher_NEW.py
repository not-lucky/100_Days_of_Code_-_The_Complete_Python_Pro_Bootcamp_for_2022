alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction.lower() == 'encode' or direction.lower() == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
    def caesar(direction, text, shift):
        characters_list_and_numbers = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        if shift > 26:
            shift = shift % 26

        new_text = ''
        for letter in text:
            if letter in characters_list_and_numbers:
                new_text += letter
                continue
            if direction == 'encode':
                new_text += alphabet[alphabet.index(letter) + shift]
            else:
                new_text += alphabet[(alphabet.index(letter) + 26) - shift]

        print(f'The {direction}d code is:\n{new_text}')

    #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(direction=direction, text=text, shift=shift)
else:
    print('Type correct keywords please.')