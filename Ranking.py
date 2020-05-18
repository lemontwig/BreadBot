from PIL import Image, ImageFont, ImageDraw
import os, json


LEVELS = {'breadlings': 0, 'yeast-ingester': 18.119, 'bread-connoisseur':63.096, 'B.S. in Bread Science': 130.907, 'M.S. in Bread Science': 219.712, 'Ph.D. in Bread Science': 328.316, 'BREAD GOD': 455.846, 'N/A': 455.846}


def makeNewBlankCard():
    img = Image.open('levelCard.png')
    return img

def downloadAvatar(link):
    os.system('wget -O avatar.webp ' + link)
    avatar = Image.open('avatar.webp').convert('RGB')
    finalAvatar = avatar.resize( (100, 100))
    finalAvatar.save('avatar.png') 
    os.system('rm avatar.webp')

def addUsername(img, userName):
    fnt = ImageFont.truetype(font='Bebas.ttf', size=25)
    draw = ImageDraw.Draw(img)
    draw.text((29,14), userName, font = fnt, fill = (0,0,0))

    fnt = ImageFont.truetype(font='Bebas.ttf', size=25)
    draw = ImageDraw.Draw(img)
    draw.text((30,13), userName, font = fnt, fill = (255,255,255))

def addAvatar(background):
   img = Image.open('avatar.png', 'r')
   img_w, img_h = img.size
   bg_w, bg_h = background.size
   offset = ((bg_w - img_w) // 11, (bg_h - img_h) // 2) #(45,50)
   background.paste(img, offset)

def addLevel(background, ID):
    with open('users.json', 'r') as userFiles:
        users = json.load(userFiles)
    userLevel = users[ID]['level']

    fnt = ImageFont.truetype(font='Azonix.otf', size=50)
    draw = ImageDraw.Draw(background)
    draw.text((194,91), str(userLevel), font = fnt, fill = (0,0,0))
    draw.text((195,90), str(userLevel), font = fnt, fill = (255,255,0))

    fnt = ImageFont.truetype(font='Azonix.otf', size=35)
    draw = ImageDraw.Draw(background)
    draw.text((169,51), "LEVEL", font = fnt, fill = (0,0,0))
    draw.text((170, 50), "LEVEL", font = fnt, fill = (255,255,0))


def addProgressBar(background, ID):
    img = Image.open('baguetteProgress.png')
    img_w, img_h = img.size #(285,21)

    with open('users.json', 'r') as userFiles:
        users = json.load(userFiles)

    userLevel = users[ID]['level']

    userExperience = int(users[ID]['experience'])
    experienceGoal = int(userExperience ** (1/1.8))
    currentGoal, nextGoal = findRole(userExperience)

    try:
        percentage = ((LEVELS[currentGoal] - userExperience) / (LEVELS[currentGoal] - LEVELS[nextGoal]))

    except ZeroDivisionError:
        print('From DaftPunker: Zero Division Error')
        background.paste(img, (307,90))

    difference = LEVELS[nextGoal] - userExperience

    if (difference >= 0):
        img = img.resize((int(img_w*percentage), img_h))
        background.paste(img, (307,90))
    
def addExperience(background, ID):
    with open('users.json', 'r') as userFiles:
        users = json.load(userFiles)

    userLevel = users[ID]['level']

    userExperience = users[ID]['experience']
    experienceGoal = userExperience ** (1/1.8)

    nextGoal = findRole(userExperience)[1]

    finalStr = f'EXP: {round(userExperience,3)} / {round(LEVELS[nextGoal], 2)}'
    
    fnt = ImageFont.truetype(font='comfortaa.ttf', size=20)
    draw = ImageDraw.Draw(background)
    draw.text((380,89), finalStr , font = fnt, fill = (0,0,0))

    return userExperience

def returnColors(role):
    if  role == 'breadlings':
        return (53,152,219)
    elif role == 'yeast-ingester':
        return (155,88,182)
    elif role == 'bread-connoisseur':
        return (38,102,58)
    elif role == 'B.S. in Bread Science':
        return (5,81,249)
    elif role == 'M.S. in Bread Science':
        return (255,0,250)
    elif role == 'Ph.D. in Bread Science':
        return (43,243,0)
    elif role == 'BREAD GOD':
        return (35,243,253)
    else: #N/A
        return (44,11,57)

def addCurrentRole(background, userExperience):
    fnt = ImageFont.truetype(font='Sunday.ttf', size = 25)
    draw = ImageDraw.Draw(background)
    currentRole = findRole(userExperience)[0]
    finalStr = f'Current Role:\n{currentRole}' 
    draw.text((349,21), finalStr , font = fnt, fill = (0,0,0))
    draw.text((350,20), finalStr , font = fnt, fill = returnColors(currentRole)) #(255,165,0))

def addNextRole(background, userExperience):
    fnt = ImageFont.truetype(font='Sunday.ttf', size = 25)
    draw = ImageDraw.Draw(background)
    nextRole = findRole(userExperience)[1]
    finalStr = f'Next Role:\n{nextRole}' 
    draw.text((349,121), finalStr , font = fnt, fill = (0,0,0))
    draw.text((350,120), finalStr , font = fnt, fill = returnColors(nextRole)) #(255,165,0))

    background.save('ranking.png')

def resize():
    img = Image.open('ranking.png')
    img_w, img_h = img.size
    ratio = 2
    img = img.resize((img_w * ratio,img_h*ratio), Image.HAMMING)
    img.save('ranking.png')


def findRole(userExperience) -> ('currentRole', 'nextRole'):

    if userExperience < LEVELS['yeast-ingester']:
        return ('breadlings', 'yeast-ingester')
    
    elif userExperience >= LEVELS['yeast-ingester'] and userExperience < LEVELS['bread-connoisseur']:

        return ('yeast-ingester', 'bread-connoisseur')

    elif userExperience >= LEVELS['bread-connoisseur'] and userExperience < LEVELS['B.S. in Bread Science']:

        return ('bread-connoisseur', 'B.S. in Bread Science')

    elif userExperience >= LEVELS['B.S. in Bread Science'] and userExperience < LEVELS['M.S. in Bread Science']:

        return ('B.S. in Bread Science', 'M.S. in Bread Science')

    elif userExperience >= LEVELS['M.S. in Bread Science'] and userExperience < LEVELS['Ph.D. in Bread Science']:

        return ('M.S. in Bread Science', 'Ph.D. in Bread Science')

    elif userExperience >= LEVELS['Ph.D. in Bread Science'] and userExperience < LEVELS['BREAD GOD']:

        return ('Ph.D. in Bread Science', 'BREAD GOD')

    else:
        return ('BREAD GOD', 'N/A')


def createRankingCard(link, userName, ID):
    downloadAvatar(link)
    background = makeNewBlankCard()
    addUsername(background, userName)
    addAvatar(background)
    addLevel(background, ID)
    addProgressBar(background, ID)
    userExperience = addExperience(background, ID)
    addCurrentRole(background, userExperience)
    addNextRole(background, userExperience)
    resize()
