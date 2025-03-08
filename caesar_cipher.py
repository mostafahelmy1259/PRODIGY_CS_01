def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        start = ord('A') if text[i].isupper() else ord('a')
        char = chr(start + (ord(text[i]) - start + key) % 26)
        result += char
    return result  # Added return statement


def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        start = ord('A') if text[i].isupper() else ord('a')
        char = chr(start + (ord(text[i]) - start + key) % 26)
        result += char
    return result  # Added return statement


message = input("Please enter a text: ")
key = int(input("Please enter a key: "))
cipher_method = input("Please choice to encrypt or decrypt: ")

if cipher_method == "encrypt":
    encrypted_message = encrypt(message, key)
    print(encrypted_message)

if cipher_method == "decrypt":
    decrypted_message = decrypt(message, key)
    print(decrypted_message)