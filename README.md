# Image-Steganography
This Python script enables image steganography with password protection using OpenCV (`cv2`) and `hashlib`. The `msgtobinary` function converts data to binary. The `encode` function embeds a text message, prefixed with the hashed password, into an image. The `decode` function extracts and verifies the hidden message.
Image Steganography
Image steganography is a technique used to hide information within an image file. It aims to conceal data in a way that makes it undetectable to the human eye. The primary goal is to secure the hidden data from unauthorized access while keeping the image visually unchanged. This method is widely used in covert communication, digital watermarking, and protecting sensitive information.

**Types of Image Steganography:**
1. Least Significant Bit (LSB) Steganography:

Description: Modifies the least significant bits of the pixel values. For instance, in an 8-bit image, only the last bit of each color channel is altered to encode the data. This method is simple and commonly used due to its minimal impact on the image quality.

2. Masking and Filtering:

Description: Data is embedded in the image using more complex methods such as filtering and masking. This approach can be more robust against detection as manipulates image characteristics beyond simple pixel values.

3. Transform Domain Techniques:

Description: Embeds data in the transformed domain (e.g., using Discrete Cosine Transform (DCT) or Discrete Wavelet Transform (DWT)). This technique adjusts image coefficients rather than pixel values, making it more resilient to image processing operations.

4. Palette-Based Steganography:
Description: Works with images that use a color palette. Data is hidden by altering the color indices in the palette, which changes the color representation of the image subtly.

**CODE EXPLANATION **
The provided Python code implements image steganography with password protection, allowing users to hide and retrieve text messages in images. 

### Key Components:

1. **Libraries**:
   - **OpenCV (`cv2`)**: For image handling and processing.
   -** PIP COMMAND ** : pip install opencv-python
   - **NumPy**: To work with image data as arrays.
   - **PIP COMMAND** : pip install numpy
   - **Hashlib**: To hash passwords securely.


2. **Functions**:
   - **`msgtobinary(msg)`**: Converts various data types (strings, bytes, numpy arrays) into binary format.
   - **`hash_password(password)`**: Hashes the given password using SHA-256.
   - **`encode_img_data(img, data, password)`**: Embeds a text message (with the hashed password) into an image by modifying pixel values. It saves the modified image with a new name and returns the original message.
   - **`decode_img_data(img, password)`**: Extracts and verifies the hidden message from the image using the provided password. It ensures that the decoded message starts with the hashed password.

3. **Command-Line Interface (`img_steg`)**:
   - Offers options to encode or decode messages.
   - For encoding, it prompts for the image path, text message, and password. It then uses `encode_img_data` to process the image.
   - For decoding, it prompts for the image path and password, using `decode_img_data` to extract and verify the hidden message.

Overall, the script provides a secure way to encode and decode messages in images using passwords for added protection.

The provided code is an implementation of image steganography, which is a technique for hiding text data within an image. This is done by manipulating the least significant bits of the image’s pixel values, specifically in the Red-Green-Blue (RGB) color model.
In this code, RGB is used to encode and decode hidden messages. The image is processed pixel by pixel, where each pixel's red, green, and blue components are modified to store binary data. The message is first converted into a binary format and then embedded into the least significant bits of the pixel values. This way, the changes are minimal and the image remains visually unchanged to the human eye.

**EXECUTION **

Encode 
![encode](https://github.com/user-attachments/assets/26402cd7-385e-47af-92e0-4af05e059efa)

Decode
![decode](https://github.com/user-attachments/assets/78fc09bf-64c8-427e-b1b6-4d9b743f84ec)

**IMAGES**
| hacker.jpg | encrypted.png |
|:--------:|:-------:|
| <img src="cybersecurity.jpg" alt="Original Image" width="400"/> | <img src="encrypted.png" alt="Encoded Image" width="400"/> |
| Original | Encoded |
