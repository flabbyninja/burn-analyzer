import os
from datetime import datetime
from json.decoder import JSONDecodeError
from unittest import TestCase

from burn_analyzer import api_to_file


class TestApiToFileLoad(TestCase):

    expected_valid_result = [['', 'Abdominal', 'Arm Curl', 'Behind Head Tricep', 'Chin Assist', 'Converging Chest Press', 'Converging Shoulder Press', 'Diverging Seated Row', 'Dual Arm', 'Dual Hand Pull', 'Dual weight bar - 7 bottom half, 7 top half, 7 full', 'Lat Pull', 'Lateral Raise', 'Leg Extension', 'Leg press', 'Pectoral Fly', 'Seated Leg Curl', 'Triceps Extension', 'Triceps Pull'], ['', '52', '52', '30', '75', '86.6', '53', '56', '46', '75', '40', '77.3', '62', '69', '109', '96', '71.3', '67', '55.3'], ['10/06', '', '', '', '', '', '54.1', '', '', '', '', '', '', '71.3', '', '109', '77.3', '', '57'], ['04/06', '', '', '', '', '', '', '', '', '', '', '75', '', '69', '', '109', '77.3']]

    def test_load_from_file_not_exists(self):
        with self.assertRaises(FileNotFoundError):
            api_to_file.load_from_file("file_does_not_exist.txt")

    def test_load_from_file_valid_format_default(self):
        data = api_to_file.load_from_file('root_valid.json')
        self.assertListEqual(data, self.expected_valid_result)

    def test_load_from_file_valid_format_with_directory(self):
        data = api_to_file.load_from_file('subdir_valid.json', 'subdir')
        self.assertListEqual(data, self.expected_valid_result)

    def test_load_from_file_invalid_format(self):
        with self.assertRaises(JSONDecodeError):
            api_to_file.load_from_file('root_broken.json')

    def test_load_from_file_invalid_dir(self):
        with self.assertRaises(FileNotFoundError):
            api_to_file.load_from_file('valid.json', 'this_directory_should_not_exist')

class TestApiToFileSave(TestCase):

    sample_data = [['Lion', 'Bear', 'Armadillo', 'Rhino', 'Three Horned Toad'], ['5', '10', '15', '20', '25'] ,['1', '2', '3', '5', '8']]

    def generate_timestamp_name(self, root_name):
        return root_name.format((datetime.now().strftime('_%Y%m%d_%H%M%S%f')))

    def test_save_to_file_default_location(self):
        output_filename = self.generate_timestamp_name('test_out.{}.json')
        api_to_file.save_to_file(self.sample_data, output_filename)
        self.assertListEqual(self.sample_data, api_to_file.load_from_file(output_filename))
        os.remove(output_filename)

    def test_save_to_file_indent_on(self):
        output_filename = self.generate_timestamp_name('test_out.{}.json')
        api_to_file.save_to_file(self.sample_data, output_filename, pretty_print=True)
        self.assertListEqual(self.sample_data, api_to_file.load_from_file(output_filename))
        os.remove(output_filename)

    def test_save_to_file_with_dir(self):
        subdir = 'subdir'
        output_filename = self.generate_timestamp_name('test_out.{}.json')
        api_to_file.save_to_file(self.sample_data, output_filename, subdir)
        self.assertListEqual(self.sample_data, api_to_file.load_from_file(output_filename, subdir))
        os.remove(os.path.join(subdir, output_filename))

    def test_save_to_file_with_dir_needs_created(self):
        subdir_name = self.generate_timestamp_name('subdir.{}')
        output_filename = self.generate_timestamp_name('test_out.{}.json')
        api_to_file.save_to_file(self.sample_data, output_filename, subdir_name)
        self.assertListEqual(self.sample_data, api_to_file.load_from_file(output_filename, subdir_name))
        os.remove(os.path.join(subdir_name, output_filename))
        os.rmdir(subdir_name)

