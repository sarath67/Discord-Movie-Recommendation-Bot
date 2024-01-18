import discord
import nltk
import random
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

API_TOKEN = 'bot_token'
OMDB_TOKEN = 'omdb_token'

surprise = [
    "Kandukondain Kandukondain", "Kaakha Kaakha", "Ghilli", "Mozhi", "Sivaji",
    "Kalavani"
]
angry = [
    "Thenali", "Middle Class Madhavan", "Chennai 600028",
    "Kalyana Samayal Saadham"
]
happy = [
    "Anniyan", "Paruthiveeran", "Subramaniapuram", "Ayan", "Madrasapattinam"
]
sad = [
    "Vennila Kabadi Kuzhu", "Naan Kadavul", "Pasanga", "Vaaranam Aayiram",
    "Mynaa"
]
fear = [
    "Chandramukhi", "Pizza", "13B", "Demonte Colony", "Sivi", "Yaavarum Nalam"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_emotions(text):
  sid = nltk.sentiment.vader.SentimentIntensityAnalyzer()
  sentiment_scores = sid.polarity_scores(text)

  emotions = {
      'Happy': sentiment_scores['pos'],
      'Sad': sentiment_scores['neg'],
      'Angry': sentiment_scores['neg'],
      'Surprise': sentiment_scores['compound'],
      'Fear': sentiment_scores['neg']
  }

  return emotions


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  user_id = message.author.id
  messages = ""

  if message.content.startswith('shini movie'):
    for chan in message.guild.text_channels:
      async for msg in chan.history(limit=5):
        if msg.author.id == user_id:

          messages = messages + " " + msg.content
    messages = messages.replace('\n', '')
    messages = messages.replace('\t', '')
    messages = messages.strip('\n')
    messages = messages.strip('\t')

    emotions = get_emotions(messages)

    Keymax = max(emotions, key=emotions.get)

    if Keymax == 'Happy':
      movie_array = happy
    elif Keymax == 'Angry':
      movie_array = angry
    elif Keymax == 'Surprise':
      movie_array = surprise
    elif Keymax == 'Sad':
      movie_array = sad
    elif Keymax == 'Fear':
      movie_array = fear

    RandomListOfIntegers = []

    while len(movie_array) < 3:
      movie_array.append(random.choice(movie_array))

    while len(RandomListOfIntegers) < 3:
      r = random.randint(0, len(movie_array) - 1)
      if r not in RandomListOfIntegers:
        RandomListOfIntegers.append(r)

    # Assign 3 random movie titles
    movie1 = movie_array[RandomListOfIntegers[0]]
    movie2 = movie_array[RandomListOfIntegers[1]]
    movie3 = movie_array[RandomListOfIntegers[2]]

    # OMDB api call with selected movies
    omdb_base_url = 'https://www.omdbapi.com/?apikey=' + OMDB_TOKEN
    movie1_url = omdb_base_url + '&t=' + movie1
    movie1_response = requests.get(movie1_url)
    movie1_json = movie1_response.json()

    movie2_url = omdb_base_url + '&t=' + movie2
    movie2_response = requests.get(movie2_url)
    movie2_json = movie2_response.json()

    movie3_url = omdb_base_url + '&t=' + movie3
    movie3_response = requests.get(movie3_url)
    movie3_json = movie3_response.json()

    # Process and format result from OMDB api
    newline = '\n'
    movie1_poster = movie1_json['Poster']
    movie2_poster = movie2_json['Poster']
    movie3_poster = movie3_json['Poster']

    movie1_year = movie1_json['Year']
    movie2_year = movie2_json['Year']
    movie3_year = movie3_json['Year']

    movie1_plot = movie1_json['Plot']
    movie2_plot = movie2_json['Plot']
    movie3_plot = movie3_json['Plot']

    movie1_id = movie1_json['imdbID']
    movie1_link = "https://www.imdb.com/title/" + movie1_id
    movie2_id = movie2_json['imdbID']
    movie2_link = "https://www.imdb.com/title/" + movie2_id
    movie3_id = movie3_json['imdbID']
    movie3_link = "https://www.imdb.com/title/" + movie3_id

    embed = discord.Embed(title="Hi there!",
                          description="Here are 3 picks based on your mood",
                          color=discord.Color.blue())
    embed.set_author(
        name="Genreator",
        icon_url=
        "https://pbs.twimg.com/profile_images/1169109470967820291/AJzI4C-S_400x400.jpg"
    )
    embed.add_field(name=f"1. {movie1}",
                    value=f"({movie1_year}) {newline} {movie1_link}",
                    inline=False)
    embed.set_image(url=f'{movie1_poster}')
    embed.set_footer(text=f"{movie1_plot}")

    await message.author.send(embed=embed)

    embed2 = discord.Embed(color=discord.Color.blue())
    embed2.add_field(name=f"2. {movie2}",
                     value=f"({movie2_year}) {newline} {movie2_link}",
                     inline=False)
    embed2.set_image(url=f'{movie2_poster}')
    embed2.set_footer(text=f"{movie2_plot}")

    await message.author.send(embed=embed2)

    embed3 = discord.Embed(color=discord.Color.blue())
    embed3.add_field(name=f"3. {movie3}",
                     value=f"({movie3_year}) {newline} {movie3_link}",
                     inline=False)
    embed3.set_image(url=f'{movie3_poster}')
    embed3.set_footer(text=f"{movie3_plot}")

    await message.author.send(embed=embed3)


client.run(API_TOKEN)
