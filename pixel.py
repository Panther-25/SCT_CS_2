from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key=50):
    try:
        img = Image.open(image_path).convert("RGB")
        arr = np.array(img)
        encrypted_arr = np.bitwise_xor(arr, key)
        encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))
        encrypted_img.save("encrypted.png")
        print("✅ Image Encrypted and saved as encrypted.png")
        return encrypted_img
    except Exception as e:
        print("❌ Error during encryption:", e)

def decrypt_image(image_path, key=50):
    try:
        img = Image.open(image_path).convert("RGB")
        arr = np.array(img)
        decrypted_arr = np.bitwise_xor(arr, key)
        decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))
        decrypted_img.save("decrypted.png")
        print("✅ Image Decrypted and saved as decrypted.png")
        return decrypted_img
    except Exception as e:
        print("❌ Error during decryption:", e)

if __name__ == "__main__":
    file_path = input("Enter path to image (e.g., input.png): ").strip()

    if os.path.exists(file_path):
        try:
            key = int(input("Enter encryption key (1–255): "))
            if not (1 <= key <= 255):
                raise ValueError("Key must be between 1 and 255.")

            # Encrypt
            encrypted = encrypt_image(file_path, key)

            # Decrypt
            if encrypted:
                decrypt_image("encrypted.png", key)

        except ValueError as ve:
            print("❌ Invalid input:", ve)
    else:
        print("❌ File does not exist.")
