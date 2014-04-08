#encode: utf-8

import settings
import pika
import tweepy
import json
import jinja2

def get_api(api_key, api_secret, access_key, access_secret):
    handler = tweepy.auth.OAuthHandler(api_key, api_secret);
    handler.set_access_token(access_key, access_secret);
    return tweepy.API(handler);

def callback(ch, method, properties, body):
    global api;

    body = json.loads(body)
    template = body["template"]
    tpl = jinja2.Template(open("messages/" + template + ".tpl").read().decode("utf-8"));
    tweet = tpl.render(body["data"]);
    api.update_status(tweet);
    print u"tweet: " + tweet;

api = None;

if __name__ == '__main__':
        
    api = get_api(settings.API_KEY, settings.API_SECRET, settings.ACCESS_KEY, settings.ACCESS_SECRET);

    connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=settings.QUEUE_NAME);
    channel.basic_consume(callback, queue=settings.QUEUE_NAME, no_ack=True)

    channel.start_consuming()
    print "start bot_server"
