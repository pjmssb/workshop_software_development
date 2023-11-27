# Command line adapter for instance_manager
from instance_manager_port import InstanceManagerPort
import re


class CLIInstanceManager(InstanceManagerPort):
    
    def _is_arn_well_formed(self, arn: str) -> bool:
        
        '''
        Simple ARN format validation (can be extended for 
        more specific ARN formats)
        '''
        pattern = r'arn:aws:ec2:[a-z0-9-]+:\d+:instance/[a-z0-9-]+'
        return re.match(pattern, arn) is not None
           
    def stop_instance(self, instance_name: str) -> (int, str):

        if not self._is_arn_well_formed(instance_name):
            return self.SERVER_BAD_ARN_CODE, self.SERVER_BAD_ARN_TEXT

        last_char = instance_name.upper()[len(instance_name)-1]
        # if instance name ends in 'X' responds the instance was not found
        if last_char == 'X':
            return self.SERVER_NOT_FOUND_CODE, self.SERVER_NOT_FOUND_TEXT

        # if instance name ends in 'Y' responds the instance was not found
        if last_char == 'Y':
            return self.SERVER_SHUTDOWN_FAILED_CODE, \
                self.SERVER_SHUTDOWN_FAILED_TEXT

        # In any other case returns success
        return self.SERVER_SHUTDOWN_SUCCESS_CODE, \
            self.SERVER_SHUTDOWN_SUCCESS_TEXT
