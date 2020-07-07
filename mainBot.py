import discord, random, urllib.request, json, asyncio, os, sys, shutil
import BreadScrape, Ranking, imageFun, cleverbotfree.cbfree, time#my libs
import youtube_dl
from collections import defaultdict as dd

import urllib
from discord.ext import commands
from discord.utils import get

with open('API_KEYS.txt', 'r') as KEYS:
    API_KEYS = eval(KEYS.read())


TOKEN = API_KEYS['discord']

 
ROLE_IDS = {'breadlings': 557820232283062274,
            'yeast-ingester': 599123170515222529,
            'bread-connoisseur': 601203043786162232,
            'B.S. in Bread Science': 601204030462754847,
            'M.S. in Bread Science': 601204267742920704,
            'Ph.D. in Bread Science': 601204509695410186,
            'BREAD GOD': 601204729196052510,
            'Commander of Bread': 557802373787942933}

activities = ["MagentaSquash on YouTube", 
              "with bread",
              "with bread crumbs",
              "with bagels",
              "with its baguette",
              "with its own tears",
              "with code | !help "]

# first ID is me
MODS = ['389240189223960581', '555227403371413507', '181234541929824256', '217423241113894913', '461709709825540126']

queues = {}

#EXPERIENCE_PTS = .1

client = commands.Bot(command_prefix = '!')
client.remove_command('help')


@client.command(pass_context=True)
async def help(ctx):
    
    YTHelp = discord.Embed(
        color = discord.Colour.red()
    )
    ImageHelp = discord.Embed(
        color =  discord.Colour.orange()
    )
    LevelHelp = discord.Embed(
        color =  discord.Colour.blue()
    )

    MusicHelp = discord.Embed(
        color = discord.Colour.green()
    )
    """
    MiscHelp = discord.Embed(
        color = discord.Color.magenta()
    )
    """

    YTHelp.set_author(name='Youtube Commands')
    YwwTHelp.add_field(name='yt', value = 'Search any youtube video', inline = True)
    YTHelp.add_field(name='video', value = 'Gives random magenta squash video', inline = True)
    YTHelp.add_field(name='subcount|subs', value = 'Get subcount of YTer', inline = True)

    ImageHelp.set_author(name='Image Manipulation')
    ImageHelp.add_field(name='deepfry', value='Deepfries image', inline=True)
    ImageHelp.add_field(name='mirrorL', value = 'Mirrors left part of image', inline = True)
    ImageHelp.add_field(name='mirrorR', value = 'Mirrors right part of image', inline = True)
    ImageHelp.add_field(name='swirl', value = 'Swirls the center of the image', inline = True)


    LevelHelp.set_author(name='Leveling System')
    LevelHelp.add_field(name='levels', value = 'Shows leveling system', inline = True)
    LevelHelp.add_field(name='rank', value = 'Shows current standing', inline = True)
    LevelHelp.add_field(name='leaderboard|lb', value = 'Shows the top 15 users', inline = True)

    """

    MusicHelp.set_author(name='Music Commands')
    MusicHelp.add_field(name='spotify|s', value = 'Search spotify', inline = True)
    MusicHelp.add_field(name='join', value = 'Breadbot will join your voice channel', inline=True)
    MusicHelp.add_field(name='play', value = 'Breadbot will play your requested songs', inline=True)
    MusicHelp.add_field(name='quit', value = 'Breadbot will leave your voice channel', inline=True)
    """
    

    MiscHelp.set_author(name= 'Misc. Help')
    MiscHelp.add_field(name='anagram', value='Anagrams 23 letters', inline = True)
    MiscHelp.add_field(name='bread', value='Gives random image of bread', inline = True)
    MiscHelp.add_field(name='help', value='Shows this message', inline = True)
    MiscHelp.add_field(name='magenta8', value='Ask a question!', inline = True)
    MiscHelp.add_field(name='social', value = 'Magenta\'s Social Media', inline = True)
    MiscHelp.add_field(name='talk|t', value = 'Talk to me!', inline = True)
    MiscHelp.add_field(name='rockdog', value = 'See dumb rockdog', inline = True)
    MiscHelp.add_field(name='count', value = 'See the current member count!', inline = True)
    MiscHelp.add_field(name='spotify|s', value = 'Search spotify', inline = True)



    await ctx.send(ctx.message.author.mention, embed = YTHelp)
    await ctx.send(embed=ImageHelp)
    await ctx.send(embed=LevelHelp)
    await ctx.send(embed=MusicHelp)
    await ctx.send(embed=MiscHelp)



 

