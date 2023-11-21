#Command line adapter for instance_manager 
from instance_manager_port import InstanceManagerPort

class AWSEC2InstanceManager(InstanceManagerPort):
    
    def __init__(self, instance_name:str) -> None:
        self.instance_name = instance_name
        
                            
    def stop_instance(self) -> (int,str):
        pass #TBD lógica para detener una instancia ec2
        

        