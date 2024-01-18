# Discord-Movie-Recommendation-Bot
# Discord Movie Recommender Bot

## Overview
This Discord bot utilizes sentiment analysis to recommend movies based on the user's mood. The bot analyzes recent messages, categorizes emotions, and suggests personalized movie recommendations from predefined lists. Movie details are fetched from the OMDb API, and recommendations are sent to users via Discord embeds.

## Features
- **Sentiment Analysis:** Analyzes user messages to determine emotions (happy, sad, angry, surprise, fear).
- **Movie Recommendations:** Recommends three movies based on the user's mood.
- **OMDb Integration:** Fetches movie details (posters, release years, IMDb links, plot summaries) from the OMDb API.
- **Discord Embeds:** Sends visually appealing recommendation messages to users.

## Setup
1. Install required libraries: `discord`, `nltk`, `requests`.
   ```bash
   pip install discord nltk requests
2. Get API tokens
3. Replace placeholders in the script:

  API_TOKEN: Replace with your Discord bot token.
  OMDB_TOKEN: Replace with your OMDb API token.
4. run the bot

## Usage
-Trigger the bot by sending a message starting with "shini movie" on your Discord server. The bot will analyze your recent messages, determine your mood, and send personalized movie recommendations.
