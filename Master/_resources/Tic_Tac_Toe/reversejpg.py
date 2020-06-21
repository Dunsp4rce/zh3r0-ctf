with open("image", "rb") as file:
    bytes_rev = b""
    bytes_read  = bytearray(file.read())
    print(bytes_read)
    bytes_rev += bytes_read[::-1]
    with open("modified_image.jpg", "wb") as newfile:
        newfile.write(bytes_rev)