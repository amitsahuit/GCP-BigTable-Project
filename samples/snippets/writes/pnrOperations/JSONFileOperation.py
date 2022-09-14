# importing the module
import json
 
# Opening JSON file and convert into dict
def read_json(completeFileLocation):
    with open(completeFileLocation) as json_file:
        data = json.load(json_file)
        return data
          
# read_json('C://Users//asahu23//OneDrive - DXC Production//Desktop//TBJ//BigtableProject//samples//snippets//writes//Raghav-PNR-01.json')