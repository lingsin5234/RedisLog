from django_rq import job
from .azure_blob_handler import blob_downloader
from .oper import database_structure as ds
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
        data = b

    # send request to Azure OCR
    result = req.post(post_url, data=data, headers=headers)
    print(json.dumps(result.text, indent=4))

    # update database that this one is completed
    query = 'UPDATE mnl_load_receipt SET processed_bool=? WHERE container_name=? AND image_name=?'
    c = ds.engine.connect()
    c.execute(query, True, container_name, image_name)

    # check that it has been processed
    query = 'SELECT * FROM mnl_load_receipt WHERE processed_bool=?'
    results = c.execute(query, True).fetchall()
    print(results)
    c.close()

    # add a time delay for some latency
    t.sleep()
