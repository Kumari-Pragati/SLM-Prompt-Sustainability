import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_lowercase('Hello World'), 'HW')

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_no_lowercase(self):
        self.assertEqual(remove_lowercase('HELLO WORLD'), 'HELLO WORLD')

    def test_numbers_and_special_chars(self):
        self.assertEqual(remove_lowercase('1234567890!@#$%^&*()'), '1234567890!@#$%^&*()')

    def test_mixed_case(self):
        self.assertEqual(remove_lowercase('Hello WoRlD'), 'HW')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(12345)
