import unittest
from unittest.mock import patch
from moto import mock_ec2
import sys
sys.path.append('./src')  
from aws_ec2_instance_adapter import AWSEC2InstanceManager

class TestAWSEC2InstanceManager(unittest.TestCase):

    @mock_ec2
    def setUp(self):
        self.instance_manager = AWSEC2InstanceManager()

    @patch('aws_ec2_instance_adapter.boto3.client')
    def test_stop_instance_with_well_formed_arn_success(self, mock_boto_client):
        mock_client = mock_boto_client.return_value
        mock_client.stop_instances.return_value = {}

        instance_arn = "arn:aws:ec2:region:account:instance/instance-id"
        code, message = self.instance_manager.stop_instance(instance_arn)
        self.assertEqual(code, self.instance_manager.SERVER_SHUTDOWN_SUCCESS_CODE)
        self.assertIn("Success", message)

    # Add more tests for different scenarios like bad ARN, instance not found, shutdown failed, etc.

if __name__ == '__main__':
    unittest.main()
