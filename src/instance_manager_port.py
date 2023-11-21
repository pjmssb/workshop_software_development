#Port for instance managers adapters implemented as abstract class

from abc import ABC, abstractmethod
class InstanceManagerPort(ABC):
    
    SERVER_SHUTDOWN_SUCCESS_CODE = 200
    SERVER_SHUTDOWN_SUCCESS_TEXT = "Success - Instance shutdown"
    SERVER_SHUTDOWN_FAILED_CODE = 500
    SERVER_SHUTDOWN_FAILED_TEXT = "Fail - Instance didn't shutdown"
    SERVER_NOT_FOUND_CODE = 400
    SERVER_NOT_FOUND_TEXT = "Fail - Instance not found"
              
    @abstractmethod
    def stop_instance(self) -> (int,str):
        '''
        Concrete implementations of this method should check the instance
        allows shutdown checking the tag allows_shutdown with value true 
        
        '''
        pass
    