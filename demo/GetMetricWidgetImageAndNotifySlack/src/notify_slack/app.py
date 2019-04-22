# -*- coding: utf-8 -*-

import os
import json
from slackclient import SlackClient

import log
logger = log.get_logger('INFO')

verification_token = os.environ['SlackVerificationToken']
slack = SlackClient(verification_token)

def upload_file(event):
    logger.info(json.dumps({
        'action': 'upload_file',
        'args': event
    }))
    if not event.get('image'): return None
    res = slack.api_call(
        'files.upload',
        title = event.get('title'),
        initial_comment = event.get('initial_comment'),
        content = event.get('content'),
        channels = [event.get('channel')],
        file = bytes.fromhex(event.get('image')),
    )
    logger.info(json.dumps(res))
    return res

def handle(event):
    upload_file(event)

def lambda_handler(event, context):
    records = event.get('Records')
    for record in records:
        item = json.loads(record['Sns']['Message'])
        handle(item)
