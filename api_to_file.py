import pickle
import sheets_api


def save_to_file(data):
    afile = open(r'sheet.pkl', 'wb')
    pickle.dump(data, afile)
    afile.close()


def load_from_file():
    file2 = open(r'sheet.pkl', 'rb')
    new_data = pickle.load(file2)
    file2.close()
    return new_data


if __name__ == '__main__':
    print('Initialising API')
    creds_file, scope, sheet_id, _ = sheets_api.load_settings()
    service = sheets_api.initialise_sheets_api(creds_file, scope)
    print('Retrieving data')
    values = sheets_api.load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print('Persisting data')
    save_to_file(values)
    print('Done')