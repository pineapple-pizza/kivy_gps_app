from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, farm_data):
        super().__init__()
        
        #set the fields
        
        headers = "Id,Name,Website,Facebook,Twitter,Youtube,Street,City,Country,Zip,X,Y"
        headers = headers.split(',')
        
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = farm_data[i]
            setattr(self, attribute_name, attribute_value)