import json
import os
import smtplib
from kafka import KafkaConsumer

consumer = KafkaConsumer(
        os.environ['TOPIC_NAME'],
        bootstrap_servers=os.environ['KAFKA_BROKER'],
        auto_offset_reset='earliest',
        group_id=os.environ['CONSUMER_GROUP'])


def consume():
    for msg in consumer:
        try:
            body = json.loads(msg.value)
            content = body['body']
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            sender = 'iiits.oj@iiits.in'
            recipient = body['email']
            mail.login('iiits.oj@gmail.com', 'Admin@321')
            header = 'To:' + recipient + '\n' + 'From:' \
                     + sender + '\n' + 'subject:'+body['subject']+'\n'
            content = header + content
            mail.sendmail(sender, recipient, content)
            mail.close()
        except():
            print("Error");


consume()
