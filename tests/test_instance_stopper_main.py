import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import sys
sys.path.append('../src')  
from instance_stopper_main import main

class TestInstanceStopperMain(unittest.TestCase):

    @patch('instance_stopper_main.CLIInstanceManager')
    @patch('instance_stopper_main.FileLoggerAdapter')
    def test_main_local_environment(self, MockFileLoggerAdapter, MockCLIInstanceManager):
        # Setup mocks
        mock_logger = MockFileLoggerAdapter.return_value
        mock_instance_manager = MockCLIInstanceManager.return_value
        mock_instance_manager.stop_instance.return_value = (200, "Success - Instance shutdown")

        # Define test data
        instances = [
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbx',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
        'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
        ]
        environment = 'LOCAL'

        # Call the function
        main(instances, environment)

        # Assertions
        self.assertEqual(mock_instance_manager.stop_instance.call_count, len(instances))
        for instance in instances:
            mock_instance_manager.stop_instance.assert_any_call(instance)
            mock_logger.log.assert_any_call('instance_management', unittest.mock.ANY, unittest.mock.ANY)

    @patch('instance_stopper_main.AWSEC2InstanceManager')
    @patch('instance_stopper_main.CloudWatchLoggerAdapter')
    def test_main_cloud_environment(self, MockCloudWatchLoggerAdapter, MockAWSEC2InstanceManager):
        # Setup mocks
        mock_logger = MockCloudWatchLoggerAdapter.return_value
        mock_instance_manager = MockAWSEC2InstanceManager.return_value
        mock_instance_manager.stop_instance.return_value = (200, "Success - Instance shutdown")

        # Define test data
        instances = [
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbx',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
        'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
        ]
        environment = 'CLOUD'

        # Call the function
        main(instances, environment)

        # Assertions
        self.assertEqual(mock_instance_manager.stop_instance.call_count, len(instances))
        for instance in instances:
            mock_instance_manager.stop_instance.assert_any_call(instance)
            mock_logger.log.assert_any_call('instance_management', unittest.mock.ANY, unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()
