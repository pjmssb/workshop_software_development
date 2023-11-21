#Command line adapter for instance_manager 
from instance_manager_port import InstanceManagerPort

class CLIInstanceManager(InstanceManagerPort):
    
    def __init__(self, instance_name:str) -> None:
        self.instance_name = instance_name
              
    def stop_instance(self) -> (int,str):

        last_char = self.instance_name.upper()[len(self.instance_name)-1]
        #if instance name ends in 'X' responds the instance was not found
        if last_char == 'X':
            return self.SERVER_NOT_FOUND_CODE, self.SERVER_NOT_FOUND_TEXT

        #if instance name ends in 'Y' responds the instance was not found
        if last_char == 'Y':
            return self.SERVER_SHUTDOWN_FAILED_CODE, self.SERVER_SHUTDOWN_FAILED_TEXT

        #In any other case returns success
        return self.SERVER_SHUTDOWN_SUCCESS_CODE, self.SERVER_SHUTDOWN_SUCCESS_TEXT
        

        