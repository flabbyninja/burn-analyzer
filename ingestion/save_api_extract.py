import logging
from os.path import join

from burn_analyzer import sheets_api
from burn_analyzer.api_to_file import save_to_file
from burn_analyzer.config import load_settings

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    print('Loading settings')
    creds_file, scope, sheet_id, _, local_dir, indent = load_settings()
    print('Initialising Sheets API using scope {}'.format(scope))
    service = sheets_api.initialise_sheets_api(creds_file, scope)

    extract_range = 'Current!A2:AV50'
    print('Retrieving data {} from Sheets API using {}'.format(extract_range, sheet_id))
    values = sheets_api.load_sheet_data(service, sheet_id, extract_range)

    output_file = 'sheet.json'
    print('Persisting data to {}'.format(join(local_dir, output_file)))
    save_to_file(values, output_file, local_dir, pretty_print=indent)
    print('Done')