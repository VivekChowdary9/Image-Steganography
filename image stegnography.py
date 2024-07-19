import cv2
import numpy as np
import hashlib

def msgtobinary(msg):
    if isinstance(msg, str):
        result = ''.join(format(ord(i), "08b") for i in msg)
    elif isinstance(msg, bytes):
        result = ''.join(format(i, "08b") for i in msg)
    elif isinstance(msg, np.ndarray):
        result = [format(i, "08b") for i in msg.flatten()]
    elif isinstance(msg, (int, np.uint8)):
        result = format(msg, "08b")
    else:
        raise TypeError("Input type is not supported in this function")
    
    return result

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def encode_img_data(img, data, password):
    if len(data) == 0:
        raise ValueError('Data entered to be encoded is empty')

    hashed_password = hash_password(password)

    nameoffile = input("\nEnter the name of the New Image (Stego Image) after Encoding (with extension): ")
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    if not any(nameoffile.endswith(ext) for ext in valid_extensions):
        raise ValueError('Invalid file extension. Please use one of the following: ' + ', '.join(valid_extensions))

    no_of_bytes = (img.shape[0] * img.shape[1] * 3) // 8

    if len(data) > no_of_bytes:
        raise ValueError("Insufficient bytes Error, Need Bigger Image or give Less Data !!")

    data += '^^*'  # Ending delimiter for decoding

    data_to_encode = hashed_password + data  # Prepend the hashed password to the data
    binary_data = msgtobinary(data_to_encode)
    length_data = len(binary_data)

    index_data = 0

    for row in img:
        for pixel in row:
            r = msgtobinary(pixel[0])
            g = msgtobinary(pixel[1])
            b = msgtobinary(pixel[2])
            if index_data < length_data:
                pixel[0] = int(r[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data < length_data:
                pixel[1] = int(g[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data < length_data:
                pixel[2] = int(b[:-1] + binary_data[index_data], 2)
                index_data += 1
            if index_data >= length_data:
                break
        if index_data >= length_data:
            break

    cv2.imwrite(nameoffile, img)
    print("\nEncoded the data successfully in the Image and the image is successfully saved with name ", nameoffile)
    return data[:-3]  # Return the original data (without the delimiter)

def decode_img_data(img, password):
    hashed_password = hash_password(password)
    data_binary = ""
    for row in img:
        for pixel in row:
            r = msgtobinary(pixel[0])
            g = msgtobinary(pixel[1])
            b = msgtobinary(pixel[2])
            data_binary += r[-1]
            data_binary += g[-1]
            data_binary += b[-1]

            total_bytes = [data_binary[i:i+8] for i in range(0, len(data_binary), 8)]
            decoded_data = ""
            for byte in total_bytes:
                if len(byte) < 8:
                    continue
                decoded_data += chr(int(byte, 2))
                if decoded_data[-3:] == "^^*":
                    if decoded_data.startswith(hashed_password):
                        print("\n\nThe Encoded data which was hidden in the Image was: ", decoded_data[len(hashed_password):-3])
                        return decoded_data[len(hashed_password):-3]  # Return the decoded data (without the delimiter and password)
                    else:
                        raise ValueError("Incorrect password")
                    return

def img_steg():
    encoded_text = ""
    password = ""
    while True:
        print("\n\t\tIMAGE STEGANOGRAPHY OPERATIONS\n")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter the Choice: "))
        if choice1 == 1:
            image_path = input("Enter the path of the image to encode into: ")
            image = cv2.imread(image_path)
            if image is None:
                print("Error: Image not found or unable to read.")
                continue
            data = input("\nEnter the data to be Encoded in Image: ")
            password = input("Enter the password for encoding: ")
            encoded_text = encode_img_data(image, data, password)
        elif choice1 == 2:
            image_path = input("Enter the path of the image you need to decode (e.g., C:\\path\\to\\image.jpg): ")
            image1 = cv2.imread(image_path)
            if image1 is None:
                print("Error: Image not found or unable to read.")
                continue
            password = input("Enter the password for decoding: ")
            try:
                decoded_text = decode_img_data(image1, password)
                if decoded_text == encoded_text:
                    print("\nSuccess: The decoded text matches the encoded text.")
                else:
                    print("\nWarning: The decoded text does not match the encoded text.")
            except ValueError as e:
                print(e)
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")

if __name__ == "__main__":
    img_steg()
