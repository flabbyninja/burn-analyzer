import os
from os.path import join
from unittest import TestCase

from oauth2client.client import HttpAccessTokenRefreshError

from burn_analyzer import sheets_api, config


class TestInitialiseSheetsApi(TestCase):

    def test_initialise_sheets_api_good_creds(self):
        sheets_api.initialise_sheets_api(join(os.pardir, os.pardir, 'client_secret.json'), 'https://www.googleapis.com/auth/spreadsheets.readonly')

    def test_initialise_sheets_api_bad_scope(self):
        with self.assertRaises(HttpAccessTokenRefreshError):
            sheets_api.initialise_sheets_api(join(os.pardir, os.pardir, 'client_secret.json'), 'something_invalid')

    def test_initialise_sheets_api_missing_creds(self):
        with self.assertRaises(FileNotFoundError):
            sheets_api.initialise_sheets_api('these_creds_should_not_exist', 'DUMMY_VALUE')

class TestLoadSheetData(TestCase):

    def test_load_sheet_data(self):
        _, scopes, spreadsheet_id, _, _, _ = config.load_settings(join(os.pardir, os.pardir, 'config.yml'))
        service = sheets_api.initialise_sheets_api(join(os.pardir, os.pardir, 'client_secret.json'), scopes)
        sheets_api.load_sheet_data(service, spreadsheet_id, 'Current!A2:AV50')

