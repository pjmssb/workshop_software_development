import unittest
from unittest.mock import patch
import sys
sys.path.append('./src')  # Adjust the path according to your project structure
import lambda_handler

class TestLambdaHandler(unittest.TestCase):

    @patch('lambda_handler.instance_stopper_main.main')
    def test_lambda_handler(self, mock_main):
        # Call the lambda handler
        response = lambda_handler.lambda_handler()

        # Assert that main function was called correctly
        expected_instances = [
            'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
            'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbx',
            'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
            'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
            'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
        ]
        mock_main.assert_called_once_with(expected_instances, 'CLOUD')

        # Assert that the response is correct
        expected_response = {
            'statusCode': 200,
            'body': 'Process initiated... check logs to see the progress'
        }
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
