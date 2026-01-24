import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase_typical_case(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_remove_lowercase_with_numbers(self):
        self.assertEqual(remove_lowercase('Hello123World456'), 'HW')

    def test_remove_lowercase_with_special_chars(self):
        self.assertEqual(remove_lowercase('Hello@World#'), 'HW')

    def test_remove_lowercase_with_uppercase(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_remove_lowercase_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_remove_lowercase_all_lowercase(self):
        self.assertEqual(remove_lowercase('abcdefghijklmnopqrstuvwxyz'), '')

    def test_remove_lowercase_all_uppercase(self):
        self.assertEqual(remove_lowercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test_remove_lowercase_mixed_case(self):
        self.assertEqual(remove_lowercase('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
