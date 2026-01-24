import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')

    def test_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_no_uppercase(self):
        self.assertEqual(remove_uppercase('helloworld'), 'helloworld')

    def test_all_uppercase(self):
        self.assertEqual(remove_uppercase('HELLOWORLD'), 'loworld')

    def test_mixed_case(self):
        self.assertEqual(remove_uppercase('HelloWorLD'), 'elloorld')

    def test_special_characters(self):
        self.assertEqual(remove_uppercase('H@ll0WorLD'), '@@ll0orld')

    def test_numbers_and_uppercase(self):
        self.assertEqual(remove_uppercase('H3ll0WorLD'), '3ll0orld')
