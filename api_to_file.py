import pickle
import json
import sheets_api


def save_to_file(data, filename, format='json'):
    if format == 'pickle':
        afile = open(filename, 'wb')
        pickle.dump(data, afile)
    else:
        afile = open(filename, 'w')
        js = json.dumps(data)
        afile.write(js)
    afile.close()


def load_from_file(filename, format='json'):
    if format == 'pickle':
        source_file = open(filename, 'rb')
        new_data = pickle.load(source_file)
    else:
        source_file = open(filename, 'r')
        js = source_file.read()
        new_data = json.loads(js)
    source_file.close()
    return new_data


if __name__ == '__main__':
    print('Initialising API')
    creds_file, scope, sheet_id, _ = sheets_api.load_settings()
    service = sheets_api.initialise_sheets_api(creds_file, scope)
    print('Retrieving data')
    values = sheets_api.load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print('Persisting data')
    save_to_file(values, 'sheet.json')
    print('Done')