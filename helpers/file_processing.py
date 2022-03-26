import os
import json

from datetime import datetime

# Date for reference of when this data was parsed
dt_obj = datetime.strptime(str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')),
                           '%Y-%m-%d %H:%M:%S')
millisec_date = dt_obj.timestamp() * 1000

def read_from_json(file_name):
    f = open(file_name)
    data = json.load(f)
    f.close()
    return data

def write_to_json(file_name, content):
    file_path = os.getcwd() + '/file_out/' + str(int(millisec_date)) + '--' + file_name + '.json'
    if content:
        with open(file_path, 'w') as parsed_file:
            parsed_file.write(json.dumps(content))

def read_file_names(file_path):
    names = []
    for filename in os.listdir(file_path):
        f = os.path.join(file_path, filename)
        if os.path.isfile(f):
            names.append(f)

    return names
