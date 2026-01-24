import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_remove_lowercase_typical_case(self):
        self.assertEqual(remove_lowercase('Hello World'), 'HW')

    def test_remove_lowercase_with_numbers(self):
        self.assertEqual(remove_lowercase('Hello123World456'), 'HW')

    def test_remove_lowercase_with_special_characters(self):
        self.assertEqual(remove_lowercase('Hello@World#'), 'HW')

    def test_remove_lowercase_with_uppercase(self):
        self.assertEqual(remove_lowercase('Hello World'), 'HW')

    def test_remove_lowercase_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_remove_lowercase_all_lowercase(self):
        self.assertEqual(remove_lowercase('hello world'), '')

    def test_remove_lowercase_error_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(12345)
