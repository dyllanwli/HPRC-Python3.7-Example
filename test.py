import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
boundbox = [-171.791110603, 18.91619, -66.96466, 71.3577635769]

def sperateBoundbox(degree):
    
    minlong = boundbox[0]
    minlat = boundbox[1]
    maxlong = boundbox[2]
    maxlat = boundbox[3]

    degree = 1000

    boxs = []
    detal_lat = (maxlat-minlat)/degree
    detal_long = (maxlong - minlong)/degree

    l1 = minlong
    l2 = minlat


    for x in range(degree):
        l1 = minlong
        l2 += detal_lat
        l4 = l2 + detal_lat
        for y in range(degree):
            l1 += detal_long
            l3 = l1 + detal_long
            box = [l1, l2, l3, l4]
            boxs.append(box)
    return boxs


import csv

def create_csv():
    title = ['_api',
             '_json',
             'author',
             'contributors',
             'coordinates',
             'created_at',
             'destroy',
             'display_text_range',
             'entities',
             'favorite',
             'favorite_count',
             'favorited',
             'filter_level',
             'geo',
             'id',
             'id_str',
             'in_reply_to_screen_name',
             'in_reply_to_status_id',
             'in_reply_to_status_id_str',
             'in_reply_to_user_id',
             'in_reply_to_user_id_str',
             'is_quote_status',
             'lang',
             'parse',
             'parse_list',
             'place',
             'quote_count',
             'reply_count',
             'retweet',
             'retweet_count',
             'retweeted',
             'retweets',
             'source',
             'source_url',
             'text',
             'timestamp_ms',
             'truncated',
             'user']
    with open('example.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(title)

def write_csv(data):
    with open('example.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

status_frame = []
create_csv()
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        contents = []
        for attr in dir(status):
            if not attr.startswith("__"):
                contents.append(getattr(status, attr))
                write_csv(contents)
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(locations = boundbox, is_async=False)