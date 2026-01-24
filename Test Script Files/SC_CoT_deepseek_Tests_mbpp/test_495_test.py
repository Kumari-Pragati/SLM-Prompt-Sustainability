import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_no_lowercase(self):
        self.assertEqual(remove_lowercase('HELLO'), 'HELLO')

    def test_numbers_and_special_characters(self):
        self.assertEqual(remove_lowercase('He12llo@#$Wor12ld'), 'HW')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
