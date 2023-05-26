from io import BytesIO
import requests
from PIL import Image


class ImageUnreachable(Exception):
    pass


def img_overlay(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ImageUnreachable("File not reached, try again.")
    img1 = Image.open(BytesIO(response.content))
    img2 = Image.open(r"moldura.png").resize(size=img1.size)
    img1.paste(img2, (0, 0), mask=img2)
    return img1
