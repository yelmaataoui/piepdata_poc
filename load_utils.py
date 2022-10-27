import json

class set_encoder(json.JSONEncoder):
    '''encode bad json format'''
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def load(graph_liaison_output, file_name):
    '''loading output to json file'''
    json_str = json.dumps(graph_liaison_output, cls=set_encoder, indent=4)
 
    # Writing to sample.json
    with open(file_name, "w") as outfile:
        outfile.write(json_str)
    
