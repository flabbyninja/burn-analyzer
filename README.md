# burn-analyzer

Pull details from Google Sheets API, explode out clean data structure for analysis, exposing data via RESTful interface

## Create new virtualenv from current dependencies

`pip install -r requirements.txt`

## Activate venv

* BASH: `source <venv>/Scripts/activate`
* CMD: `<venv>\Scripts\activate`

## Configuration

Place a `config.yml` file in main directory containing the following:

```
scopes: https://www.googleapis.com/auth/spreadsheets.readonly
creds_file: client_secret.json
spreadsheet_id: id_from_sheets
local_mode: True
local_dir: temp
indent: True
```

`local_mode` allows development offline, saving the data structures from the Sheets API to file so you can reconstruct them. Default is local mode `false`.

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
