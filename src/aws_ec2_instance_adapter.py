# Command line adapter for instance_manager
from instance_manager_port import InstanceManagerPort
import boto3
from botocore.exceptions import ClientError
import re


class AWSEC2InstanceManager(InstanceManagerPort):

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def _is_arn_well_formed(self, arn: str) -> bool:
        '''
        Simple ARN format validation (can be extended
        for more specific ARN formats)
        '''
        pattern = r'arn:aws:ec2:[a-z0-9-]+:\d+:instance/[a-z0-9-]+'
        return re.match(pattern, arn) is not None

    def _is_instance_allow_stop(self, instance_id: str) -> bool:
        try:
            response = \
                self.ec2_client.describe_instances(InstanceIds=[instance_id])
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    for tag in instance.get('Tags', []):
                        if tag['Key'] == 'allow_stop' and \
                                tag['Value'].lower() == 'true':
                            return True
            return False
        except ClientError as error:
            print(f"Error retrieving instance information: {error}")
            return False

    def stop_instance(self, arn: str = '') -> (int, str):
        if not self._is_arn_well_formed(arn):
            return self.SERVER_BAD_ARN_CODE, self.SERVER_BAD_ARN_TEXT

        # Extract instance ID from ARN
        instance_id = arn.split('/')[-1]

        if not self._is_instance_allow_stop(instance_id):
            return self.SERVER_NOT_FOUND_CODE, self.SERVER_NOT_FOUND_TEXT

        try:
            self.ec2_client.stop_instances(InstanceIds=[instance_id])
            return self.SERVER_SHUTDOWN_SUCCESS_CODE, \
                self.SERVER_SHUTDOWN_SUCCESS_TEXT
        except ClientError as error:
            print(f"Error stopping instance: {error}")
            return self.SERVER_SHUTDOWN_FAILED_CODE, \
                self.SERVER_SHUTDOWN_FAILED_TEXT
