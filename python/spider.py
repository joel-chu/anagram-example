# spider.py
# take the word from the db then query dictionary.com to get the
# meaning of the word then store it in the db
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.dictionary.com"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
         "Cookie": "your cookie"}


def getUrl(word):
    return f"{BASE_URL}/browse/{word}"


def getHtmlDoc(word):
    res = requests.get(getUrl(word), headers = header)
    if (res.status_code == 200):
        return BeautifulSoup(res.text, "html.parser")

    return False

soup = getHtmlDoc("abort")

if (soup != False):
    # write this to a file
    html_doc =  soup.prettify()
    f = open("dictionary.html", "w+")
    f.write(html_doc)
    f.close()
else:
    print("Something went wrong! Not getting anything")
