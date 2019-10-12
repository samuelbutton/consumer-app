import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


import argparse
parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-db", "--hostname", help="Database name")
parser.add_argument("-u", "--username", help="User name")
parser.add_argument("-p", "--password", help="Password")
parser.add_argument("-size", "--size", help="Size", type=int)

args = parser.parse_args()

print( "Hostname {} User {} Password {} size {} ".format(
        args.hostname,
        args.username,
        args.password,
        args.size
        ))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#ps4",count=100,\
                           lang="en",\
                           since_id=2014-06-12).items():
    print tweet.created_at, tweet.text
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])