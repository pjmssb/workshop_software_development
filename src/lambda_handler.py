import main

def lambda_handler(event, context):
    # Hard-coded list of instances
    instances = [
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbxa',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
        'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
    ]
    environment = 'CLOUD'

    main.main(instances, environment)

    return {
        'statusCode': 200,
        'body': 'Instances processed successfully'
    }
