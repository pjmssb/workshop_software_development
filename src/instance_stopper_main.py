import sys
import datetime
from typing import List 
from cli_instance_adapter import CLIInstanceManager 
from aws_ec2_instance_adapter import AWSEC2InstanceManager 
from file_logger_adapter import FileLoggerAdapter
from cloudwatch_logger_adapter import CloudWatchLoggerAdapter

LOCAL_LOG_FILE = 'instance_stopper'
LOG_GROUP = 'instance_manager'
LOG_STREAM = 'instance_stopper'

# Main program logic for the use case
def main(instances:List[str], environment:str):
    
    
    #Select the proper logger adapter
    if environment == 'CLOUD':        
        logger = CloudWatchLoggerAdapter(LOG_GROUP, LOG_STREAM)
    else:        
        logger = FileLoggerAdapter(LOCAL_LOG_FILE)

    for instance in instances:
        try:
            #Select the proper 
            if environment == 'CLOUD':
                instance_manager = AWSEC2InstanceManager(instance)
            else:
                instance_manager = CLIInstanceManager(instance)

            # Attempt to stop the instance
            server_shutdown_result_code, server_shutdown_result_text = instance_manager.stop_instance()
                            
            # Logging the result
            timestamp = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M:%S")
            result = f"Resultado {environment}, {instance} - [{server_shutdown_result_code}] - {server_shutdown_result_text}, "
            logger.log('instance_management', timestamp, result)

        except Exception as e:
            print(f"Error: {str(e)}")
            result = f"Resultado {environment}, {instance} - [555] - Exception {str(e)}, "
            logger.log('instance_management', timestamp, result)

# Command Line entry point for the program
if __name__ == "__main__":
    # Example usage, ideally you would parse these from CLI args or Lambda event
    instances = [
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dba',
        'arn:aws:ec2:sa-east-1:529025452537:instance/i-0c115728111814dbxa',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dbb',
        'arn:aws:ec2:eu-west-3:529025452537:instance/i-0c115728111814dby',
        'arn:aws:ec2:ap-southeast-2:529025452537:instance/i-0c115728111814dbc'
    ]
    environment = 'LOCAL'  # or 'CLOUD'

    main(instances, environment)
