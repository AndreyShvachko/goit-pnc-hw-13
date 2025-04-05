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
    
def friedman_test(ciphertext):
    text = ''.join(filter(str.isalpha, ciphertext.upper()))
    N = len(text)
    if N <= 1:
        return 0, 0
    
    freq = Counter(text)
    numerator = sum(f * (f-1) for f in freq.values())
    denominator = N * (N - 1)
    IC = numerator / denominator if denominator != 0 else 0

    K = (0.0265 * N) / ((IC * (N - 1)) - 0.0385 * N + 0.065 * N)
    return round(K, 2), round(IC, 4)
    
#Приклад
plaintext = "CRYPTOGRAPHY IS FUN"
key = "KEY"

encrypted_vig = vigenere_encrypt(plaintext, key)
frequencies_vig = frequency_analysis(encrypted_vig)
decrypted_vig = vigenere_decrypt(encrypted_vig, key)
estimated_key_length, ic_value = friedman_test(encrypted_vig)

print("\n Vigenere Cipher")
print("Original: ", plaintext)
print("Encrypted: ", encrypted_vig)
print("Frequencies: ", dict(frequencies_vig))
print("Decrypted: ", decrypted_vig)
print("IC:", ic_value)
print("Estimated key length (Firedman):", estimated_key_length)