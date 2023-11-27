import instance_stopper_main


def lambda_handler():
    # Hard-coded list of instances
    instances = [
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbx',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
        'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
    ]
    environment = 'CLOUD'

    instance_stopper_main.main(instances, environment)

    return {
        'statusCode': 200,
        'body': 'Process initiated... check logs to see the progress'
    }
