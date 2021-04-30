from typing import List

from google.cloud import vision
from google.cloud.vision_v1 import AnnotateImageResponse


def detect_product(image_bytes) -> List[str]:
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_bytes)

    response: AnnotateImageResponse = client.label_detection(image=image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return [label.description for label in response.label_annotations]
