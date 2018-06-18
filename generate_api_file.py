import logging
from config import load_settings
from api_to_file import save_to_file
import sheets_api

if __name__ == '__main__':
    print('Initialising API')
    logging.basicConfig(level=logging.ERROR)
    creds_file, scope, sheet_id, _, local_dir, indent = load_settings()
    service = sheets_api.initialise_sheets_api(creds_file, scope)
    print('Retrieving data')
    values = sheets_api.load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print('Persisting data')
    save_to_file(values, 'sheet.json', local_dir, pretty_print=indent)
    print('Done')