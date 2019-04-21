# -*- coding: utf-8 -*-

import os
import json
import yaml
import boto3
import datetime

import log
logger = None

config_bucket = os.environ['ConfigBucket']
config_key = os.environ['ConfigKeyName']
target_topic = os.environ['NotificationTargetTopicArn']

s3 = boto3.resource('s3')
cw = boto3.client('cloudwatch')
sns = boto3.client('sns')


def get_config(config_bucket: str, config_key: str):
    timestamp = datetime.datetime.utcnow().timestamp()
    config_path = '/tmp/config.' + str(datetime.datetime.utcnow().timestamp())
    bucket = s3.Bucket(config_bucket)
    bucket.download_file(config_key, config_path)
    with open(config_path, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
        return config


def get_metric_widget_image(item):
    params = item.copy()
    if params.get('start'):
        params['start'] = (datetime.datetime.now() - datetime.timedelta(minutes=int(item.get('start')))).isoformat()
    return cw.get_metric_widget_image(MetricWidget=json.dumps(params))


def get_message(format, item, image) -> str:
    return f"{{{format}}}".format(hex_image=image.hex(), title=item.get('title') or "")


def notify(message: str, topic: str):
    res = sns.publish(
        TopicArn=topic,
        Message=message,
    )
    logger.info(res)
    return res


def lambda_handler(event, context):
    config = get_config(config_bucket, config_key)
    global logger
    logger = log.get_logger(config.get('log_level'))

    items = config['items']
    format = config['message_format']
    for item in items:
        metric_image = get_metric_widget_image(item)
        message = get_message(format, item, metric_image['MetricWidgetImage'])
        notify(message, target_topic)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': {}
    }
