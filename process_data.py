import logging
from os.path import join

from burn_analyzer import config, api_to_file, data_processor

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    print('Loading settings')
    _, _, _, _, local_dir, _ = config.load_settings()

    print('Loading persisted data')
    data = api_to_file.load_from_file('sheet.json', local_dir)

    print('Processing exercises from data')
    print(data_processor.get_normalised_exercises(data))
