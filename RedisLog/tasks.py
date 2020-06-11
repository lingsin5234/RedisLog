from django_rq import job
import time as t
import requests as req
import json


@job('azure')
def timer_queue():
    t.sleep(60)  # sleep 60 seconds


# image Azure OCR queue
@job('azure')
def azure_OCR(container):

    # prepare request
    azure_key = 'b630d1ac2aab47e9ba797fcbb5c25ae5'
    post_url = 'https://canadacentral.api.cognitive.microsoft.com/vision/v3.0/ocr?language=unk&detectOrientation=true'
    headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': azure_key}

    # get container

    data = {"url":"https://blobstorage005234.blob.core.windows.net/quickstartf307c613-1e65-4bb2-8e8a-4fd731cd0cdb.txt"}

    # send request to Azure OCR
    result = req.post(post_url, json=data, headers=headers)
    print(json.dumps(result.text, indent=4))
