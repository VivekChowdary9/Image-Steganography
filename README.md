# Image-Steganography
This Python script enables image steganography with password protection using OpenCV (`cv2`) and `hashlib`. The `msgtobinary` function converts data to binary. The `encode` function embeds a text message, prefixed with the hashed password, into an image. The `decode` function extracts and verifies the hidden message.
