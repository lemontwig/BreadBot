import requests
import urllib.parse
import re
import time
from random import randint
from random import choice
from random import randrange
from bs4 import BeautifulSoup as BS

responses = ['here you go bread lover!', 'yummy',
             'magenta squash\'s brother', 'BREAD',
             'I will die for bread', 'BREAD CULT']
 
with open('API_KEYS.txt', 'r') as KEYS:
    API_KEYS = eval(KEYS.read())


YOUTUBE_KEY = API_KEYS['youtube']
PIXABAY_KEYS = API_KEYS['pixabay']


def webscrapeAnagram(anagram):
    anagramURL = requests.get('https://new.wordsmith.org/anagram/anagram.cgi?',
                              params={'anagram': urllib.parse.quote(anagram),
                                      't': 15,
                                      'a': 'n'},
                              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}).text

    soup = BS(anagramURL, 'html5lib')
    specs = str(soup.find_all(class_="p402_premium"))
    beginning = specs.find('15:') + 13
    end = specs.find(
        '<script>document.body.style.cursor=\'default\';</script></div>') - 4
    wordList = specs[beginning:end].split('<br/>')
    finalList = []
    finalStr = ''
    for word in wordList:
        finalList.append(word.replace('\n', ''))

    for i in range(len(finalList)):
        try:
            if finalList[i].startswith('"p402') or finalList[i].endswith('</b>') or \
                    finalList[i].startswith('<a') or finalList[i].endswith(')'):
                finalList.pop(i)
        except IndexError:
            pass
    for word in finalList[2:-2]:
        if (len(word)) != 0:
            finalStr += (word + ', ')
    if (len(finalStr)) == 0:
        return 0

    return finalStr.strip(', ')


def getBread(userQuery: str):
    global responses
    choose = 1  # randint(0,1)
    breads = open('breadURLs.txt', 'r')
    breadList = breads.readlines()

    if (choose == 1):
        #KEYS = API_KEYS['pixabay']
        try:
            breadURL = 'https://pixabay.com/api/?key=' + choice(PIXABAY_KEYS) + '&q=' + urllib.parse.quote(
                userQuery) + '&image_type=photo&' + 'safesearch=true&' + 'per_page=200'
            r = requests.get(breadURL, headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
            imageJson = r.json()
            imageURLS = []
            if imageJson['totalHits'] < 200:
                for i in range(imageJson['totalHits']):
                    try:
                        imageURLS.append(imageJson.get('hits')
                                         [i]['largeImageURL'])
                    except KeyError:
                        choice(breadList.extend(imageURLS))

            else:
                for i in range(randrange(200)):
                    try:
                        imageURLS.append(imageJson.get('hits')
                                         [i]['largeImageURL'])
                    except KeyError:
                        choice(breadList.extend(imageURLS))

            return f' {choice(responses)} {choice(imageURLS)}'

        except AttributeError:
            try:
                return f' {choice(responses)} {choice(breadList)}'
                # return choice(breadList)
            except:
                return 'Failed to obtain bread image.'
            finally:
                breads.close()

    else:
        with open('breadURLs.txt', 'r') as breads:
            return f' {choice(responses)} {choice(breads.readlines())}'


def getRandomVideo():
    with open('ytlinks.txt', 'r') as videos:
        vList = videos.readlines()
    return 'https://youtube.com/' + choice(vList).strip('\n')


def getSpotifyTrack(query):
    spotifyURL = requests.get('https://www.google.com/search?hl=en&q=spotify+track+' + urllib.parse.quote(query),
                              headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}).text
    soup = BS(spotifyURL, 'html5lib')
    link = soup.find(class_='r')
    return (link.find('a')['href'])

def getPortaPottyImage():
    portaPottyResponses = ['please rate this porta potty', 'here you go, weirdo', 'i don\'t know why you wanted this but here', 'hope you enjoy this']
    with open('portaPottyURLS.txt', 'r') as portaPottyImages:
        return f' {choice(portaPottyResponses)} {choice(portaPottyImages.readlines()).strip()}'


def getSubCount(username):
    defaultAPI = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCQrrVVps9XlOeftIR0XhKuQ&key=' + YOUTUBE_KEY
    customSearchAPI = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + urllib.parse.quote(username) + '&key=' + YOUTUBE_KEY

    if username == '':
        r = requests.get(defaultAPI, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        data = r.json()
        amount = int(data.get('items')[0].get('statistics')['subscriberCount'])
        return f' magenta squash currently has {amount:,} subscribers!'

    else:
        r = requests.get(customSearchAPI, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        data = r.json()
        if (data['pageInfo']['totalResults'] == 0):
            return ' The username given does not exist!'
        else:
            try:
                channelID = data.get('items')[0]['id']['channelId']
                channelName = data.get('items')[0]['snippet']['channelTitle']
                finalAPI = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + channelID + '&key=' + YOUTUBE_KEY
                r = requests.get(finalAPI, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
                data = r.json()
                #channelName = data.get('items')[1]['snippet']['title']
                amount = int(data.get('items')[0].get('statistics')['subscriberCount'])
                return f' {channelName} currently has {amount:,} subscribers!'

            except:
                return f' Couldn\'t find the given username. Sorry!'


def searchVideo(query):
    if query == '':
        return ' Please have a search query.'
    else:
        vidAPI = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&key=' + YOUTUBE_KEY + '&q=' + urllib.parse.quote(query) + '&maxResults=10'

        r = requests.get(vidAPI, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        data = r.json()
        try:
            return 'https://www.youtube.com/watch?v=' + data.get('items')[0]['id']['videoId']
        except:
            return 'Couldn\'t find the video. Sorry!'

