def read_image(file_path):
    with open(file_path, "rb") as image_file:
        image_bytes = image_file.read()

    return image_bytes
