#Port for instance managers adapters

class InstanceManager:

    def __init__(self, environment:str) -> None:
        if environment == 'CLOUD':
            #This is the real think
            self = InstanceManagerCloudAdapter()
        else: 
            #For development and testing
            self = InstanceManagerMockAdapter()
        
    