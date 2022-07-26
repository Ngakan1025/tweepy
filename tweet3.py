import tweepy
import csv
import pandas as pd

api_key = 'rxiU480HOYxFdq8O0CJhRJ93K'
api_key_secret = '6W8NlC9Nq8oGMMzwhUa0En2v82GRzipQ9EXQyddImel7KQDGHN'

access_token = '1551423587210637312-kHgvfPEj71E5nRVe05fEg01nKlVjIx'
access_token_secret = 'FZHTO7JIOmeTzgue1WAKOOQkAfnporn1V3tZVJqoWZ6i6'

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searchTerm = input("Maukkan Keyword/Tag yang ingin dicari: ")
NoOfTerms = int(input("Masukkan berapa banyak tweets yang ingin dicari: "))

csvFile = open(searchTerm+".csv", "a+", newline="",
               encoding="utf-8")  # membuat csv
csvWriter = csv.writer(csvFile)  # membaca csv nya

# create dataframe
columns = ['Time', 'User Id', 'User', 'Verified', 'user Description', 'Lokasi',
           'Jumlah Like', 'Source Tweet', 'Jumlah Retweet', 'Tweet']
data = []

for tweet in tweepy.Cursor(api.search_tweets, q=searchTerm, since_id="2022-07-23", until="2022-07-25", lang="id").items(NoOfTerms):
    data.append([tweet.created_at, tweet.user.id, tweet.user.screen_name, tweet.user.verified,
                tweet.user.description, tweet.user.location, tweet.favorite_count, tweet.source, tweet.retweet_count, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv(searchTerm+".csv")
