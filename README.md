# burn-analyzer

Pull details from Google Sheets API, explode out clean data structure for analysis, exposing data via RESTful interface

## Create new virtualenv from current dependencies

`pip install -r requirements.txt`

## Activate venv

* BASH: `source <venv>/Scripts/activate`
* CMD: `<venv>\Scripts\activate`

## Configuration

Place a `.env` file in main directory containing the following:

`SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'`

`CREDS_FILE = 'client_secret.json'`

`SPREADSHEET_ID = '1_Ozr94M1N9eUffqm3bw9q4jSBljIFSCI49Tg6wegrAgI'`

Credentials are [OAUTH](https://developers.google.com/identity/protocols/OAuth2) credentials, activated through the [Google API Console](https://console.developers.google.com/) for you account.