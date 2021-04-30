from vision.detect import detect_product
from vision.helpers import read_image

hotdog = read_image("test_image/hotdog.jpg")
labels = detect_product(hotdog)
for label in labels:
    print(label.description)
