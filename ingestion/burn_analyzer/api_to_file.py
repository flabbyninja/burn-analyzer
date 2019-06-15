import json
from os import mkdir
from os.path import join, isdir


def save_to_file(data, filename, dir_name='.', pretty_print=False):
    if not isdir(dir_name):
        mkdir(dir_name)
    full_filename = join(dir_name, filename)
    with open(full_filename, 'w') as afile:
        if pretty_print:
            js = json.dumps(data, indent=4)
        else:
            js = json.dumps(data)
        afile.write(js)


def load_from_file(filename, dir_name='.'):
    full_filename = join(dir_name, filename)
    with open(full_filename, 'r') as source_file:
        js = source_file.read()
        new_data = json.loads(js)
        return new_data
