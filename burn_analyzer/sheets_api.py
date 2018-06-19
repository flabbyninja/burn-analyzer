from apiclient.discovery import build
from httplib2 import Http
from oauth2client import service_account

from burn_analyzer import config, api_to_file


def initialise_sheets_api(creds_file, scopes):
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name(creds_file, scopes)
    return build('sheets', 'v4', http=creds.authorize(Http()), cache_discovery=False)


def load_sheet_data(service, spreadsheet_id, range_name):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name, majorDimension='COLUMNS').execute()
    values = result.get('values', [])
    return values


if __name__ ==  "__main__":
    creds_file, scope, sheet_id, local_mode, local_dir, _ = config.load_settings()

    if local_mode:
        print('Running in local mode')
        exercise_data = api_to_file.load_from_file('subdir_valid.json', local_dir)
    else:
        service = initialise_sheets_api(creds_file, scope)
        exercise_data = load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print(exercise_data)
