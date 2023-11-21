# Importing necessary modules and adapters
# from cloud_instance_adapter import CloudInstanceAdapter
# from mock_instance_adapter import MockInstanceAdapter
# from cloudwatch_logging_adapter import CloudWatchLoggingAdapter
# from local_logging_adapter import LocalLoggingAdapter
import sys
import datetime
from typing import List 



#The Model
class InstanceStopper:
    SERVER_SHUTDOWN_SUCCESS = 200
    SERVER_SHUTDOWN_FAILED = 500
    SERVER_NOT_FOUND = 400

    def __init__(self) -> None:    
        pass #Here we may inject the instance_manager
        
    def stop_instance(self, instance_name:str) -> (int, str):
        print(instance_name)
        return self.SERVER_SHUTDOWN_SUCCESS, f"The server '{instance_name}' whas shutdown correctly"
    

# Main program logic for the use case
def main(instances:List[str], environment:str):
    print(environment)

    instance_stopper = InstanceStopper()

    for instance in instances:
        try:
            # Attempt to stop the instance
            server_shutdown_result_code, server_shutdown_result_text = instance_stopper.stop_instance(instance)
                            
            # Logging the result
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #logger.log(environment, timestamp, instance, result)
            print(f"Resultado [{server_shutdown_result_code}] - {server_shutdown_result_text}, {timestamp}")

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