cb = cleverbotfree.cbfree.Cleverbot()

@client.command(name='talk', description='Talk to our lovely BreadBot!', aliases=['t'])
async def talkToBreadBot(ctx,*,message):
    cb.get_form()
    message = message.replace(':','').replace('#','').replace('<','') 
    cb.send_input(message)
    await client.wait_until_ready()
    botResponse = cb.get_response()
    await client.wait_until_ready()
    await ctx.send(f'{ctx.message.author.mention} {botResponse}')

"""
@client.command(name='join', description='joins its respective voice channel', pass_context=True)
async def join(ctx):
    await ctx.message.author.voice.channel.connect()
    #await leave(voice_client,ctx)


@client.command(name='play', description='plays the first video returned')
async def play(ctx, *, videoQuery):
    global queues
    url = BreadScrape.searchVideo(videoQuery)

    def checkQueue():
        queueInfile = os.path.isdir('./Queue')
        if queueInfile:
            DIR = os.path.abspath(os.path.realpath('Queue'))
            length = len(os.listdir(DIR))
            stillQueued = length-1
            try:
                firstFile = os.listdir(DIR)[0]
            except:
                print('No more queued song(s)')
                queues.clear() #might be problematic
                return
            mainLoation = os.path.dirname(os.path.realpath(__file__))
            songPath = os.path.abspath(os.path.realpath('Queue') + '\\' + firstFile)
            if length != 0:
                print('Song done, playing next queued song')
                print(f'Songs still in queue" {stillQeued}')
                songThere = os.path.isfile('song.mp3')
                if songThere:
                    os.remove('song.mp3')
                shutil.move(songPath,mainLocation)
                for f in os.listdir('./'):
                    if f.endswith('.mp3'):
                        os.rename(f,'song.mp3')
                voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e:checkQueue())
            else:
                queues.clear()
                return
        else:
            queues.clear()
            return



    songThere = os.path.isfile('song.mp3')
    try:
        if songThere:
            os.remove('song.mp3')
            queues.clear()
            print('Removed old song file')
    except PermissionError:
        print('Trying to delete, but being played')
        return


    QueueInfile = os.path.isdir('./Queue')
    try:
        QueueFolder = './Queue'
        if QueueInfile:
            print('Removed old folder')
            shutil.rmtree(QueueFolder)
    except:
        print('No old queue folder')

    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192'
             }]
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for f in os.listdir('./'):
        if f.endswith('.mp3'):
            name = f
            print(f'REnamed: {f}')
            os.rename(f,'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'),after=lambda e:checkQueue())
        
    await ctx.send(f'Playing: {name.rsplit("-",2)[0] + name.rsplit("-",2)[1]}')


@client.command(name='pause', description='pauses song')
async def pause(ctx):
    voice = get(client.voice_clients,guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        await ctx.send('Paused')
    else:
        await ctx.send('Music is not playing!')

@client.command(name='resume', description='resumes song')
async def resume(ctx):
    voice = get(client.voice_clients,guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
        await ctx.send('Resuming')
    else:
        await ctx.send('Music is not paused')



@client.command(name='queue', description='Queue next song')
async def queueSong(ctx, *, videoQuery):

    url = BreadScrape.searchVideo(videoQuery)
    queueInfile = os.path.isdir('./Queue')
    if not(queueInfile):
        os.mkdir('Queue')
    DIR = os.path.abspath(os.path.realpath('Queue'))
    queueNum = len(os.listdir(DIR))
    queueNum += 1
    addQueue = True
    while addQueue:
        if queueNum in queues:
            queueNum += 1
        else:
            addQueue = False
            queues[queueNum] = queueNum
    queuePath = os.path.abspath(os.path.realpath('Queue') + f'\song{queueNum}.%(ext)s')
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': queuePath,
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192'
             }]
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    await ctx.send('Adding song to the queue')


            

    '''
    global PLAYCOUNT
    QUEUE.append(url)
    PLAYCOUNT += 1


    if QUEUE[PLAYCOUNT].startswith('Coul'): #didnt find it
        await ctx.send(QUEUE[PLAYCOUNT])

    else:
        voice = get(client.voice_clients, guild=ctx.guild)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192'
                 }]
            }
        if len(QUEUE) == 1:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([QUEUE[PLAYCOUNT]])

        else: #we are now queueing
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([QUEUE[PLAYCOUNT]])

        for f in os.listdir('./'):
            if f.endswith('.mp3'):
                name = f
                os.rename(f,'song.mp3')

        try:

            voice.play(discord.FFmpegPCMAudio('song.mp3'),after=lambda e:QUEUE.pop(0))
            await ctx.send('Playing...')

        except: #discord.ext.commands.errors.CommandInvokeError:
            await ctx.send(f'Queued {videoQuery}')
            QUEUE.append(url)

    '''

@client.command(name='quit', description='leaves its respective voice channel')
async def leave(ctx):

    if ctx.message.author.voice.channel == client.voice_clients[0].channel:
        if len(ctx.message.author.voice.channel.members) == 2:
            await client.voice_clients[0].disconnect()
            global PLAYCOUNT
            PLAYCOUNT = -1
        else: #more than the bot, and current player then you can't quit on behalf of the other user
            await ctx.send('There is another person in here using it.')

    else:
        await ctx.send('You must be in the voice channel to do this')
"""

