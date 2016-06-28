from twitterbot_utils import Twibot

# pylint: disable=E1101
source = Twibot().api.me().timeline
max_id = min(t.id for t in source(count=100))
tweets_temp = source(count=200, max_id=max_id)


while tweets_temp:
    max_id = min(t.id for t in tweets_temp)
    for tweet in tweets_temp:
        try:
            tweet.destroy()
        except:
            pass
    tweets_temp = source(count=200, max_id=max_id)
