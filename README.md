GetMetricWidgetImage
=====

Get Amazon CloudWatch Widget Image and Notify Amazon SNS Topic of it

## How to Deploy
### Use Serverless Application Repository

1. Upload config file(config.yaml) to S3 Bucket
2. Deploy [Application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:247601741829:applications/GetMetricWidgetImage) with Serverless Application Repository


### Use Deploy Script

1. run `cp .env.template .env}` and set up `.env` file
2. run `cp config.template.yaml config.yaml` and set up `config.yaml` file
3. run `./scripts/update_config`
4. run `./scripts/deploy`


### Nested Application

Add the resource below into your SAM template

```yaml
  GetMetricWidgetImage:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:247601741829:applications/GetMetricWidgetImage
        SemanticVersion: 1.0.0
      Parameters:
        ConfigBucket: YOUR_VALUE
        ConfigKey: YOUR_VALUE
        NotificationTargetTopicArn: YOUR_VALUE
        # RetentionInDays: '7' # Uncomment to override default value
        # Schedule: 'rate(60 minutes)' # Uncomment to override default value
```

## Demo

See: `./demo/GetMetricWidgetImageAndNotifySlack`