@client.command(name='count', description='returns the total member count')
async def sendCount(ctx):
    await ctx.send(f'{ctx.message.author.mention} There are currently {ctx.guild.member_count} members in this server!')
    with open('members.txt' , 'w') as members:
        for member in ctx.guild.members:
            pass

@client.command(name='cheems', description='returns an image of cheems')
async def sendCheems(ctx):
    await ctx.send(f'{ctx.message.author.mention} i like him', file=discord.File('cheems.jpg'))

@client.command(name='swirl', description='swirls the center of the image')
async def sendSwirl(ctx):
    try:
        if ctx.message.attachments[0].size > 2000000:
            await ctx.send(ctx.message.author.mention + ' size of image is too large.')
            return
            
        await ctx.message.attachments[0].save('userImg.jpg')

    except IndexError:
        await ctx.send(ctx.message.author.mention + ' must send an image.')
        return
    
    imageFun.swirlImage(4)
    await ctx.send(ctx.message.author.mention, file=discord.File('userImg.png'))
    os.system('rm userImg.png')


@client.command(name='deepfry', description='saturates the given image')
async def sendDeepfry(ctx):
    try:
        await ctx.message.attachments[0].save('userImg.png')

    except IndexError:
        await ctx.send(ctx.message.author.mention + ' must send an image.')
        return

    imageFun.deepfry()
    await ctx.send(ctx.message.author.mention, file=discord.File('userImg.png'))
    os.system('rm userImg.png')


@client.command(name='mirrorR', description='mirrors the RIGHT side of the given mage')
async def mirrorR(ctx):
    try:
        await ctx.message.attachments[0].save('userImg.jpg')

    except IndexError:
        await ctx.send(ctx.message.author.mention + ' must send an image.')
        return

    
    imageFun.mirrorRightImage()

    await ctx.send(ctx.message.author.mention, file=discord.File('userImg.jpg'))
    os.system('rm userImg.jpg')

@client.command(name='mirrorL', description='mirrors the LEFT side of the given image')
async def mirrorL(ctx):
    try:
        await ctx.message.attachments[0].save('userImg.jpg')
    except IndexError:
        await ctx.send(ctx.message.author.mention + ' must send an image.')
        return
    
    imageFun.mirrorLeftImage()

    await ctx.send(ctx.message.author.mention, file=discord.File('userImg.jpg'))
    os.system('rm userImg.jpg')


