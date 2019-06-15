import logging
from burn_analyzer import data_processor
from burn_analyzer import sheets_loader
from burn_analyzer.config import load_settings


# Pull data from sheets API, processing exercises and outputting results
#
def processOnlineData():
    print('Loading settings')
    creds_file, scope, sheet_id, _, local_dir, indent = load_settings()
    print('Initialising Sheets API using scope {}'.format(scope))
    service = sheets_loader.initialise_sheets_api(creds_file, scope)

    extract_range = 'Current!A2:AV50'
    print('Retrieving data {} from Sheets API using {}'.format(extract_range, sheet_id))
    data = sheets_loader.load_sheet_data(service, sheet_id, extract_range)

    print('Processing exercises from data')
    return data_processor.get_normalised_exercises(data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    print(processOnlineData())

