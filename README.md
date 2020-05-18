
<html>
    <h1 align="center">Breadbot: A Custom Discord Bot Made With Python for <a href="https://www.youtube.com/channel/UCQrrVVps9XlOeftIR0XhKuQ">Magenta Squash</a></h1>
    <p align="center">
    <img src="https://github.com/lemontwig/BreadBot/blob/master/selfie.png"></img>
    </p>
</html>

# Commands Supported
## Leveling System

<html>
<p>
Created a leveling system to engage users into obtaining XP points by talking in the server. The more they talk, the more they rank up!
</p>
</html>

```
!levels
```
Returns [this image](https://github.com/lemontwig/BreadBot/blob/master/levels.png) to show the levels mapped to their roles.


```
!ranking
```
Returns a custom ranking card [like these.](https://i.imgur.com/l30XQHt.png) Utilizes Pillow and reads from the JSON file to obtain current XP and level.

```
!leaderboard | !lb
```
Obtains the top 15 users of the server and uses matplotlib to create a bar graph showing their current XP standing [like this](https://imgur.com/gallery/QG80zEq) (the usernames are blocked).

## YouTube 

```
!yt <query>
```
Uses the YouTube API to search for a video using the given query. Will return the first video returned by the API.

```
!subcount <username> | !subs <username>
```
Will try its best to return the subcount of the given username. If no username is given, it will return the subcount of [Magenta Squash](https://www.youtube.com/channel/UCQrrVVps9XlOeftIR0XhKuQ)

## Image Manipulation
```
!deepfry <image>
```
Will deepfry the given image. Uses Pillow to bump up the contrast and saturation... for fun.

```
!swirl <image>
```
Will swirl the center of the image. Why? Users wanted it, I think.

```
!mirrorL <image> | !mirrorR <image>
```
Will take the left/right part of the image to mirror it to the opposite side. Uses Pillow.

## Misc. Commands

```
!talk <message> | !t <message>
```
Uses an alternative free Cleverbot (basically a headless driver connecting to Cleverbot as a "user"). Simulates talking to my bot.


```
!anagram <query>
```
Uses Wordsmith and BeautifulSoup4 to obtain some anagrams of the given query. Allows up to 23 characters (Wordsmith's limit).

```
!spotify <query> | !s <query>
```
Tries its best to look up the song/album/artist on Spotify.

```
!count
```
Returns the current member count in the server. Currently over 600!

```
!bread
```
Uses Pixabay to fetch images of bread. It's the main theme of the YouTube account.

```
!portapotty
```
Randomly chooses an image of a portypotty from a text file. Users wanted this and I wanted to see if I can fetch porta potty images, so here we are.

```
!rockdog
```
Returns an image of [rockdog.](https://github.com/lemontwig/BreadBot/blob/master/rockdog.jpg) There's kinda a cult thing goin' on.

```
!magenta8 <question>
```
Returns a magical fate... or just randomly picks a decision for you. Literally an 8ball.

```
!social
```
Just returns Magenta Squash's social media accounts.


```
!help
```
Returns what I wrote above!


# Uses
- [Discord Py](https://discordpy.readthedocs.io/en/latest/)
- [YouTube API](https://developers.google.com/youtube/v3)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Matplotlib](https://matplotlib.org/)
- [Pixabay API](https://pixabay.com/api/docs/)
- [Cleverbot Free](https://github.com/plasticuproject/cleverbotfree)
- [Wordsmith Anagram](https://wordsmith.org/anagram/)
