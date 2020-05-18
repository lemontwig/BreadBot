import requests
import urllib.parse
from random import choice
from random import randrange


def getPortaPotty():

    portaPottyList = eval(open('portapotty.txt', 'r').read())
    imagesList = open('portaPottyURLS.txt', 'w')
    for d in portaPottyList:
        imagesList.write(d['media'] + '\n')
    imagesList.close()

if __name__ == '__main__':
    getPortaPotty()
