import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')

    def test_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_string_with_no_uppercase(self):
        self.assertEqual(remove_uppercase('helloworld'), 'helloworld')

    def test_string_with_numbers_and_symbols(self):
        self.assertEqual(remove_uppercase('h3ll0W0rld!'), '3ll0orld!')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_uppercase('H@W#O$L%E^R&'), '@#$%^&')

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_uppercase('HeLLoWorLD'), 'elloorld')
