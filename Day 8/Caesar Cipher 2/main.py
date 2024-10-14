import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
    return cipher_text

def decrypt(original_text, shift_amount):
    deciphered_text= ""
    for char in original_text:
        shifted_position = alphabet.index(char) - shift_amount
        deciphered_text += alphabet[shifted_position]
    print(deciphered_text)

def caesar(option, message, shift_amount):
    result = ""
    for char in message:
        if char not in alphabet:
            result += char
        else:
            if option == "decode":
                shifted_position = alphabet.index(char) - shift_amount
            else:
                shifted_position = alphabet.index(char) + shift_amount
                shifted_position %= len(alphabet)
            result += alphabet[shifted_position]
    print(f"Your {option}d result is: {result}")

play_again = True

while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    restart = input("Type 'yes' if you want to go again \n")
    if restart != "yes":
        play_again = False


