def rot13(text):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + 13) % 26 +
                               ascii_offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text


text = input("Enter a text to encode using ROT13: ")
encoded_text = rot13(text)
print("Encoded text:", encoded_text)
