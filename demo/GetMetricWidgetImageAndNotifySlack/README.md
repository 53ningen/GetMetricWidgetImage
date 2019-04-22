GetMetricWidgetImageAndNotifySlack
=====

Get Amazon CloudWatch Widget Image and Notify Slack Channel of it

## How to Deploy
### Use Serverless Application Repository

1. Generate SlackVerificationToken and Fill it into `.env` file
2. Update `.env` and `config.yaml`
3. Upload Config File(config.yaml) to S3 Bucket: `./scripts/update_config`
4. Deploy this Application: `./scripts/deploy`
