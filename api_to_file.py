import pickle
import json
import sheets_api
from os.path import join, isdir
from config import load_settings
from os import mkdir


def save_to_file(data, filename, dir_name='.', output_format='json', pretty_print=False):
    if not isdir(dir_name):
        mkdir(dir_name)
    full_filename = join(dir_name, filename)
    if output_format == 'pickle':
        afile = open(full_filename, 'wb')
        pickle.dump(data, afile)
    else:
        afile = open(full_filename, 'w')
        if pretty_print:
            js = json.dumps(data, indent=4)
        else:
            js = json.dumps(data)
        afile.write(js)
    afile.close()


def load_from_file(filename, dir_name='.', input_format='json'):
    full_filename = join(dir_name, filename)
    if input_format == 'pickle':
        source_file = open(full_filename, 'rb')
        new_data = pickle.load(source_file)
    else:
        source_file = open(full_filename, 'r')
        js = source_file.read()
        new_data = json.loads(js)
    source_file.close()
    return new_data


if __name__ == '__main__':
    print('Initialising API')
    creds_file, scope, sheet_id, _, local_dir, indent = load_settings()
    service = sheets_api.initialise_sheets_api(creds_file, scope)
    print('Retrieving data')
    values = sheets_api.load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print('Persisting data')
    save_to_file(values, 'subdir_valid.json', local_dir, pretty_print=indent)
    print('Done')