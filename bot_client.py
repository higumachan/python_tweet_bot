#coding: utf-8

import sys
sys.path.append("../")

import pika
import json
import settings

def tweet(template_file, **kwargs):
    body = {
         "template": template_file,
         "data": kwargs,
     }
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=settings.QUEUE_NAME)

    channel.basic_publish(exchange='', routing_key=settings.QUEUE_NAME, body=json.dumps(body))
    connection.close();

if __name__ == '__main__':
    tweet("update_ranking", user={"name": u"なでこ",}, problem={"_id": "1"});
