import tweepy
import config
import csv
from datetime import date, datetime, timedelta
import time

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

mens_shoe_brands = ['Air Jordan', 'New Balance', 'Nike', 'Adidas', 'Greats The Court', 'Salomon', 'Y-3']

present = datetime.now()
past_date = present - timedelta(days=1)

count = 0;
# for brand in mens_shoe_brands
t0 = time.time()
# try:
for tweet in tweepy.Cursor(api.search,q="Air Jordan",count=100,\
                       lang="en",\
                       since_id=past_date).items():
    if (tweet.created_at < past_date): break
    count = count + 1
# except tweepy.TweepError as e:
#     # do nothing while we figure out what went wrong
#     print("error")

t1 = time.time()
td = t1 - t0;
print(count)
print(td)

count = 0;
# for brand in mens_shoe_brands
t0 = time.time()

result = True
resultsTweets = []
last_id = None

while result:
    result = api.search(q='Air Jordan', count=100, lang="en", max_id=last_id)
    # print(result[0].created_at)
    resultsTweets.extend(result)
    # print(len(resultsTweets))
    if (result[-1].created_at < past_date): break
    last_id = result[-1].id - 1
    # process_result(result)
for res in  resultsTweets:
    if (res.created_at < past_date): resultsTweets.remove(res)

t1 = time.time()
td = t1 - t0;
print(len(resultsTweets))
print(td)


    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
