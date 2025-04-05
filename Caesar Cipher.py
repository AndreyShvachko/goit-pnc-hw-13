from collections import Counter

def caesar_encrypt(text, shift):
    result =""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 +shift) % 26 + 65)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, - shift)


def frequency_analysis(text):
    filtered = [char for char in text.upper() if char.isalpha()]
    return Counter(filtered)


#Приклад
original_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
shift = 3
encrypted = caesar_encrypt(original_text, shift)
frequencies = frequency_analysis(encrypted)
decrypted = caesar_decrypt(encrypted, shift)


print("Caesar Cipher")
print("Original: ", original_text)
print("Encrypted: ", encrypted)
print("Frequencies: ", dict(frequencies))
print("Decrypted: ", decrypted)

