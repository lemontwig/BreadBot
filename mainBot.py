import discord
import random
import multiScraper
from discord.ext.commands import Bot

TOKEN = 'NTk3NTIwMjM1ODg0NzA3ODYy.XSJfTw.ItBVmzQ1pGlFEr9Kp4Abx-QeAPk'
PREFIXES = ('?', '!')
#client = discord.Client()
client = Bot(command_prefix=PREFIXES)


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


@client.command(name="anagram",
                description="anagrams any given word(s)",
                pass_context=True)
async def spitAnagram(context):
    print(f"Message: {context.message}")

    print( multiScraper.main(context.message) )
    await client.say(multiScraper.main(context.message))
# end of anagram scraper

"""
@client.event
async def on_message(message):
	if message.startswith("!anagram"):
		await client.say(multiScraper.main(message)
"""

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
