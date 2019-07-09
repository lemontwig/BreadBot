import requests
import time
import datetime
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup as BS, NavigableString, Tag

payload = {}
masterList = []


def getHTML(givenWord: str) -> bytes:
    givenWord = str(givenWord)

    payload['anagram'] = givenWord
    result = urlencode(payload, quote_via=quote_plus)
    URL = f"https://new.wordsmith.org/anagram/anagram.cgi?{result}&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=0&source=adv"
    clientConnection = urlopen(URL)
    anagramHTML = clientConnection.read()
    clientConnection.close()
    return anagramHTML


def makeSoup(anagramHTML) -> BS:
    pageSoup = BS(anagramHTML, 'html.parser')
    return pageSoup


def getAnagrams(pageSoup: BS):
    count = 0
    for br in pageSoup.findAll('br'):
        next_s = br.nextSibling
        if not (next_s and isinstance(next_s, NavigableString)):
            continue

        next2_s = next_s.nextSibling
        if next2_s and isinstance(next2_s, Tag) and next2_s.name == 'br':
            text = str(next_s).strip().split('\n')
            if (len(text[0]) <= len(payload['anagram']) and text[0] != payload['anagram']):
                masterList.append(text[0])
                if (len(masterList) == 10):
                    return
                elif(len(masterList) == 0):
                    return 'No Anagram'


def main(word):
    getAnagrams(makeSoup(getHTML(word)))
    main = ''
    for w in masterList:
        w += ' '
        main += w
    return main.strip()


if __name__ == '__main__':
    print(main(input('Word: ')))
