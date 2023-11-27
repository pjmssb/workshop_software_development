import unittest
from unittest.mock import patch
import os
import sys
from datetime import datetime
sys.path.append('./src')  
from file_logger_adapter import FileLoggerAdapter

class TestFileLoggerAdapter(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_log(self, mock_open):
        logger = FileLoggerAdapter("test_log")
        timestamp = datetime(2023, 1, 1, 12, 0)
        logger.log("TestEvent", timestamp, "Test info")

        # Check if the correct file is opened
        mock_open.assert_called_once_with("test_log-2023-01-01.log", 'a')

        # Check if the write function is called with the correct string
        handle = mock_open()
        handle.write.assert_called_once_with("2023-01-01 12:00:00 - TestEvent - Test info\n")

if __name__ == '__main__':
    unittest.main()
