import os
from os.path import join, dirname
import api_to_file

from apiclient.discovery import build
from dotenv import load_dotenv
from httplib2 import Http
from oauth2client import service_account


def load_settings(dotenv_path=None):
    if dotenv_path == None:
        dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    CREDS_FILE = os.environ.get("CREDS_FILE")
    SCOPES = os.environ.get("SCOPES")
    SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
    LOCAL_MODE = os.environ.get("LOCAL_MODE")

    return CREDS_FILE, SCOPES, SPREADSHEET_ID, LOCAL_MODE


def initialise_sheets_api(creds_file, scopes):
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name(creds_file, scopes)
    return build('sheets', 'v4', http=creds.authorize(Http()))


def load_sheet_data(service, spreadsheet_id, range_name):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name, majorDimension='COLUMNS').execute()
    values = result.get('values', [])
    return values


def read_exercises(exercide_data):
    return None

def read_dates(exercise_data):
    return None


if __name__ ==  "__main__":
    creds_file, scope, sheet_id, local_mode = load_settings()


    if local_mode:
        print('Running in local mode')
        exercise_data = api_to_file.load_from_file()
    else:
        service = initialise_sheets_api(creds_file, scope)
        exercise_data = load_sheet_data(service, sheet_id, 'Current!A2:AV50')
    print(exercise_data)
