def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    Parameters:
        text (str): The message to encrypt or decrypt.
        shift (int): The number of positions to shift the alphabet.
        mode (str): 'encrypt' to encrypt, 'decrypt' to decrypt. Default is 'encrypt'.

    Returns:
        str: The resulting encrypted or decrypted text.
    """
    if mode == 'decrypt':
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == "__main__":
    print("Caesar Cipher Program")
    mode = input("Would you like to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    else:
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
            result = caesar_cipher(text, shift, mode)
            print(f"\nThe resulting text is: {result}")
        except ValueError:
            print("Shift value must be an integer.")
