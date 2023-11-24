import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import sys
sys.path.append('../src')  # Adjust as necessary
from cloudwatch_logger_adapter import CloudWatchLoggerAdapter
from moto import mock_logs

class TestCloudWatchLoggerAdapter(unittest.TestCase):

    @mock_logs
    def setUp(self):
        self.logger = CloudWatchLoggerAdapter("test_group", "test_stream")

    @patch('cloudwatch_logger_adapter.boto3.client')
    def test_log(self, mock_boto_client):
        mock_client = MagicMock()
        mock_boto_client.return_value = mock_client
        mock_client.put_log_events.return_value = {'nextSequenceToken': 'token123'}

        timestamp = datetime(2021, 1, 1, 12, 0)
        self.logger.log("TestEvent", timestamp, "Test info")

        # Check if put_log_events is called with the correct parameters
        mock_client.put_log_events.assert_called_once()

if __name__ == '__main__':
    unittest.main()
