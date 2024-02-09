def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (a number between 0 and 25): "))
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted/Decrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
