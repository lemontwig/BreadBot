from PIL import Image, ImageOps, ImageFont, ImageDraw, ImageEnhance
import math
import matplotlib.pyplot as plt
import numpy as np
import random


def makeNewImage(original, mirror, side):
    oWidth, oHeight = original.size
    mWidth, mHeight = mirror.size
    finalImage = Image.new('RGB', ( (oWidth + mWidth) , (oHeight)))

    if side == 'left':
        
        finalImage.paste(original)
        finalImage.paste(mirror,(oWidth,0))

        finalImage.save('userImg.jpg')

    else:
    
        finalImage.paste(original, (oWidth,0))
        finalImage.paste(mirror) #left upper right bottom

        finalImage.save('userImg.jpg')


def mirrorLeftImage():
    myImage = Image.open('userImg.jpg')
    imgW, imgH = myImage.size

    croppedImgLeft = myImage.crop((0,0,imgW//2, imgH)) #left top right bottom
    mirrorLeft = ImageOps.mirror(croppedImgLeft)
    makeNewImage(croppedImgLeft, mirrorLeft, 'left')


def mirrorRightImage():
    myImage = Image.open('userImg.jpg')
    imgW, imgH = myImage.size
    croppedImgRight = myImage.crop((imgW//2, 0, imgW, imgH ))
    mirrorRight = ImageOps.mirror(croppedImgRight)
    makeNewImage(croppedImgRight, mirrorRight, 'right')
    

def deepfry():
    myImage = Image.open('userImg.png')
    myImage = myImage.convert('RGBA')

    operations = [ImageEnhance.Sharpness, ImageEnhance.Contrast]
    factors = [2000,4]
    for op in zip(operations,factors):
        finalImage = op[0](myImage).enhance(op[1])

    finalImage.save('userImg.png')


def swirlImage(degree):

    img = Image.open('userImg.jpg')
    img = img.convert('RGBA')
    degree = min(max(0,degree),100) / 1000
    width, height = img.size
    pix = img.load()
    center = width / 2, height / 2
    dst_img = Image.new("RGBA", (width, height))
    dst_pix = dst_img.load()
    for w in range(width):
        for h in range(height):
            offset_x = w - center[0]
            offset_y = h - center[1]
            radian = math.atan2(offset_y, offset_x)
            radius = math.sqrt(offset_x ** 2 + offset_y ** 2)
            x = int(radius * math.cos(radian + radius * degree)) + center[0]
            y = int(radius * math.sin(radian + radius * degree)) + center[1]
            x = min(max(0, x), width - 1)
            y = min(max(0, y), height - 1)
                                               
            dst_pix[w, h] = pix[x, y]

    dst_img.save('userImg.png')

def leaderboardHist(forHist):
    #usernames = [(username,xp)]
    usernames = []
    xp = []
    for user in forHist:
        usernames.append(user[0])
        xp.append(user[1])


    fig,ax = plt.subplots(figsize=(20,13))

    colors = ['#f2f489', '#98c6eb', '#b28dff',
              '#e1476b', '#dc4dc3', '#a34a9c',
              '#d5f816', '#355a90', '#6070bb',
              '#abdee6','#ffabab','#ffccb6',
              '#ff968A','#97c1a9','#ffdbcc']

    random.shuffle(colors)
    ypos = np.arange(len(usernames))
    bars = ax.bar(ypos, xp, color = colors)
    ax.set_title('Top 15 Users',fontsize=30)
    ax.set_ylabel('Total XP',fontsize=30)
    ax.set_xticks(ypos)
    ax.set_xticklabels(usernames, rotation=85, size = 14)#y_pos,bars, rotation = 55,size=14)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval/2, yval, ha='center', va='bottom',fontsize=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('userHist.png')
    plt.clf()
    return

if __name__ == '__main__':
    leaderboardHist()

