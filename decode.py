import sys


def rot13_decode(encoded_text):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - 13) % 26 +
                               ascii_offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text


# rotate 13 nums in the unicode
def rot13uc_decode(text):
    decoded_text = ""
    for char in text:
        encoded_char = chr(ord(char) - 13)
        decoded_text += encoded_char
    return decoded_text


encoded_text = input("Enter the encoded text: ")
if len(sys.argv) >= 2 and sys.argv[1] == "-u":
    decoded_text = rot13uc_decode(encoded_text)
else:
    decoded_text = rot13_decode(encoded_text)
print("Decoded text:", decoded_text)
