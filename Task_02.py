from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypts an image by applying a mathematical operation to each pixel.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the encrypted image.
        key (int): Encryption key (integer).
    """
    # Open the image and convert to array
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # Encrypt the pixels
    encrypted_array = (image_array + key) % 256  # Ensure pixel values remain in 0-255
    
    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypts an image encrypted with the encrypt_image function.
    
    Args:
        input_path (str): Path to the encrypted image.
        output_path (str): Path to save the decrypted image.
        key (int): Decryption key (integer).
    """
    # Open the encrypted image and convert to array
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # Decrypt the pixels
    decrypted_array = (image_array - key) % 256  # Ensure pixel values remain in 0-255
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    print("Image Encryption Tool")
    mode = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    else:
        input_path = input("Enter the path to the input image: ").strip()
        output_path = input("Enter the path to save the output image: ").strip()
        try:
            key = int(input("Enter the key (integer): "))
            if mode == "encrypt":
                encrypt_image(input_path, output_path, key)
            else:
                decrypt_image(input_path, output_path, key)
        except ValueError:
            print("The key must be an integer.")
