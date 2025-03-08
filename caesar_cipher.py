def encrypt(text, key):
    result = ""
    for i in range(len(message)):
        #print(message[i])
        start = ord('A') if message[i].isupper() else ord('a')
        char = chr(start + (ord(message[i]) - start + key) % 26)
        result += char


message = input("Please enter a text: ")
key = int(input("Please enter a key: "))
cipher_method = input("Please choice to encrypt or decrypt: ")


if cipher_method == "encrypt":
    encrypted_message = encrypt(message, key)
    print(encrypted_message)