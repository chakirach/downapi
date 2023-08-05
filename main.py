
from typing import Union
from fastapi import FastAPI
import requests
import json
import time
from fastapi.responses import RedirectResponse, HTMLResponse
import random

app = FastAPI()

def channelsearch(channel):
  url = "https://all-media-downloader.p.rapidapi.com/download"
  print(channel)
  payload = { "url": channel }
  headers = {
  	"content-type": "application/x-www-form-urlencoded",
  	"X-RapidAPI-Key": "a3e5a1eba4mshaac9e2bcc2d9949p1eec49jsn6230f553eb03",
  	"X-RapidAPI-Host": "all-media-downloader.p.rapidapi.com"
  }
  response = requests.post(url, data=payload, headers=headers)
  jess_dict2 = json.loads(response.text)
  return jess_dict2


@app.get("/")
def read_root():
    return {"Hello": "yes22"}
  
@app.get("/gotolink2/{item_id}")
def gotolink2(item_id: str, q: Union[str, None] = None):
    print(jess_dict2)
    return {item_id}

@app.get("/gotolink3/{item_id}")
def gotolink3(item_id: str, q: Union[str, None] = None):
    url2 = "https://all-media-downloader.p.rapidapi.com/download"
    print(item_id)
    print("heeloooo")
    payload = { "url": str(item_id) }
    headers = {
    	"content-type": "application/x-www-form-urlencoded",
    	"X-RapidAPI-Key": "a3e5a1eba4mshaac9e2bcc2d9949p1eec49jsn6230f553eb03",
    	"X-RapidAPI-Host": "all-media-downloader.p.rapidapi.com"
    }
    response = requests.post(url2, data=payload, headers=headers)
    jess_dict2 = json.loads(response.text)
    print(jess_dict2)
    return {jess_dict2}

@app.get("/gotolink/{item_id}")
async def gotolink(item_id: str, q: Union[str, None] = None):
    link=getlinkfromid(item_id)
    if link!="false":
        response = RedirectResponse(url=link,status_code=303)
    else:
        response = RedirectResponse(url="https://drive.google.com/uc?id=1ixtBSHFEMH9zyDkRNLU79hYSpA5ZHAd&export=download",status_code=303)

    return response
