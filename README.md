# PRODIGY_CS_02
Image Encryption using pixel manipulation

This encrytion method utilizes the manipulation of pixels such as changing every pixel's property and translocating pixels in the image.
Here, The Image is taken and changed into an array of pixels.
Then, I make the image go through two layers of encryption:
Changing the RGB values of every pixel by XORing them with a Psuedo-random value that can be determined using the Key being used
After the RGB values are altered, The pixels are translocated such that the pixels taken row-wise are arranged column-wise
The resulting array is again constructed into an image and saved as an Encrypted image.

The decrypt_image function takes the encrypted image and the key and reverses the translocation and RGB value XORing process to return the original image.
Thus successfully decrypting the image.
