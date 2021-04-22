# spider.py
# take the word from the db then query dictionary.com to get the
# meaning of the word then store it in the db
import requests
from bs4 import BeautifulSoup
from lxml import html

BASE_URL = "https://www.dictionary.com"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
         "Cookie": "your cookie"}


def getUrl(word):
    return f"{BASE_URL}/browse/{word}"


def getHtmlDoc(word):
    res = requests.get(getUrl(word), headers = header)
    if (res.status_code == 200):
        # return res.content # don't use res.text
        return BeautifulSoup(res.text, "html.parser")

    return False

def writeToFile(html_doc, word):
    f = open(f"dictionary-{word}.html", "w+")
    f.write(html_doc)
    f.close()

def writeToDb(html_doc, word):
    """
    write this to the db for now
    """
    sql = "UPDATE anagrams SET dict=? WHERE word=?"
    

    return True

def run(word):
    soup = getHtmlDoc(word)

    if (soup != False):
        # write this to a file
        data = content.select("#base-pw > main > section > section > div:nth-child(2)")
        # we need to write this to the database instead
        if (len(data) > 0):
            writeToDb(data[0], word)
    else:
        print("Something went wrong! Not getting anything")



"""
# we need to find a div with class="css-1avshm7"
f = open("dictionary.html", "r")
html_file = f.read()
f.close()

content = BeautifulSoup(html_file, 'html.parser')
# data = content.find_all('div', attrs={'class': 'css-1avshm7'})
data1 = content.select("#base-pw > main > section > section > div:nth-child(2)")
#base-pw > main > section > section > div:nth-child(2)

print(data1)
"""

# print(len(data))

# tree = html.fromstring(html_file)
# word_def = tree.xpath('//*[@id="base-pw"]/main/section/section/div[1]/text()')

# print(word_def)


# //*[@id="base-pw"]/main/section/section/div[1]
# /html/body/div[1]/div/div/div[2]/main/section/section/div[1]/section[2]
# //*[@id="base-pw"]/main/section/section/div[1]/section[2]
# //*[@id="base-pw"]/main/section/section/div[1]/section[3]
#


# soup1 = BeautifulSoup(html, "html.parser")
