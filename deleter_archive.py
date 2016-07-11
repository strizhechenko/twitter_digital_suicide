# coding: utf-8
import os
import sys
import json
from zipfile import ZipFile
from twitterbot_utils import Twibot


def extract(archive, output):
    u""" распаковываем архив """
    if not os.path.isdir(output):
        os.mkdir(output)
    os.chdir(output)
    ZipFile(archive).extractall()


def read_tweets(dump):
    u""" читаем 'json'-дампы """
    return json.loads(open(dump).read().split('\n', 1)[1])


def read_tweets_all(output):
    u""" Получаем группы твитов из кусочков json"""
    datadir = output + '/data/js/tweets/'
    return [read_tweets(datadir + dump) for dump in os.listdir(datadir)]


def tweets_ids(tweets_all):
    u""" из групп твитов получаем прямой список id """
    return [tweet.get('id') for tweet_group in tweets_all for tweet in tweet_group]


def archive2ids(archive, output, cwd='/Users/oleg/git/purge_twitter'):
    u""" даём на вход путь до архива, на выходе - список id твитов """
    archive = cwd + '/twitter.zip'
    output = cwd + '/output'
    extract(archive, output)
    return tweets_ids(read_tweets_all(output))


def main():
    api = Twibot().api
    cwd = os.getcwd()
    archive = cwd + '/twitter.zip'
    output = cwd + '/output'
    ids = archive2ids(archive, output, cwd)

    if len(sys.argv) > 1:
        last_tweet_id = int(sys.argv[1])
        ids = [tweet_id for tweet_id in ids if tweet_id >= last_tweet_id]

    for tweet_id in ids:
        print 'destroy', tweet_id
        try:
            tweet = api.get_status(tweet_id)
            tweet.destroy()
            with open('last_deleted_tweet_id') as last_tweet_file:
                last_tweet_file.write(str(tweet_id))
        except Exception as err:
            print err

if __name__ == '__main__':
    main()
