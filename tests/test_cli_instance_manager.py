import unittest
import sys
sys.path.append('./src')  
from cli_instance_adapter import CLIInstanceManager

class TestCLIInstanceManager(unittest.TestCase):

    def setUp(self):
        self.instance_manager = CLIInstanceManager()

    def test_stop_instance_with_well_formed_arn_success(self):
        instance_name = "arn:aws:ec2:region:account:instance/instance-id"
        code, message = self.instance_manager.stop_instance(instance_name)
        self.assertEqual(code, self.instance_manager.SERVER_SHUTDOWN_SUCCESS_CODE)
        self.assertIn("Success", message)

    def test_stop_instance_with_bad_arn(self):
        instance_name = "bad-arn-format"
        code, message = self.instance_manager.stop_instance(instance_name)
        self.assertEqual(code, self.instance_manager.SERVER_BAD_ARN_CODE)
        self.assertIn("ARN string is not well formatted", message)

    # Add more tests for different scenarios like instance not found, shutdown failed, etc.

if __name__ == '__main__':
    unittest.main()
