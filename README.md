# burn-analyzer

Pull details from Google Sheets API, explode out clean data structure for analysis, exposing data via RESTful interface

## Create new virtualenv from current dependencies

`pip install -r requirements.txt`

## Activate venv

* BASH: `source <venv>/Scripts/activate`
* CMD: `<venv>\Scripts\activate`

## Configuration

Place a `.env` file in main directory containing the following:

```
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CREDS_FILE = 'client_secret.json'
SPREADSHEET_ID = '1_Ozr94M1N9eUffqm3bw9q4jSBljIFSCI49Tg6wegrAgI'
```

Credentials use [OAUTH](https://developers.google.com/identity/protocols/OAuth2) and should be in JSON format, activated through the [Google API Console](https://console.developers.google.com/) for you account.

## To `vendor` the packages

Vendor all the dependencies from a requirements.txt file for deployment

`pip freeze > requirements.txt`

`pip install -t vendor -r requirements.txt`

### Vendoring for GCP

WIthin `appengine_config.py`, in same folder as `app.yaml`

```
# appengine_config.py

from google.appengine.ext import vendor`

# Add any libraries install in the "lib" folder.
vendor.add('vendor')
```
