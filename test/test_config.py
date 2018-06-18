from unittest import TestCase
from config import load_settings
from yaml.scanner import ScannerError


class TestConfig(TestCase):

    expected_settings = ('client_secret.json', 'https://www.googleapis.com/auth/spreadsheets.readonly', 'dummy_value', True, 'temp', True)

    def test_load_settings_valid_default_name(self):
        self.assertEquals(load_settings(), self.expected_settings)

    def test_load_settings_valid_filename(self):
        self.assertEquals(load_settings('config.yml'), self.expected_settings)

    def test_load_settings_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_settings('this_file_should_not_exist.yml')

    def test_load_settings_invalid_yaml(self):
        with self.assertRaises(ScannerError):
            load_settings('config_invalid.yml')

    def test_load_settings_missing_parameters(self):
        with self.assertRaises(KeyError):
            load_settings('config_missing_values.yml')

    def test_load_settings_valid_subdir(self):
        settings = load_settings(dirname='subdir')
        self.assertEquals(settings, self.expected_settings)

    def test_load_settings_missing_subdir(self):
        with self.assertRaises(FileNotFoundError):
            load_settings(dirname='this_subdir_should_not_exist')
