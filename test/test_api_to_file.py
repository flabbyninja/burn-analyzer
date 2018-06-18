from unittest import TestCase
import api_to_file
from json.decoder import JSONDecodeError


class TestApiToFile(TestCase):

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