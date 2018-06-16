import os
from dotenv import load_dotenv
from os.path import join, dirname
import yaml

def load_settings(filename=None):
    if (filename == None):
        filename = 'config.yml'
    with open(filename) as config_file:
        config = yaml.load(config_file)
        local_mode = config['local_mode']
        if config['local_mode'] is None:
            local_mode = False
        return config['creds_file'], config['scopes'], config['spreadsheet_id'], local_mode, config['local_dir']