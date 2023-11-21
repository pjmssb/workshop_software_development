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
            # Attempt to stop the instance
            if environment == 'CLOUD':
                instance_manager = AWSEC2InstanceManager(instance)
            else:
                instance_manager = CLIInstanceManager(instance)
            
            server_shutdown_result_code, server_shutdown_result_text = instance_manager.stop_instance()
                            
            # Logging the result
            timestamp = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M:%S")
            result = f"Resultado [{environment}, {instance} - {server_shutdown_result_code}] - {server_shutdown_result_text}, "
            logger.log('instance_management', timestamp, result)

        except Exception as e:
            # Handle any exceptions that occur
            print(f"Error: {str(e)}")
            #logger.log(environment, datetime.datetime.now(), instance, f"Error: {str(e)}")

# Command Line entry point for the program
if __name__ == "__main__":
    # Example usage, ideally you would parse these from CLI args or Lambda event
    instances = ['instance1', 'instance2', 'instance8000']
    environment = 'LOCAL'  # or 'CLOUD'

    main(instances, environment)
