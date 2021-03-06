import tweepy
from datetime import datetime
import csv
import os
# import daemon

def test(api):
    # Test api
    public_tweets = api.home_timeline()
    print(len(public_tweets))


def load_config_tk(filename):
    with open(filename, "r") as f:
        consumer_key, consumer_secret, access_token, access_token_secret = [line.strip() for line in f.readlines()]
        print(consumer_key, consumer_secret, access_token, access_token_secret)
        return consumer_key, consumer_secret, access_token, access_token_secret

def sperateBoundbox(degree):

    minlong = boundbox[0]
    minlat = boundbox[1]
    maxlong = boundbox[2]
    maxlat = boundbox[3]

    degree = 1000

    boxs = []
    detal_lat = (maxlat - minlat) / degree
    detal_long = (maxlong - minlong) / degree

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


def create_csv(filename):
    print("Start running on", filename)
    title = [
        "_api",
        "_json",
        "author",
        "contributors",
        "coordinates",
        "created_at",
        "destroy",
        "display_text_range",
        "entities",
        "favorite",
        "favorite_count",
        "favorited",
        "filter_level",
        "geo",
        "id",
        "id_str",
        "in_reply_to_screen_name",
        "in_reply_to_status_id",
        "in_reply_to_status_id_str",
        "in_reply_to_user_id",
        "in_reply_to_user_id_str",
        "is_quote_status",
        "lang",
        "parse",
        "parse_list",
        "place",
        "quote_count",
        "reply_count",
        "retweet",
        "retweet_count",
        "retweeted",
        "retweets",
        "source",
        "source_url",
        "text",
        "timestamp_ms",
        "truncated",
        "user",
    ]
    with open(filename, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(title)


def write_csv(data):
    filename = datetime.now().strftime("%Y%m%d-%H") + ".csv"
    if os.path.isfile(filename):
        pass
    else:
        create_csv(filename)
    with open(filename, "a") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        contents = []
        if ignoreGeoTag or status.geo is not None:
            for attr in dir(status):
                if not attr.startswith("__"):
                    contents.append(getattr(status, attr))
            # print(status.text)
            write_csv(contents)

    def on_error(self, status_code):
        if status_code == 420:
            print("Error: Status Code 420")
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.



consumer_key, consumer_secret, access_token, access_token_secret = load_config_tk("token.tk")

# setup api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# test
test(api)

#setup boundbox
boundbox = [-171.791110603, 18.91619, -66.96466, 71.3577635769]

#setup geoconfig: if Ture, get every tweet; if False, only tweet with geotag will write down
ignoreGeoTag = False

# with daemon.DaemonContext():
print("Start running on", datetime.now().strftime("%Y%m%d-%H%M%S"))
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(locations=boundbox, is_async=False)

