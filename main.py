# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def google_api_call(title, author):
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&inauthor:{author}&orderBy=relevance')

    return organize_google_response(response.json())


def img_check(unclean_list):
    image_format = "image/jpeg"
    for i in unclean_list:
        url = f'https://covers.openlibrary.org/b/isbn/{i}-L.jpg'
        site = urlopen(url)
        meta = site.info()
        try:
            meta['Content-Type'] in image_format
        except TypeError:
            pass
        else:
            return url


def organize_google_response(response_json):
    isbn_unclean_list = []
    for i in response_json['items']:
        try:
            check_ISBN(i["volumeInfo"]["industryIdentifiers"])
        except KeyError:
            pass
        else:
            isbn = i["volumeInfo"]["industryIdentifiers"][0]["identifier"]
            isbn_unclean_list.append(isbn)

    return img_check(isbn_unclean_list)


def check_ISBN(list_item):
    if "ISBN" in list_item[0]['type']:
        return True
    else:
        return False


@app.get("/get")
def return_URL(title, author):

    response_dict = google_api_call(title, author)
    return response_dict
