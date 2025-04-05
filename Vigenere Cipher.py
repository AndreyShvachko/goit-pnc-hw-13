from collections import Counter

def frequency_analysis(text):
    filtered = [char for char in text.upper() if char.isalpha()]
    return Counter(filtered)


def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            encrypted_char = chr((ord(char) - 65 +shift) % 26 + 65)
            result  += encrypted_char
            key_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in cipher.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            result += decrypted_char
            key_index += 1
        else:
            result += char
        return result
    
#Приклад
plaintext = "CRYPTOGRAPHY IS FUN"
key = "KEY"

encrypted_vig = vigenere_encrypt(plaintext, key)
frequencies_vig = frequency_analysis(encrypted_vig)
decrypted_vig = vigenere_decrypt(encrypted_vig, key)

print("\n Vigenere Cipher")
print("Original: ", plaintext)
print("Encrypted: ", encrypted_vig)
print("Frequencies: ", dict(frequencies_vig))
print("Decrypted: ", decrypted_vig)