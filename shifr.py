def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

text = input("Введите текст: ")
shift = int(input("Введите шаг сдвига: "))

encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст: ", encrypted_text)

decrypted_text = caesar_decipher(encrypted_text, shift)
print("Расшифрованный текст: ", decrypted_text)