from google.cloud import vision
from google.cloud.vision_v1 import AnnotateImageResponse


async def async_detect_image(base64_image):
    client = vision.ImageAnnotatorAsyncClient()

    response = await client.batch_annotate_images(

    )


def detect_product(image_bytes):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_bytes)

    response: AnnotateImageResponse = client.label_detection(image=image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return response.label_annotations
