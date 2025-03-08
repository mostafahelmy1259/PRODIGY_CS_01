def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        start = ord('A') if text[i].isupper() else ord('a')
        char = chr(start + (ord(text[i]) - start + key) % 26)
        result += char
    print(result) 


def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        start = ord('A') if text[i].isupper() else ord('a')
        char = chr(start + (ord(text[i]) - start - key) % 26)
        result += char
    print(result)  


message = input("Please enter a text: ")
key = int(input("Please enter a key: "))
cipher_method = input("Please choice to encrypt or decrypt: ")

if cipher_method == "encrypt":
    encrypt(message, key)
elif cipher_method == "decrypt":
    decrypt(message, key)
else:
    exit()
   