def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        elif '0' <= char <= '9':
            # Handle numbers
            encrypted_text += chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
        else:
            # Keep other characters (spaces, punctuation) as they are
            encrypted_text += char
    return encrypted_text