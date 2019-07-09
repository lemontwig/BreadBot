import discord, random, asyncio, json, urllib.parse, urllib.request
#import multiScraper
from discord.ext.commands import Bot

TOKEN = 'NTk3NTIwMjM1ODg0NzA3ODYy.XSJfTw.ItBVmzQ1pGlFEr9Kp4Abx-QeAPk'
PREFIXES = ('?', '!')
#client = discord.Client()
client = Bot(command_prefix=PREFIXES)
asyncState = type('', (), {})( )
asyncState.userMessage = ''

# Say hello!
@client.command(name="hello",
                description="Gives a friendly hello!",
                aliases=["intro", "hi"],
                pass_context=True)
async def sayHello(context):
    greetings = [f'What\'s up {context.message.author.mention}!', f'Hey guys! {context.message.author.mention} here.',
                  f'Hello {context.message.author.mention}']
    await client.say(random.choice(greetings))
# End of hello!

#"Magic" 8 Ball here
@client.command(name="magenta8",
                description="Answers yes/no questions",
                aliases=["8ball"],
                pass_context=True)
async def magenta_8(context, *args):
    if((list(args))[len(args)-1].endswith('?')):
        await client.say(context.message.author.mention + " Magenta8 says: " + random.choice(["It is certain", "Without a doubt", "Yes - definitely", "Most likely", "Yes" , "Cannot predict now", "Ask again later", "Forget about that. Eat bread.", "Don't count on it", "The bread gods say no", "Very doubtful"]) )
    else:
        await client.say(context.message.author.mention + " Make sure your question ends with a '?'")
# End of Magic 8 Ball

# start of breadscraping


@client.command(name="bread",
                description="Webscrapes google for images of delicious bread",
                pass_context=True)
async def getBread(context):
    await client.say("My master is working on this")
# end of breadscraping

# anagram scraper

def getAnagram(word):
	URL = 'http://www.anagramica.com/best/:' + word
	response = None
	try:
	    final = ''
	    response = urllib.request.urlopen(URL)
	    jsonText = response.read().decode(encoding = 'utf-8')
	    results = json.loads(jsonText)
	    for word in results['best']:
	        final += (word + ' ')
	    return final.strip().replace(' ', ', ')
		    
	except urllib.error.URLError:
	    pass
	finally:
	    if response != None:
		    response.close()


@client.command(name="anagram",
                description="anagrams the first word after the command",
                pass_context=True)
async def spitAnagram(context):
    try:

        await client.say(  context.message.author.mention + ' anagram(s) for ' + asyncState.userMessage + ': ' +  getAnagram((asyncState.userMessage.strip())))

    except: #will update with specific exception
        await client.say(context.message.author.mention + ' failed to obtain anagram')

    finally:
        asyncState.userMessage = ''

        
# end of anagram scraper

@client.event
async def on_message(message):
    if (message.content.startswith("!anagram")):
	    index = len('!anagram')
	    asyncState.userMessage = message.content[index:]
	    print( len(asyncState.userMessage))
    await client.process_commands(message)


@client.event
async def on_ready():
    await(client.change_presence(game=discord.Game(name=random.choice(
        ["with bread", "with bread crumbs", "with bagels", "with its baguette"]))))
    print('Logged in as')
    print(f"USER NAME: {client.user.name}")
    print(f"CLIENT ID: {client.user.id}")
    print('------')

if __name__ == '__main__':
    client.run(TOKEN)