@client.command(name = "leaderboard", description = 'Displays the top 15 users', aliases = ['lb'])
async def leaderboard(ctx):

#   {id: [level,xp]}
    with open('users.json', 'r') as users:
        allUsers = json.load(users)

    sortedUsers = sorted(allUsers.items(), key = lambda x: float(x[1]['experience']), reverse = True)

    forHist = []

    displayCount = 0
    
    for user in sortedUsers:
        if displayCount == 15:
            break
        username = str(client.get_user(int(user[0])))
        if username != 'None' and user[0] not in MODS:
            if user[0] in [str(member.id) for member in ctx.guild.members]:
                forHist.append((username, round(float(user[1]['experience']),3)))
                """
                valueStr = '**' + username + '** with **' + str(int(user[1]['experience'])) + '** XP'
                userLeaderBoard.add_field(name=ordinalNums[displayCount], value = valueStr, inline = False)
                """
                displayCount += 1


    imageFun.leaderboardHist(forHist)
    await ctx.send((ctx.message.author.mention), file= discord.File('userHist.png'))
    os.remove('userHist.png')
    return



@client.command(name = 'kick', description='Kicks user')
async def kick(ctx, * , member: discord.Member):
    if str(ctx.message.author.id) == '389240189223960581' or str(ctx.message.author.id) == '555227403371413507' or str(ctx.message.author.id) == '181234541929824256':
        await member.kick()
        await ctx.send(str(member) + ' has been kicked.')


@client.command(name = 'ban', description='Bans user')
async def ban(ctx, * , member: discord.Member):
    if str(ctx.message.author.id) == '389240189223960581' or str(ctx.message.author.id) == '555227403371413507' or str(ctx.message.author.id) == '181234541929824256': 
        await member.ban()
        await ctx.send(str(member) + ' has been banned.')

