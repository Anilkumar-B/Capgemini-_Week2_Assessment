"""•	10. Build a `SmartPhone` class inheriting from `MobileDevice`,
 which in turn inherits from `Electronics`.
 Demonstrate method overriding and attribute reuse."""


class Electronics():
    def __init__(self,device_name):
        self.device_name=device_name
        
class MobileDevice(Electronics):
    def __init__(self,device_name,camera):
        super().__init__(device_name)
        self.camera=camera
    
    
class SmartPhone(MobileDevice):
    def __init__(self,device_name,camera,battery):
        super().__init__(device_name,camera)
        self.battery=battery
    
    def device_details(self):
        print(f'Electronic name: {self.device_name} have {self.camera} pixel camera, battery {self.battery} mah battery')

smartphone=SmartPhone("Moto",64,5000)
smartphone.device_details()