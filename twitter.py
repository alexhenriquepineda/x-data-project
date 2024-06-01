import os
import tweepy
from api_keys import CONSUMER_KEY, CONSUMER_SECRET, BEARER_TOKEN, ACCESS_KEY, ACCESS_SECRET


def make_twitter_post(files_folder, pdf_name, text):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(
        ACCESS_KEY,
        ACCESS_SECRET,
    )

    newapi = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
    )

    api = tweepy.API(auth)
    media_ids = []
    image_files = sorted(os.listdir(files_folder + pdf_name))
    image_files = image_files[:4]
    for image in image_files:
        res = api.media_upload(files_folder + pdf_name + "/" + image)
        media_ids.append(res.media_id_string)

    newapi.create_tweet(text=text, media_ids=media_ids)

    print(f"TWEET REALIZADO COM SUCESSO")

