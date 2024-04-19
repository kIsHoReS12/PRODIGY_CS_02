from PIL import Image
import numpy as np
import random

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    img_array = np.array(img)
    imgrows=len(img_array)
    imgpixperrow=len(img_array[0])
    rowval=0
    pixval=0
    random.seed(key)
    random_key1 = random.randint(0, 255)
    random_key2 = random.randint(0, 255)
    
    encrypted_img_array = np.bitwise_xor(img_array, random_key1)
    encrypted_img_array = np.bitwise_xor(encrypted_img_array, random_key2)
    half_encryted_array = encrypted_img_array.copy()
    for x in half_encryted_array:
        for y in x:
            if(pixval>=imgrows):
                pixval=0
                rowval+=1
            encrypted_img_array[pixval][rowval]=y
            pixval+=1
    encrypted_img = Image.fromarray(encrypted_img_array)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img = encrypted_img.convert("RGB")
    encrypted_img_array = np.array(encrypted_img)
    imgrows=len(encrypted_img_array)
    imgpixperrow=len(encrypted_img_array[0])
    rowval=0
    pixval=0
    random.seed(key)
    random_key1 = random.randint(0, 255)
    random_key2 = random.randint(0, 255)
    
    half_decrypted_array=encrypted_img_array.copy()
    for x in range(imgpixperrow):
        for y in range(imgrows):
            if(pixval>=imgpixperrow):
                pixval=0
                rowval+=1
            half_decrypted_array[rowval][pixval]=encrypted_img_array[y][x]
            pixval+=1
    decrypted_array = np.bitwise_xor(half_decrypted_array, random_key2)
    decrypted_array = np.bitwise_xor(decrypted_array, random_key1)    
    
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

if __name__=="__main__":
    image_path = "sample_cyber_img.png"
    key = 12345
    encrypt_image(image_path, key)
    decrypt_image("encrypted_image.png", key)