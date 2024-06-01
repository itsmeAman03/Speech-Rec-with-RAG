import requests
from imports import URL
from dotenv import load_dotenv

def text_to_text_translate(in_lang:str,out_lang:str,text_in:str)-> str:
    load_dotenv()
    payload = {
        "source": in_lang,
        "target": out_lang,
        "q": text_in
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": X-RapidAPI-Key,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(URL, data=payload, headers=headers)

    text = response["data"]["translations"][0]['translatedText']
    return text