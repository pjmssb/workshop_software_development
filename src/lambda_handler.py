import main

def lambda_handler(event, context):
    # Hard-coded list of instances
    instances = [
        arn:aws:ec2:<REGION>:<ACCOUNT_ID>:instance/<instance-id>.
    ]

    # Environment set to 'CLOUD'
    environment = 'CLOUD'

    # Call the main function from main.py
    main.main(instances, environment)

    return {
        'statusCode': 200,
        'body': 'Instances processed successfully'
    }
