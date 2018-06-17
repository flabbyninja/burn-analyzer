import os
from os.path import join
import yaml

def load_settings(filename=None, dirname='.'):
    if (filename == None):
        filename = 'config.yml'
    full_filename = join(dirname, filename)
    with open(full_filename) as config_file:
        config = yaml.load(config_file)
        local_mode = config['local_mode']
        if config['local_mode'] is None:
            local_mode = False
        return config['creds_file'], config['scopes'], config['spreadsheet_id'], local_mode, config['local_dir'], config['indent']