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

    return CREDS_FILE, SCOPES, SPREADSHEET_ID


def initialise_sheets_api(creds_file, scopes):
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name(creds_file, scopes)
    return build('sheets', 'v4', http=creds.authorize(Http()))


# Initialise environment
CREDS_FILE, SCOPES, SPREADSHEET_ID = load_settings()

# Initialise Sheets API (read-only) using Service Account details from .env file
service = initialise_sheets_api(CREDS_FILE, SCOPES)


def read_exercises(range_name, spreadsheet_id=SPREADSHEET_ID, ):
    return None


def load_sheet_data(spreadsheet_id, range_name):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name, majorDimension='COLUMNS').execute()
    values = result.get('values', [])
    return values


def read_dates(exercise_data):
    return None


if __name__ ==  "__main__":
    # load spreadsheet data into memory
    exercise_data = load_sheet_data(SPREADSHEET_ID, 'Current!A2:AV50')
    print(exercise_data)

    # for exercise in exercise_data:
    #     print(exercise)
