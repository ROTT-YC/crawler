from PIL import Image
from io import BytesIO
import requests, io, time

def load_pic(dict_img, img_path):
    # webp transition
    if dict_img.endswith("webp"):
        res = requests.get(dict_img, stream = True)
        img = Image.open(BytesIO(res.content))
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format = 'JPEG')
        imgByteArr = imgByteArr.getvalue()

        with open(img_path, 'wb') as f:
            f.write(imgByteArr)

    else:
        img = requests.get(dict_img)
        with open(img_path, 'wb') as f:
            f.write(img.content)
        time.sleep(3)