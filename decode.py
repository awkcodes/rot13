def rot13_decode(encoded_text):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - 13) % 26 + ascii_offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text


# Test the function
encoded_text = input("Enter the encoded text: ")
decoded_text = rot13_decode(encoded_text)
print("Decoded text:", decoded_text)