@client.command(name = 'unban', description='Unbans user')
async def unban(ctx, * , member):
    if str(ctx.message.author.id) == '389240189223960581' or str(ctx.message.author.id) == '555227403371413507' or str(ctx.message.author.id) == '181234541929824256':
        bannedUsers = await ctx.guild.bans()
        memberName, memberDescriminator = member.split('#')
        for banEntry in bannedUsers:
            user = banEntry.user
            if (user.name, user.discriminator) == (memberName, memberDescriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

@client.command(name='rockdog', description='sends dumb image of rock dog')
async def rockDog(ctx):
    await ctx.send((ctx.message.author.mention), file = discord.File('rockdog.jpg'))

@client.command(name='rank', description='Returns your own ranking card to check your level and experience points.')
async def getRanking(ctx):
    #userID = str(ctx.message.author.id)
    avatarLink = str(ctx.author.avatar_url)
    userName = ctx.author.name
    Ranking.createRankingCard(avatarLink, userName, str(ctx.author.id))
    await ctx.send((ctx.message.author.mention), file= discord.File('ranking.png'))
    os.system('rm ranking.png')
    os.system('rm avatar.png')
    

#"Magic" 8 Ball here
@client.command(name="magenta8",
                description="Answers yes/no questions",
                aliases=["8ball"],
                pass_context=True)
async def magenta_8(ctx, *, question):
    responses = ["It is certain", 
                 "Without a doubt", 
                 "Yes - definitely",
                 "Most likely", 
                 "Yes", 
                 "Cannot predict now", 
                 "Ask again later", 
                 "Forget about that. Eat bread.", 
                 "Don't count on it", 
                 "The bread gods say no", 
                 "Very doubtful"]
    await ctx.send(ctx.message.author.mention + " Magenta8 says: " + random.choice(responses))
# End of Magic 8 Ball


@client.command(name = 'spotify', aliases = ['s'],
                description = 'attempts to send back the given spotify track from the given search query. (only as accurate as you make it to be)', pass_context = True)
async def returnSpotifyTrack(ctx, *, query):
    #spotifyResponses = [' i tried ', ' hopefully its what u wanted ', ' here u go ']
    link = BreadScrape.getSpotifyTrack(query)
    await ctx.send(ctx.author.mention + ' ' + link)

#start of getting random video
@client.command(name='video',
                description = 'Randomly picks a Magenta Squash video')
async def sendRandomVideo(ctx):
    videoResponses = [' freshly picked: ', ' here you go: ', ' enjoy! ']
    await ctx.send(ctx.message.author.mention + random.choice(videoResponses) + BreadScrape.getRandomVideo())

#end of getting random video

# start of breadscraping
@client.command(name="bread",
                description="Randomly picks a bread from Wikipedia's List of Bread and sends an image of that picked bread",
                pass_context=True)
async def getBread(ctx):
    breads = ['bread', 'biscuit', 'flat bread', 'leavened', 'pancake', 'rye bread', 'sourdough bread', 'yeast bread', 'white bread', 'toast bread']
    pickedBread = random.choice(breads)
    response = BreadScrape.getBread(pickedBread)
    await ctx.send(ctx.message.author.mention + response)
# end of breadscraping

#portapotty
@client.command(name='portapotty',
                description='Randomly picks a porta-potty image')
async def sendPortaPotty(ctx):
    response = BreadScrape.getPortaPottyImage()
    await ctx.send(ctx.message.author.mention + response)
#end of portapotty

@client.command(name='subcount', aliases = ['subs'],  description='Will return the amount of subscribers the given channel has. Default will display for Magenta Squash')
async def sendSubCount(ctx, *, username=''):
    response = BreadScrape.getSubCount(username)
    await ctx.send(ctx.message.author.mention + response)

#start of anagraming

async def getAnagram(anagram):
    try:
        return BreadScrape.webscrapeAnagram(anagram)
    except:
        return None

@client.command(name = 'anagram',
                description = 'anagrams the given word(s) (up to the first 23 letters!)')
async def spitAnagram(ctx, *, anagram):
    if (len(anagram) > 23):
        await ctx.send(f'{ctx.author.mention} the limit is 23 letters!')
        return

    response = await getAnagram(anagram)
    
    if (response == None):
        await ctx.send(f'{ctx.author.mention} failed to obtain anagram!')

    elif (response == 0):
        await ctx.send(f'{ctx.author.mention} No anagrams found for: {anagram}')

    else:
        await ctx.send(f'{ctx.author.mention} anagram(s) for {anagram}: {response}')    
#end of anagraming

#start of fetching own level
@client.command(name = 'levels',
                description = 'Displays the level hierarchy')
async def getLevel(ctx):
    #await client.wait_until_ready()
    await ctx.send((ctx.message.author.mention), file= discord.File('levels.png'))

#end of fetching own level

@client.command(name = 'social',
                description = 'returns all of magenta squash\'s social media accounts and such')
async def returnSocial(ctx):
    await ctx.send('''discord: https://discord.gg/fgjTUW5
subreaddit: https://www.reddit.com/r/magentasquash
instabread: https://www.instagram.com/magentasquash 
twitter: https://twitter.com/MagentaSquash
cringetok: https://www.tiktok.com/@magentasquash''')

@client.command(name= 'yt',
                description='does a youtube search for the given query')
async def returnYTSearch(ctx, *, query=''):
    link = BreadScrape.searchVideo(query)
    await ctx.send(f'{ctx.message.author.mention} {link}')

async def add_user(users, member):
    if (client.user.id != member.id):
        mID = str(member.id)
        if (mID not in users):
            users[mID] = {}
            users[mID]['experience'] = 0
            users[mID]['level'] = 1
            return ('not exists' , 0)
        else:
            return ('exists', users[mID]['level'])
            
async def add_experience(message, users, member):

    userMessage = (message.content).split()

    if (client.user.id != member.id):
        mID = str(member.id)
        if len(userMessage) > 2 and len(userMessage) < 15:
            users[mID]['experience'] = float(users[mID]['experience']) + round(random.uniform(0, .05), 2)  #EXPERIENCE_PTS
        elif len(userMessage) >= 15:
            users[mID]['experience'] = float(users[mID]['experience']) + round(random.uniform(0, .1), 2)  #EXPERIENCE_PTS


        return await level_up(users, member)

async def level_up(users, member):
    if (client.user.id != member.id):
        mID = str(member.id)
        experience = users[mID]['experience']
        currentLevel = users[mID]['level']
        nextLevel = int(experience ** (1/1.8))
        if (currentLevel < nextLevel):
            users[mID]['level'] = nextLevel
            return (True, nextLevel)
    return (False, None)


async def promote_user(message, users, member):

    level = users[str(member.id)]['level']

    if (level == 5): #yeast-ingester
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['breadlings'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['yeast-ingester'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} has been promoted to yeast-ingester!')

    elif (level == 10): #bread-connoisseur
        
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['yeast-ingester'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['bread-connoisseur'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} has been promoted to bread-connoisseur!')
        
    elif (level == 15): #BS
        
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['bread-connoisseur'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['B.S. in Bread Science'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} you have been given a B.S. in Bread Science!')
        
    elif (level == 20): #MS
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['B.S. in Bread Science'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['M.S. in Bread Science'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} you have been given an M.S. in Bread Science!')
    elif (level == 25): #PHD
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['M.S. in Bread Science'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['Ph.D. in Bread Science'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} Hello doctor! You have been given a Ph.D. in Bread Science!')
    elif (level == 30): #BREAD GOD
        removeRole = discord.utils.get(member.guild.roles, id = ROLE_IDS['Ph.D. in Bread Science'])
        await member.remove_roles(removeRole)
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['BREAD GOD'])
        await member.add_roles(role)
        await message.channel.send(f'{message.author.mention} you are now a BREAD GOD.')
    else:
        await message.channel.send(f'{message.author.mention} You\'re now on level {level}!')

def revertPromotion(level, member):
    if level < 5:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['breadlings'])

    elif level >= 5 and level <=9:

        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['yeast-ingester'])
    elif level >=10 and level <= 14:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['bread-connoisseur'])

    elif level >= 15 and level <= 19:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['B.S. in Bread Science'])

    elif level >= 20 and level <= 24:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['M.S. in Bread Science'])

    elif level >= 25 and level <= 29:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['Ph.D. in Bread Science'])

    else:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['BREAD GOD'])


    return role
        

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as userFiles:
        users = json.load(userFiles)
    
    response = await add_user(users, member) 
    if response[0] == 'exists':
        role = revertPromotion(response[1], member)
    else:
        role = discord.utils.get(member.guild.roles, id=ROLE_IDS['breadlings'])

    await member.add_roles(role)
    

    with open('users.json', 'w') as userFiles:
        json.dump(users, userFiles)

@client.event
async def on_message(message):
    
    if message.author.id == client.user.id:
        return


    if message.guild == None:
        await message.channel.send('This bot only works in servers!')
        return

    if '!t' in message.content or '!talk' in message.content:
        await message.channel.send('Broken for now. Please wait till father stops being lazy')
        #await client.process_commands(message)
        return
    

    await client.wait_until_ready()
    with open('users.json', 'r') as userFiles:
        users = json.load(userFiles)

    
    await add_user(users, message.author)
    userTuple = await add_experience(message, users, message.author)
    if (userTuple[0]):
        await promote_user(message, users, message.author)


    with open('users.json', 'w') as userFiles:
        json.dump(users, userFiles)

    await client.process_commands(message)

async def status_task():
    while True:
        game = discord.Game(random.choice(activities))
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(1800)

async def keepConnection():
    cb.browser.get(cb.url)

@client.event
async def on_ready():
    
    client.loop.create_task(status_task())
    #client.loop.create_task(keepConnection())

    print(discord.__version__)
    print('We have logged in as {0.user}'.format(client))
    print(f'ID: {client.user.id}')

if __name__ == '__main__':
    client.run(TOKEN)

