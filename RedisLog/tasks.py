from django_rq import job
from .azure_blob_handler import blob_downloader
import time as t
import requests as req
import json


@job('azure')
def timer_queue():
    t.sleep(60)  # sleep 60 seconds


# image Azure OCR queue
@job('azure')
def azure_OCR(container_name, image_name):

    # prepare request
    azure_key = 'b630d1ac2aab47e9ba797fcbb5c25ae5'
    post_url = 'https://canadacentral.api.cognitive.microsoft.com/vision/v3.0/ocr?language=unk&detectOrientation=true'
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': azure_key}

    # get container, download, convert image to raw binary
    downloaded_url = blob_downloader(container_name, image_name)
    print(downloaded_url)
    with open(downloaded_url, "rb") as image:
        f = image.read()
        b = bytearray(f)
        print(len(b))
        data = b[0]

    # send request to Azure OCR
    result = req.post(post_url, json=data, headers=headers)
    print(json.dumps(result.text, indent=4))
