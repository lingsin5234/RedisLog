from django_rq import job
import time as t
import requests as req


@job
def timer_queue():
    t.sleep(60)  # sleep 60 seconds


# image Azure OCR queue
@job
def azure_OCR():

    # send the image to azure
    azure_key = 'b630d1ac2aab47e9ba797fcbb5c25ae5'
    post_url = 'https://canadacentral.api.cognitive.microsoft.com/vision/v3.0/ocr?language=unk&detectOrientation=true'
    headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': azure_key}
    data = {"url":"https://portfolio.sinto-ling.ca/static/img/receipt-images/shoppers.jpg"}
    result = req.post(post_url, data, headers=headers)
    print(result)
    print(result.text)
